#!/usr/bin/env python3
"""Exact checks of random-order greedy maximal independent-set laws on double stars."""
from fractions import Fraction
from itertools import permutations
from collections import Counter
from math import factorial

def formula(a,b):
    n=a+b+2
    u=Fraction(n-1,n*(a+1))
    v=Fraction(n-1,n*(b+1))
    w=1-u-v
    return (u,v,w)

def greedy(a,b,order):
    n=a+b+2
    edges={frozenset((0,1))}
    edges.update(frozenset((0,x)) for x in range(2,2+a))
    edges.update(frozenset((1,x)) for x in range(2+a,n))
    adj=[set() for _ in range(n)]
    for x,y in edges:
        adj[x].add(y); adj[y].add(x)
    chosen=set()
    for x in order:
        if not (adj[x]&chosen):chosen.add(x)
    return frozenset(chosen)

def exact(a,b):
    n=a+b+2
    c=Counter(greedy(a,b,pi) for pi in permutations(range(n)))
    Iu=frozenset([0]+list(range(2+a,n)))
    Iv=frozenset([1]+list(range(2,2+a)))
    I0=frozenset(range(2,n))
    assert set(c)=={Iu,Iv,I0}, (a,b,c)
    return tuple(Fraction(c[s],factorial(n)) for s in (Iu,Iv,I0))

def bias(a,b):
    return sum((abs(t-Fraction(1,3)) for t in formula(a,b)),Fraction(0))/2

if __name__=='__main__':
    count=0
    for a in range(1,5):
        for b in range(a,6):
            if a+b+2>9:continue
            assert formula(a,b)==exact(a,b),(a,b,formula(a,b),exact(a,b))
            count+=1
    for a in range(1,201):
        for b in range(a,201):
            assert bias(a,b)>=Fraction(1,15)
            assert (bias(a,b)==Fraction(1,15))==((a,b)==(1,2))
    assert formula(1,2)==(Fraction(2,5),Fraction(4,15),Fraction(1,3))
    assert bias(1,1)==Fraction(1,12)
    assert bias(2,2)==Fraction(1,9)
    fixed_cases=0
    for n in range(3,201):
        star_bias=Fraction(n-2,2*n)
        options=[(star_bias, ('star',n-1))]
        for a in range(1,(n-2)//2+1):
            options.append((bias(a,n-2-a), ('double',a,n-2-a)))
        minimum=min(v for v,_ in options)
        minimizers=[key for v,key in options if v==minimum]
        if n==3: predicted=Fraction(1,6); typ=('star',2)
        elif n==4: predicted=Fraction(1,12); typ=('double',1,1)
        elif n==5: predicted=Fraction(1,15); typ=('double',1,2)
        elif n==6: predicted=Fraction(1,9); typ=('double',2,2)
        else: predicted=Fraction(1,3)-Fraction(n-1,n*(n-2)); typ=('double',1,n-3)
        assert minimum==predicted and minimizers==[typ],(n,minimum,minimizers,predicted,typ)
        fixed_cases+=1
    print('ALL CHECKS PASSED')
    print('direct_permutation_profiles=',count)
    print('exact_formula_parameter_profiles=',20100)
    print('fixed_order_optimization_profiles=',fixed_cases)
    print('sharp_unique_example=(a,b)=(1,2); probability=(2/5,4/15,1/3); bias=1/15')
    print('baseline_bias_1_1=1/12; baseline_bias_2_2=1/9')
