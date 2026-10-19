"""Independent exact small-volume and analytic identity checks for dimer jamming."""
from functools import lru_cache
from fractions import Fraction
from math import exp, sqrt, pi
import random


def state_law(A, B, C):
    @lru_cache(None)
    def rec(a, b, c):
        weights = [a*b, a*c, b*c, c*(c-1)//2]
        total = sum(weights)
        if not total:
            return {a+b+c: Fraction(1)}
        children = [(a-1,b-1,c), (a-1,b,c-1), (a,b-1,c-1), (a,b,c-2)]
        ans = {}
        for weight, child in zip(weights, children):
            if not weight: continue
            for residual, prob in rec(*child).items():
                ans[residual] = ans.get(residual, Fraction(0)) + prob * Fraction(weight,total)
        return ans
    return rec(A,B,C)


def graph_law(a,b,c):
    N = a+b+c
    group = [0]*a + [1]*b + [2]*c
    edges = [(i,j) for i in range(N) for j in range(i+1,N)
             if not (group[i] == group[j] and group[i] != 2)]
    @lru_cache(None)
    def rec(mask):
        live = [(i,j) for i,j in edges if mask & (1<<i) and mask & (1<<j)]
        if not live: return {mask.bit_count():Fraction(1)}
        ans={}
        for i,j in live:
            child=mask & ~(1<<i) & ~(1<<j)
            for k,p in rec(child).items():
                ans[k]=ans.get(k,Fraction(0))+p/Fraction(len(live))
        return ans
    return rec((1<<N)-1)


def exact_inequality_check():
    # Algebraic upper bounds: for L>=10, C<=L and AB<=(A+B)^2/4,
    # generator of 2C/L at most -C/(2N);
    # generator of N*C/L^2 at most (N*C/L^2)*(C+7)/N.
    for L in range(10,2000):
        f = Fraction(L*L,2*(L-2))-Fraction(L*L,L-1)+Fraction(L,L-1)+1
        w = (Fraction(L*L*(L-1),(L-2)**2)-Fraction(L**3,(L-1)**2)
             +Fraction(L*(3*L-2),(L-1)**2)+1)
        assert f <= -Fraction(L,4)
        assert w <= 7
        assert Fraction(L*L-10*L+8,4*(L-2)) == -f-Fraction(L,4)
        assert (Fraction((2*L-3)*(L*L-8*L+8),(L-2)**2*(L-1)) == 7-w)
    print('Exact generator-bound identities: PASS (integer L=10..1999 and factored algebra).')


def variance(alpha):
    gamma=1-2*alpha
    return (2*alpha**2/gamma) * (exp(-gamma/alpha)-(1+gamma/alpha)*exp(-2*gamma/alpha))


def simulate(a,b,c,rng):
    while True:
        weights=(a*b,a*c,b*c,c*(c-1)//2)
        total=sum(weights)
        if not total: return a+b+c
        x=rng.randrange(total)
        if x<weights[0]: a-=1;b-=1
        elif x<sum(weights[:2]): a-=1;c-=1
        elif x<sum(weights[:3]): b-=1;c-=1
        else: c-=2


def main():
    exact_inequality_check()
    for abc in [(1,1,2),(2,2,2),(2,2,4),(3,3,2)]:
        first=state_law(*abc);second=graph_law(*abc)
        assert first==second,(abc,first,second)
        assert all(k%2==0 for k in first)
        print(f'Exact count-chain / labeled-graph agreement: {abc}: '+
              ', '.join(f'{k}:{v}' for k,v in sorted(first.items())))
    for alpha in (.2,.3,.4):
        gamma=1-2*alpha
        v=variance(alpha)
        assert v>0
        # Independent trapezoidal quadrature of the martingale bracket.
        steps=50000; dx=1/alpha/steps
        integral=dx*sum((1-(i+.5)*alpha*dx)*exp(gamma*(i+.5)*dx)
                        for i in range(steps))
        quad=exp(-2*gamma/alpha)*2*alpha*gamma*integral
        assert abs(quad-v)<2e-9,(alpha,quad,v)
        print(f'Variance integral alpha={alpha}: {v:.12f}; E|Z|={sqrt(2*v/pi):.12f}')
    rng=random.Random(20261015)
    for N,alpha,trials in [(1000,.3,1500),(2000,.4,1000)]:
        a=round(N*alpha);c=N-2*a
        counts=[simulate(a,a,c,rng) for _ in range(trials)]
        mean=sum(counts)/trials/sqrt(N)
        target=sqrt(2*variance(alpha)/pi)
        # Wide probabilistic guard, only a sanity check, not a proof.
        assert abs(mean-target) < .09
        print(f'Seeded simulation N={N}, alpha={alpha}: scaled mean={mean:.5f}, limit={target:.5f}')
    print('All independent checks passed.')

if __name__=='__main__': main()
