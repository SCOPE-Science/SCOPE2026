#!/usr/bin/env python3
"""Exact-check order-four de Bruijn palindrome transition probabilities."""
from fractions import Fraction
from itertools import product
from collections import Counter

def all_cycles(q=2,k=4):
    used=set();s=[0]*(k-1)
    def rec():
        if len(used)==q**k:
            yield tuple(s[:q**k]);return
        for a in range(q):
            e=tuple(s[-(k-1):])+(a,)
            if e not in used:
                used.add(e);s.append(a)
                yield from rec()
                s.pop();used.remove(e)
    yield from rec()

def theoretical(q,a,b,c):
    if a==b==c:return Fraction(0)
    x=lambda A,B:int(A==B)
    R=1-Fraction(1,q)-Fraction(x(a,c),q)+Fraction(2*x(a,c)-x(b,c)-x(a,b),q*q)+Fraction(2*x(a,b)-2,q**3)
    return R/Fraction(q-1)

def cofactor_prob(q,a,b,c):
    import sympy as sp
    verts=list(product(range(q),repeat=3));idx={x:i for i,x in enumerate(verts)}
    N=len(verts);L=sp.zeros(N)
    for u in verts:
        i=idx[u]
        for z in range(q):
            j=idx[u[1:]+(z,)];L[i,i]+=1;L[i,j]-=1
    s=(a,b,c);v=(b,c,b);t=(c,b,a)
    M=L.copy();M[idx[s],idx[v]]+=1;M[idx[s],idx[t]]-=1
    M[idx[v],idx[v]]-=1;M[idx[v],idx[t]]+=1
    tr=L[:N-1,:N-1].det(method='domain-ge')
    tprime=M[:N-1,:N-1].det(method='domain-ge')
    return sp.Rational(tprime,tr*(q-1)),tr

def main():
    seqs=set();counts=Counter();pc=Counter()
    for x in all_cycles():
        # Canonically rotate to its unique 0000 factor.
        pos=next(i for i in range(len(x)) if all(x[(i+j)%len(x)]==0 for j in range(4)))
        x=x[pos:]+x[:pos]
        if x in seqs:continue
        seqs.add(x)
        n=len(x);cnt=0
        for i in range(n):
            p=tuple(x[(i+j)%n] for j in range(5))
            if p==p[::-1]:pc[p]+=1;cnt+=1
        counts[cnt]+=1
    assert len(seqs)==16 and counts==Counter({0:8,2:8}),(len(seqs),counts)
    for a,b,c in product(range(2),repeat=3):
        actual=Fraction(pc[(a,b,c,b,a)],len(seqs))
        assert actual==theoretical(2,a,b,c),(a,b,c,actual,theoretical(2,a,b,c))
    print('BINARY_EXHAUSTIVE_OK',len(seqs),dict(counts))
    for q in (2,3):
        for name,abc in [('equal_a_b',(0,0,1)),('equal_a_c',(0,1,0)),('equal_b_c',(1,0,0))]+([('all_distinct',(0,1,2))] if q>=3 else []):
            actual,t=cofactor_prob(q,*abc)
            expect=theoretical(q,*abc)
            assert actual==expect,(q,name,actual,expect)
            assert t==q**(q**3-4),(q,t,q**(q**3-4))
            print('TREE_CHECK',q,name,actual)
    for q in range(2,16):
        theoretical_mean=sum((theoretical(q,a,b,c) for a,b,c in product(range(q),repeat=3)),Fraction(0))
        assert theoretical_mean==q*q-2-Fraction(2,q)
    print('ALL_PALINDROME_MEAN_CHECKS_PASSED')
if __name__=='__main__':main()
