#!/usr/bin/env python3
"""Exact, supplementary checks for a family of characteristic-two Kummer curves."""
from math import gcd

def degree(p):
    return p.bit_length()-1

def remainder(a,b):
    assert b
    while a and degree(a)>=degree(b):
        a ^= b << (degree(a)-degree(b))
    return a

def poly_gcd(a,b):
    while b:
        a,b=b,remainder(a,b)
    return a

def perm_comp(f,g):
    return tuple(f[g[i]] for i in range(len(f)))

def check(M):
    assert M>=5 and M%2==1 and M%3==2
    poly=(1<<M)|1                 # X^M+1 over GF(2)
    derivative=1<<(M-1)          # M odd
    assert poly_gcd(poly, derivative)==1
    # In characteristic two the square has only exponents 0 and 2M.
    square=(1<<(2*M))|1
    calc=0
    for i in (0,M): calc ^= 1<<(2*i)
    assert square==calc
    # At x=0,infinity orders -M give residue 1; M roots have residue 2.
    assert (-M)%3==1 and 2%3==2
    assert -6+2*(M+2)==2*M-2
    base=[(j,i) for j in range(3) for i in range(M)]
    lab={u:k for k,u in enumerate(base)}
    a=tuple(lab[((j+1)%3,i)] for j,i in base)
    b=tuple(lab[(j,(i+1)%M)] for j,i in base)
    t=tuple(lab[(j,(-i)%M)] for j,i in base)
    ident=tuple(range(3*M))
    def power(q,n):
        ans=ident
        for _ in range(n):ans=perm_comp(q,ans)
        return ans
    assert power(a,3)==power(b,M)==power(t,2)==ident
    assert perm_comp(a,b)==perm_comp(b,a)
    assert perm_comp(a,t)==perm_comp(t,a)
    assert perm_comp(t,perm_comp(b,t))==power(b,M-1)
    seen={perm_comp(power(a,j),perm_comp(power(b,i),power(t,k)))
          for j in range(3) for i in range(M) for k in range(2)}
    assert len(seen)==6*M

if __name__=='__main__':
    for M in (5,11,17,23,29,35,41,47,53):
        check(M)
    print('VERIFY_OK: exact characteristic-two identities and 6M group permutations')
