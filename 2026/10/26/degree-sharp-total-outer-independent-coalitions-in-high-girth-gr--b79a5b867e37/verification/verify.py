#!/usr/bin/env python3
"""Independent finite checks for a degree-sharp total outer-independent coalition theorem."""
from itertools import combinations


def graph(n, edges):
    a = [0]*n
    for u,v in edges:
        assert 0 <= u < v < n
        a[u] |= 1 << v
        a[v] |= 1 << u
    return tuple(a)


def cycle(n):
    return graph(n, {tuple(sorted((i,(i+1)%n))) for i in range(n)})


def cycle_bouquet(lengths):
    edges=[]; last=1
    for k in lengths:
        vertices=[0]+list(range(last,last+k-1)); last += k-1
        for i in range(k):edges.append(tuple(sorted((vertices[i],vertices[(i+1)%k]))))
    return graph(last,edges)


def petersen():
    e=[]
    for i in range(5):
        e.extend([(min(i,(i+1)%5),max(i,(i+1)%5)),(i,5+i),
                  tuple(sorted((5+i,5+(i+2)%5)))])
    return graph(10,e)


def heawood():
    e=[]
    for i in range(7):
        for j in (i,(i+1)%7,(i+3)%7):e.append((j,7+i))
    return graph(14,e)


def cube(d):
    return graph(1<<d,[(i,i^(1<<j)) for i in range(1<<d) for j in range(d) if i < (i^(1<<j))])


def degree(a):return max(x.bit_count() for x in a)


def is_toi(a,mask):
    n=len(a); full=(1<<n)-1
    for x in range(n):
        if not a[x]&mask:return False
    outside=full^mask
    for x in range(n):
        if ((outside>>x)&1) and (a[x]&outside):return False
    return True


def local_condition(a,v):
    n=len(a); N=a[v]; X=((1<<n)-1)^N
    # Every vertex other than v has a neighbour in X, and N is independent.
    return all(not ((N>>u)&1 and a[u]&N) for u in range(n)) and all(a[u]&X for u in range(n) if u!=v)


def construct(a,v):
    n=len(a); N=a[v]; X=((1<<n)-1)^N
    parts=[X]+[1<<i for i in range(n) if (N>>i)&1]
    assert sum(p.bit_count() for p in parts)==n
    assert not any(is_toi(a,p) for p in parts)
    assert all(is_toi(a,X|p) for p in parts[1:])
    return parts


def girth_at_least_five(a):
    n=len(a)
    for u in range(n):
        for v in range(u+1,n):
            if a[u] & (1<<v):
                assert a[v] & (1<<u)
                if a[u]&a[v]:return False
            if (a[u]&a[v]).bit_count()>1:return False
    return True


def direct_coalition_number(a):
    n=len(a); good=[is_toi(a,s) for s in range(1<<n)]
    best=0
    def visit(parts,next_i):
        nonlocal best
        if next_i==n:
            if len(parts)<=best:return
            if any(good[p] for p in parts):return
            if all(any(good[p|q] for j,q in enumerate(parts) if p!=q) for p in parts):
                best=len(parts)
            return
        bit=1<<next_i
        for j in range(len(parts)):
            parts[j]|=bit;visit(parts,next_i+1);parts[j]^=bit
        parts.append(bit);visit(parts,next_i+1);parts.pop()
    visit([],0)
    return best


def check_case(name,a,exhaustive=False,require_girth=True):
    n=len(a)
    if require_girth:
        assert min(x.bit_count() for x in a)>=2 and girth_at_least_five(a)
    D=degree(a)
    v=next(i for i,x in enumerate(a) if x.bit_count()==D and local_condition(a,i))
    ps=construct(a,v)
    assert len(ps)==D+1
    if exhaustive:
        val=direct_coalition_number(a)
        assert val==D+1,(name,D,val)
    print('%s n=%d Delta=%d partition=%d local_vertex=%d%s' %
          (name,n,D,len(ps),v,' exact_partition_enumeration=OK' if exhaustive else ''))


def main():
    # Exhaustively check the hypothesis and the canonical coalition construction on every graph through order six.
    inspected=0; qualifying=0
    for n in range(3,7):
        pair=list(combinations(range(n),2))
        for mask in range(1<<len(pair)):
            a=graph(n,[p for i,p in enumerate(pair) if (mask>>i)&1]);inspected+=1
            if min(x.bit_count() for x in a)<2 or not girth_at_least_five(a):continue
            qualifying+=1
            check_case('small-%d-%d'%(n,mask),a,exhaustive=True)
    print('all_graphs_up_to_six=%d eligible=%d'%(inspected,qualifying))
    for n in (7,8):check_case('cycle-%d'%n,cycle(n),exhaustive=True)
    check_case('two-five-cycles-wedge',cycle_bouquet([5,5]),exhaustive=True)
    check_case('Petersen',petersen(),exhaustive=True)
    check_case('Heawood',heawood(),exhaustive=False)
    for d in (3,4):
        check_case('hypercube-%d'%d,cube(d),require_girth=False)
    # Boundary checks: the degree bound need not be attained without the hypotheses.
    def boundary(name,a,expected):
        val=direct_coalition_number(a)
        assert val==expected and val<degree(a)+1
        print('%s n=%d Delta=%d coalition=%d boundary=OK'%(name,len(a),degree(a),val))
    boundary('complete-four',graph(4,combinations(range(4),2)),3)
    boundary('four-vertex-path',graph(4,[(0,1),(1,2),(2,3)]),2)
    boundary('K33-minus-matching',graph(6,[(0,3),(0,4),(0,5),(1,3),(1,5),(2,3),(2,4)]),3)
    print('VERIFY_OK')

if __name__=='__main__':main()
