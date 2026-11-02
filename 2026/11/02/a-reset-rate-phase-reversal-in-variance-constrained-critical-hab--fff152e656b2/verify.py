#!/usr/bin/env python3
"""Numerical checks for variance-constrained relocation thresholds.
Only standard-library Python is needed; checks are finite corroboration, not proof.
"""
import math

TESTS = 0

def check(predicate, message):
    global TESTS
    TESTS += 1
    if not predicate:
        raise AssertionError(message)

def close(a, b, tol=2e-10):
    check(abs(a-b) <= tol * (1+abs(a)+abs(b)), f"not close: {a} {b}")

def laws(c, sigma):
    v=sigma*sigma
    p=v/(c*c)
    return {
        'shell': [(-sigma, .5),(sigma,.5)],
        'edge_center': [(0.,1-p),(-c,p/2),(c,p/2)],
    }

def dirichlet_resolvent(L, z, s, D):
    y=L*z
    if abs(s) < 1e-13:
        return (L*L-y*y)/(2*D)
    if s > 0:
        k=math.sqrt(s/D)
        # For test ranges the hyperbolic functions do not overflow.
        return (1-math.cosh(k*y)/math.cosh(k*L))/s
    k=math.sqrt(-s/D)
    if k*L >= math.pi/2:
        raise ValueError('outside positive Dirichlet resolvent domain')
    return (math.cos(k*y)/math.cos(k*L)-1)/(-s)

def residue(L, law, r, g=1, D=1):
    return r*sum(w*dirichlet_resolvent(L,z,r-g,D) for z,w in law)

def critical_length(law, r, g=1, D=1):
    if r<=0 or g<=0 or D<=0:
        raise ValueError('positive rates required')
    lo=0.; hi=math.sqrt(D/g)*2
    if r<g:
        hi=min(hi, .999999*math.pi/2*math.sqrt(D/(g-r)))
    for _ in range(200):
        if residue(hi,law,r,g,D)>1: break
        hi*=1.25
        if r<g:
            hi=min(hi,.99999999*math.pi/2*math.sqrt(D/(g-r)))
    else: raise AssertionError('bracket not found')
    for _ in range(95):
        mid=(lo+hi)*.5
        if residue(mid,law,r,g,D) <1: lo=mid
        else:hi=mid
    return (lo+hi)*.5

def tri_solve_f(L,N,r,g,D):
    h=2*L/(N+1)
    t=D/(h*h)
    b=2*t+r-g
    # Tridiagonal SPD -D Laplacian + (r-g) I, Dirichlet ends
    p=[0.]*N; d=[0.]*N
    for j in range(N):
        den=b-(t*p[j-1] if j else 0.)
        p[j]=t/den
        d[j]=(1+(t*d[j-1] if j else 0.))/den
    f=[0.]*N
    for j in range(N-1,-1,-1):
        f[j]=d[j]+(p[j]*f[j+1] if j<N-1 else 0.)
    return f

def discrete_residue(L,law,r,g,D,N=199):
    f=tri_solve_f(L,N,r,g,D)
    ans=0.
    for z,w in law:
        idx=int(round((z+1)*(N+1)/2))-1
        check(abs((-1+(idx+1)*2/(N+1))-z)<1e-12, 'reset point on grid')
        ans +=r*w*f[idx]
    return ans

def execute():
    c=.9;sigma=.5
    ls=laws(c,sigma)
    for law in ls.values():
        close(sum(w for _,w in law),1)
        close(sum(z*w for z,w in law),0)
        close(sum(z*z*w for z,w in law),sigma**2)
    for r in [.05,.1,.3,.6,.75,.9,1.,1.1,1.5,2.5,3.,5.,10.]:
        roots={s:critical_length(law,r) for s,law in ls.items()}
        for s,L in roots.items():
            close(residue(L,ls[s],r),1,1e-12)
            check(L>0 and math.isfinite(L),'positive finite root')
            if r<1:check(math.sqrt(1-r)*L<math.pi/2,'positive resolvent domain')
            for shift in [.99,1.01]:
                check((residue(shift*L,ls[s],r)-1)*(shift-1)>0, 'root crosses once')
            # Independent finite-difference Dirichlet boundary problem.
            approx=discrete_residue(L,ls[s],r,1,1)
            check(abs(approx-1)<.003, f'discrete residual {r}, {s}, {approx}')
        if r<1:
            check(roots['edge_center']<roots['shell'],'sub-growth reversal')
        elif r>1:
            check(roots['shell']<roots['edge_center'],'super-growth reversal')
        else:
            close(roots['shell'],roots['edge_center'],1e-12)
            close(roots['shell'],math.sqrt(2/(1-sigma**2)),1e-12)
        for j in range(1,20):
            t=j/20
            mu=[(z,t*w) for z,w in ls['shell']]+[(z,(1-t)*w) for z,w in ls['edge_center']]
            L=critical_length(mu,r)
            low=min(roots.values());high=max(roots.values())
            check(low-1e-9<=L<=high+1e-9, 'convex mixture threshold bounds')
            if r!=1:check(low+1e-10<L<high-1e-10, 'strict interior bound')
    # Independent parameter scales: scaling should be sqrt(D/g)
    # when ratio r/g, c, sigma fixed.
    for r_over_g in [.25,1.,2.,4.]:
        for D,g in [(.5,3),(1.8,.8),(5.,2.1)]:
            for law in ls.values():
                a=critical_length(law,r_over_g*g,g,D)
                b=critical_length(law,r_over_g,1,1)*math.sqrt(D/g)
                close(a,b,2e-11)
    # Convexity-of-moment-kernel checks by midpoint secant in squared radius.
    for s in [-.8,-.5,-.1,.15,.75,2.]:
        L=min(1.,(.95*math.pi/2/math.sqrt(-s)) if s<0 else 1.)
        for j in range(1,21):
            w1=(j-1)*c*c/21;w2=(j+1)*c*c/21;wm=(w1+w2)/2
            F=lambda w:dirichlet_resolvent(L,math.sqrt(w),s,1)
            if s>0:check(F(wm)>.5*(F(w1)+F(w2)), 'positive-s concavity')
            else:check(F(wm)<.5*(F(w1)+F(w2)), 'negative-s convexity')
    print(f"PASS {TESTS} deterministic checks")

if __name__=='__main__':
    execute()
