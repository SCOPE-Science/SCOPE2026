#!/usr/bin/env python3
"""Exact finite-field verification for triangular cyclic cellular automata."""
def matrix(p,L,m):
    d=(m+1)*L
    a=[[0]*d for _ in range(d)]
    def ix(k,g):return k*L+g
    for g in range(L):
        a[ix(0,g)][ix(0,g)]=1
        for k in range(1,m+1):
            a[ix(k,g)][ix(k,(g+1)%L)]=1
            a[ix(k,g)][ix(k-1,g)]=(p-1)%p
    return a

def mul(a,b,p):
    n=len(a);o=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,x in enumerate(a[i]):
            if x:
                for j,y in enumerate(b[k]):
                    if y:o[i][j]=(o[i][j]+x*y)%p
    return o

def power(a,e,p):
    n=len(a);o=[[int(i==j) for j in range(n)] for i in range(n)]
    while e:
        if e&1:o=mul(o,a,p)
        a=mul(a,a,p);e//=2
    return o

def identity(a):
    return all(v==int(i==j) for i,row in enumerate(a) for j,v in enumerate(row))

def expect(p,L,m):
    q=L
    while q%p==0:q//=p
    a=L//q
    s=1
    while s<m+a:s*=p
    return q*s

def run():
    cases=0
    for p in (2,3,5):
        for L in range(1,9):
            for m in range(1,7):
                if (m+1)*L>45:continue
                a=matrix(p,L,m); e=expect(p,L,m)
                assert identity(power(a,e,p)),(p,L,m,e,'fails proposed period')
                assert all(not identity(power(a,e//v,p)) for v in range(2,e+1) if e%v==0 and all(v%q for q in range(2,int(v**.5)+1))), (p,L,m,e,'period not least')
                cases+=1
    print('PERIOD_EXACT_CHECK_PASS',cases)
if __name__=='__main__':run()
