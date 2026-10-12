"""Exact two-demand chain-transport identity and critical crossover checks.

Run: python3 verify.py. Standard library only.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, exp, isclose


def t_s(s):
    assert s >= 3
    h = s // 2
    if s % 2:
        min_part = h * (h + 1) * (4 * h - 1) // 6
    else:
        min_part = h * (h - 1) * (4 * h + 1) // 6
    return 2 * comb(s, 3) + min_part


def capacity_formula(n, p):
    assert n >= 4
    baseline = Fraction(4, n * (n-1)) * sum(
        (n-h)*h*p**h for h in range(1,n)
    )
    loss = Fraction(1,3*comb(n,4)) * sum(
        (n-s)*t_s(s)*p**s for s in range(3,n)
    )
    return baseline-loss,baseline,loss


def capacity_direct_outcomes(n,p):
    """Independent enumeration of matching, edge masks, and optimal feasible deliveries."""
    pairings = (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
    acc=Fraction(0)
    for points in combinations(range(n),4):
        for pairing in pairings:
            intervals = [set(range(points[i],points[j])) for i,j in pairing]
            w = [len(I) for I in intervals]
            for mask in range(1<<(n-1)):
                k=mask.bit_count()
                prob = p**k*(1-p)**(n-1-k)
                feasible=[all((mask>>e)&1 for e in I) for I in intervals]
                reward=max([0]+[w[i] for i in range(2) if feasible[i]]+
                    ([w[0]+w[1]] if all(feasible) and intervals[0].isdisjoint(intervals[1]) else []))
                acc+=prob*reward
    return acc/(3*comb(n,4))


def phi(lam):
    """High accuracy Simpson evaluation of the limiting integral."""
    m=8000
    step=1/m
    def fun(x):
        return (4*x*(1-x)-(10/3)*x**3*(1-x))*exp(-lam*x)
    return step/3*(fun(0)+fun(1)+sum((4 if j%2 else 2)*fun(j*step) for j in range(1,m)))


def capacity_float(n,p):
    baseline=4/(n*(n-1))*sum((n-h)*h*p**h for h in range(1,n))
    loss=1/(3*comb(n,4))*sum((n-s)*t_s(s)*p**s for s in range(3,n))
    return baseline-loss,loss


def main():
    checks=0
    for n in range(4,9):
        for p in (Fraction(0),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(1)):
            lhs=capacity_direct_outcomes(n,p)
            rhs,b,d=capacity_formula(n,p)
            assert lhs==rhs,(n,p,lhs,rhs)
            assert d >= 0
            checks+=1
    for s in range(3,25):
        direct=sum(min(a,c)+2*b for a in range(1,s-1)
              for b in range(1,s-a) for c in [s-a-b] if c>=1)
        assert direct==t_s(s),(s,direct,t_s(s))
        checks+=1
    for p in [Fraction(1,4), Fraction(1,3), Fraction(1,2), Fraction(3,4)]:
        target=8*float(p**3*(3+2*p)/((1-p)**4*(1+p)))
        n=2400
        _,loss=capacity_float(n,float(p))
        assert abs(n**3*loss/target-1)<0.013,(p,n**3*loss,target)
        checks+=1
    for lam in [0.0,0.2,1.0,3.0,8.0]:
        n=2400
        val,_=capacity_float(n,exp(-lam/n))
        assert abs(val/n-phi(lam))<0.001,(lam,val/n,phi(lam))
        checks+=1
    assert isclose(phi(0),0.5,abs_tol=1e-10)
    print('VERIFY_OK',checks)

if __name__=='__main__':
    main()
