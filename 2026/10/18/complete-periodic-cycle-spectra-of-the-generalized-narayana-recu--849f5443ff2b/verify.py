#!/usr/bin/env python3
"""Exact-arithmetic checks of a complete family of modular recurrence cycle spectra."""
from collections import Counter

def predicted(c,k):
    ans=Counter()
    if c&1:
        ans[1]=1
        for j in range(1,k+1):ans[7*(1<<(j-1))]=1<<(2*(j-1))
    elif c==0:ans[1]=1<<k
    else:
        h=(abs(c)&-abs(c)).bit_length()-1
        if h>=2:
            ans[1]=1<<min(k,h)
            for j in range(1,max(0,k-h)+1):ans[1<<j]=1<<(h-1)
        else:
            t=(abs(c+2)&-abs(c+2)).bit_length()-1 if c!=-2 else 1000000
            ans[1]=2
            if k>=2:ans[2]=(1<<min(k-1,t))-1
            for j in range(2,max(0,k-t)+1):ans[1<<j]=1<<(t-1)
    return +ans

def actual(c,k):
    m=1<<k;seen=bytearray(m**3);cnt=Counter()
    for z in range(m**3):
        if seen[z]:continue
        pos={};path=[];v=z
        while v not in pos and not seen[v]:
            pos[v]=len(path);path.append(v)
            a=v%m;b=(v//m)%m;d=v//(m*m)
            v=b+m*(d+m*((c*a+d)%m))
        if v in pos:cnt[len(path)-pos[v]]+=1
        for w in path:seen[w]=1
    return cnt

# The two possible odd-coefficient lifts modulo four are checked directly.
def mul(x,y,m):return [[sum(x[i][h]*y[h][j] for h in range(3))%m for j in range(3)] for i in range(3)]
def mpow(a,n,m):
    out=[[int(i==j) for j in range(3)] for i in range(3)]
    while n:
        if n&1:out=mul(out,a,m)
        a=mul(a,a,m);n//=2
    return out
def det(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
for c in [1,3]:
    a=[[0,1,0],[0,0,1],[c,0,1]]
    ap=mpow(a,7,4)
    assert all((ap[i][j]-int(i==j))%2==0 for i in range(3) for j in range(3))
    b=[[(ap[i][j]-int(i==j))//2 for j in range(3)] for i in range(3)]
    assert det(b)%2==1
    assert det([[b[i][j]+int(i==j) for j in range(3)] for i in range(3)])%2==1
for c in [-8,-6,-4,-2,-1,0,1,2,3,4,6,8]:
    for k in range(1,5):
        assert actual(c,k)==predicted(c,k),(c,k,actual(c,k),predicted(c,k))
        count=sum(period*mult for period,mult in predicted(c,k).items())
        assert count==(1<<k)**3 if c&1 else count==1<<k,(c,k,count)
print('VERIFY_OK; exact lift checks and 48 exhaustive state digraphs')
