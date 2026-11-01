"""Independent finite rational checks for a dyadic return-law calculation.

The infinite-tail statements follow from the accompanying analytic proof, not these checks.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import pi, sqrt


def algebraic_probabilities(p, N):
    """Coefficients from r=z(p+(1-p)r*r), R=z((1-p)r+p/(2-r))."""
    q = 1-p
    r=[F(0)]*(N+1)
    u=[F(0)]*(N+1)
    u[0]=F(1,2)
    for n in range(1,N+1):
        r[n]=(p if n==1 else F(0))+q*sum((r[j]*r[n-1-j] for j in range(1,n-1)),F(0))
        u[n]=F(1,2)*sum((r[j]*u[n-j] for j in range(1,n+1)),F(0))
    return [F(0)]+[q*r[n-1]+p*u[n-1] for n in range(1,N+1)]


def hitting_probabilities(p, N):
    """Direct Markov evolution of the initial Lebesgue-conditioned binary cells."""
    q=1-p
    probability=[F(0)]*(N+1)
    probability[1]=p/F(2)
    state=defaultdict(F)
    state[1]+=q
    for j in range(1,N):
        state[j]+=p*F(1,2**(j+1))
    for n in range(2,N+1):
        nxt=defaultdict(F)
        for j,m in state.items():
            if j==1:probability[n]+=p*m
            else:nxt[j-1]+=p*m
            nxt[j+1]+=q*m
        state=nxt
    return probability


def floats(p,N):
    q=1-p
    r=[0.0]*(N+1); u=[0.0]*(N+1);u[0]=.5
    for n in range(1,N+1):
        r[n]=(p if n==1 else 0)+q*sum(r[j]*r[n-1-j] for j in range(1,n-1))
        u[n]=.5*sum(r[j]*u[n-j] for j in range(1,n+1))
    return [0.0]+[q*r[n-1]+p*u[n-1] for n in range(1,N+1)]


def predicted(p,n):
    q=1-p
    if p<.8:
        rho=1/(2*sqrt(p*q));a=sqrt(p/q)
        cp=rho*a*(q+p/(2-a)**2)/sqrt(2*pi)
        cm=rho*a*(q+p/(2+a)**2)/sqrt(2*pi)
        return (cp+(-1)**n*cm)*rho**(-n)*n**(-1.5)
    if abs(p-.8)<1e-10:
        return p**n*n**(-.5)/(2*sqrt(2*pi))
    return p*(p-4*q)/(p+4*q)**2 * ((p+4*q)/2)**n

if __name__=='__main__':
    cases=[F(1,2),F(3,5),F(4,5),F(9,10),F(1,1)]
    for p in cases:
        left=algebraic_probabilities(p,26)
        right=hitting_probabilities(p,26)
        assert left==right,(p,[(i,left[i],right[i]) for i in range(1,27) if left[i]!=right[i]])
        assert left[1]==p/2
        assert all(t>=0 for t in left)
        print('exact rational 26-coefficient return comparison PASS:',str(p))
    assert algebraic_probabilities(F(1),26)[1:]==[F(1,2**n) for n in range(1,27)]
    print('deterministic doubling endpoint PASS')
    for p, n, tolerance in [(.6,300,.025),(.8,300,.015),(.9,200,1e-5),(.99,100,1e-6)]:
        empirical=floats(p,n)[n]
        approximate=predicted(p,n)
        rel=abs(empirical/approximate-1)
        print('asymptotic spot check',p,n,'relative_error',rel)
        assert rel<tolerance
    assert F(9,10)*(F(9,10)-4*F(1,10))/(F(9,10)+4*F(1,10))**2 == F(45,169)
    assert (F(9,10)+4*F(1,10))/2 == F(13,20)
    print('exact pole residue at p=9/10: 45/169, rate 13/20 PASS')
    print('ALL VERIFICATION CHECKS PASS; asymptotics are analytically proved, not certified by finite tests.')
