#!/usr/bin/env python3
"""Independent finite-cylinder checks for group-valued difference processes.

Enumerates source words directly and separately evaluates the conditional
orientation entropy. Finite checks do not certify asymptotic convergence.
"""
from fractions import Fraction
from itertools import product, permutations
from math import log2


def entropy(probabilities):
    return -sum(float(w) * log2(float(w)) for w in probabilities if w)


def cyclic(n):
    symbols = tuple(range(n))
    return symbols, lambda a, b:(a+b)%n, lambda a:(-a)%n, 0


def symmetric_three():
    symbols = tuple(permutations(range(3)))
    identity = (0,1,2)
    return symbols, lambda a,b:tuple(a[b[j]] for j in range(3)), lambda a:tuple(a.index(j) for j in range(3)), identity


def weight(word, law):
    acc=Fraction(1)
    for v in word:
        acc*=law[v]
    return acc


def exact_cylinder(k,n,law,group):
    elements,mul,inv,_=group
    values={}
    for word in product(elements,repeat=n+k):
        p=weight(word,law)
        if not p:
            continue
        out=tuple(mul(inv(word[i]),word[i+k]) for i in range(n))
        values[out]=values.get(out,Fraction(0))+p
    assert sum(values.values())==1
    return entropy(values.values())


def ambiguity(L,law,group):
    elements,mul,_,_=group
    total=0.0
    for word in product(elements,repeat=L):
        p=weight(word,law)
        if not p:continue
        weights=[weight([mul(h,x) for x in word],law) for h in elements]
        v=sum(weights)
        assert v>0
        total+=float(p)*entropy([w/v for w in weights])
    return total


def output_entropy_formula(k,n,law,group):
    sizes=[1+len(range(j,n,k)) for j in range(k)]
    return (n+k)*entropy(law.values())-sum(ambiguity(L,law,group) for L in sizes)


def stabilizer(law,group):
    elements,mul,_,_=group
    return [g for g in elements if all(law[mul(g,x)]==law[x] for x in elements)]


def models():
    g3=cyclic(3)
    g4=cyclic(4)
    ga=symmetric_three()
    z3={i:q for i,q in enumerate(map(Fraction, ['1/2','1/3','1/6']))}
    z4_uniform={i:Fraction(1,4) for i in range(4)}
    z4_half={i:v for i,v in enumerate(map(Fraction,['1/3','1/6','1/3','1/6']))}
    z4_generic={i:v for i,v in enumerate(map(Fraction,['1/2','1/4','1/8','1/8']))}
    el,mul,_,e=ga
    transposition=tuple([1,0,2])
    subgroup={e,transposition}
    unused=set(el)
    s3={}
    for mass in [Fraction(1,2),Fraction(1,3),Fraction(1,6)]:
        representative=next(iter(unused))
        coset={mul(h,representative) for h in subgroup}
        unused.difference_update(coset)
        for x in coset:
            s3[x]=mass/len(coset)
    assert not unused
    return [('Z3-generic',g3,z3),('Z4-uniform',g4,z4_uniform),
            ('Z4-order-two',g4,z4_half),('Z4-generic',g4,z4_generic),
            ('S3-order-two',ga,s3)]


def main():
    checks=0
    for label,group,law in models():
        H=stabilizer(law,group)
        assert H
        for k in [1,2]:
            for n in [1,2,3,4] if len(law)<=4 else [1,2,3]:
                direct=exact_cylinder(k,n,law,group)
                formula=output_entropy_formula(k,n,law,group)
                assert abs(direct-formula)<1e-10, (label,k,n,direct,formula)
                checks+=1
        assert 0<=entropy(law.values())-log2(len(H))<=log2(len(law))
        print(label,'alphabet=',len(law),'stabilizer_order=',len(H),'excess_per_chain=',
              round(entropy(law.values())-log2(len(H)),8))
    print(f'VERIFY_OK: {checks} independent group-valued finite-cylinder entropy identities across cyclic and nonabelian examples')

if __name__=='__main__':
    main()
