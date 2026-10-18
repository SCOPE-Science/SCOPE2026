#!/usr/bin/env python3
"""Exact reproducible edge-open-packing bounds on binary 5- and 6-cubes."""

def edges(n):
    return [(u,u^(1<<j)) for u in range(1<<n) for j in range(n) if u < (u^(1<<j))]

def conflict(e,f):
    a,b=e; c,d=f
    if len({a,b,c,d})<4:
        return False
    return any((x^y).bit_count()==1 for x in (a,b) for y in (c,d))

def companion_graph(n):
    ee=edges(n)
    N=len(ee)
    compat=[0]*N
    for i in range(N):
        for j in range(i+1,N):
            if not conflict(ee[i],ee[j]):
                compat[i] |= 1<<j
                compat[j] |= 1<<i
    return ee,compat

def nonexistence(n,target):
    # Every edge is equivalent by a cube translation and coordinate permutation.
    # Thus any selected set of size target can be moved to include edge ee[0].
    ee,adj=companion_graph(n)
    calls=0
    def exists(P,depth):
        nonlocal calls
        calls+=1
        if depth>=target:
            return True
        if depth+P.bit_count()<target:
            return False
        U=P
        order=[]
        colors=[]
        color=0
        while U:
            color+=1
            available=U
            while available:
                b=available & -available
                i=b.bit_length()-1
                order.append(i)
                colors.append(color)
                U^=b
                available ^= b
                available &= ~adj[i]
        for idx in range(len(order)-1,-1,-1):
            if depth+colors[idx]<target:
                return False
            i=order[idx]
            if exists(P&adj[i],depth+1):
                return True
            P &= ~(1<<i)
        return False
    assert not exists(adj[0],1)
    return calls

WITNESSES={
 5:[(0,1),(0,2),(0,4),(11,15),(13,15),(14,15),
    (19,23),(21,23),(22,23),(24,25),(24,26),(24,28)],
 6:sorted((min(c,c^(1<<j)),max(c,c^(1<<j)))
          for c in (0,15,51,60) for j in range(6))
}

def main():
    for n,size in [(5,12),(6,24)]:
        S=WITNESSES[n]
        assert len(S)==size and len(set(S))==size
        E=set(edges(n))
        assert set(S)<=E
        for i,e in enumerate(S):
            for f in S[i+1:]:
                assert not conflict(e,f),(e,f)
        calls=nonexistence(n,size+1)
        print(f'Q{n}: edges={n*2**(n-1)}, witness={size}, exact_upper={size}, search_nodes={calls}')
    print('VERIFY_OK')
if __name__=='__main__':
    main()
