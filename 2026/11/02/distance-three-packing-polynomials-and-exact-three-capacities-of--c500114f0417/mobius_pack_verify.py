#!/usr/bin/env python3
"""Independent exact checker for the distance-three packing census of Moebius ladders.
Usage: python3 mobius_pack_verify.py
"""
from functools import lru_cache
from math import comb


def expected(m):
    out = [1]
    for t in range(1, m // 2 + 1):
        surplus = m - 2*t
        if surplus == 0:
            out.append(4 if t % 2 else 0)
        elif surplus > 0:
            s = sum(comb(t,r)*comb(surplus-1,r-1)*(2**r)
                    for r in range(1,min(t,surplus)+1))
            assert (m*s)%t==0
            out.append(m*s//t)
    return out


def direct_graph_polynomial(m):
    n=2*m
    adj = [set(((i-1)%n,(i+1)%n,(i+m)%n)) for i in range(n)]
    closed2=[]
    for i in range(n):
        z={i}|adj[i]
        for j in adj[i]:
            z.update(adj[j])
        mask=sum(1<<v for v in z)
        closed2.append(mask)
    @lru_cache(None)
    def solve(mask):
        if not mask:return (1,)
        v=(mask & -mask).bit_length()-1
        a=solve(mask & ~(1<<v))
        b=solve(mask & ~closed2[v])
        res=[0]*max(len(a),len(b)+1)
        for i,x in enumerate(a):res[i]+=x
        for i,x in enumerate(b):res[i+1]+=x
        while len(res)>1 and res[-1]==0:res.pop()
        return tuple(res)
    return list(solve((1<<n)-1)),solve.cache_info().currsize


def main():
    for m in range(5,25):
        pred=expected(m)
        got, states=direct_graph_polynomial(m)
        while pred[-1]==0: pred.pop()
        assert got==pred, (m,pred,got)
        a=max(i for i,n in enumerate(got) if n)
        a_expected=m//2-(m%4==0)
        count_expected=m*(m-2) if m%4==0 else 4 if m%4==2 else 2*m
        assert a==a_expected and got[a]==count_expected, (m,a,got[a])
        assert sum(got)>0
        print('m',m,'max',a,'number',got[a],'total',sum(got),'memo_states',states)
    print('VERIFY_OK m=5..24 all polynomial coefficients, exact maxima, labelled optimum counts')

if __name__=='__main__':main()
