#!/usr/bin/env python3
"""Exact arithmetic for six genus-three quartic models over characteristic 13.

No external dependencies. All counts are exhaustive finite-field computations.
"""
from itertools import product
from math import factorial

P=13
MODULI = {1:(0,1), 2:(1,3,1), 3:(1,0,4,1)}
EXPECTED={1:(16,244,2128),2:(19,145,2128),4:(7,121,2128)}
POLYS={1:(1,2,39,52,507,338,2197),
       2:(1,5,0,-65,0,845,2197),
       4:(1,-7,0,91,0,-1183,2197)}
# Coefficient order increasing. The top three values are forced by the
# functional equation for a genus-three zeta polynomial.

def field(n):
    modulus=MODULI[n]
    one=(1,)+(0,)*(n-1)
    zero=(0,)*n
    def mul(a,b):
        v=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):
                v[i+j]=(v[i+j]+a[i]*b[j])%P
        for k in range(2*n-2,n-1,-1):
            c=v[k]
            for j in range(n):
                v[k-n+j]=(v[k-n+j]-c*modulus[j])%P
        return tuple(v[:n])
    def power(a,nexp):
        output=one
        while nexp:
            if nexp&1: output=mul(output,a)
            a=mul(a,a)
            nexp//=2
        return output
    def element(v): return tuple((v//P**j)%P for j in range(n))
    def scalar(a,c): return tuple((c*v)%P for v in a)
    def add(a,b): return tuple((x+y)%P for x,y in zip(a,b))
    return one,zero,mul,power,element,scalar,add

def polynomial_irreducibility_check():
    # For degree 2 and 3, no roots is exactly irreducibility.
    for n in (2,3):
        mod=MODULI[n]
        for a in range(P):
            assert sum(c*pow(a,j,P) for j,c in enumerate(mod))%P != 0

def count_points(n):
    one,zero,mul,power,element,scalar,add=field(n)
    q=P**n
    counts={(A,d):1 for A,d in product((1,2,4),(1,2))}
    for raw in range(q):
        t=element(raw)
        t2=mul(t,t)
        t4=mul(t2,t2)
        for d in (1,2):
            v=add(add(scalar(t4,d*d),scalar(t2,d)),scalar(one,5))
            for A in (1,2,4):
                rhs=scalar(v,-A)
                if rhs==zero: multiplicity=1
                elif power(rhs,(q-1)//3)==one: multiplicity=3
                else: multiplicity=0
                counts[A,d]+=multiplicity
    return counts

def multicoeff(diagonal_target,A,d):
    monomials=((3,0,1),(0,4,0),(0,2,2),(0,0,4))
    coeff=(1,A*d*d,A*d,5*A)
    s=0
    for j0 in range(13):
        for j1 in range(13-j0):
            for j2 in range(13-j0-j1):
                j3=12-j0-j1-j2
                js=(j0,j1,j2,j3)
                mon=tuple(sum(js[k]*monomials[k][i] for k in range(4)) for i in range(3))
                if mon!=diagonal_target: continue
                val=factorial(12)
                for k in js: val//=factorial(k)
                for k in range(4):val*=pow(coeff[k],js[k],P)
                s+=val
    return s%P

def hasse_witt_check(A,d):
    # For plane quartics, Hasse-Witt (i,j) is the coefficient of
    # (p-1)(1,1,1)+p*i-j in F^(p-1), where i and j range over
    # degree-one monomials X,Y,Z. All off-diagonal entries vanish:
    # X exponents not divisible by 3, or Y exponents odd.
    vecs=((1,0,0),(0,1,0),(0,0,1))
    matrix=[]
    for i in vecs:
        row=[]
        for j in vecs:
            t=tuple(12+13*i[k]-j[k] for k in range(3))
            row.append(multicoeff(t,A,d))
        matrix.append(tuple(row))
    assert matrix==[(0,0,0),(0,{1:11,2:8,4:7}[A],0),(0,0,0)]
    return matrix

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tuple(c)

def check_polynomials():
    assert POLYS[1]==poly_mul(poly_mul((1,0,13),(1,0,13)),(1,2,13))
    assert POLYS[2]==poly_mul((1,0,-13,0,169),(1,5,13))
    assert POLYS[4]==poly_mul((1,0,-13,0,169),(1,-7,13))
    for A in (1,2,4):
        count=EXPECTED[A]
        S=[P**i+1-count[i-1] for i in (1,2,3)]
        c1=-S[0]
        c2=(S[0]**2-S[1])//2
        c3=-(S[0]**3-3*S[0]*S[1]+2*S[2])//6
        assert (1,c1,c2,c3,P*c2,P*P*c1,P**3)==POLYS[A]

if __name__=='__main__':
    polynomial_irreducibility_check()
    check_polynomials()
    for A,d in product((1,2,4),(1,2)):
        hasse_witt_check(A,d)
    for n in (1,2,3):
        obs=count_points(n)
        for (A,d),v in obs.items():
            assert v==EXPECTED[A][n-1],(n,A,d,v)
        print('field_degree',n,'counts',sorted(obs.items()))
    print('VERIFY_OK')
