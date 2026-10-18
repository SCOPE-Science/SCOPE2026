#!/usr/bin/env python3
"""Exact finite-state certificate for total identifying domination on prisms.
Run: python3 verify.py (Python standard library only).
"""
from itertools import product, combinations
from hashlib import sha256
from array import array

ALPHABET=range(4)
STATES=list(product(ALPHABET,repeat=4))
STATE_INDEX={s:i for i,s in enumerate(STATES)}
INF=10**6

def pop(x): return x.bit_count()

def local_ok(p):
    # A length-five window has ten vertices (column,level).
    marks=0
    for j in range(5):
        for a in range(2):
            if (p[j]>>a)&1:
                marks|=1<<(2*j+a)
    def hood(j,a,closed=False):
        vertices=[(j-1,a),(j+1,a),(j,1-a)]
        if closed: vertices.append((j,a))
        return sum(1<<(2*k+b) for k,b in vertices if 0<=k<5)
    for a in range(2):
        if marks & hood(2,a)==0:
            return False
    # Each unordered close pair is checked at its first cyclic column.
    for a in range(2):
        for j in (1,2,3):
            for b in range(2):
                if j==1 and b<=a:continue
                if marks & (hood(1,a,True)^hood(j,b,True))==0:
                    return False
    return True

def graph():
    edges=[]
    for s in STATES:
        for c in ALPHABET:
            if local_ok(s+(c,)):
                edges.append((STATE_INDEX[s],STATE_INDEX[s[1:]+(c,)],pop(c)))
    return edges

def components(edges):
    size=len(STATES)
    adj=[[] for _ in range(size)]
    rev=[[] for _ in range(size)]
    for u,v,_ in edges:
        adj[u].append(v);rev[v].append(u)
    seen=set();order=[]
    def dfs(u):
        seen.add(u)
        for v in adj[u]:
            if v not in seen:dfs(v)
        order.append(u)
    for u in range(size):
        if u not in seen: dfs(u)
    seen.clear();ret=[]
    def rdfs(u,comp):
        seen.add(u);comp.add(u)
        for v in rev[u]:
            if v not in seen:rdfs(v,comp)
    for u in reversed(order):
        if u not in seen:
            c=set();rdfs(u,c);ret.append(c)
    cyclic=[c for c in ret if len(c)>1 or any(u==v and u in c for u,v,_ in edges)]
    assert len(cyclic)==1, [len(c) for c in cyclic]
    return cyclic[0]

def reduced_edges(edges,comp):
    ordered=sorted(comp)
    index={u:i for i,u in enumerate(ordered)}
    return ordered,[(index[u],index[v],w) for u,v,w in edges if u in comp and v in comp]

def powers(edges,count):
    m=1+max(max(u,v) for u,v,w in edges)
    current=[[INF]*m for _ in range(m)]
    for i in range(m):current[i][i]=0
    snapshots={}
    for k in range(1,count+1):
        nxt=[[INF]*m for _ in range(m)]
        for u,v,w in edges:
            for start in range(m):
                z=current[start][u]+w
                if z<nxt[start][v]:nxt[start][v]=z
        current=nxt
        if k in (7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23):
            snapshots[k]=current
    return snapshots

def direct_requirements(n):
    v=2*n
    openhood=[]
    for j in range(n):
        for a in range(2):
            openhood.append(sum(1<<(2*k+b) for k,b in (((j-1)%n,a),((j+1)%n,a),(j,1-a))))
    closed=[openhood[t]|(1<<t) for t in range(v)]
    allreq=set(openhood)
    for a in range(v):
        for b in range(a+1,v):allreq.add(closed[a]^closed[b])
    assert 0 not in allreq
    # Remove supersets: only inclusion-minimal hitting constraints matter.
    return tuple(sorted((x for x in allreq if not any(y!=x and x&y==y for y in allreq)),key=lambda x:(pop(x),x)))

def direct_ok(mask,req):
    return all(mask&x for x in req)

