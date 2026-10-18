#!/usr/bin/env python3
"""Independent finite-field verification of the elementary symmetric cubic singular-support classification."""
from itertools import product
from math import comb


def esym3_and_gradient(x):
    n = len(x)
    e1=e2=e3=0
    for a in x:
        e3=(e3+a*e2)%3
        e2=(e2+a*e1)%3
        e1=(e1+a)%3
    return e3,tuple((e2-a*e1+a*a)%3 for a in x)

def positive_support_pattern(x):
    n=len(x)
    nonzero = tuple(i for i,a in enumerate(x) if a)
    if len(nonzero)>0 and len(nonzero)%9==1 and len(set(x[i] for i in nonzero))==1 and all(x[i]==0 for i in range(n) if i not in nonzero):
        return True
    if n%9 == 2 and len(set(x))==1 and x[0]: return True
    if n%9 == 2 and len(set(x))==2: # partition lines require both sizes congruent 1 mod9
        for v in set(x):
            k=x.count(v)
            if k%9==1 and (n-k)%9==1: return True
    if n%9 in (5,8) and len(set(x))==2 and all(a in (1,2) for a in x):
        s=x.count(1); t=x.count(2)
        return s%9==t%9==(7 if n%9==5 else 4)
    return False

def predicted(n):
    B=sum(comb(n,k) for k in range(1,n+1) if k%9==1)
    if n%9==2:
        L=B//2
        return ('lines',L)
    if n%9==5:
        return ('points',B+sum(comb(n,k) for k in range(1,n) if k%9==7)//2)
    if n%9==8:
        return ('points',B+sum(comb(n,k) for k in range(1,n) if k%9==4)//2)
    return ('points',B)

def rank_mod3(A):
    A=[list(row) for row in A]
    R=len(A); C=len(A[0]); k=0
    for c in range(C):
        p=next((i for i in range(k,R) if A[i][c]%3),None)
        if p is None:continue
        A[p],A[k]=A[k],A[p]
        u=pow(A[k][c],-1,3)
        A[k]=[(u*a)%3 for a in A[k]]
        for i in range(R):
            if i!=k and A[i][c]:
                f=A[i][c]
                A[i]=[(a-f*b)%3 for a,b in zip(A[i],A[k])]
        k+=1
        if k==R:break
    return k

def checker():
    for n in range(4,11):
        hits=0; predicted_count=predicted(n)
        for lead in range(n):
            for tail in product(range(3),repeat=n-lead-1):
                x=(0,)*lead + (1,) + tail
                f,g=esym3_and_gradient(x)
                is_sing=(f==0 and all(t==0 for t in g))
                pred=positive_support_pattern(x)
                if is_sing!=pred:
                    raise AssertionError((n,x,is_sing,pred,f,g))
                if is_sing:
                    hits+=1
                    if n%9!=2:
                        e1=sum(x)%3
                        H=[[0 if i==j else (e1-x[i]-x[j])%3 for j in range(n)] for i in range(n)]
                        expected = n-2 if n%9 in (5,8) else n-1
                        r=rank_mod3(H)
                        if r != expected:
                            raise AssertionError((n,x,r,expected))
        if predicted_count[0]=='points' and hits!=predicted_count[1]:
            raise AssertionError((n,hits,predicted_count))
        print(f'n={n}: {hits} projective F3-singular points; prediction={predicted_count}; Hessian ranks verified')
    n=11
    # Exhaustively check all 88573 projective F3 points and the 11-line star.
    hits=0
    for lead in range(n):
        for tail in product(range(3), repeat=n-lead-1):
            x=(0,)*lead+(1,)+tail
            f,g=esym3_and_gradient(x)
            truth=(f==0 and not any(g))
            pred=positive_support_pattern(x)
            assert truth == pred, (n,x,truth,pred)
            hits += truth
    assert hits==34
    # n=11 critical star: confirm points of all 11 lines over F3
    lines=set()
    for i in range(n):
        for a,b in product(range(3),repeat=2):
            if a==b==0: continue
            x=[b]*n;x[i]=a
            if x[i]==0 and all(z==0 for z in x):continue
            leading=next(z for z in x if z)
            x=tuple(z*pow(leading,-1,3)%3 for z in x)
            f,g=esym3_and_gradient(x)
            assert f==0 and not any(g)
            lines.add(x)
    assert len(lines)==1+3*n
    print('n=11: 11 distinct lines, all sharing one point, 34 F3-projective points on union')
    print('VERIFY_OK')
if __name__=='__main__': checker()
