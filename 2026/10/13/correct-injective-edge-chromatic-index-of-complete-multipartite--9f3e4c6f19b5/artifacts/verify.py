from itertools import combinations
from functools import lru_cache


def integer_partitions(n, min_parts=2):
    out=[]
    def rec(rem, maxv, cur):
        if rem==0:
            if len(cur)>=min_parts:
                out.append(tuple(cur))
            return
        for x in range(min(maxv,rem),0,-1):
            cur.append(x); rec(rem-x,x,cur); cur.pop()
    rec(n,n,[])
    return out


def graph(sizes):
    verts=[]
    part=[]
    for i,s in enumerate(sizes):
        for j in range(s):
            verts.append((i,j)); part.append(i)
    edges=[]
    for a,b in combinations(range(len(verts)),2):
        if part[a]!=part[b]: edges.append((a,b))
    return verts,part,edges


def adj_vertex(u,v,part):
    return u!=v and part[u]!=part[v]


def edge_conflict(e,f,part):
    a,b=e; c,d=f
    s=set(e)&set(f)
    if s:
        if len(s)!=1: return False
        x=next(iter(s))
        y=b if a==x else a
        z=d if c==x else c
        return adj_vertex(y,z,part)  # common triangle
    # line-graph distance 2 iff a connector edge joins an endpoint of e to an endpoint of f
    return any(adj_vertex(x,y,part) for x in e for y in f)


def same_cut(e,f,part):
    return frozenset((part[e[0]],part[e[1]]))==frozenset((part[f[0]],part[f[1]]))


def theorem_conflict(e,f,part):
    if same_cut(e,f,part):
        return len(set(e)&set(f))==0
    return True


def conflict_graph(sizes):
    _,part,edges=graph(sizes)
    m=len(edges)
    A=[set() for _ in range(m)]
    for i,j in combinations(range(m),2):
        if edge_conflict(edges[i],edges[j],part):
            A[i].add(j);A[j].add(i)
    return edges,A,part


def chromatic_number(A):
    n=len(A)
    if n==0: return 0
    order=sorted(range(n), key=lambda v: len(A[v]), reverse=True)
    best=n
    color=[-1]*n
    sat=[set() for _ in range(n)]
    uncolored=set(range(n))

    def choose():
        return max(uncolored, key=lambda v:(len(sat[v]),len(A[v])))
    def rec(used):
        nonlocal best
        if not uncolored:
            best=min(best,used); return
        if used>=best: return
        v=choose()
        forbidden={color[w] for w in A[v] if color[w]>=0}
        # existing colors first
        for c in range(used):
            if c in forbidden: continue
            color[v]=c; uncolored.remove(v)
            changed=[]
            for w in A[v]:
                if w in uncolored and c not in sat[w]: sat[w].add(c); changed.append(w)
            rec(used)
            for w in changed: sat[w].remove(c)
            uncolored.add(v); color[v]=-1
        if used+1<best:
            c=used
            color[v]=c; uncolored.remove(v)
            changed=[]
            for w in A[v]:
                if w in uncolored and c not in sat[w]: sat[w].add(c); changed.append(w)
            rec(used+1)
            for w in changed: sat[w].remove(c)
            uncolored.add(v); color[v]=-1
    # greedy upper bound
    greedy={}
    for v in order:
        fs={greedy[w] for w in A[v] if w in greedy}
        c=0
        while c in fs:c+=1
        greedy[v]=c
    best=1+max(greedy.values())
    rec(0)
    return best


def formula(sizes):
    return sum(min(sizes[i],sizes[j]) for i in range(len(sizes)) for j in range(i+1,len(sizes)))


def optimal_partition_count_formula(sizes):
    t=sum(1 for i in range(len(sizes)) for j in range(i+1,len(sizes)) if sizes[i]==sizes[j] and sizes[i]>=2)
    return 1<<t


def count_unlabeled_optimal(A,k,cap=10_000_000):
    # canonical restricted-growth color assignments in a fixed vertex order;
    # each set partition into independent classes is counted once.
    n=len(A)
    if n==0:return 1
    order=sorted(range(n), key=lambda v:len(A[v]), reverse=True)
    classes=[]
    count=0
    def rec(pos):
        nonlocal count
        if count>cap: raise RuntimeError('count cap')
        if pos==n:
            if len(classes)==k: count+=1
            return
        # cannot reach k if too few vertices remain
        if len(classes)+(n-pos)<k:return
        v=order[pos]
        for c,cl in enumerate(classes):
            if all(w not in A[v] for w in cl):
                cl.append(v);rec(pos+1);cl.pop()
        if len(classes)<k:
            classes.append([v]);rec(pos+1);classes.pop()
    rec(0)
    return count


def construction(sizes):
    verts,part,edges=graph(sizes)
    colors={}
    color_id=0
    for i in range(len(sizes)):
        for j in range(i+1,len(sizes)):
            # choose smaller shore; deterministic tie choose i
            center_part=i if sizes[i]<=sizes[j] else j
            centers=[v for v,p in enumerate(part) if p==center_part]
            for center in centers:
                for ei,e in enumerate(edges):
                    if center in e and frozenset((part[e[0]],part[e[1]]))==frozenset((i,j)):
                        colors[ei]=color_id
                color_id+=1
    assert len(colors)==len(edges)
    for a,b in combinations(range(len(edges)),2):
        if colors[a]==colors[b] and edge_conflict(edges[a],edges[b],part):
            raise AssertionError(('construction conflict',sizes,edges[a],edges[b]))
    if color_id!=formula(sizes): raise AssertionError(('construction count',sizes,color_id,formula(sizes)))
    return len(edges)


def run():
    structural_pairs=0; exact_types=0; exact_edges=0; count_types=0; counted_partitions=0
    # Exact conflict graph and chromatic-number stress tests through order 7.
    for n in range(2,8):
        for sizes in integer_partitions(n):
            edges,A,part=conflict_graph(sizes)
            for x,y in combinations(range(len(edges)),2):
                got=edge_conflict(edges[x],edges[y],part)
                want=theorem_conflict(edges[x],edges[y],part)
                if got!=want: raise AssertionError(('structure',sizes,edges[x],edges[y],got,want))
                structural_pairs+=1
            chi=chromatic_number(A)
            if chi!=formula(sizes): raise AssertionError(('chi',sizes,chi,formula(sizes)))
            exact_types+=1; exact_edges+=len(edges)
            # Exact optimal partition counts through order 6 where tractable.
            if n<=6:
                cnt=count_unlabeled_optimal(A,chi)
                want=optimal_partition_count_formula(sizes)
                if cnt!=want: raise AssertionError(('count',sizes,cnt,want))
                count_types+=1; counted_partitions+=cnt
    constructive_types=0; constructive_edges=0
    # Larger direct construction checks through order 25.
    for n in range(2,26):
        for sizes in integer_partitions(n):
            constructive_edges+=construction(sizes)
            constructive_types+=1
    print('ALL CHECKS PASSED; exact_types=%d; exact_edges=%d; structural_pairs=%d; count_types=%d; counted_optimal_partitions=%d; constructive_types=%d; constructive_edges=%d; max_constructive_order=25' % (
        exact_types,exact_edges,structural_pairs,count_types,counted_partitions,constructive_types,constructive_edges))

if __name__=='__main__': run()
