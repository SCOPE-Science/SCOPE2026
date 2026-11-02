"""Exact integer checker for sixth moments of nine-term Fourier squares.

Run: python sixth_moment_checker.py
The program computes P^3 coefficients by two independent combinatorial routes.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, permutations, product
from math import factorial

FREE=((0,2),(1,1),(1,2),(2,0),(2,1),(2,2))
TRIPLES=[]
for triple in product(range(9), repeat=3):
    i=sum(v//3 for v in triple)
    j=sum(v%3 for v in triple)
    f=[0]*6
    for v in triple:
        ij=divmod(v,3)
        if ij in FREE: f[FREE.index(ij)]+=1
    TRIPLES.append(((i,j),tuple(f),1))
MULTISETS=[]
for triple in combinations_with_replacement(range(9),3):
    i=sum(v//3 for v in triple)
    j=sum(v%3 for v in triple)
    f=[0]*6
    for v in triple:
        ij=divmod(v,3)
        if ij in FREE: f[FREE.index(ij)]+=1
    count=factorial(3)
    for x in set(triple):count//=factorial(triple.count(x))
    MULTISETS.append(((i,j),tuple(f),count))

def sixth(phases,q,ordered):
    groups=defaultdict(lambda:[0]*q)
    for ij,exponents,mult in (TRIPLES if ordered else MULTISETS):
        groups[ij][sum(a*b for a,b in zip(phases,exponents))%q]+=mult
    if q==2:
        return sum((v[0]-v[1])**2 for v in groups.values())
    if q==3:
        return sum((v[0]-v[2])**2 - (v[0]-v[2])*(v[1]-v[2]) + (v[1]-v[2])**2 for v in groups.values())
    raise ValueError('q must be 2 or 3')

def check():
    expect={2:(1641,4,19),3:(1197,2,63)}
    histograms={}
    for q in (2,3):
        histogram=Counter(); winners=[];minimum=None
        for phases in product(range(q),repeat=6):
            value=sixth(phases,q,True)
            assert value==sixth(phases,q,False),(q,phases)
            histogram[value]+=1
            if minimum is None or value<minimum:
                minimum=value;winners=[phases]
            elif value==minimum:winners.append(phases)
        assert (minimum,len(winners),len(histogram))==expect[q]
        assert sum(histogram.values())==q**6
        histograms[q]=histogram
        print(f'q={q} minimum={minimum} normalized_minimizers={winners} levels={len(histogram)} assignments={q**6}')
        print('spectrum='+repr(sorted(histogram.items())))
    return histograms

if __name__=='__main__':check()
