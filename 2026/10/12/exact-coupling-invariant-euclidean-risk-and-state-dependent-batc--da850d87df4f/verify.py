"""Exact-rational finite-horizon checks for a pair-coupled minibatch descent identity.
Run with: python3 verify.py. Uses Python's standard library only.
Finite enumerations supplement, and do not prove, the all-horizon recurrence.
"""
from fractions import Fraction as F
from itertools import combinations

PAIRS = tuple(combinations(range(4), 2))

def transitions(a, b, c):
    assert a >= 0 and b >= 0 and c >= 0 and a+b+c == 1
    return { (0,1): a/2, (2,3): a/2,
             (0,2): b/2, (1,3): b/2,
             (0,3): c/2, (1,2): c/2 }

def step(x, S, rho):
    y=list(x)
    for i in S: # use PRE-update values for every selected coordinate
        y[i] = -rho * x[i ^ 1]
    return tuple(y)

def formula(x, rho, a, k):
    r=(1+rho*rho)/2
    u=sum(t*t for t in x)
    w=x[0]*x[1]+x[2]*x[3]
    expected_norm=u*r**k
    expected_objective = r**k * (F(1,2)*u*(1-rho*rho)/(1+rho*rho)
           + a**k *(rho*w + rho*rho*u/(1+rho*rho)))
    return expected_norm, expected_objective

def objective(x, rho):
    return sum(v*v for v in x)/2 + rho*(x[0]*x[1]+x[2]*x[3])

def sweep(x, rho, a, b, c, bound):
    d={x:F(1)}
    count=0
    probs=transitions(a,b,c)
    for k in range(bound+1):
        en=sum(prob*sum(t*t for t in state) for state,prob in d.items())
        ef=sum(prob*objective(state,rho) for state,prob in d.items())
        nn,ff=formula(x,rho,a,k)
        assert en==nn, (x,rho,a,b,c,k,'norm',en,nn)
        assert ef==ff, (x,rho,a,b,c,k,'objective',ef,ff)
        count+=2
        if k<bound:
            nd={}
            for state, weight in d.items():
                for S, pp in probs.items():
                    if pp==0:continue
                    y=step(state,S,rho)
                    nd[y]=nd.get(y,F(0))+weight*pp
            d=nd
            assert sum(d.values())==1
    return count

def main():
    count=0
    initials=[tuple(map(F,z)) for z in ((1,1,1,1),(1,-1,1,-1),(1,2,-2,3),(0,1,2,0))]
    for rho in (F(1,5),F(1,2),F(4,5)):
        for a,b,c in ((F(0),F(1),F(0)),(F(0),F(1,2),F(1,2)),
                      (F(1,3),F(1,6),F(1,2)),(F(1,2),F(1,4),F(1,4)),
                      (F(3,4),F(1,4),F(0)),(F(1),F(0),F(0))):
            for x in initials:
                count+=sweep(x,rho,a,b,c,5)
    # Independent exact optimization and condition-number identities.
    for rho in (F(1,10),F(1,3),F(2,3),F(9,10),F(99,100)):
        r=(1+rho*rho)/2
        x=(F(1),)*4
        for k in range(1,9):
            f_best=formula(x,rho,F(0),k)[1]
            f_worst=formula(x,rho,F(1),k)[1]
            assert f_worst / f_best == (1+rho*rho)/(1-rho)
            assert f_best < formula(x,rho,F(1,2),k)[1] < f_worst
            count+=3
        y=(F(1),F(-1),F(1),F(-1))
        for k in range(1,9):
            assert formula(y,rho,F(1),k)[1] < formula(y,rho,F(0),k)[1]
            count+=1
    print('PASS:',count,'exact rational objective/norm/optimality identities, horizons through 5 and 8')

if __name__=='__main__':
    main()
