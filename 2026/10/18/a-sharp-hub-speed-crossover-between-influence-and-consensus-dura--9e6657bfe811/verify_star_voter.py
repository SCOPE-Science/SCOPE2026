#!/usr/bin/env python3
"""Exact finite checks for the heterogeneous voter model on a star.
Scientific verification only; the unrestricted formula is proved analytically.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

def H(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))

def solve(a,b):
    """Exact linear solver with simultaneous row elimination."""
    n=len(b)
    rows=[[F(v) for v in a[i]]+[F(b[i])] for i in range(n)]
    for j in range(n):
        p=next(k for k in range(j,n) if rows[k][j])
        rows[j],rows[p]=rows[p],rows[j]
        u=rows[j][j]
        rows[j]=[t/u for t in rows[j]]
        for k in range(n):
            if k!=j:
                t=rows[k][j]
                if t:rows[k]=[x-t*y for x,y in zip(rows[k],rows[j])]
    return [r[-1] for r in rows]

def reduced(n,c):
    """States k=1..n discordant leaves; center always has a single state."""
    q=[[F(0) for _ in range(n)] for _ in range(n)]
    for k in range(1,n+1):
        i=k-1
        transitions=[(k-1,F(k)),(n-k,c*F(k,n))]
        for nxt,rate in transitions:
            q[i][i]+=rate
            if nxt>0:q[i][nxt-1]-=rate
    t=solve(q,[F(1)]*n)
    return t

def full_chain(n,c):
    """An independent full 2^(n+1)-state calculation (no lumping)."""
    states=[mask for mask in range(1,(1<<(n+1))-1)]
    index={s:i for i,s in enumerate(states)}
    m=len(states)
    q=[[F(0) for _ in range(m)] for _ in range(m)]
    for a,mask in enumerate(states):
        hub=mask&1
        for v in range(n+1):
            if v==0:
                for leaf in range(1,n+1):
                    if ((mask>>leaf)&1)!=hub:
                        nxt=mask^1
                        rate=c/F(n)
                        q[a][a]+=rate
                        if nxt in index:q[a][index[nxt]]-=rate
            else:
                if ((mask>>v)&1)!=hub:
                    nxt=mask^(1<<v)
                    q[a][a]+=F(1)
                    if nxt in index:q[a][index[nxt]]-=F(1)
    times=solve(q,[F(1)]*m)
    return times[index[1]],times[index[2]]

def exact_checks():
    cases=0
    for n in range(2,13):
        for c in [F(1,4),F(1,2),F(1),F(3,2),F(3),F(n),F(n+3,2)]:
            t=reduced(n,c)
            assert t[0]==(n+c*H(n-1))/(n+c),(n,c,'leaf',t[0])
            assert t[n-1]==n*H(n)/(n+c),(n,c,'center',t[n-1])
            if n<=5:
                hub,leaf=full_chain(n,c)
                assert hub==t[n-1] and leaf==t[0],(n,c,hub,leaf,t)
            cases+=1
        th=F(n)*(H(n)-1)/H(n-1)
        assert 0<th<n and n*H(n)-(n+th*H(n-1))==0
        assert (F(1,1+th)-th/(n*(1+th)))>0
    for n,c in [(4,F(3)),(4,F(1)),(7,F(5)),(11,F(12))]:
        t=reduced(n,c)
        assert (t[n-1]>t[0])==(c<F(n)*(H(n)-1)/H(n-1))
        assert (F(1,1+c)>c/(n*(1+c)))==(c<n)
    print("PASS: 77 exact lumped systems (2..12), 28 independent full-state systems (2..5), thresholds and probabilities.")
    print("n=4, center rate=3:", "T_center",F(4)*H(4)/7,
          "T_leaf",(4+3*H(3))/7,
          "p_center",F(1,4),"p_leaf",F(3,16),
          "threshold",4*(H(4)-1)/H(3))
if __name__=="__main__":
    exact_checks()
