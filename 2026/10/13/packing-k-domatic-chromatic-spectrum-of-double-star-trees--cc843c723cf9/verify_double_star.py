#!/usr/bin/env python3
"""Self-contained checks for packing-domatic colorings of double stars.
No dependency beyond Python standard library; finite checks support a separate universal proof.
"""
from itertools import product

def distances(a,b):
    n=a+b+2
    edges=[(0,1)]+[(0,i) for i in range(2,2+a)]+[(1,i) for i in range(2+a,n)]
    d=[[n+1]*n for _ in range(n)]
    for i in range(n):d[i][i]=0
    for x,y in edges:d[x][y]=d[y][x]=1
    for h in range(n):
        for i in range(n):
            for j in range(n):d[i][j]=min(d[i][j],d[i][h]+d[h][j])
    return d

def valid(d,f,groups):
    n=len(d)
    if sorted(sum((list(s) for s in groups),[]))!=list(range(n)):return False
    for i in range(n):
        for j in range(i):
            if f[i]==f[j] and d[i][j]<=f[i]:return False
    return all(all(any(d[x][v]<=f[x] for x in S) for v in range(n)) for S in groups)

def predicted(a,b,k):
    n=a+b+2
    if k in (2,3):return 3
    if k==a+2 or k==b+2:return k
    return k+1

def witness(a,b,k):
    n=a+b+2; A=list(range(2,2+a));B=list(range(2+a,n))
    if k in (2,3):
        f=[2,3]+[1]*(n-2)
        parts=[A+B,[0],[1]]
        if k==2:parts[0]+=parts.pop()
        return f,parts
    if k==a+2:
        f=[1,2]+list(range(3,a+3))+[1]*b
        return f,[[0]+B,[1]]+[[v] for v in A]
    if k==b+2:
        f=[2,1]+[1]*a+list(range(3,b+3))
        return f,[[1]+A,[0]]+[[v] for v in B]
    f=[0]*n
    low=(A+B)[:n-k]
    for v in low:f[v]=1
    f[0]=2
    rest=[v for v in range(1,n) if v not in low]
    for label,v in enumerate(rest,3):f[v]=label
    return f,[[0]+low]+[[v] for v in rest]

def possible_with_k_colors(a,b,k):
    """Exhaustively search status classes 1,2,H; H gets distinct labels >=3.
    Check possible dominating-broadcast partitions, allowing low vertices to
    join an H anchor (when one exists). This is equivalent to all colorings.
    """
    d=distances(a,b);n=len(d);full=(1<<n)-1
    for status in product((1,2,3),repeat=n):
        h=status.count(3)
        if h>k-2:continue
        if any(status[i]==status[j] and ((status[i]==1 and d[i][j]<=1) or
           (status[i]==2 and d[i][j]<=2)) for i in range(n) for j in range(i)):
            continue
        # With diameter three, each H-status vertex receives its own color 3..h+2.
        low=[i for i in range(n) if status[i]<3]
        good=[]
        for mask in range(1,1<<len(low)):
            s=[low[i] for i in range(len(low)) if mask>>i&1]
            if all(any(d[u][v]<=status[u] for u in s) for v in range(n)):
                good.append(mask)
        maxlow=0
        if good:maxlow=1
        if any(x&y==0 for ix,x in enumerate(good) for y in good[ix+1:]):maxlow=2
        if h and h+maxlow>=k:return True
        if not h and maxlow>=k and any(sum((1<<i) for i in range(len(low)) if (x|y)>>i&1)==(1<<len(low))-1 for x in good for y in good if not x&y):
            return True
    return False

def main():
    constructions=0
    for a in range(1,15):
        for b in range(1,15):
            d=distances(a,b)
            for k in range(2,a+b+3):
                f,groups=witness(a,b,k)
                assert max(f)==predicted(a,b,k),(a,b,k,f)
                assert valid(d,f,groups),(a,b,k,f,groups)
                constructions+=1
    tests=0
    for a in range(1,5):
        for b in range(1,5):
            if a+b>6:continue
            n=a+b+2
            for k in range(3,n+1):
                actual=possible_with_k_colors(a,b,k)
                expected=predicted(a,b,k)==k
                assert actual==expected,(a,b,k,actual,expected)
                tests+=1
    print(f'PASS: {constructions} all-parameter construction profiles (1<=a,b<=14); '
          f'{tests} exhaustive palette-equality profiles (a,b<=4, a+b<=6).')
if __name__=='__main__':main()
