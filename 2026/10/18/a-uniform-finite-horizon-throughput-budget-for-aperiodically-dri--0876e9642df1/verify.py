"""Exact edge/storage identity checks for the quadratic-hindrance transport chain.

Run: python verify.py
Only Python standard library is required. The finite checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import product


def make_reference(e):
    """Choose rates so the specified rational occupancy is an exact equilibrium."""
    n = len(e)
    ee = [F(1)] + list(e) + [F(0)]
    c = [ee[i] * (1-ee[i+1]**2) for i in range(n+1)]
    rate = [1 / ci for ci in c]
    ratio = [ee[i]*2*ee[i]/(1-ee[i]**2) for i in range(1,n+1)]
    p = [F(1)]
    for r in ratio:
        p.append(p[-1] * r)
    p = [pi/sum(p) for pi in p]
    return ee, c, rate, p


def identity(e, x, u):
    n=len(e)
    ee,c,lam,p=make_reference(e)
    xx=[F(1)]+list(x)+[F(0)]
    R=F(1)
    z=[F(0)]+[xx[j]-ee[j] for j in range(1,n+1)]+[F(0)]
    eta=[(1-ee[i+1]**2)*z[i]-2*ee[i]*ee[i+1]*z[i+1] for i in range(n+1)]
    rho=[xx[i]*(1-xx[i+1]**2)-c[i]-eta[i] for i in range(n+1)]
    d=[eta[i]**2/c[i]-(1-eta[i]/c[i])*rho[i] for i in range(n+1)]
    q=[u[i]*xx[i]*(1-xx[i+1]**2) for i in range(n+1)]
    zdot=[q[j-1]-q[j] for j in range(1,n+1)]
    Vdot=sum(p[j]/ee[j]*z[j]*zdot[j-1] for j in range(1,n+1))
    Hdot=Vdot+sum(sum(p[:j])*zdot[j-1] for j in range(1,n+1))
    rhs=sum(p[i]*u[i]*c[i] for i in range(n+1))
    lhs=q[-1]+sum(p[i]*u[i]*d[i] for i in range(n+1))+Hdot
    assert lhs == rhs, ('storage balance', e,x,u,lhs,rhs)
    assert -Vdot == sum(p[i]*q[i]*eta[i]/c[i] for i in range(n+1))
    assert all(di>=0 for di in d), ('negative edge dissipation', e,x,d)
    if x == e:
        assert all(di==0 for di in d)
    else:
        assert sum(pi*di for pi,di in zip(p,d))>0
    return len(d)+3


def run():
    rational=[F(0),F(1,5),F(1,2),F(4,5),F(1)]
    rate_sets=[[F(1) for _ in range(5)], [F(2+i,3) for i in range(5)], [F(7-i,4) for i in range(5)]]
    equilibrium_sets=[(F(1,3),),(F(1,4),F(1,2)),(F(2,7),F(3,5),F(1,3))]
    checks=0
    for equilibrium in equilibrium_sets:
        n=len(equilibrium)
        for state in product(rational,repeat=n):
            for rs in rate_sets:
                checks+=identity(equilibrium,state,rs[:n+1])
    # Symbolic one-site nonperiodicity-safe relation, verified over a rational grid.
    for b in (F(1,5),F(1,3),F(2,3),F(4,5)):
        h=1-b*b
        for y in rational:
            z=y-b
            c=h
            s=2*b*z/h
            A=(1-y*y)/h
            d0=c*(1-A*(1+s))
            explicit=(1+b*b+2*b*y)*z*z/h
            assert d0 == explicit
            checks+=1
    print(f'VERIFY_OK: {checks} exact rational identities/nonnegative dissipations; n=1,2,3; all boundary states sampled')

if __name__=='__main__':
    run()
