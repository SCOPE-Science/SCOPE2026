#!/usr/bin/env python3
"""Self-contained integer Smith-form cross-check for partial-matching deletions."""
from math import prod

def smith_diag(matrix):
    a=[list(map(int,r)) for r in matrix]
    m=len(a); n=len(a[0]) if m else 0
    k=0
    while k<min(m,n):
        nz=[(abs(a[i][j]),i,j) for i in range(k,m) for j in range(k,n) if a[i][j]]
        if not nz: break
        _,i,j=min(nz)
        a[k],a[i]=a[i],a[k]
        for row in a: row[k],row[j]=row[j],row[k]
        while True:
            pivot=a[k][k]
            if pivot==0: raise AssertionError('zero pivot')
            done=False
            for i in range(k+1,m):
                if a[i][k]:
                    q,r=divmod(a[i][k], pivot)
                    for j in range(k,n): a[i][j]-=q*a[k][j]
                    if r:
                        a[k],a[i]=a[i],a[k]
                        done=True
                        break
            if done: continue
            for j in range(k+1,n):
                if a[k][j]:
                    q,r=divmod(a[k][j], pivot)
                    for i in range(k,m): a[i][j]-=q*a[i][k]
                    if r:
                        for row in a: row[k],row[j]=row[j],row[k]
                        done=True
                        break
            if done: continue
            if any(a[i][k] for i in range(k+1,m)) or any(a[k][j] for j in range(k+1,n)):
                continue
            bad=next(((i,j) for i in range(k+1,m) for j in range(k+1,n) if a[i][j]%pivot!=0),None)
            if bad:
                i,j=bad
                for col in range(k,n): a[k][col]+=a[i][col]
                continue
            break
        k+=1
    return [abs(a[i][i]) for i in range(min(m,n))]

def laplacian_reduced(n,t):
    M=[[0]*(2*n-1) for _ in range(2*n-1)]
    for i in range(n):
        for j in range(n):
            if i==j and i<t: continue
            x,y=i,n+j
            if x<2*n-1: M[x][x]+=1
            if y<2*n-1: M[y][y]+=1
            if x<2*n-1 and y<2*n-1:
                M[x][y]-=1; M[y][x]-=1
    return M

def theorem_factors(n,t):
    q=n-t; A=n*(n-2); C=A+t
    if t==1: return [n]*(2*n-5)+[n*(n-1)*(n-1)]
    return [n]*(2*q-2)+[A]*(t-2)+[A*C]

def main():
    cases=0
    for n in range(3,11):
        for t in range(1,n):
            d=smith_diag(laplacian_reduced(n,t))
            expected=theorem_factors(n,t)
            assert sorted(x for x in d if x>1)==sorted(expected),(n,t,d,expected)
            assert all(d[i+1]%d[i]==0 for i in range(len(d)-1)), (n,t,d)
            cases+=1
    print(f'VERIFY_OK full_smith_cases={cases} orders=3..10 intermediate_matching_deletions')

if __name__=='__main__': main()
