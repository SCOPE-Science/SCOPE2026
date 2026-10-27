#!/usr/bin/env python3
"""Exact checks for cyclic binary (1,3)-pseudoperiodicity."""
from collections import defaultdict
from math import comb

def predicted(n, t):
    if t == 0:
        return 2
    if t & 1 or 2*t < n or 3*t > 2*n:
        return 0
    k = n-t
    s = 2*t-n
    num = 2*n*comb(k, s)
    assert num % k == 0
    return num // k

def direct(n):
    hist=defaultdict(int)
    for b in range(1<<n):
        a=[(b>>i)&1 for i in range(n)]
        if all(a[i] == a[(i+1)%n] or a[i]==a[(i+3)%n] for i in range(n)):
            t=sum(a[i] != a[(i+1)%n] for i in range(n))
            hist[t]+=1
    return dict(hist)

def matrix(n):
    # Edge from (a,b) to (b,c) has weight v^a if a=0 or b != c.
    states = [(0,0),(0,1),(1,0),(1,1)]
    T = [[None]*4 for _ in range(4)]
    for i,(a,b) in enumerate(states):
        for c in (0,1):
            if not a or b!=c:
                j=states.index((b,c)); T[i][j]=a
    # polynomial matrix over integer coefficients
    M=[[({0:1} if i==j else {}) for j in range(4)] for i in range(4)]
    for step in range(1,n+1):
        N=[[defaultdict(int) for j in range(4)] for i in range(4)]
        for i in range(4):
            for k in range(4):
                for d,w in M[i][k].items():
                    for j in range(4):
                        if T[k][j] is not None:
                            N[i][j][d+T[k][j]]+=w
        M=N
    p=defaultdict(int)
    for i in range(4):
        for t,val in M[i][i].items():
            if t%2==0: p[t]+=2*val
    return dict(p)

def recurrence(max_n):
    # The weighted nonconstant trace polynomial follows Newton sums
    # for lambda^3-v*lambda-v^2, where p0=3,p1=0,p2=2v.
    p=[{0:3},{},{1:2}]
    for n in range(3,max_n+1):
        a=defaultdict(int)
        for d,v in p[n-2].items():a[d+1]+=v
        for d,v in p[n-3].items():a[d+2]+=v
        p.append(dict(a))
    for n in range(1,max_n+1):
        expected={t:predicted(n,t) for t in range(n+1) if predicted(n,t)}
        got={0:2}
        for t,v in p[n].items():
            if t%2==0:
                got[t]=got.get(t,0)+2*v
        assert got == expected,(n,got,expected)
    return [sum(predicted(n,t) for t in range(n+1)) for n in range(1,max_n+1)]

def main():
    total=0
    for n in range(1,19):
        h=direct(n)
        expect={t:predicted(n,t) for t in range(n+1) if predicted(n,t)}
        assert h==expect,(n,h,expect)
        total+=1<<n
    for n in range(1,71):
        expect={t:predicted(n,t) for t in range(n+1) if predicted(n,t)}
        assert matrix(n)==expect,(n,matrix(n),expect)
    seq=recurrence(180)
    # An independent implementation via direct transition exclusion.
    for n in range(1,15):
        c=0
        for b in range(1<<n):
            d=[((b>>i)&1)^((b>>((i+1)%n))&1) for i in range(n)]
            if all(tuple(d[(i+j)%n] for j in range(3)) not in [(1,0,0),(1,1,1)] for i in range(n)):
                c+=1
        assert c==seq[n-1]
    print('PSEUDOPERIOD_13_CYCLIC_PASS',
          'all_binary_words_n=1..18',f'words={total}',
          'independent_direct_differences_n=1..14',
          'transfer_matrix_n=1..70',
          'cubic_Newton_recurrence_n=1..180')
    print('first_20_counts',seq[:20])
if __name__=='__main__': main()
