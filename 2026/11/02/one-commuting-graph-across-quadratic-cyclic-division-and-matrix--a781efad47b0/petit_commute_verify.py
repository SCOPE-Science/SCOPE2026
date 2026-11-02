#!/usr/bin/env python3
"""Finite-field exhaustive checks of the quadratic Petit commuting formula."""

def gf(p,coeff):
    n=len(coeff); size=p**n
    def digits(x):
        z=[]
        for _ in range(n): z.append(x%p);x//=p
        return z
    def encode(z):return sum((int(v)%p)*p**i for i,v in enumerate(z[:n]))
    tab=[digits(i) for i in range(size)]
    def add(a,b):return encode([(tab[a][i]+tab[b][i])%p for i in range(n)])
    def neg(a):return encode([-x for x in tab[a]])
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):
        x=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):x[i+j]=(x[i+j]+tab[a][i]*tab[b][j])%p
        for j in range(2*n-2,n-1,-1):
            for k in range(n):x[j-n+k]=(x[j-n+k]-x[j]*coeff[k])%p
        return encode(x)
    def power(a,e):
        z=1
        while e:
            if e&1:z=mul(z,a)
            a=mul(a,a);e//=2
        return z
    return size,add,sub,mul,power

def run(q,p,poly):
    N,add,sub,mul,powr=gf(p,poly)
    assert N==q*q
    sigma=[powr(x,q) for x in range(N)]
    F=[x for x in range(N) if sigma[x]==x]
    assert len(F)==q
    norm=lambda x:mul(x,sigma[x])
    aparams=[next(x for x in F if x!=0),next(x for x in range(N) if x not in F)]
    pairs=[(u,v) for u in range(N) for v in range(N)]
    def prod(z,w,a):
        u,v=z;x,y=w
        return add(mul(u,x),mul(a,mul(v,sigma[y]))),add(mul(u,y),mul(v,sigma[x]))
    for a in aparams:
        zcenter=0; counted=0
        for z in pairs:
            u,v=z
            if v==0 and u in F:expected=set(pairs)
            else:expected={(add(mul(c,u),f),mul(c,v)) for c in F for f in F}
            assert len(expected) in (q*q,q**4)
            actual={w for w in pairs if prod(z,w,a)==prod(w,z,a)}
            assert actual==expected,(q,a,z)
            counted+=len(actual)
            if len(actual)==q**4:zcenter+=1
        assert zcenter==q
        assert counted==q**6+q**5-q**3
        if a not in F:
            # Proper nonassociative algebra has non-subalgebra centralizers.
            z=(0,1)
            assert prod(z,z,a) not in {(add(mul(c,z[0]),f),mul(c,z[1])) for c in F for f in F}
        print(f'GF({q}) coefficient={"associative" if a in F else "proper"} algebra_elements={len(pairs)} central={zcenter} commuting_pairs={counted} cliques={q*q+q+1} clique_size={q*q-q}')

def main():
    run(2,2,[1,1])             # F4: x^2+x+1
    run(3,3,[1,0])             # F9: x^2+1
    run(4,2,[1,1,0,0])         # F16: x^4+x+1
    run(5,5,[2,0])             # F25: x^2+2
    print('VERIFY_OK')
if __name__=='__main__':main()
