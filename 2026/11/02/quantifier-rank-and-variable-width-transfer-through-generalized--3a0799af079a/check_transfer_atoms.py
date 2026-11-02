#!/usr/bin/env python3
"""Spot-check the rank-preserving atomic translation over finite odd abelian kernels."""
import itertools

def test(moduli):
    A=list(itertools.product(*(range(m) for m in moduli)))
    zero=tuple(0 for _ in moduli)
    def add(a,b):return tuple((u+v)%m for u,v,m in zip(a,b,moduli))
    def sub(a,b):return tuple((u-v)%m for u,v,m in zip(a,b,moduli))
    V=list(itertools.product(A,range(2)))
    def mul(x,y):
        a,i=x;b,j=y
        return (add(a,b) if i==0 else sub(a,b),(i+j)%2)
    for x in V:
        a,i=x
        assert (x==(zero,0) or mul(x,x)!=(zero,0)) == (i==0)
    for x,y,z in itertools.product(V,repeat=3):
        a,i=x;b,j=y;c,k=z
        expected=(i+j)%2==k and (add(a,b)==c if i==0 else add(c,b)==a)
        assert (mul(x,y)==z)==expected
    return len(V),len(V)**3
for moduli in [(3,),(5,),(3,3)]:
    N,total=test(moduli)
    print('CHECK_OK',moduli,'elements',N,'atomic_triples',total)
print('ATOM_VERIFICATION_OK')
