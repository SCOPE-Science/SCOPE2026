#!/usr/bin/env python3
"""Independent root-count verifier for cubic Möbius correlations over binary fields.
Run: python3 verify_cubic_mobius.py
Only finite test fields are checked; the general formula requires the algebraic proof.
"""
from itertools import combinations

def mul(x, y, mod, m):
    z = 0
    while y:
        if y & 1:
            z ^= x
        x <<= 1
        if x & (1 << m):
            x ^= mod
        y >>= 1
    return z

def pw(x, n, mod, m):
    z=1
    while n:
        if n&1: z=mul(z,x,mod,m)
        x=mul(x,x,mod,m)
        n>>=1
    return z

def mu_cubic(a,b,c,q,mod,m):
    # Factor-pattern test from all roots and direct squarefreeness test.
    roots=0
    repeated=False
    for t in range(q):
        f=mul(mul(t,t,mod,m),t,mod,m)^mul(a,mul(t,t,mod,m),mod,m)^mul(b,t,mod,m)^c
        if f==0:
            roots+=1
            # derivative is t*t+b, computed at the root, not by a discriminant.
            if mul(t,t,mod,m)^b ==0:
                repeated=True
    if repeated:
        return 0
    assert roots in (0,1,3),(a,b,c,roots)
    return 1 if roots==1 else -1

def derivative_roots(shifts,q,mod,m):
    p=[1]
    for c in shifts:
        out=[0]*(len(p)+1)
        for j,coef in enumerate(p):
            out[j]^=mul(coef,c,mod,m)
            out[j+1]^=coef
        p=out
    roots=0
    for x in range(q):
        v=0
        for j in range(1,len(p),2):
            v ^= mul(p[j],pw(x,j-1,mod,m),mod,m)
        roots+=(v==0)
    return roots

def run_field(m,mod,sets):
    q=1<<m
    assert all(pw(x,q-1,mod,m)==1 for x in range(1,q))
    signs=[[[mu_cubic(a,b,c,q,mod,m) for c in range(q)] for b in range(q)] for a in range(q)]
    checked=0
    for shifts in sets:
        assert len(shifts)==len(set(shifts)) and len(shifts)>0
        total=sum(__import__('math').prod(signs[a][b][c^s] for s in shifts)
                  for a in range(q) for b in range(q) for c in range(q))
        rhs=q*q*derivative_roots(shifts,q,mod,m)
        assert total==rhs,(q,shifts,total,rhs)
        checked+=1
    return checked,q**3*checked

def main():
    configs=[(1,0b11,[s for k in range(1,3) for s in combinations(range(2),k)]),
             (3,0b1011,[s for k in range(1,9) for s in combinations(range(8),k)]),
             (5,0b100101,[(0,),(0,1),(0,1,2),(0,1,2,3),
                          (0,1,2,4),(0,1,2,3,4),(0,1,2,3,4,5),
                          (0,1,2,3,4,5,6,7),(0,1,2,4,8,16),
                          (0,1,3,5,7,9,11,13,15)])]
    tests=terms=0
    for m,mod,sets in configs:
        c,n=run_field(m,mod,sets)
        print('PASS field_size',1<<m,'shift_sets',c,'cubic_terms',n)
        tests+=c;terms+=n
    # Odd-extension assumption is necessary: q=4, two shifts fail.
    q=4;m=2;mod=0b111
    signs=[[[mu_cubic(a,b,c,q,mod,m) for c in range(q)] for b in range(q)] for a in range(q)]
    exceptional=sum(signs[a][b][c]*signs[a][b][c^1] for a in range(q) for b in range(q) for c in range(q))
    assert exceptional==32 and derivative_roots((0,1),q,mod,m)==0
    print('VERIFY_OK shift_sets',tests,'cubic_terms',terms,'sharp_even_degree_control',exceptional)

if __name__=='__main__':main()
