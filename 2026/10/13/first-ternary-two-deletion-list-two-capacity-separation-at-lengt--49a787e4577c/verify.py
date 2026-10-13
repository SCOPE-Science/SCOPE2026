#!/usr/bin/env python3
"""Verify finite ternary two-deletion list-code separation using exact incidence arithmetic."""
from fractions import Fraction
from itertools import combinations, product
from collections import Counter
from pathlib import Path
import json
import subprocess

ROOT=Path(__file__).resolve().parent

def shadow(word):
    return {tuple(word[i] for i in I) for I in combinations(range(len(word)),len(word)-2)}

def code(n,L):
    if n==2:
        return [(0,)*2] if L==1 else [(0,0),(1,1)]
    lines=(ROOT/f'code_{n}_{L}.txt').read_text().splitlines()
    return [tuple(map(int,w)) for w in lines]

def incidence(n):
    W=list(product(range(3),repeat=n))
    T=list(product(range(3),repeat=n-2))
    S=[shadow(w) for w in W]
    return W,T,S

TARGET={(2,1):1,(2,2):2,(3,1):3,(3,2):4,(4,1):3,(4,2):6,(5,1):6,(5,2):12,(6,1):11,(6,2):24}

def cert(n,L,W,T,S):
    data=json.loads((ROOT/'dual_certificates.json').read_text())[f'{n}:{L}']
    y={t:Fraction(a) for t,a in zip(T,data['y'])}
    z={int(j):Fraction(a) for j,a in data['z'].items()}
    assert len(y)==len(T)
    assert all(a>=0 for a in y.values()) and all(a>=0 for a in z.values())
    for j,s in enumerate(S):
        assert sum((y[t] for t in s),Fraction(0))+z.get(j,Fraction(0))>=1
    bound=L*sum(y.values(),Fraction(0))+sum(z.values(),Fraction(0))
    assert bound<TARGET[n,L]+1
    print('DUAL',n,L,str(bound))

def main():
    for n in range(2,7):
        W,T,S=incidence(n)
        for L in (1,2):
            C=code(n,L)
            assert len(C)==TARGET[n,L] and len(C)==len(set(C))
            counts=Counter(t for c in C for t in shadow(c))
            assert max(counts.values())<=L
            if n<=5:cert(n,L,W,T,S)
    # A unique two-deletion code is a clique in the graph of disjoint shadows.
    W,T,S=incidence(6)
    edges=[]
    for i,s in enumerate(S):
        edges.append([j for j,t in enumerate(S) if j!=i and s.isdisjoint(t)])
    assert all((j in edges[i])==(i in edges[j]) for i in range(len(W)) for j in edges[i])
    data='729\n'+'\n'.join(' '.join(map(str,row)) for row in edges)+'\n'
    subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'clique.cpp'),'-o',str(ROOT/'clique')],check=True)
    p=subprocess.run([str(ROOT/'clique')],input=data,text=True,capture_output=True,check=True,timeout=90)
    print('CLIQUE',p.stdout.strip())
    assert p.stdout.strip().startswith('best=11 ')
    print('VERIFY_OK')
if __name__=='__main__':main()
