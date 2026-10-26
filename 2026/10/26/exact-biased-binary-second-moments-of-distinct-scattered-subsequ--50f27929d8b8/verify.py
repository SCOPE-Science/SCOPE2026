#!/usr/bin/env python3
"""Independent exact enumerations and moment recurrence checks for a binary-word statistic."""
from fractions import Fraction as Q
from itertools import product

def count_direct(word):
    subseqs={''}
    for letter in word:
        subseqs|={s+letter for s in tuple(subseqs)}
    return len(subseqs)

def predicted(p,n):
    t=p*(1-p)
    m=[Q(4),Q(9),Q(16)+18*t]
    for _ in range(3,max(3,n+1)):
        m.append(3*m[-1]-(3-5*t)*m[-2]+(1-3*t)*m[-3])
    # mean C+1 via expectation update, independent of the second moment update
    u=v=Q(1)
    for _ in range(n):
        u,v=u+(1-p)*v,v+p*u
    return u+v,m[n]

cases=0
for p in (Q(1,4),Q(1,3),Q(2,5),Q(1,2),Q(3,4)):
    for n in range(11):
        mean=Q(0);second=Q(0)
        for word in product('01',repeat=n):
            prob=p**word.count('1')*(1-p)**word.count('0')
            h=count_direct(word)+1
            mean+=prob*h
            second+=prob*h*h
            cases+=1
        a,b=predicted(p,n)
        assert (mean,second)==(a,b),(p,n,mean,second,a,b)
        assert second-mean**2>=0
try:
    import sympy as sp
    p,l=sp.symbols('p l'); q=1-p
    T=sp.Matrix([[1,2*q,q],[p,1,q],[p,2*p,1]])
    assert sp.expand(T.charpoly(l).as_expr()-((l-1)**3-5*p*q*l+3*p*q))==0
    symbolic=True
except ImportError:
    symbolic=False
print('VERIFY_OK independent_full_subsequence_sets=',cases,' rational_biases=5 lengths=0..10 symbolic=',symbolic,sep='')
