#!/usr/bin/env python3
"""Exact rational consistency tests for toric-scroll chamber and obstruction curve theorems.
No external dependencies. Use `python3 verify.py`."""
from fractions import Fraction as F
from itertools import combinations


def predicted(m,a,b):
    d=b-m*a
    return ((a-2)*(b-m-2)>0 and (a+2)*(b+m+2)>0
            and (abs(d)!=2-m if m <= 1 else abs(d)>m-2))


def solve_fullrank(mat, rhs):
    """Return unique rational solution for a full-column-rank consistent system."""
    n=len(mat); p=len(mat[0]); z=[[F(v) for v in mat[i]]+[F(rhs[i])] for i in range(n)]
    piv=[]; r=0
    for c in range(p):
        j=next((j for j in range(r,n) if z[j][c]),None)
        if j is None:continue
        z[r],z[j]=z[j],z[r]
        x=z[r][c]
        z[r]=[w/x for w in z[r]]
        for j in range(n):
            if j!=r and z[j][c]:
                x=z[j][c]
                z[j]=[a-x*b for a,b in zip(z[j],z[r])]
        piv.append(c);r+=1
    if any(all(v==0 for v in row[:p]) and row[p]!=0 for row in z):return None
    if len(piv)!=p:return None
    out=[F(0)]*p
    for j,c in enumerate(piv):out[c]=z[j][p]
    return out


def convex_meets_affine(U,T,S):
    # A feasible representation in quotient by span(T-T0) has an extreme
    # representation supported on <= 5-|T| affinely independent vertices.
    d=len(T)-1
    for k in range(1,min(len(S),4-d)+1):
        for J in combinations(S,k):
            # sum(lambda_i u_i)-sum(theta_j(T_j-T_0))=T_0;
            # sum(lambda_i)=1; lambda_i>=0; theta_j unrestricted.
            A=[]
            for coord in range(3):
                A.append([U[s][coord] for s in J]+[-(U[t][coord]-U[T[0]][coord]) for t in T[1:]])
            A.append([1]*k+[0]*d)
            rhs=[*U[T[0]],1]
            sol=solve_fullrank(A,rhs)
            if sol is not None and all(x>=0 for x in sol[:k]):return True
    return False


def toric_criterion(m,a,b):
    U=[(0,1,a),(1,0,b),(0,-1,0),(-1,m,0),(0,0,1),(0,0,-1)]
    top=[frozenset((i,j,t)) for i,j in [(0,1),(1,2),(2,3),(3,0)] for t in (4,5)]
    cones={frozenset(c) for topc in top for k in (1,2) for c in combinations(topc,k)}
    for T in cones:
        S=set().union(*(Q-T for Q in top if T<=Q))
        if convex_meets_affine(U,sorted(T),sorted(S)):
            return False
    return True


def check_minimal_curve(m,d):
    k=m-2; h=abs(d)
    assert m>=2 and h<=k
    p=1 if (k+h)%2==0 else 2
    q=p*(k+h)//2
    assert 2*q==p*(k+h)
    assert q>=p*h
    # K_Y|D=-2S_h+(k-h)F, C=p S_h+qF, D=F_h.
    assert p*(k+h)-2*q==0
    # Adjunction gives arithmetic genus.
    C2=-h*p*p+2*p*q
    KF_C=p*(h-2)-2*q
    genus=(C2+KF_C)//2+1
    assert 2*genus == C2+KF_C+2
    assert genus==(0 if p==1 else k-1)
    if p==2:
        assert (k+h)%2==1
        assert (k+h)//2 != (k+h)/2
    return p,genus


def main():
    count=0;pass_count=0
    for m in range(0,7):
        for a in range(-4,6):
            for b in range(-7,9):
                p=predicted(m,a,b)
                q=toric_criterion(m,a,b)
                if p!=q: raise AssertionError(('chamber_disagreement',m,a,b,p,q))
                count+=1;pass_count+=int(p)
    curves=0
    for m in range(2,30):
        for d in range(-(m-2),m-1):
            check_minimal_curve(m,d)
            curves+=1
    assert predicted(4,-1,0)  # published Example 6.12
    assert not predicted(2,0,0) # split F_2 x P^1, crepant obstruction
    assert not predicted(3,3,9) # no invariant curve obstruction, vertical surface obstructs
    assert predicted(3,3,6)
    print('VERIFY_OK exact_fan_samples=%d generating=%d obstruction_curves=%d' % (count,pass_count,curves))

if __name__=='__main__':main()
