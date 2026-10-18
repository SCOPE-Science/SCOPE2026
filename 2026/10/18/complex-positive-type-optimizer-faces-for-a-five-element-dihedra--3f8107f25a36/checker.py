"""Independent numerical checks of finite-dihedral positive-type optimizer formulas.

This uses standard-library arithmetic only. It corroborates, rather than proves,
the exact symbolic argument. Run: python3 checker.py
"""
import itertools
import math

TOL=3e-10
cases=0
faces=0

def samples(n):
    return sorted(set(round(abs(math.cos(math.pi*k/n)),14) for k in range(n)))

def symmetric_min_eigenvalue(n,u,t):
    # Eigenvalues of the full two-dimensional Fourier block, including
    # reducible endpoints k=0 and k=n/2.
    return min(1+2*u*math.cos(2*math.pi*k/n)
               -2*abs(t)*abs(math.cos(math.pi*k/n)) for k in range(n))

def general_min_eigenvalue(n,u,v,b,c):
    return min(1+2*u*math.cos(2*math.pi*k/n)-math.sqrt(
        4*v*v*math.sin(2*math.pi*k/n)**2
        +b*b+c*c+2*b*c*math.cos(2*math.pi*k/n))
        for k in range(n))

def lp_max(n):
    # All two-constraint vertices for (u,y) with y>=0. Include the
    # finite Fourier inequalities at every sample of n-th roots.
    z=samples(n)
    con=[(4*x*x-2,-x, -1) for x in z]
    # q=1+(4z^2-2)u-z*y>=0, hence a*u+b*y=-1.
    con.append((0,1,0))  # y=0
    verts=[]
    for (a,b,c),(d,e,f) in itertools.combinations(con,2):
        det=a*e-b*d
        if abs(det)<1e-12:continue
        u=(c*e-b*f)/det
        y=(a*f-c*d)/det
        if y>=-TOL and all(1+A*u+B*y>=-TOL for A,B,_ in con[:-1]):
            verts.append((u,y))
    assert verts, n
    return max(1+2*u+y for u,y in verts)

for n in range(3,121):
    z=samples(n)
    lower=[a for a in z if a < .5-1e-12]
    upper=[a for a in z if a > .5+1e-12]
    if n%3:
        alpha=max(lower)
        beta=min(upper)
        u=1/(2+4*alpha*beta)
        t=(alpha+beta)/(1+2*alpha*beta)
        optimum=1+2*u+2*t
        assert symmetric_min_eigenvalue(n,u,t)>-TOL
        assert abs(general_min_eigenvalue(n,u,0,t,t))<TOL
        assert abs(optimum-lp_max(n))<1e-9,(n,optimum,lp_max(n))
        # Exact dual multipliers derived from the two nearest contacts.
        lam=(2*beta-1)*(1+beta)/((beta-alpha)*(1+2*alpha*beta))
        mu=(1-2*alpha)*(1+alpha)/((beta-alpha)*(1+2*alpha*beta))
        assert lam>0 and mu>0
        assert abs(lam*alpha+mu*beta-1)<1e-10
        assert abs(lam*(4*alpha*alpha-2)+mu*(4*beta*beta-2)+2)<1e-10
    else:
        beta=min(upper)
        lo=1/(2*(1+beta))
        hi=1/(2*(1+max(lower))) if lower else 1.
        optimum=3.
        for u in (lo,(lo+hi)/2,hi):
            t=1-u
            assert symmetric_min_eigenvalue(n,u,t)>-TOL, (n,u)
            assert abs(general_min_eigenvalue(n,u,0,t,t))<TOL
            assert abs(1+2*u+2*t-3)<1e-12
            faces+=1
        assert abs(lp_max(n)-3)<1e-9,(n,lp_max(n))
    cases+=1

print(f'PASS: {cases} orders, {faces} interval witnesses; all full irrep blocks PSD;')
print('the analytic optima equal independently enumerated two-variable LP vertices.')
