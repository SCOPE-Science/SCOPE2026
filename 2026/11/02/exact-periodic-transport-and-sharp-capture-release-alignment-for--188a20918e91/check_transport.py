"""Reproducible algebra, discrete-transport convergence and rearrangement checks.
This program is a finite diagnostic; the general result is proved analytically.
"""
import math
import itertools
from fractions import Fraction
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def formula(v, alpha, gammas, deltas):
    g = sum(gammas) / len(gammas)
    r = sum(x/y for x,y in zip(gammas,deltas))/len(gammas)
    return v*v/((alpha+g)*(1+r))


def finite_generator_diffusion(v, alpha, gammas, deltas):
    """Independent nearest-grid velocity-jump approximation on a periodic ring."""
    m=len(gammas)
    dx=1.0/m
    q=lil_matrix((3*m,3*m),dtype=float)
    transitions=[]
    for j in range(m):
        for s in (0,1):
            i=3*j+s
            k=3*((j+(1 if s==0 else -1))%m)+s
            h=3*j+(1-s)
            r=3*j+2
            transitions.extend([(i,k,v/dx,(1 if s==0 else -1)*dx),
                                (i,h,alpha/2,0.0),(i,r,gammas[j],0.0)])
        i=3*j+2
        transitions.extend([(i,3*j,deltas[j]/2,0.0),(i,3*j+1,deltas[j]/2,0.0)])
    for i,k,rate,disp in transitions:
        q[i,k]+=rate
        q[i,i]-=rate
    q=q.tocsr()
    b=np.zeros(3*m)
    for i,k,rate,disp in transitions: b[i]+=rate*disp
    reduced=q[1:,1:]
    h=np.zeros(3*m)
    h[1:]=spsolve(reduced,-b[1:])
    R=np.mean(np.asarray(gammas)/np.asarray(deltas))
    pi=np.zeros(3*m)
    for j in range(m):
        pi[3*j]=pi[3*j+1]=1/(2*m*(1+R))
        pi[3*j+2]=(gammas[j]/deltas[j])/(m*(1+R))
    assert np.max(np.abs(pi@q))<5e-9
    drift=sum(pi[i]*rate*disp for i,k,rate,disp in transitions)
    assert abs(drift)<1e-9
    residual=np.linalg.norm(q@h+b,ord=np.inf)
    assert residual<3e-8, residual
    variance_rate=sum(pi[i]*rate*(disp+h[k]-h[i])**2 for i,k,rate,disp in transitions)
    return variance_rate/2


def run():
    checks=0
    # General generator identity, checked by pointwise exact rational arithmetic.
    for A in (Fraction(1,2),Fraction(3,4),Fraction(5,3)):
        for gs in ((Fraction(1,2),Fraction(3,2)),(Fraction(1,5),Fraction(4,5),Fraction(3,2)),(Fraction(1,3),Fraction(2,3),Fraction(4,3),Fraction(8,3))):
            G=sum(gs)/len(gs)
            v=Fraction(7,5)
            g=v/(A+G)
            for gamma in gs:
                hp=(gamma-G)/(A+G)
                for s in (-1,1):
                    generator=s*(v*(1+hp)-(A+gamma)*g)
                    assert generator==0
                    checks+=1
    # Exact endpoint computations for all pairings of independent rate histograms.
    for gammas in ((1,2,5),(1,2,4,8),(1,2,3,5,9)):
        deltas=tuple(range(2,2+len(gammas)))
        all_R=[sum(x/y for x,y in zip(gammas,perm))/len(gammas) for perm in itertools.permutations(deltas)]
        R_min=sum(x/y for x,y in zip(sorted(gammas),sorted(deltas)))/len(gammas)
        R_max=sum(x/y for x,y in zip(sorted(gammas),sorted(deltas,reverse=True)))/len(gammas)
        assert abs(min(all_R)-R_min)<1e-12
        assert abs(max(all_R)-R_max)<1e-12
        checks+=len(all_R)
    # Numerical homogenization using a different, entirely finite Markov chain.
    for gamma_profile,delta_profile in [
        ([0.5,1.5],[0.5,1.5]),
        ([0.5,1.5],[1.5,0.5]),
        ([0.4,1.4,2.0],[2.2,0.7,1.5]),
    ]:
        target=formula(1.4,1.2,gamma_profile,delta_profile)
        errors=[]
        for refinement in (12,24,48):
            gammas=[x for x in gamma_profile for _ in range(refinement)]
            deltas=[x for x in delta_profile for _ in range(refinement)]
            observed=finite_generator_diffusion(1.4,1.2,gammas,deltas)
            err=abs(observed-target)
            errors.append(err)
            assert err < 0.07, (observed,target,err)
            checks+=1
        assert errors[-1] < errors[0], errors
        checks+=1
        print('pairing',gamma_profile,delta_profile,'target',target,'errors',errors)
    # Two-compartment example, conservation of rate distributions and sharp ratio.
    common=formula(1.4,1.2,[0.5,1.5],[0.5,1.5])
    opposite=formula(1.4,1.2,[0.5,1.5],[1.5,0.5])
    assert abs(common/opposite-4/3)<1e-12
    checks+=1
    print(f'All {checks} exact/finite checks passed; expected diffusion ratio={common/opposite:.12g}.')

if __name__=='__main__':
    run()
