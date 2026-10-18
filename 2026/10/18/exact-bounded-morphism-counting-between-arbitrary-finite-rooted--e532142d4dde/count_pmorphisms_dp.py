"""Exact bounded-morphism counts for finite rooted trees (reflexive descendant frames).
Tree is a parent vector with parent[0]=-1 and parent[i]<i for i>0.
No external dependencies. The count is for maps of the vertex sets, not map orbits.
"""
from itertools import combinations


def children(parent):
    ch=[[] for _ in parent]
    assert parent[0] == -1
    for i in range(1,len(parent)):
        assert 0 <= parent[i] < i
        ch[parent[i]].append(i)
    return ch


def count_bounded_surjections(source_parent,target_parent):
    cs=children(source_parent)
    ct=children(target_parent)
    n,m=len(cs),len(ct)
    # Each row is computed from the source leaves upwards.
    F=[[0]*m for _ in range(n)]
    for s in range(n-1,-1,-1):
        for t in range(m-1,-1,-1):
            k=len(ct[t])
            # A(c,t): total bounded mappings of T_c to any generated target subtree U_u, u>=t.
            A={c:F[c][t]+sum(A_cache[c][v] for v in ct[t]) for c in cs[s]} if cs[s] else {}
            # Cover every immediate child of target t by some child source subtree.
            total=0
            for mask in range(1<<k):
                val=1
                for c in cs[s]:
                    possible=A[c]
                    if mask:
                        possible-=F[c][t]
                        for j,v in enumerate(ct[t]):
                            if mask & (1<<j):possible-=F[c][v]
                    val*=possible
                total+=(-1 if mask.bit_count()%2 else 1)*val
            F[s][t]=total
        if 'A_cache' not in locals(): A_cache=[None]*n
        A_cache[s]=[0]*m
        for t in range(m-1,-1,-1):
            A_cache[s][t]=F[s][t]+sum(A_cache[s][v] for v in ct[t])
    return F[0][0]


def count_bounded_surjections_simpler(source_parent,target_parent):
    """Second, enumerative DP: no inclusion-exclusion. Independent coverage enumeration."""
    cs=children(source_parent)
    ct=children(target_parent)
    n,m=len(cs),len(ct)
    descendants=[[] for _ in range(m)]
    for t in range(m-1,-1,-1):
        descendants[t]=[t]+[u for v in ct[t] for u in descendants[v]]
    F=[[0]*m for _ in range(n)]
    for s in range(n-1,-1,-1):
        for t in range(m-1,-1,-1):
            # each subtree maps onto cone of chosen child image
            required=(1<<len(ct[t]))-1
            ways={0:1}
            for c in cs[s]:
                nw={}
                for u in descendants[t]:
                    if u == t: mask=required
                    elif u in ct[t]: mask=1<<ct[t].index(u)
                    else: mask=0
                    for have,w in ways.items():
                        key=have | mask
                        nw[key]=nw.get(key,0)+w*F[c][u]
                ways=nw
            F[s][t]=ways.get(required,0)
    return F[0][0]


def canonical_tree(parent):
    cs=children(parent)
    def rec(i):return tuple(sorted((rec(c) for c in cs[i]),key=str))
    return rec(0)


def trees_up_to(n):
    """All unlabelled nonplane rooted trees as sorted tuple nesting."""
    bysize={1:[()]}
    for size in range(2,n+1):
        options=[]
        for subsize in range(1,size):options += [(subsize,tuple(z)) for z in bysize[subsize]]
        # Build multisets of child trees by increasing index, total size size-1.
        curr=[]
        def rec(start,rem):
            if not rem:
                curr.append(tuple(options[i][1] for i in indices));return
            for j in range(start,len(options)):
                w=options[j][0]
                if w<=rem:
                    indices.append(j);rec(j,rem-w);indices.pop()
        indices=[];rec(0,size-1)
        bysize[size]=curr
    return bysize


def parent_from_shape(shape):
    parent=[-1]
    def rec(sh,i):
        for child in sh:
            j=len(parent);parent.append(i)
            rec(child,j)
    rec(shape,0)
    return tuple(parent)

if __name__ == '__main__':
    bysize=trees_up_to(8)
    print('ROOTED_TREE_COUNTS',[(i,len(bysize[i])) for i in range(1,9)])
    tested=0;nonzero=0;largest=0
    for ns in range(1,9):
        for source in bysize[ns]:
            sp=parent_from_shape(source)
            for mt in range(1,ns+1):
                for target in bysize[mt]:
                    tp=parent_from_shape(target)
                    a=count_bounded_surjections(sp,tp)
                    b=count_bounded_surjections_simpler(sp,tp)
                    if a!=b:raise AssertionError((sp,tp,a,b))
                    tested+=1;nonzero+=(a>0);largest=max(largest,a)
    print('INDEPENDENT_RECURRENCE_MATCH',tested,'NONZERO',nonzero,'MAX',largest)
    # As checks, a source star with a leaves maps to a target star with b leaves
    # in exactly the number of onto functions [a] -> [b].
    from math import comb
    for a in range(0,10):
        for b in range(0,10):
            sp=(-1,)+(0,)*a;tp=(-1,)+(0,)*b
            actual=count_bounded_surjections(sp,tp)
            expected=sum((-1)**j*comb(b,j)*(b-j)**a for j in range(b+1)) if b else 1
            if actual!=expected:raise AssertionError(('STAR',a,b,actual,expected))
    print('STAR_SURJECTION_IDENTITY_OK',100)
