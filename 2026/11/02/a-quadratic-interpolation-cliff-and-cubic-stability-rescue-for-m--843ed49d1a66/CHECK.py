#!/usr/bin/env python3
"""Exact arithmetic checks for cubic projective-harmonic MUB sampling.

Usage: python3 CHECK.py
Requires only the Python standard library. Finite checks supplement the
symbolic factorizations and all-parameter proof in RESULT.md.
"""
from fractions import Fraction as F
from math import comb


def zonal(k, d, t):
    u = F(1) - F(t)
    value = F(0)
    for j in range(k + 1):
        term = F((-1) ** j * comb(k, j)) * u ** j
        for a in range(j):
            term *= F(k + d - 1 + a, d - 1 + a)
        value += term
    return value


def eigenvalues(k, d, m):
    u, v = zonal(k, d, 0), zonal(k, d, F(1, d))
    return (1-u, 1+(d-1)*u-d*v, 1+(d-1)*u+d*(m-1)*v)


def gram(k, d, m):
    N = d*m
    return [[zonal(k, d, (F(1) if i == j else
                             F(0) if i//d == j//d else F(1, d)))
             for j in range(N)] for i in range(N)]


def matvec(A, v):
    return [sum(a*x for a,x in zip(row,v)) for row in A]


def rank(A):
    M = [[F(x) for x in row] for row in A]
    n, p, r = len(M), len(M[0]), 0
    for col in range(p):
        pivot = next((j for j in range(r,n) if M[j][col]),None)
        if pivot is None: continue
        M[r],M[pivot] = M[pivot],M[r]
        z=M[r][col]
        M[r]=[v/z for v in M[r]]
        for j in range(n):
            if j==r or not M[j][col]:continue
            z=M[j][col]
            M[j]=[a-z*b for a,b in zip(M[j],M[r])]
        r+=1
        if r==n: break
    return r


def omega(exponent):
    return [(1,0),(0,1),(-1,-1)][exponent%3]


def eisenstein_norm(a,b):
    return a*a-a*b+b*b


def qutrit_mubs():
    # Four MUBs: coordinate basis plus three quadratic chirp bases.
    pts=[('std',i,0) for i in range(3)]
    pts += [('chirp',a,b) for a in range(3) for b in range(3)]
    overlaps=[]
    for i,x in enumerate(pts):
        row=[]
        for j,y in enumerate(pts):
            if x[0]=='std' and y[0]=='std':
                t=F(int(x[1]==y[1]))
            elif x[0]=='std' or y[0]=='std':
                t=F(1,3)
            else:
                a,b=x[1:];c,e=y[1:]
                u=v=0
                for z in range(3):
                    h,l=omega((c-a)*z*z+(e-b)*z)
                    u+=h;v+=l
                t=F(eisenstein_norm(u,v),9)
            assert t == (1 if i==j else 0 if i//3==j//3 else F(1,3))
            row.append(t)
        overlaps.append(row)
    return overlaps


def main():
    assert len(qutrit_mubs())==12
    checks=0
    for d in range(3,71):
        for k in (1,2,3):
            u,v=zonal(k,d,0),zonal(k,d,F(1,d))
            if k==1:
                assert u == -F(1,d-1) and v==0
            elif k==2:
                assert u==F(2,d*(d-1))
                assert v==-F(d+2,d**3)
            else:
                assert u==-F(6,d*(d-1)*(d+1))
                assert v==F(4*(d-2)*(d+3),d**4*(d+1))
            checks+=2
        for m in range(1,d+2):
            w2,b2,c2=eigenvalues(2,d,m)
            assert w2==F((d-2)*(d+1),d*(d-1))
            assert b2==F((d+1)*(d+2),d*d)
            assert c2==F((d+2)*(d+1-m),d*d)
            w3,b3,c3=eigenvalues(3,d,m)
            assert w3==F((d+2)*(d*d-2*d+3),d*(d-1)*(d+1))
            assert b3==F((d-2)**2*(d+2)*(d+3),d**3*(d+1))
            assert c3==F((d-2)*(d+3)*((d-2)*(d+2)+4*m),d**3*(d+1))
            assert w2>0 and b2>0 and c2>=0
            assert (c2==0)==(m==d+1)
            assert w3>0 and b3>0 and c3>0
            checks+=9
        w2,b2,c2=eigenvalues(2,d,d)
        assert min(w2,b2,c2)==c2 and max(w2,b2,c2)==b2
        assert b2/c2==d+1
        w3,b3,c3=eigenvalues(3,d,d+1)
        assert min(w3,b3,c3)==b3
        if d==3:
            assert max(w3,b3,c3)==w3 and w3/b3==F(9,2)
        else:
            assert max(w3,b3,c3)==c3
            assert c3/b3==F(d*(d+4),(d-2)*(d+2))<F(9,2)
        checks+=5
    for d in (3,4,5,7):
        for m in (1,2,d,d+1):
            for k in (1,2,3):
                G=gram(k,d,m)
                w,b,c=eigenvalues(k,d,m)
                expected = (m*(d-1) if k==1 else d*m-(m==d+1 and k==2))
                assert rank(G)==expected
                W=[F(0)]*(d*m); W[0]=1; W[1]=-1
                assert matvec(G,W)==[w*x for x in W]
                if m>1:
                    B=[F(1)]*d+[F(-1)]*d+[F(0)]*(d*(m-2))
                    assert matvec(G,B)==[b*x for x in B]
                C=[F(1)]*(d*m)
                assert matvec(G,C)==[c*x for x in C]
                checks+=4
    # Exceptional qubit dimension: degree-two kernel loses the within-basis sector.
    assert zonal(2,2,0)==1
    assert eigenvalues(3,2,3)==(2,0,0)
    print('MUB_PROJECTIVE_CUBIC_EXACT_CHECK_OK',checks,'rational checks; qutrit chirps exact')

if __name__=='__main__': main()
