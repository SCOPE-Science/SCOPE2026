#!/usr/bin/env python3
"""Pure-integer Bareiss determinants and spectral product verification.
No symbolic algebra or calls to the Smith-normal-form checker.
"""

def exact_det(a):
    a=[row[:] for row in a]
    n=len(a); sign=1;prev=1
    for k in range(n-1):
        if a[k][k] == 0:
            h=next((j for j in range(k+1,n) if a[j][k]),None)
            if h is None:return 0
            a[k],a[h]=a[h],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*p-a[i][k]*a[k][j]
                assert num%prev == 0
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def construct(n,k):
    N=2*n
    L=[[0]*N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            w=k if i==j else 1
            L[i][i]+=w
            L[n+j][n+j]+=w
            L[i][n+j]-=w
            L[n+j][i]-=w
    return L

def main():
    tested=0
    for n in range(3,14):
        for k in range(0,8):
            L=construct(n,k)
            actual=exact_det([row[:-1] for row in L[:-1]])
            t=n-1+k;q=n-2+2*k
            expected=(n**(n-2))*(q**(n-1))*t
            assert actual==expected,(n,k,actual,expected)
            tested+=1
    print('MATRIX_TREE_ALL_PASS',tested,'cases n=3..13 k=0..7')
if __name__=='__main__':main()
