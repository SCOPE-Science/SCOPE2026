"""Independent finite-chain verification of the hyperstar majority-rule theorem.

Python 3 standard library only. Uses exact Fraction arithmetic. Every state of
small hyperstars is solved from its first-step Markov equations; no randomness.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb


def types_from_bits(x):
    return tuple(x[1+2*j] if x[1+2*j]==x[2+2*j] else 2
                 for j in range((len(x)-1)//2))


def markov_solver(weights):
    weights=tuple(weights)
    @lru_cache(None)
    def solve(types):
        # Pair components are 0,1,or 2 (unresolved 0/1); return both hub values.
        m=len(types)
        if 2 not in types:
            ans=F(int(len(set(types))==1))
            return ans,ans
        w0=sum((weights[j] for j,t in enumerate(types) if t==0),F(0))
        w1=sum((weights[j] for j,t in enumerate(types) if t==1),F(0))
        wm=1-w0-w1
        b0=b1=F(0)
        for j,t in enumerate(types):
            if t==2:
                child=list(types);child[j]=0
                b0+=weights[j]*solve(tuple(child))[0]
                child[j]=1
                b1+=weights[j]*solve(tuple(child))[1]
        common=(w0*b0+w1*b1)/wm
        return common+b0,common+b1
    return solve


def prediction(x,weights):
    t=types_from_bits(x)
    hub=x[0]
    z={i for i,a in enumerate(t) if a==0}
    o={i for i,a in enumerate(t) if a==1}
    if z and o:return F(0)
    if not z and not o:return F(1)
    pure=z or o
    color=0 if z else 1
    return F(1) if color==hub else sum((weights[j] for j in pure),F(0))


def exact_iid(m,p):
    z=1-p
    return (z*z*(1+2*p)*(1-p*p)**(m-1)
            +p*p*(3-2*p)*(p*(2-p))**(m-1))


def run():
    checks=0
    for m in range(1,7):
        for weights in (tuple(F(1,m) for _ in range(m)),
                        tuple(F(2*(j+1),m*(m+1)) for j in range(m))):
            solve=markov_solver(weights)
            for x in product((0,1),repeat=2*m+1):
                t=types_from_bits(x)
                got=solve(t)[x[0]]
                want=prediction(x,weights)
                assert got==want,(m,weights,x,got,want)
                checks+=1
            for q in (F(0),F(1,5),F(1,2),F(2,3),F(1)):
                got=F(0)
                for x in product((0,1),repeat=2*m+1):
                    got+=solve(types_from_bits(x))[x[0]]*q**sum(x)*(1-q)**(len(x)-sum(x))
                want=exact_iid(m,q)
                assert got==want,(m,weights,q,got,want)
                checks+=1
        # Combinatorial independent binomial tally also exactly matches the formula.
        p=F(2,5);u=(1-p)**2;v=p*p;w=2*p*(1-p)
        finite=w**m
        for c in range(1,m+1):
            finite+=comb(m,c)*u**c*w**(m-c)*((1-p)+p*F(c,m))
            finite+=comb(m,c)*v**c*w**(m-c)*(p+(1-p)*F(c,m))
        assert finite==exact_iid(m,p)
        checks+=1
    print('PASS',checks,'exact rational finite-state/initial-law comparisons')

if __name__=='__main__':run()
