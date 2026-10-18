"""Reproduce exact open-neighborhood shattering profiles on line graphs of complete graphs.
All computations use Python's standard library and integer arithmetic.
Run: python3 verify.py
"""
from itertools import combinations
from math import comb, factorial

# Graph types with at most four edges. Vertices are 0,...,v-1.
# The order of edges in each tuple fixes the binary trace-mask convention.
TYPES = {
 1: [((0,1),)],
 2: [((0,1),(0,2)), ((0,1),(2,3))],
 3: [((0,1),(0,2),(0,3)), ((0,1),(0,2),(1,2)),
     ((0,1),(0,2),(1,3)), ((0,1),(0,2),(3,4)),
     ((0,1),(2,3),(4,5))],
 4: [((0,1),(0,2),(0,3),(0,4)),
     ((0,1),(0,2),(0,3),(1,2)),
     ((0,1),(0,2),(0,3),(1,4)),
     ((0,1),(0,2),(0,3),(4,5)),
     ((0,1),(0,2),(1,2),(3,4)),
     ((0,1),(0,2),(1,3),(2,3)),
     ((0,1),(0,2),(1,3),(2,4)),
     ((0,1),(0,2),(1,3),(4,5)),
     ((0,1),(0,2),(3,4),(3,5)),
     ((0,1),(0,2),(3,4),(5,6)),
     ((0,1),(2,3),(4,5),(6,7))]
}
# Counts of distinct traces with 0, 1, 2 fresh vertices.
EXPECTED_TRACE_COUNTS = {
 1: [(1,2,2)],
 2: [(3,3,4),(2,4,4)],
 3: [(3,7,8),(3,3,4),(3,7,8),(7,8,8),(4,7,7)],
 4: [(10,15,16),(3,7,8),(10,15,16),(8,13,13),
     (7,8,8),(3,7,8),(10,15,16),(8,13,13),
     (15,15,16),(11,13,13),(7,11,11)]
}
# Count of labeled graphs per chosen vertex support, v!/|Aut(F)|.
EMBEDDING_COUNTS = {
 1: [1], 2: [3,3], 3: [4,1,12,30,15],
 4: [5,12,60,60,10,3,60,180,90,315,105]
}

def trace_masks(edges, n):
    seen=set()
    for a,b in combinations(range(n),2):
        mask=0
        for i,(u,v) in enumerate(edges):
            if (a,b)!=(u,v) and (a==u or a==v or b==u or b==v):
                mask |= 1<<i
        seen.add(mask)
    return seen

def signature(edges):
    vs=set(x for e in edges for x in e)
    adj={v:set() for v in vs}
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    todo=set(vs);comps=[]
    while todo:
        start=min(todo); todo.remove(start)
        comp={start};todo_stack=[start]
        while todo_stack:
            u=todo_stack.pop()
            for w in adj[u]&todo:
                todo.remove(w);comp.add(w);todo_stack.append(w)
        comps.append((len(comp),tuple(sorted((len(adj[x]) for x in comp),reverse=True))))
    return tuple(sorted(comps))

def exact_count(n, k):
    if k==0: return 1
    m=comb(n,2)
    es=list(combinations(range(n),2))
    active=[]
    for e in es:
        bit=0
        for j,f in enumerate(es):
            if e!=f and (e[0] in f or e[1] in f): bit|=1<<j
        active.append(bit)
    goal=(1 << (1<<k))-1
    total=0
    for I in combinations(range(m),k):
        amask=sum(1<<i for i in I)
        masks=0
        for bit in active:
            intersection=bit&amask
            t=0
            for j,index in enumerate(I):
                t|=((intersection>>index)&1)<<j
            masks|=1<<t
            if masks==goal: break
        if masks==goal:total+=1
    return total

def C(n,k): return comb(n,k) if n>=k else 0

def expected(n):
    return [1, C(n,2) if n>=3 else 0,
       (3*C(n,3)+3*C(n,4)) if n>=5 else 0,
       (16*C(n,4)+30*C(n,5)) if n>=6 else 0,
       (125*C(n,5) if n>=7 else 0)+(90*C(n,6) if n>=8 else 0)]

def main():
    type_map={}
    for k,rows in TYPES.items():
        assert len(rows)==(1,2,5,11)[k-1]
        for j,edges in enumerate(rows):
            v=1+max(x for e in edges for x in e)
            assert len(set(x for e in edges for x in e))==v
            for t,expect in enumerate(EXPECTED_TRACE_COUNTS[k][j]):
                observed=len(trace_masks(edges,v+t))
                assert observed==expect, (k,j,t,observed,expect)
            sig=signature(edges)
            assert (k,sig) not in type_map
            type_map[(k,sig)]=j
        print('REPRESENTATIVES',k,'types',len(rows),'trace_table=PASS')
    # Completeness of the finite graph-type list: on at most 2k vertices
    # any isolate-free k-edge graph is tested by its component-degree signature.
    seen={k:set() for k in TYPES}
    for k in TYPES:
        es=list(combinations(range(2*k),2))
        for chosen in combinations(es,k):
            support=set(x for e in chosen for x in e)
            if support != set(range(len(support))):continue
            sig=signature(chosen)
            assert (k,sig) in type_map, (k,chosen,sig)
            seen[k].add(sig)
        assert len(seen[k])==len(TYPES[k])
    print('GRAPH_TYPES_COMPLETE',sum(map(len,seen.values())),'PASS')
    # Check the binomial-orbit multiplier for each representative by embeddings
    # at its minimum possible support size, using edge-signatures.
    for k,rows in TYPES.items():
        for j,edges in enumerate(rows):
            v=1+max(x for e in edges for x in e)
            value=0
            for chosen in combinations(combinations(range(v),2),k):
                if len(set(x for e in chosen for x in e))==v and signature(chosen)==signature(edges):
                    value+=1
            assert value==EMBEDDING_COUNTS[k][j],(k,j,value)
    print('LABELED_MULTIPLIERS','PASS')
    tested=0
    for n in range(2,11):
        got=[exact_count(n,k) for k in range(5)]
        assert got==expected(n),(n,got,expected(n))
        tested+=sum(C(comb(n,2),k) for k in range(1,5))
        print('SHATTER_COUNTS',n,got,'PASS')
    print('VERIFY_OK candidate_subsets',tested,'trace_table=PASS class_completeness=PASS orbit_sizes=PASS exact_coefficients=PASS')
if __name__=='__main__': main()
