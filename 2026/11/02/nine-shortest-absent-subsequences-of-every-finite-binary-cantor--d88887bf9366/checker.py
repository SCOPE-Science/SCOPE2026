#!/usr/bin/env python3
"""Standalone verification of finite Cantor scattered-subsequence formulas."""

def next_states(w):
    n=len(w); d=[[n,n] for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        d[i][:]=d[i+1][:]
        d[i][int(w[i])]=i
    return d

def shortest_missing(w):
    n=len(w); nx=next_states(w); dist=[0]*(n+1)
    for p in range(n,-1,-1):
        def remaining(c):
            q=nx[p][c]+1
            return dist[q] if q<=n else 0
        dist[p]=1+min(remaining(0),remaining(1))
    paths=[('',0)]
    for _ in range(dist[0]):
        other=[]
        for v,p in paths:
            for c in (0,1):
                q=nx[p][c]+1
                d=dist[q] if q<=n else 0
                if d==dist[p]-1:
                    other.append((v+str(c),q))
        paths=other
    return dist[0],{v for v,p in paths}

def predicted(m):
    return {a+'1'*(m-3)+b for a in ('00','01','11') for b in ('00','10','11')}

def test():
    for h in range(2,16):
        m=2*h
        g='101000'*(h-1)+'101'
        d,absent=shortest_missing(g)
        assert d==m+1 and absent==predicted(m),(h,d,absent)
    c='1'
    for n in range(1,5):
        c=c+'0'*(3**(n-1))+c
        if n>=2:
            m=2**n
            d,absent=shortest_missing(c)
            assert d==m+1 and absent==predicted(m),(n,d,absent)
            if n<=3:
                nx=next_states(c)
                for mask in range(1<<(m+1)):
                    v=f'{mask:0{m+1}b}';p=0
                    for letter in v:
                        p=nx[p][int(letter)]+1
                        if p>len(c):break
                    assert (p>len(c))==(v in absent),(n,v)
    print('OK: auxiliary family h=2..15; Cantor n=2..4; independent enumeration n=2..3')

if __name__=='__main__':test()
