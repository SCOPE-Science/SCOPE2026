"""Exact checks of doubly envy-free agents in random serial dictatorship.
Run using: python CHECK.py. Python standard library only.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import factorial, comb


def joint_probability(n, selected):
    # Compute conditional survival factors directly from independent rankings.
    chosen = set(selected)
    t = 0
    p = Q(1)
    for j in range(1,n+1):
        r = n-j+1
        if j in chosen:
            p *= Q(r,n)  # Gets overall top choice, protects prior choices too.
            t += 1
        else:
            p *= Q(r,r+t)  # Ranks best available above all protected choices.
    return p


def distribution_from_joint(n):
    # Inclusion-exclusion on all k-subsets of protected serial positions.
    factorial_moments=[sum((joint_probability(n,S) for S in combinations(range(1,n+1),k)), Q(0)) for k in range(n+1)]
    out={}
    for j in range(n+1):
        prob=sum(((-1)**(k-j)*comb(k,j)*factorial_moments[k] for k in range(j,n+1)),Q(0))
        if prob: out[j]=prob
    return out


def distribution_exhaustive(n):
    orders=list(permutations(range(n)))
    hist=Counter()
    for prefs in product(orders,repeat=n):
        ranks=[{a:t for t,a in enumerate(p)} for p in prefs]
        available=set(range(n)); assigned=[]
        for i in range(n):
            house=next(a for a in prefs[i] if a in available)
            assigned.append(house); available.remove(house)
        both=sum(assigned[i]==prefs[i][0] and
                 all(ranks[j][assigned[j]]<ranks[j][assigned[i]] for j in range(n) if j!=i)
                 for i in range(n))
        hist[both]+=1
    return {k:Q(v,factorial(n)**n) for k,v in hist.items()}


def main():
    for n in range(1,13):
        for k in range(n+1):
            target=Q(factorial(k),n**k)
            for sel in combinations(range(1,n+1),k):
                assert joint_probability(n,sel)==target,(n,sel)
        law=distribution_from_joint(n)
        mean=sum((j*p for j,p in law.items()),Q(0))
        variance=sum((j*j*p for j,p in law.items()),Q(0))-mean**2
        assert mean==1 and variance==Q(2*(n-1),n)
        if n<=4:
            assert law==distribution_exhaustive(n),(n,law)
    assert distribution_from_joint(3)=={0:Q(4,9),1:Q(1,3),3:Q(2,9)}
    print('PASS: all joint k-subset identities for n=1..12')
    print('PASS: entire distribution and first two moments for n=1..12')
    print('PASS: independent exhaustive profiles n=1..4 (331776 profiles at n=4)')

if __name__=='__main__':main()
