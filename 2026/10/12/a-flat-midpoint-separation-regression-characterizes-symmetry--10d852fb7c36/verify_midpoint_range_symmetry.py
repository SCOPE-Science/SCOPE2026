#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

def is_symmetric(support, weights):
    total=sum(weights)
    mu=sum(Fraction(x*w,total) for x,w in zip(support,weights))
    mass={Fraction(x):Fraction(w,total) for x,w in zip(support,weights)}
    for x,p in mass.items():
        if mass.get(2*mu-x, Fraction(0)) != p:
            return False
    return True

def flat_conditional_sum(support, weights):
    total=sum(weights)
    probs=[Fraction(w,total) for w in weights]
    by_r={}
    for i,x in enumerate(support):
        for j,y in enumerate(support):
            p=probs[i]*probs[j]
            r=abs(Fraction(x)-Fraction(y))
            s=Fraction(x)+Fraction(y)
            if r not in by_r:
                by_r[r]=[Fraction(0),Fraction(0)]
            by_r[r][0]+=p
            by_r[r][1]+=p*s
    vals=[num/den for den,num in by_r.values()]
    return all(v==vals[0] for v in vals)

def run():
    grid=list(range(-3,4))
    laws=flat=sym=0
    for k in range(2,6):
        for support in combinations(grid,k):
            for weights in product((1,2,3), repeat=k):
                laws+=1
                a=flat_conditional_sum(support,weights)
                b=is_symmetric(support,weights)
                if a: flat+=1
                if b: sym+=1
                assert a==b, (support,weights,a,b)
    assert laws==9072
    assert flat==396 and sym==396
    print(f"VERIFY_OK laws={laws} flat={flat} symmetric={sym}")

if __name__=='__main__':
    run()
