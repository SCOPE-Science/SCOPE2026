#!/usr/bin/env python3
"""Reproducible independent numerical checks for a simplex pair-distance onset law."""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.stats import qmc
from scipy.special import beta


def simplex_data(vertices):
    vertices = np.asarray(vertices, dtype=float)
    d = vertices.shape[1]
    B = (vertices[1:] - vertices[0]).T
    assert abs(np.linalg.det(B)) > 1e-10
    grad = np.linalg.inv(B)  # rows of independent barycentric gradients
    grads = np.vstack((-np.sum(grad, axis=0), grad))
    V = abs(np.linalg.det(B))/math.factorial(d)
    vectors = []
    for k in range(1, d+1):
        for idx in itertools.combinations(range(d+1), k):
            v = grads[list(idx)].sum(axis=0)
            if not any(np.allclose(v,w,rtol=1e-12,atol=1e-12) for w in vectors):
                vectors.append(v)
    vec = np.asarray(vectors)
    norms = np.linalg.norm(vec,axis=1)
    mx = norms.max()
    winners = vec[np.isclose(norms,mx,rtol=1e-10,atol=1e-10)]
    assert len(winners)%2==0
    return V, grads, vec, mx, winners


def q_from_barycentric(grads, displacements):
    y = np.asarray(displacements) @ grads.T
    return np.maximum(y,0).sum(axis=-1)


def independent_intersection_volume(vertices, offset):
    vertices=np.asarray(vertices,float)
    d=vertices.shape[1]
    base = (vertices[1:]-vertices[0]).T
    grads=np.vstack((-np.linalg.inv(base).sum(axis=0),np.linalg.inv(base)))
    # Each simplex, original and translated, contributes d+1 facet inequalities.
    offsets=1-grads @ vertices[0]  # not the actual affine lambda intercepts; see below
    # lambda_i(x) = grads_i dot x + b_i
    b = np.array([1.0,0.0,0.0,0.0]) - grads @ vertices[0] if d==3 else np.r_[1.,np.zeros(d)] - grads @ vertices[0]
    constraints=[]
    for displacement in (np.zeros(d),offset):
        for n,shift in zip(grads,b):
            # n.dot(x) + (shift-n.dot(displacement)) >= 0
            constraints.append((n,shift-n @ displacement))
    inter=[]
    for sub in itertools.combinations(range(2*(d+1)),d):
        M=np.asarray([constraints[j][0] for j in sub]); c=np.asarray([-constraints[j][1] for j in sub])
        if abs(np.linalg.det(M))<1e-12:continue
        x=np.linalg.solve(M,c)
        if all(n@x+t>=-1e-9 for n,t in constraints):
            if not any(np.linalg.norm(x-v)<1e-8 for v in inter):inter.append(x)
    if len(inter)<=d:return 0.0
    return ConvexHull(np.array(inter)).volume


def cap(d,r,a):
    from scipy.integrate import quad
    omega = math.pi**((d-1)/2)/math.gamma((d+1)/2)
    val = quad(lambda s:(s-a)**d*(r*r-s*s)**((d-1)/2),a,r,epsabs=1e-14)[0]
    return omega*val/a**d


def cap_leading(d,a):
    omega = math.pi**((d-1)/2)/math.gamma((d+1)/2)
    return omega*2**((d-1)/2)*a**(-(d+1)/2)*beta(d+1,(d+1)/2)


def check_case(vertices,radius_increments):
    V,grads,vectors,t,winners=simplex_data(vertices)
    d=len(vertices)-1
    a=1/t
    norms=np.linalg.norm(vectors,axis=1)
    losers=norms[~np.isclose(norms,t,atol=1e-10,rtol=1e-10)]
    upper_nonmax=1/losers.max() if len(losers) else float('inf')
    dirs=winners/t
    ang=np.arccos(np.clip(dirs@dirs.T,-1,1))
    ang[np.eye(len(dirs),dtype=bool)]=np.inf
    upper_overlap=a/math.cos(0.5*ang.min()) if ang.min()<math.pi-1e-7 else float('inf')
    upper=min(upper_nonmax,upper_overlap)
    print(f"dimension={d} volume={V:.9g} first_radius={a:.9g} multiplicity={len(winners)} exact_branch_to={upper:.9g}")
    rng=np.random.default_rng(8127)
    # independent halfspace-polytope intersection, not the covariogram formula
    for j in range(32):
        z=rng.normal(size=d); z*=rng.uniform(0.02,0.85)*a/np.linalg.norm(z)
        observed=independent_intersection_volume(vertices,z)
        predicted=V*max(0,1-q_from_barycentric(grads,z))**d
        assert abs(predicted-observed)<2e-9*max(1,V),(j,observed,predicted)
    if d==3:
        U=qmc.Sobol(d=2,scramble=True,seed=92418).random_base2(19)
        z=1-2*U[:,0]
        teta=2*math.pi*U[:,1]
        dirs_sample=np.column_stack([np.sqrt(1-z*z)*np.cos(teta),np.sqrt(1-z*z)*np.sin(teta),z])
        q=q_from_barycentric(grads,dirs_sample)
        for inc in radius_increments:
            r=a+inc
            assert r<upper,(r,upper)
            pos=np.maximum(0,r*q-1)
            radial = np.where(q>0,(pos**4/4+2*pos**5/5+pos**6/6)/np.maximum(q,1e-100)**3,0)
            observed=(4*math.pi/V)*radial.mean()
            predicted=len(winners)*math.pi*(r-a)**5*(a+5*r)/(60*V*a**3)
            relerr=abs(observed-predicted)/predicted
            assert relerr<0.012,(observed,predicted,relerr)
            leading=len(winners)*math.pi/(10*V*a*a)
            print(f"  delta={inc:.7g} independent_radial={observed:.10g} cap_exact={predicted:.10g} rel_err={relerr:.5g} leading={leading:.8g}")
    for t in (0.003*a,0.009*a,0.017*a):
        measured=cap(d,a+t,a)
        approx=cap_leading(d,a)*t**((3*d+1)/2)
        assert abs(measured/approx-1)<0.07
    print('  INTERSECTION_AND_CAP_CHECK_OK')


def main():
    tet=np.array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]],float)
    check_case(tet,[0.030,0.060])
    s=1/(2*math.sqrt(2))
    reg=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)*s
    check_case(reg,[0.026,0.054])
    tri=np.array([[0.,0.],[1.,0.],[0.25,1.3]])
    check_case(tri,[])
    simplex4=np.vstack((np.zeros((1,4)),np.eye(4)))
    check_case(simplex4,[])
    print('SIMPLEX_DISTANCE_ONSET_CHECK_OK')

if __name__=='__main__':main()
