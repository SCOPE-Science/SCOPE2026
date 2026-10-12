#!/usr/bin/env python3
"""Exhaustive and sampled finite-field checks of rank spectra for idempotent derivations of quadratic jets."""
import itertools, random
from collections import Counter

def gauss_rank(cols,q):
    M=[list(col) for col in zip(*cols)] if cols else []
    # input columns converted to rows
    if not M:return 0
    h=len(M); w=len(M[0]); r=0
    for j in range(w):
        piv=next((i for i in range(r,h) if M[i][j]%q),None)
        if piv is None:continue
        M[r],M[piv]=M[piv],M[r]
        z=pow(M[r][j],-1,q)
        M[r]=[(z*a)%q for a in M[r]]
        for i in range(h):
            if i!=r and M[i][j]:
                a=M[i][j]; M[i]=[(M[i][k]-a*M[r][k])%q for k in range(w)]
        r+=1
        if r==h:break
    return r

def D_columns(n,q,coefs):
    quad=[(i,j) for i in range(n) for j in range(i,n)]
    N=1+n+len(quad); cols=[tuple(0 for _ in range(N))]
    # coefs list D(x_i) in m; order first n linear then quadratics
    for i in range(n): cols.append(tuple([0]+list(coefs[i])))
    for i,j in quad:
        result=[0]*N
        # reset and direct Leibniz D(x_i x_j) = D(x_i)x_j+x_iD(x_j)
        for k in range(n):
            p=quad.index(tuple(sorted((k,j))))
            result[1+n+p]=(result[1+n+p]+coefs[i][k])%q
            p=quad.index(tuple(sorted((i,k))))
            result[1+n+p]=(result[1+n+p]+coefs[j][k])%q
        cols.append(tuple(result))
    return cols

def test(n,q,exhaustive=True,samples=10000):
    quad=n*(n+1)//2; dim=n+quad
    source=itertools.product(range(q), repeat=n*dim) if exhaustive else (tuple(random.randrange(q) for _ in range(n*dim)) for _ in range(samples))
    hist=Counter(); nonids=0; tot=0
    for v in source:
        coefs=[v[i*dim:(i+1)*dim] for i in range(n)]
        cols=D_columns(n,q,coefs)
        good=all(tuple(sum(cols[i][k]*cols[k][j] for k in range(len(cols)))%q for j in range(len(cols)))==cols[i] for i in range(len(cols)))
        # previous line multiplies rows/cols? D² e_i = sum_k col_i[k] col_k ; yes j coordinate
        if good:
            rank=gauss_rank(cols,q);hist[rank]+=1
        else: nonids+=1
        tot+=1
    return hist,tot

def gaussian(n,r,q):
    a=b=1
    for i in range(r): a*=q**(n-i)-1; b*=q**(r-i)-1
    return a//b

def formula(n,q):
    h=Counter({0:1})
    if q%2:
        return h
    for r in range(1,n+1):
        u=n-r
        freedom=r*(r*(r+1)//2 +u*(u+1)//2 +u*u)
        h[r*(u+1)]+=gaussian(n,r,q)*q**(r*u+freedom)
    return h

if __name__=='__main__':
    # n=1 all odd primes and even prime
    for n,q in [(1,2),(1,3),(1,5),(2,2),(2,3)]:
        hist,tot=test(n,q)
        exp=formula(n,q)
        print('EXHAUSTIVE',n,q,tot,sorted(hist.items()),'PREDICT',sorted(exp.items()))
        assert hist==exp,(n,q,hist,exp)
    # The exceptional possibility of constant coefficients in characteristic 3,
    # n=1, is checked against the defining relation and idempotence directly.
    extra=0
    for a,b,c in itertools.product(range(3),repeat=3):
        cols=((0,0,0),(a,b,c),(0,2*a%3,2*b%3))
        good=all(tuple(sum(cols[i][k]*cols[k][j] for k in range(3))%3
                       for j in range(3))==cols[i] for i in range(3))
        extra+=good
    assert extra==1
    print('FULL_CONSTANT_CHECK_n1_p3',extra)
    # GF(4)=F2[a]/(a^2+a+1): multiplication by reduction.
    def mul4(a,b):
        z=0
        for i in range(2):
            if (b>>i)&1:z ^= a<<i
        if z&8:z ^= 0b1100  # x^3 = x^2+x; reduce (x^2+x+1)*x
        if z&4:z ^= 0b111   # x^2 = x+1
        return z
    gf4=Counter()
    for b,c in itertools.product(range(4),repeat=2):
        # D(t)=b*t+c*t^2, and D(t^2)=0 in characteristic two.
        if mul4(b,b)==b and mul4(b,c)==c:
            gf4[0 if b==c==0 else 1]+=1
    assert gf4==Counter({0:1,1:4})
    print('GF4_EXHAUSTIVE_n1',sorted(gf4.items()))
    random.seed(1938)
    for n,q,s in [(3,2,15000),(2,5,5000)]:
        hist,tot=test(n,q,False,s)
        assert set(hist).issubset(set(formula(n,q)))
        print('SAMPLED',n,q,tot,sorted(hist.items()))
    # Construct guaranteed idempotents via quadratic shears, and test ranks.
    for n in (2,3,4):
        quad=[(i,j) for i in range(n) for j in range(i,n)]
        m=len(quad)
        for r in range(n+1):
            for _ in range(30):
                H=[[random.randrange(2) for _ in range(m)] for _ in range(n)]
                coefs=[]
                for i in range(n):
                    linear=[int(i==k and i<r) for k in range(n)]
                    quadratic=[(H[i][j]*(int(i<r)+int(a<r)+int(b<r)))%2
                               for j,(a,b) in enumerate(quad)]
                    coefs.append(linear+quadratic)
                cols=D_columns(n,2,coefs)
                assert all(tuple(sum(cols[i][k]*cols[k][j] for k in range(len(cols)))%2
                                 for j in range(len(cols)))==cols[i] for i in range(len(cols)))
                assert gauss_rank(cols,2)==r*(n-r+1)
    print('SHEAR_RANK_CHECK_OK')
    print('VERIFY_OK')
