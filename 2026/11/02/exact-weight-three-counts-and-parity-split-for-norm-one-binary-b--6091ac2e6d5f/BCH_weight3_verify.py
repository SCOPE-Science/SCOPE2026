#!/usr/bin/env python3
"""Independent finite checks of a norm-one BCH weight-three formula.

Execute: python3 BCH_weight3_verify.py
Only the standard Python library is required.
"""

def multiply(a,b,modulus,m):
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&(1<<m):a^=modulus
    return out & ((1<<m)-1)

def power(a,n,modulus,m):
    out=1
    while n:
        if n&1:out=multiply(out,a,modulus,m)
        a=multiply(a,a,modulus,m)
        n//=2
    return out

def polygcd(a,b):
    while b:
        r=a
        while r and r.bit_length()>=b.bit_length():
            r^=b<<(r.bit_length()-b.bit_length())
        a,b=b,r
    return a

def irreducible(poly,m):
    x=2
    for i in range(1,m+1):
        x=multiply(x,x,poly,m)
        if i<=m//2 and m%i==0 and polygcd(x^2,poly)!=1:return False
    return x==2

def run():
    for s in range(1,6):
        q=1<<s;m=3*s;n=q*q+q+1
        modulus=next(p for p in range((1<<m)|1,1<<(m+1),2) if irreducible(p,m))
        H={x for x in range(1,1<<m) if power(x,n,modulus,m)==1}
        assert len(H)==n
        triples={tuple(sorted((x,y,x^y))) for x in H for y in H
                  if x<y and x^y in H and x^y != y and x^y != x}
        degree_by_element={x:0 for x in H}
        for triple in triples:
            assert len(set(triple))==3
            for x in triple:degree_by_element[x]+=1
        expected_degree=q+(s%2)
        expected_triples=n*expected_degree//3
        assert len(triples)==expected_triples, (s,len(triples),expected_triples)
        assert set(degree_by_element.values())=={expected_degree},(s,set(degree_by_element.values()))
        K=len({x for x in H if x!=1 and x^1 in H})
        assert K==2*expected_degree
        Fq={x for x in range(1<<m) if power(x,q,modulus,m)==x}
        assert len(Fq)==q
        image=set()
        for t in Fq-{0,1}:
            t2=multiply(t,t,modulus,m)
            t3=multiply(t2,t,modulus,m)
            denominator=t2^t
            a=multiply(t3^t^1,power(denominator,q-2,modulus,m),modulus,m)
            assert a in Fq
            image.add(a)
            u=power(t^1,q-2,modulus,m)
            assert u not in (0,1)
            u2=multiply(u,u,modulus,m)
            u3=multiply(u2,u,modulus,m)
            phi_u=multiply(u3^u^1,power(u2^u,q-2,modulus,m),modulus,m)
            assert phi_u==a, (s,t,u,a,phi_u)
        expected_image=(q-2)//3 if s%2 else (q+2)//3
        assert len(image)==expected_image, (s,len(image),expected_image)
        print(f's={s} q={q} n={n} modulus={hex(modulus)} K={K} degree={expected_degree} A3={len(triples)} reducible_cubics={len(image)} irreducible_cubics={q-len(image)}')
    print('NORM_ONE_BCH_WEIGHT3_VERIFY_OK')

if __name__=='__main__':run()
