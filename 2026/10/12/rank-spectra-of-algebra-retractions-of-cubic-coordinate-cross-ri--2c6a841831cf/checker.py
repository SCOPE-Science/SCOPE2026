#!/usr/bin/env python3
"""Exhaustive finite-field checks of the retraction-rank polynomial.
Independent search of generator-image coefficients in the quotient algebra.
"""
from collections import Counter
from itertools import product
from math import comb


def add(a,b,q):
    if q == 4:
        return a ^ b
    return (a+b)%q


def mul(a,b,q):
    if q == 4:
        x=0
        for t in range(2):
            if (b>>t)&1: x ^= a << t
        if x & 8: x ^= 12 # x^3=x(x+1)=x^2+x in GF4
        if x & 4: x ^= 7 # x^2=x+1
        return x
    return (a*b)%q


def dot(x,y,q):
    z=0
    for a,b in zip(x,y): z=add(z,mul(a,b,q),q)
    return z


def matvec(cols,v,q):
    return [dot(row,v,q) for row in cols]


def check_exhaustive(n,q):
    vectors=list(product(range(q),repeat=n))
    projections=Counter()
    # Encode the images x_i -> linear-coordinate vector p_i, quadratic vector h_i.
    # The generated map sends x_i^2 -> componentwise squares of p_i.
    Ps=[]
    for columns in product(vectors,repeat=n):
        # distinct source generators must multiply to zero
        if any(any(mul(columns[i][j],columns[k][j],q) for j in range(n))
               for i in range(n) for k in range(i+1,n)):
            continue
        if any(tuple(sum_vectors(columns,columns[i],q)) != columns[i] for i in range(n)):
            continue
        Ps.append(columns)
    for P in Ps:
        roots=sum(1 for i in range(n) if P[i][i] == 1 and all(P[j][i] == 0 for j in range(n) if j != i))
        # Column i of P gives image of x_i. Need rank by pivot-candidates:
        r=matrank(P,q)
        for H in product(vectors,repeat=n):
            # Idempotence on the source x_i: F(F(x_i)) = F(x_i).
            ok=True
            for i in range(n):
                # linear term P(P(x_i))
                z1=sum_vectors(P,P[i],q)
                # quadratic term H(P(x_i)) + R(H(x_i))
                z2=sum_vectors(H,P[i],q)
                for j in range(n):
                    for a in range(n):
                        z2[j]=add(z2[j],mul(H[i][a],mul(P[a][j],P[a][j],q),q),q)
                if tuple(z1)!=P[i] or tuple(z2)!=H[i]:
                    ok=False
                    break
            if not ok: continue
            projections[1+2*r]+=1
    expected={1+2*r:comb(n,r)*(1+r*(q-1))**(n-r)*q**(2*r*(n-r)) for r in range(n+1)}
    assert dict(projections)==expected,(n,q,dict(projections),expected)
    return expected


def sum_vectors(columns,coeff,q):
    n=len(columns)
    return [sum_field([mul(coeff[i],columns[i][j],q) for i in range(n)],q)
            for j in range(n)]


def sum_field(values,q):
    z=0
    for v in values:z=add(z,v,q)
    return z


def matrank(columns,q):
    M=[list(row) for row in zip(*columns)]
    n=len(M); r=0
    for col in range(n):
        pivot=next((i for i in range(r,n) if M[i][col]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        inv=next(a for a in range(1,q) if mul(a,M[r][col],q)==1)
        M[r]=[mul(inv,x,q) for x in M[r]]
        for i in range(n):
            if i!=r and M[i][col]:
                coeff=M[i][col]
                M[i]=[add(M[i][j],neg(mul(coeff,M[r][j],q),q),q) for j in range(n)]
        r+=1
    return r


def neg(a,q):
    if q==4:return a
    return (-a)%q


def main():
    for n,q in ((1,2),(2,2),(2,3),(2,4),(3,2)):
        r=check_exhaustive(n,q)
        print(f'F_{q} n={n}:',r,'total=',sum(r.values()))
    print('VERIFY_OK')

if __name__=='__main__':main()
