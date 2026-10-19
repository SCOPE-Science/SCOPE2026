#!/usr/bin/env python3
"""Exact finite-field replay for prescribed commutators in 4-by-4 unitriangular matrices."""
from itertools import product
from collections import Counter


def expected(q, u, v, w):
    val = q**7 * (q*q-1)
    if u == v == 0:
        val += q**9-q**7
        if w == 0:
            val += q**8
    return val


def matrix_of(t, q):
    a,b,c,d,e,f = t
    return ((1,a,d,f), (0,1,b,e), (0,0,1,c), (0,0,0,1))


def mm(A,B,q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4))%q
                       for j in range(4)) for i in range(4))


def inv(U,q):
    M = tuple(tuple((U[i][j]-(i==j))%q for j in range(4)) for i in range(4))
    I = tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
    M2=mm(M,M,q); M3=mm(M2,M,q)
    return tuple(tuple((I[i][j]-M[i][j]+M2[i][j]-M3[i][j])%q
                  for j in range(4)) for i in range(4))


def exhaustive(q):
    elems = list(product(range(q),repeat=6))
    Acounts, Gcounts = Counter(),Counter()
    direct_checks = 0
    for ix, x in enumerate(elems):
        a,b,c,d,e,f=x
        for iy,y in enumerate(elems):
            A,B,C,D,E,F=y
            u = (a*B-A*b)%q
            v = (b*C-B*c)%q
            w = (a*E-A*e+d*C-D*c)%q
            wg = (w-(a+A)*v)%q
            Acounts[(u,v,w)]+=1
            Gcounts[(u,v,wg)]+=1
            if q == 2 or (ix*len(elems)+iy)%37 == 0:
                U,V = matrix_of(x,q), matrix_of(y,q)
                H=mm(mm(mm(inv(U,q),inv(V,q),q),U,q),V,q)
                assert H[0][2]==u and H[1][3]==v and H[0][3]==wg
                assert all(H[i][j]==int(i==j) for i in range(4) for j in range(4)
                           if (i,j) not in ((0,2),(1,3),(0,3)))
                direct_checks+=1
    for u,v,w in product(range(q), repeat=3):
        want=expected(q,u,v,w)
        assert Acounts[(u,v,w)]==want,("associative Lie",q,(u,v,w),Acounts[(u,v,w)],want)
        assert Gcounts[(u,v,w)]==want,("group",q,(u,v,w),Gcounts[(u,v,w)],want)
    assert len(Acounts)==len(Gcounts)==q**3
    assert sum(Acounts.values())==sum(Gcounts.values())==q**12
    return direct_checks


def gf4_mult(a,b):
    z=0
    for i in range(2):
        if b & (1<<i): z^=a<<i
    # x^2 = x+1
    if z&8: z ^= 0b1110
    if z&4: z ^= 0b111
    return z


def check_extension():
    q=4
    counts=Counter()
    exceptional=Counter()
    for a,b,c,A,B,C in product(range(q),repeat=6):
        u=gf4_mult(a,B)^gf4_mult(A,b)
        v=gf4_mult(b,C)^gf4_mult(B,c)
        counts[(u,v)]+=1
        if a==A==c==C==0: exceptional[(u,v)]+=1
    for u,v in product(range(q),repeat=2):
        assert counts[(u,v)]==q*q*(q*q-1)+q**4*(u==v==0)
        assert exceptional[(u,v)]==q*q*(u==v==0)


def main():
    assert exhaustive(2)==4096
    assert exhaustive(3)>14000
    check_extension()
    for q in (2,3,4,5):
        zero=expected(q,0,0,0)
        assert zero==q**6*(2*q**3+q*q-2*q)
        assert (q**3-q)*q**7*(q*q-1)+(q-1)*2*q**7*(q*q-1)+zero==q**12
    print('VERIFY_OK')

if __name__ == '__main__': main()
