#!/usr/bin/env python3
"""Exact and numerical checks for multichannel scattering on equilateral quantum graphs."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import sqrt

N=16
V=[(i,j) for i in range(4) for j in range(4)]
D={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def graphs():
    rook=[[int(i!=j and (V[i][0]==V[j][0] or V[i][1]==V[j][1])) for j in range(N)] for i in range(N)]
    sh=[[int(i!=j and ((V[j][0]-V[i][0])%4,(V[j][1]-V[i][1])%4) in D) for j in range(N)] for i in range(N)]
    return rook,sh

def check_srg(A):
    for i in range(N):
        assert A[i][i]==0 and sum(A[i])==6
        for j in range(N):
            assert A[i][j]==A[j][i]
            assert sum(A[i][t]*A[t][j] for t in range(N)) == (6 if i==j else 2)

def canonical(A,ind):
    t=len(ind)
    def word(ii):
        return tuple(A[ii[x]][ii[y]] for x in range(t) for y in range(x+1,t))
    return min(word(ii) for ii in permutations(ind))

def profiles(A,t):
    d={}
    for q in combinations(range(N),t):
        key=canonical(A,q)
        d[key]=d.get(key,0)+1
    return d

def inverse_rational(M):
    n=len(M)
    rows=[[F(x) for x in M[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if rows[i][j]!=0)
        rows[p],rows[j]=rows[j],rows[p]
        d=rows[j][j]
        rows[j]=[x/d for x in rows[j]]
        for i in range(n):
            if i!=j:
                z=rows[i][j]
                if z: rows[i]=[a-z*b for a,b in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]

def solve_complex(A,b):
    n=len(A)
    w=[[complex(v) for v in A[i]]+[complex(b[i])] for i in range(n)]
    for j in range(n):
        p=max(range(j,n),key=lambda i:abs(w[i][j]))
        assert abs(w[p][j])>1e-12
        w[j],w[p]=w[p],w[j]
        d=w[j][j]
        w[j]=[v/d for v in w[j]]
        for i in range(n):
            if i!=j:
                fac=w[i][j]
                if fac: w[i]=[a-fac*b for a,b in zip(w[i],w[j])]
    return [w[i][-1] for i in range(n)]

def scattering(R,ports,s):
    t=len(ports)
    C=[[complex(int(i==j))-1j*s*complex(R[ports[i]][ports[j]]) for j in range(t)] for i in range(t)]
    result=[]
    for col in range(t):
        # f_S = -2 i sin(k l) (I - i sin(k l) R_SS)^-1 R_SS e_col;
        # b = f_S - a.
        b=[-2j*s*complex(R[ports[i]][ports[col]]) for i in range(t)]
        f=solve_complex(C,b)
        result.append([f[i]-int(i==col) for i in range(t)])
    return [[result[j][i] for j in range(t)] for i in range(t)]

def run():
    rook,sh=graphs()
    for A in (rook,sh):check_srg(A)
    rp={t:profiles(rook,t) for t in (1,2,3,4)}
    sp={t:profiles(sh,t) for t in (1,2,3,4)}
    assert all(set(rp[t])==set(sp[t]) for t in (1,2,3))
    assert len(rp[3])==len(sp[3])==4
    assert set(rp[3])=={(0,0,0),(0,0,1),(0,1,1),(1,1,1)}
    K4=(1,1,1,1,1,1)
    assert rp[4].get(K4,0)==8 and sp[4].get(K4,0)==0
    for A in (rook,sh):
        M=[[3*int(i==j)-A[i][j] for j in range(N)] for i in range(N)]
        R=inverse_rational(M)
        for i in range(N):
            for j in range(N):
                expected=F(3,5)*int(i==j)+F(1,5)*A[i][j]-F(2,15)
                assert R[i][j]==expected
        # At k*l=pi/3, the exact resolvent gives unitary scattering.
        s=sqrt(3)/2
        samples=[(0,), (0,1), (0,1,2), (0,1,2,3)]
        for ports in samples:
            B=scattering(R,ports,s)
            for i in range(len(ports)):
                for j in range(len(ports)):
                    val=sum(B[k][i].conjugate()*B[k][j] for k in range(len(ports)))
                    assert abs(val-int(i==j))<1e-11
    print('VERIFY_OK SRG=16_6_2_2 roots=6,2,-2 K4_rook=8 K4_shrikhande=0 small_induced_supports=equal m=1..3 exact_resolvent_identity=true unitary_scattering=true')

if __name__=='__main__':run()
