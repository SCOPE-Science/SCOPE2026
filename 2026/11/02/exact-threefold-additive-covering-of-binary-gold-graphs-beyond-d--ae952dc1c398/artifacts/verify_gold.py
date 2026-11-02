#!/usr/bin/env python3
"""Exact finite-field verification of additive Gold graph sumsets."""
from math import gcd

def poly_mod(a,p):
    while a and a.bit_length() >= p.bit_length():
        a ^= p << (a.bit_length()-p.bit_length())
    return a

def poly_gcd(a,b):
    while b: a,b=b,poly_mod(a,b)
    return a

def mul(a,b,m,pol):
    v=0; q=1<<m
    while b:
        if b&1:v^=a
        b>>=1;a<<=1
        if a&q:a^=pol
    return v

def square(a,m,pol):return mul(a,a,m,pol)

def poly_irred(pol,m):
    x=2
    for _ in range(m): x=poly_mod(square(x,m,pol),pol)
    if x!=poly_mod(2,pol):return False
    for d in range(1,m):
        if m%d==0:
            # All proper divisors are checked, an intentionally redundant irreducibility test.
            y=poly_mod(2,pol)
            for _ in range(d):y=poly_mod(square(y,m,pol),pol)
            if poly_gcd(pol,y^poly_mod(2,pol))!=1:return False
    return True

def run():
    polys={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011,7:0b10000011,8:0x11b}
    cases=0; full=0; odd=0
    for m,pol in polys.items():
        assert poly_irred(pol,m),(m,pol)
        q=1<<m
        for r in range(1,m+1):
            q0=1<<gcd(m,r); n=m//gcd(m,r)
            frob=list(range(q))
            for _ in range(r): frob=[square(u,m,pol) for u in frob]
            distribution=[0]*q
            for u in range(q):
                for v in range(q):
                    w=mul(frob[u],v,m,pol)^mul(u,frob[v],m,pol)
                    distribution[w]+=1
            # Independently form all two-point sums from the original graph.
            pvals=[mul(u,frob[u],m,pol) for u in range(q)]
            pairs={(x^y,pvals[x]^pvals[y]) for x in range(q) for y in range(q)}
            assert len(pairs)==1+(q-1)*q//q0,(m,r,len(pairs))
            image={i for i,c in enumerate(distribution) if c}
            if n==1:
                assert image=={0}
            elif n==2:
                subfield={u for u in range(q) if frob[u]==u}
                assert len(subfield)==q0 and image==subfield
            else:
                assert len(image)==q,(m,r,n,len(image),q)
                full+=1
            if n%2==1:
                assert distribution[0]==q+(q-1)*q0
                assert all(c==q-q0 for c in distribution[1:])
                odd+=1
            cases+=1
    print('VERIFY_OK exact_gold_cases=%d full_cover_cases=%d odd_fiber_cases=%d'%(cases,full,odd))
if __name__=='__main__':run()
