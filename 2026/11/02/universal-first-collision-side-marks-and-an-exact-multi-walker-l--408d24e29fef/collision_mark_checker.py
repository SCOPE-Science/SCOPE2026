"""Exact finite-state checks for independent continuous-time walkers on complete bipartite graphs.

Python standard library only. All finite checks use rational arithmetic; the
asymptotic assertion in the accompanying proof is analytic, not computer-certified.
"""
from fractions import Fraction as F


def rates(m,n,k,a):
    b=k-a
    assert 0<=a<=m and 0<=b<=n
    down=F(a*(n-b),n)
    up=F(b*(m-a),m)
    hitA=F(a*b,m)
    hitB=F(a*b,n)
    assert down+up+hitA+hitB==k
    return down,up,hitA,hitB


def solve(a,b):
    n=len(b)
    a=[row[:] + [y] for row,y in zip(a,b)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j])
        a[j],a[p]=a[p],a[j]
        v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j]
                if v:a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]


def transform(m,n,k,s,side):
    states=list(range(max(0,k-n),min(m,k)+1))
    mat=[[F(0) for _ in states] for _ in states]
    rhs=[]
    for i,a in enumerate(states):
        down,up,hA,hB=rates(m,n,k,a)
        mat[i][i]=s+k
        if down:mat[i][states.index(a-1)]-=down
        if up:mat[i][states.index(a+1)]-=up
        rhs.append(hA if side=='A' else hB if side=='B' else hA+hB)
    return dict(zip(states,solve(mat,rhs)))


def verify():
    count=0
    for m in range(1,6):
        for n in range(1,6):
            for k in range(2,min(5,m+n)+1):
                for a in range(max(0,k-n),min(m,k)+1):
                    b=k-a
                    # Independent microscopic enumeration of all legal walker jumps.
                    places=list(range(a))+list(range(m,m+b))
                    totals=[F(0)]*4
                    for x in places:
                        other=range(m,m+n) if x<m else range(m)
                        prob=F(1,len(other))
                        for y in other:
                            if y in places:
                                totals[2 if y<m else 3]+=prob
                            else:
                                totals[0 if x<m else 1]+=prob
                            count+=1
                    assert tuple(totals)==rates(m,n,k,a)
                    count+=1
                for s in [F(0),F(1,3),F(2)]:
                    aa=transform(m,n,k,s,'A')
                    bb=transform(m,n,k,s,'B')
                    both=transform(m,n,k,s,'both')
                    for a in aa:
                        assert aa[a]+bb[a]==both[a]
                        assert aa[a]*(m+n)==both[a]*n
                        assert bb[a]*(m+n)==both[a]*m
                        if s==0: assert both[a]==1
                        count+=4
    return count

if __name__=='__main__':
    print('PASS',verify(),'exact rational checks')
