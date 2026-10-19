#!/usr/bin/env python3
"""Independent exact commutant and numerical spectral checks for a weighted two-hub tree."""
from fractions import Fraction
from itertools import product


def predicted_nullity(p, q, a, b, c, d):
    # Compare squares to avoid radicals.
    return int(p == 2) + int(q == 2) + int(c == d and p * a*a == q * b*b)


def make_h(p,q,a,b,w,c,d):
    n=p+q+2
    h=[[0]*n for _ in range(n)]
    h[p][p]=c; h[p+1][p+1]=d
    for i in range(p):
        h[i][p]=h[p][i]=a
    h[p][p+1]=h[p+1][p]=w
    for j in range(q):
        h[p+1][p+2+j]=h[p+2+j][p+1]=b
    return h


def exact_rank_of_diagonal_commutant(H):
    """Rank of diag:{Z=Z^T,HZ=ZH}->Q^n, by rational row elimination.

    This is an algebraic calculation on integer commutation equations; no
    eigenvalues, spectral projectors, predicted rank or floating point is used.
    """
    n=len(H)
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    position={ij:k for k,ij in enumerate(pairs)}
    def loc(i,j):
        return position[(min(i,j),max(i,j))]
    basis={}
    def push(row):
        row={k:Fraction(v) for k,v in row.items() if v}
        while row:
            k=min(row)
            v=row[k]
            if k not in basis:
                basis[k]={u:z/v for u,z in row.items()}
                return 1
            for u,z in basis[k].items():
                row[u]=row.get(u,0)-v*z
                if not row[u]:del row[u]
        return 0
    cr=0
    for i in range(n):
        for j in range(i+1,n):
            row={}
            for k in range(n):
                if H[i][k]:
                    idx=loc(k,j)
                    row[idx]=row.get(idx,0)+H[i][k]
                if H[k][j]:
                    idx=loc(i,k)
                    row[idx]=row.get(idx,0)-H[k][j]
            cr+=push(row)
    increment=0
    for i in range(n):
        increment+=push({loc(i,i):1})
    assert len(basis)==cr+increment
    return increment,cr


def exact_profiles():
    profiles=[]
    for p,q in product(range(2,6),repeat=2):
        for a,b,w,c,d in [(1,1,1,0,0),(1,2,1,1,1),
                           (2,1,3,0,1),(1,1,2,-2,2),
                           (3,3,1,-1,-1)]:
            profiles.append((p,q,a,b,w,c,d))
    profiles.extend([(2,8,2,1,3,0,0),(8,2,1,2,2,2,2),
                     (4,9,3,2,1,0,0),(9,4,2,3,3,1,1),
                     (4,9,3,2,3,0,1),(9,4,2,3,1,-2,2)])
    cells=0
    for p,q,a,b,w,c,d in profiles:
        H=make_h(p,q,a,b,w,c,d)
        rank,cr=exact_rank_of_diagonal_commutant(H)
        null=len(H)-rank
        expectation=predicted_nullity(p,q,a,b,c,d)
        assert null==expectation,(p,q,a,b,w,c,d,null,expectation,cr)
        cells+=len(H)**2
    return len(profiles),cells


def jacobi_diagonalization(H):
    """Orthogonal diagonalization by cyclic largest-entry Jacobi rotations."""
    from math import sqrt
    n=len(H)
    a=[[float(x) for x in row] for row in H]
    U=[[float(i==j) for j in range(n)] for i in range(n)]
    for _ in range(40*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),
                key=lambda ij: abs(a[ij[0]][ij[1]]))
        apq=a[p][q]
        if abs(apq)<2e-13:break
        tau=(a[q][q]-a[p][p])/(2*apq)
        t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t)
        ss=t*c
        app=a[p][p]; aqq=a[q][q]
        a[p][p]=app-t*apq
        a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.0
        for k in range(n):
            if k!=p and k!=q:
                akp=a[k][p]; akq=a[k][q]
                a[k][p]=a[p][k]=c*akp-ss*akq
                a[k][q]=a[q][k]=ss*akp+c*akq
            vkp=U[k][p]; vkq=U[k][q]
            U[k][p]=c*vkp-ss*vkq
            U[k][q]=ss*vkp+c*vkq
    else:
        raise RuntimeError('Jacobi iteration did not converge')
    order=sorted(range(n),key=lambda i:a[i][i])
    return [a[i][i] for i in order],[[U[k][i] for i in order] for k in range(n)]


def spectral_profiles():
    tests=0;entries=0
    for p,q in product(range(2,9),repeat=2):
        for tag,a,b,w,c,d in [
             ('unit',1.,1.,1.,0.,0.),
             ('unbalanced',1.,1.7,.6,1.,1.),
             ('detuned',.8,1.1,1.3,2.,-1.),
             ('balanced',3./p**.5, 3./q**.5, .9,0.,0.),
             ('balanced_detuned',3./p**.5, 3./q**.5, 1.7,2.,-2.)]:
            H=make_h(p,q,a,b,w,c,d)
            evals,U=jacobi_diagonalization(H)
            n=len(H)
            M=[[0.0]*n for _ in range(n)]
            idx=0
            while idx<n:
                end=idx+1
                while end<n and abs(evals[end]-evals[idx])<1e-8:
                    end+=1
                E=[[sum(U[x][k]*U[y][k] for k in range(idx,end))
                    for y in range(n)] for x in range(n)]
                for x in range(n):
                    for y in range(n):
                        M[x][y]+=E[x][y]**2
                idx=end
            P=[row[:] for row in M]
            rank=0
            for cidx in range(n):
                pr=max(range(rank,n),key=lambda i: abs(P[i][cidx]))
                if abs(P[pr][cidx])<1e-8:continue
                P[rank],P[pr]=P[pr],P[rank]
                fac=P[rank][cidx]
                for j in range(cidx,n):P[rank][j]/=fac
                for i in range(rank+1,n):
                    f=P[i][cidx]
                    if f:
                        for j in range(cidx,n):P[i][j]-=f*P[rank][j]
                rank+=1
            expected=int(p==2)+int(q==2)
            if (tag=='balanced' or (tag=='unit' and p==q)):
                expected+=1
            assert n-rank==expected,(p,q,tag,n-rank,expected)
            assert max(abs(sum(row)-1.) for row in M)<3e-10,(p,q,tag)
            tests+=1;entries+=n*n
    return tests,entries

if __name__=='__main__':
    a,b=exact_profiles()
    c,d=spectral_profiles()
    print('VERIFY_OK exact_commutant_profiles=',a,
          'exact_matrix_positions=',b,
          'spectral_profiles=',c,
          'spectral_matrix_entries=',d)
