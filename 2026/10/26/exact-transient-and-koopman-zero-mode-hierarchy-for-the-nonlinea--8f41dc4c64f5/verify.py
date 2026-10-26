"""Reproducible finite checks for the parity-sector theorem for rule 154.

Independent of proof; exhaustive samples cannot establish assertions for all ring sizes.
Run: python3 verify.py
"""
from collections import defaultdict

def update(x, n):
    mask = (1 << n) - 1
    left = ((x << 1) & mask) | (x >> (n - 1))
    right = (x >> 1) | ((x & 1) << (n - 1))
    return left ^ right ^ (x & right)

def v2(x):
    k=0
    while x%2==0:
        k+=1;x//=2
    return k

def recurrent_pair_scc():
    verts = [(a,b,A,B) for a in range(2) for b in range(2)
             for A in range(2) for B in range(2)
             if (a,b)!=(A,B)]
    local=lambda a,b,c:a^c^(b&c)
    edges={}
    for a,b,A,B in verts:
        ends=[]
        for c in range(2):
            for C in range(2):
                w=(b,c,B,C)
                if w in verts and local(a,b,c)==local(A,B,C):
                    ends.append(w)
        edges[a,b,A,B]=ends
    # Strongly connected components by reachability on twelve states.
    def reach(v):
        visited={v}; stack=[v]
        while stack:
            for w in edges[stack.pop()]:
                if w not in visited:
                    visited.add(w);stack.append(w)
        return visited
    components=set()
    for v in verts:
        c=tuple(sorted(w for w in verts if v in reach(w) and w in reach(v)))
        if len(c)>1 or v in edges[v]: components.add(c)
    expected={
      tuple(sorted(((0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)))),
      tuple(sorted(((0,1,1,0),(1,0,0,1)))),
    }
    assert components == expected, (components, expected)
    return len(verts),len(components)

def main():
    states_checked=0
    for n in range(3,17):
        size=1<<n
        image=[update(x,n) for x in range(size)]
        if n%2:
            assert len(set(image))==size,('odd',n)
            continue
        m=n//2;q=1<<v2(m)
        assert len(set(image))==size-(1<<m),('image',n)
        # Analyse actual functional graph using iterative elimination.
        deg=[0]*size
        for y in image:deg[y]+=1
        stack=[i for i,d in enumerate(deg) if not d]
        k=0
        while k<len(stack):
            v=stack[k];k+=1;w=image[v];deg[w]-=1
            if deg[w]==0:stack.append(w)
        observed_periodic=size-len(stack)
        expected_periodic=size-(1<<(m+1))+(1<<(m-q+1))
        assert observed_periodic==expected_periodic,(n,observed_periodic,expected_periodic)
        # Verify exact image ranks at all stages, and the whole preperiod histogram.
        cur=list(range(size));ranks=[]
        for t in range(q+2):
            observed_rank=len(set(cur));pred=size-(1<<(m+1))+(1<<(m-min(t,q)+1))
            assert observed_rank==pred,(n,t,observed_rank,pred)
            ranks.append(observed_rank)
            cur=[image[x] for x in cur]
        # Prove count of exact preperiods computationally by computing distances to cycles.
        cyc=[i for i in range(size) if deg[i]>0]
        dist=[-1]*size
        for i in cyc:dist[i]=0
        # Advance simultaneously; an image's distance is known after each wave.
        for t in range(1,q+1):
            for x in range(size):
                if dist[x]<0 and dist[image[x]]==t-1:dist[x]=t
        assert all(d>=0 for d in dist)
        for t in range(1,q+1):
            pred=1<<(m-q+t)
            got=dist.count(t)
            assert got==pred,(n,t,got,pred)
        assert max(dist)==q
        # Nilpotent zero-mode blocks are obtained from image-rank second differences.
        Bs=[ranks[t-1]-2*ranks[t]+ranks[t+1] for t in range(1,q+1)]
        predicted=[(1<<(m-t)) if t<q else (1<<(m-q+1)) for t in range(1,q+1)]
        assert Bs==predicted,(n,Bs,predicted)
        assert sum((i+1)*b for i,b in enumerate(Bs))==size-expected_periodic
        states_checked+=size
    nv,nc=recurrent_pair_scc()
    print('VERIFY_OK states_examined_even=',states_checked,
          'ring_sizes=3..16','offdiagonal_pair_vertices=',nv,'cyclic_pair_components=',nc)

if __name__ == '__main__':main()
