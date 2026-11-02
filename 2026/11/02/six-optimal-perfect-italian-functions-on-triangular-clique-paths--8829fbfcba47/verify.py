#!/usr/bin/env python3
"""Exact, standalone finite-state certificate for perfect Italian functions.
Run: python3 verify.py. Uses only the Python standard library.
All 27^2 column-pair states are included, including unreachable states.
"""
from itertools import product, permutations
from hashlib import sha256
from json import dumps

C = tuple(product((0, 1, 2), repeat=3))
Q = len(C)
ZERO = (0, 0, 0)
WEIGHT = tuple(sum(c) for c in C)
INF = 10**15

def local(a, b, c):
    """A zero in middle column b has neighbor-label sum exactly two."""
    sb = sum(b)
    return all(b[r] != 0 or sb + a[r] + c[r] == 2 for r in range(3))

# State dictionary maps (previous, last) indices to (cost, multiplicity).
# Absent states mean infinite cost and zero multiplicity.
ADMISSIBLE = {(a, b): tuple(c for c in range(Q) if local(C[a], C[b], C[c]))
              for a in range(Q) for b in range(Q)}

def start():
    return {(a,b): (WEIGHT[a]+WEIGHT[b], 1)
            for a in range(Q) for b in range(Q) if local(ZERO,C[a],C[b])}

def advance(D):
    E={}
    for (a,b),(v,ct) in D.items():
        for c in ADMISSIBLE[a,b]:
            pair=(b,c); t=v+WEIGHT[c]
            old=E.get(pair)
            if old is None or t<old[0]:
                E[pair]=(t,ct)
            elif t==old[0]:
                E[pair]=(t,old[1]+ct)
    return E

def finish(D):
    finals=[(v,ct) for (a,b),(v,ct) in D.items()
            if local(C[a],C[b],ZERO)]
    v=min(v for v,ct in finals)
    return v,sum(ct for q,ct in finals if q==v)

def shift(D):
    return {k:(v+1,ct) for k,(v,ct) in D.items()}

def witnesses(n):
    ans=[]
    for order in permutations(range(3)):
        # periodic row labels r_1,r_2,r_3,...
        r=lambda j: order[(j-1)%3]
        columns=[]
        for j in range(1,n+1):
            selected={r(1),r(2)} if j==1 else (
                     {r(n-1),r(n)} if j==n else {r(j)})
            columns.append(tuple(int(k in selected) for k in range(3)))
        ans.append(tuple(columns))
    return ans

def graph_valid(columns):
    n=len(columns)
    for j in range(n):
        for row in range(3):
            if columns[j][row] != 0:continue
            s=sum(columns[j][other] for other in range(3) if other != row)
            if j:s+=columns[j-1][row]
            if j+1<n:s+=columns[j+1][row]
            if s != 2:return False
    return True

def direct_bounded(n, limit):
    """Independent vertex-by-vertex exhaustive search of ALL labelings
    of weight <= limit, using graph neighborhoods, without column states.
    """
    N=3*n
    adj=[]
    for j in range(n):
        for r in range(3):
            adj.append(tuple(j*3+s for s in range(3) if s!=r)+
                       ((j-1)*3+r,) * (j>0)+
                       ((j+1)*3+r,) * (j+1<n))
    labels=[0]*N
    counts=[0]*(limit+1)
    def rec(i, budget, wt):
        if i==N:
            for v in range(N):
                if labels[v]==0 and sum(labels[u] for u in adj[v])!=2:
                    return
            counts[wt]+=1
            return
        for val in range(min(2,budget)+1):
            labels[i]=val
            rec(i+1,budget-val,wt+val)
    rec(0,limit,0)
    return counts

def main():
    D=start()
    tables={2:D}
    for n in range(3,15):
        D=advance(D)
        tables[n]=D
    # Exact all-state minimum-plus/tie-count vector identity, not sampling.
    assert shift(tables[13])==tables[14], '13-to-14 stationary certificate failed'
    for n in range(4,15):
        assert finish(tables[n])==(n+2,6),(n,finish(tables[n]))
    # By recurrence homogeneity the 13-to-14 vector identity propagates
    # indefinitely, proving n+2 and six solutions at all n >= 4.
    for n in range(4,50):
        W=witnesses(n)
        assert len(W)==len(set(W))==6
        assert all(graph_valid(v) and sum(map(sum,v))==n+2 for v in W)
    for n in (4,5,6):
        counts=direct_bounded(n,n+2)
        assert sum(counts[:-1])==0 and counts[-1]==6,(n,counts)
    v13=tables[13]
    payload=tuple((a,b,v13.get((a,b),(INF,0)))
                  for a in range(Q) for b in range(Q))
    fingerprint=sha256(dumps(payload,separators=(',',':')).encode()).hexdigest()
    print('VERIFY_OK: 27 columns, 729 pair states,',len(v13),'reachable')
    print('D13->D14 exact full-vector equality with cost +1 and unchanged tie counts')
    print('Base optimal minima/counts n=4..14: (n+2,6); six periodic constructions n=4..49')
    print('Independent vertex-neighborhood exhaustive labelings of weight<=n+2: n=4,5,6')
    print('State-vector SHA256:',fingerprint)
    print('Base table:', {n:finish(tables[n]) for n in range(2,15)})

if __name__=='__main__':main()
