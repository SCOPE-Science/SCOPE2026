"""Exact arithmetic checks for the bursty-batch coupon collector theorem.

All tests use rational arithmetic, with independent state recursion and
inclusion--exclusion implementations for roundwise coverage probabilities.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def tail_coverage(n, b, t):
    """P(all seen by t), from subset inclusion-exclusion."""
    return sum(((-1)**j * comb(n, j) *
                (Q(1) - Q(1, b) + Q(1, b)*Q(n-j,n)**b)**t)
               for j in range(n+1))


def ordinary_coverage(n, t):
    return sum(((-1)**j*comb(n,j)*Q(n-j,n)**t)
               for j in range(n+1))


def transitions(n, b, seen):
    probs = [Q(0)]*(n+1)
    probs[seen] += Q(b-1,b)
    for tup in product(range(n), repeat=b):
        nxt = seen+len(set(x for x in tup if x >= seen))
        probs[nxt] += Q(1,b*n**b)
    assert sum(probs) == 1
    return probs


def mean_state(n,b):
    E=[Q(0)]*(n+1)
    for s in range(n-1,-1,-1):
        P=transitions(n,b,s)
        E[s]=(1+sum(P[u]*E[u] for u in range(s+1,n+1)))/(1-P[s])
    return E[0]


def mean_residue(n,b):
    # Independent G_j geom(j/n), with support 1,2,...; Fourier-free residue convolution.
    mass=[Q(1)]+[Q(0)]*(b-1)
    for j in range(1,n+1):
        p=Q(j,n); q=1-p
        # residue law P(G mod b = r) = p*q^(k-1)/(1-q^b), k in 1..b
        residues=[Q(0)]*b
        for k in range(1,b+1):
            residues[k%b]=p*q**(k-1)/(1-q**b)
        nxt=[Q(0)]*b
        for a in range(b):
            for c in range(b):
                nxt[(a+c)%b]+=mass[a]*residues[c]
        mass=nxt
    assert sum(mass)==1
    delta=sum(mass[r]*((b-r)%b) for r in range(b))
    return sum(Q(n,j) for j in range(1,n+1))+delta, delta


def cdf_state(n,b,t):
    tr=[transitions(n,b,s) for s in range(n+1)]
    f=[Q(1)]+[Q(0)]*n
    for _ in range(t):
        g=[Q(0)]*(n+1)
        for s in range(n+1):
            for u in range(s,n+1):
                g[u]+=f[s]*tr[s][u]
        f=g
    return f[n]


def main():
    checks=0
    for n in range(2,7):
        for b in range(2,5):
            m,delta=mean_residue(n,b)
            assert m==mean_state(n,b)
            checks+=1
            assert 0<delta<b-1
            checks+=1
            for t in range(0,11):
                assert tail_coverage(n,b,t)==cdf_state(n,b,t)
                checks+=1
            assert tail_coverage(n,b,n-1)>ordinary_coverage(n,n-1)==0
            checks+=1
    for n in range(2,41):
        _,delta=mean_residue(n,2)
        assert delta == (Q(1)-Q((-1)**n,comb(2*n-1,n)))/2
        checks+=1
    print(f'PASS {checks} independent exact rational comparisons')

if __name__=='__main__':
    main()
