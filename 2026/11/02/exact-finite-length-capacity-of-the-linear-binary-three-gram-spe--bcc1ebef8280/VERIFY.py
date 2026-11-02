#!/usr/bin/env python3
"""Standalone checks for exact linear binary three-gram profile enumeration.
Uses only Python's standard library. Finite checks support but do not prove the theorem.
"""
from itertools import combinations

Q = [1, 6, -1, -1, 4, 5, 9, 4, 0, -3, 0, 2]

def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return out

DEN=[1]
for block in ([1,-2,1],[1,0,-1],[1,0,0,-1],[1,0,0,0,-1]):
    DEN=multiply(DEN,block)

def formula_to_m(M):
    arr=[]
    for m in range(M+1):
        val=(Q[m] if m<len(Q) else 0)
        for j in range(1,min(m,len(DEN)-1)+1):val-=DEN[j]*arr[m-j]
        arr.append(val)
    return arr

EDGES=[(0,0),(0,1),(1,2),(1,3),(2,0),(2,1),(3,2),(3,3)]

def is_valid(c):
    out=[0]*4;inc=[0]*4;active=set();neighbor=[set() for _ in range(4)]
    for k,(v,w) in enumerate(EDGES):
        if c[k]:
            out[v]+=c[k];inc[w]+=c[k]
            active.add(v);active.add(w)
            neighbor[v].add(w);neighbor[w].add(v)
    if not active:return False
    delta=[out[i]-inc[i] for i in range(4)]
    if any(abs(t)>1 for t in delta):return False
    if not (delta==[0,0,0,0] or (delta.count(1)==delta.count(-1)==1)):
        return False
    stack=[next(iter(active))];seen=set(stack)
    while stack:
        v=stack.pop()
        for w in neighbor[v]:
            if w not in seen:seen.add(w);stack.append(w)
    return seen==active


def compositions(total,k):
    # Stars-and-bars, one tuple per 8-vector.
    for bars in combinations(range(total+k-1),k-1):
        prev=-1;cur=[]
        for v in bars:
            cur.append(v-prev-1);prev=v
        cur.append(total+k-2-prev)
        yield tuple(cur)

def count_flow_vectors(m):
    return sum(is_valid(v) for v in compositions(m,8))

def word_profile(word,n):
    vec=[0]*8
    for shift in range(n-3,-1,-1):vec[(word>>shift)&7]+=1
    return tuple(vec)

def euler_reconstruct(c):
    out=[0]*4;inc=[0]*4
    adj=[[] for _ in range(4)]
    for i,(v,w) in enumerate(EDGES):
        out[v]+=c[i];inc[w]+=c[i]
        adj[v].extend([w]*c[i])
    starts=[i for i in range(4) if out[i]-inc[i]==1]
    start=starts[0] if starts else next(i for i in range(4) if out[i])
    stack=[start];trail=[]
    while stack:
        u=stack[-1]
        if adj[u]:stack.append(adj[u].pop())
        else:trail.append(stack.pop())
    trail.reverse()
    assert len(trail)==sum(c)+1
    bits=[start>>1,start&1]
    for node in trail[1:]:bits.append(node&1)
    got=word_profile(int(''.join(map(str,bits)),2),len(bits))
    assert got==c, (c,got)


def run():
    f=formula_to_m(70)
    expect={3:8,4:15,5:28,6:52,7:92,8:151,9:240,10:363,11:532,12:757,
            13:1048,14:1416,15:1880,16:2449,17:3140,18:3971}
    for n,target in expect.items():
        assert f[n-2]==target,(n,f[n-2],target)
    for n in range(3,17):
        profiles={word_profile(x,n) for x in range(1<<n)}
        assert len(profiles)==f[n-2],('literal',n,len(profiles),f[n-2])
        print('brute',n,len(profiles))
    for m in range(1,17):
        total=count_flow_vectors(m)
        assert total==f[m],('flow',m,total,f[m])
        print('flow',m,total)
    # Certificate replay on all short vectors, not merely random examples.
    count=0
    for m in range(1,10):
        for c in compositions(m,8):
            if is_valid(c):euler_reconstruct(c);count+=1
    print('Euler witnesses:',count)
    print('Recurrence coefficients through m=70:',len(f))
    print('VERIFY_OK')

if __name__=='__main__':run()