def brute(n):
    req=direct_requirements(n)
    for k in range(2*n+1):
        total=0;witness=None
        for ss in combinations(range(2*n),k):
            bits=sum(1<<j for j in ss)
            if direct_ok(bits,req):
                total+=1
                if witness is None:witness=bits
        if total:return k,total,witness
    raise AssertionError('no code')

def cyclic_ok(p):
    n=len(p)
    return all(local_ok(tuple(p[(i+j)%n] for j in range(5))) for i in range(n))

def encode_columns(bitset,n):
    return tuple(sum(1<<a for a in range(2) if bitset>>(2*j+a)&1) for j in range(n))

def shortest_closed_walk(edges,ordered,n):
    # Exact constructive witness from the min-plus state graph.
    m=len(ordered)
    best=(INF,None,None)
    for source in range(m):
        d=[INF]*m;d[source]=0
        parents=[]
        for t in range(n):
            nxt=[INF]*m;pred=[None]*m
            for u,v,w in edges:
                if d[u]+w<nxt[v]:
                    nxt[v]=d[u]+w;pred[v]=u
            d=nxt;parents.append(pred)
        if d[source]<best[0]:best=(d[source],source,parents)
    val,source,parents=best
    cur=source;states=[cur]
    for t in range(n-1,-1,-1):
        cur=parents[t][cur];assert cur is not None
        states.append(cur)
    assert states[-1]==source
    steps=list(reversed(states))
    # A transition appends the final column of its destination 4-tuple.
    pattern=tuple(STATES[ordered[steps[i+1]]][3] for i in range(n))
    assert sum(pop(c) for c in pattern)==val
    assert cyclic_ok(pattern)
    bits=sum(1<<(2*j+a) for j,c in enumerate(pattern) for a in range(2) if c>>a&1)
    assert direct_ok(bits,direct_requirements(n))
    return val,pattern

def main():
    edges=graph()
    assert len(edges)==661,len(edges)
    c=components(edges)
    ordered,e=reduced_edges(edges,c)
    assert len(c)==147 and len(e)==489,(len(c),len(e))
    mats=powers(e,23)
    assert all(mats[9][i][j]<INF for i in range(147) for j in range(147))
    assert all(mats[16][i][j]==mats[9][i][j]+6 for i in range(147) for j in range(147))
    bases=[min(mats[n][i][i] for i in range(147)) for n in range(7,14)]
    assert bases==[6,8,9,9,10,11,12],bases
    for n in range(7,24):
        d=min(mats[n][i][i] for i in range(147))
        expected=6*(n//7)+[0,2,3,3,4,5,6][n%7]
        assert d==expected,(n,d,expected)
    print('AUTOMATON states=256 edges=661 cyclic_scc=147 cyclic_edges=489')
    print('MINPLUS D16_equals_D9_plus_6 all_21609_entries=TRUE')
    print('TRACES n7_to_13',bases)
    for n in range(3,9):
        optimum,count,bits=brute(n)
        expected=4 if n==3 else (6*(n//7)+[0,2,3,3,4,5,6][n%7] if n>=7 else n)
        assert optimum==expected,(n,optimum,expected)
        if n>=7:
            p=encode_columns(bits,n)
            assert cyclic_ok(p)
        print('BRUTE n=%s optimum=%s count=%s'%(n,optimum,count))
    for n in (7,8):
        req=direct_requirements(n)
        for p in product(ALPHABET,repeat=n):
            bits=sum(1<<(2*j+a) for j,c in enumerate(p) for a in range(2) if c>>a&1)
            assert cyclic_ok(p)==direct_ok(bits,req),(n,p)
        print('EQUIVALENCE n=%s checked=%s'%(n,4**n))
    for n in list(range(7,14)) + [14,15,20,21,22,23]:
        val,p=shortest_closed_walk(e,ordered,n)
        assert val==6*(n//7)+[0,2,3,3,4,5,6][n%7]
        print('WITNESS',n,val,''.join(str(x) for x in p))
    # Minimum formula for n=3..6 is direct brute; for n>=7, D16 = D9+6
    # implies every D_(n+7)=D_n+6 for n>=9 by right multiplication.
    # Remaining n=7,8 are covered by the direct traces n14,15.
    print('VERIFY_OK')
if __name__=='__main__':main()
