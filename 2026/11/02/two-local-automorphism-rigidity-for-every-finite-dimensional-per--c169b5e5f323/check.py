#!/usr/bin/env python3
"""Exhaustive independent small-field two-local test; symbolic proof is in RESULT.md."""
from itertools import product, permutations

def prod(x,y,a):
    s=[(x[i] & y[i]) for i in range(2)]
    return tuple((s[0]*a[0][j]+s[1]*a[1][j])%2 for j in range(2))

def det(a):
    return (a[0][0]*a[1][1]-a[0][1]*a[1][0])%2

def main():
    V=list(product(range(2),repeat=2))
    maps=0
    checked=0
    for flat in product(range(2),repeat=4):
        A=(flat[:2],flat[2:]);
        if det(A)==0: continue
        aut=[]
        for sigma in permutations(range(2)):
            f=lambda x,sigma=sigma: tuple(x[sigma.index(j)] for j in range(2))
            if all(f(prod(x,y,A))==prod(f(x),f(y),A) for x in V for y in V):
                aut.append(tuple(f(x) for x in V))
        assert aut
        aut=set(aut)
        two_local=set()
        for output in product(V,repeat=len(V)):
            if all(any(g[i]==output[i] and g[j]==output[j] for g in aut)
                   for i in range(len(V)) for j in range(len(V))):
                two_local.add(output)
        assert two_local==aut, (A,two_local,aut)
        maps+=len(two_local)
        checked+=1
    assert checked==6
    print('VERIFY_OK: six invertible 2x2 structure matrices over F2; all 256 maps each; '+str(maps)+' total automorphism incidences')
if __name__=='__main__': main()
