"""Exact finite checks for the 3-cut complexes of Möbius ladders.
Requires only the Python 3 standard library.
"""
from collections import deque
from math import gcd
from itertools import combinations
from functools import lru_cache


def data(n):
    assert n >= 4
    m = 2*n
    edges = {frozenset((i,(i+1)%m)) for i in range(m)}
    edges.update(frozenset((i,i+n)) for i in range(n))
    return m,edges


def connected_triple(t,edges):
    return sum(frozenset(e) in edges for e in combinations(t,2)) == 2


def dual_counts(n):
    m,edges = data(n)
    triples = [t for t in combinations(range(m),3) if connected_triple(t,edges)]
    tset = {frozenset(t) for t in triples}
    squares = [t for t in combinations(range(m),4)
               if all(frozenset(s) in tset for s in combinations(t,3))]
    five = [t for t in combinations(range(m),5)
            if all(frozenset(s) in tset for s in combinations(t,3))]
    assert len(triples) == 6*n
    assert len(squares) == n
    assert not five
    assert {frozenset((i,(i+1)%m,(i+1+n)%m,(i+n)%m)) for i in range(n)} == {frozenset(s) for s in squares}

    all_edges = list(combinations(range(m),2))
    edge_index = {frozenset(e):i for i,e in enumerate(all_edges)}
    triangle_index = {frozenset(t):i for i,t in enumerate(triples)}

    def rank(columns):
        pivots = {}
        for x in columns:
            while x:
                p = x.bit_length()-1
                if p in pivots: x ^= pivots[p]
                else:
                    pivots[p]=x
                    break
        return len(pivots)

    r2=rank(sum(1<<edge_index[frozenset(e)] for e in combinations(t,2)) for t in triples)
    r3=rank(sum(1<<triangle_index[frozenset(t)] for t in combinations(s,3)) for s in squares)
    assert r2==5*n,(n,r2)
    assert r3==n,(n,r3)
    b1=len(all_edges)-(m-1)-r2
    assert b1==2*n*(n-4)+1,(n,b1)
    assert len(triples)-r2-r3==0
    return m,len(all_edges),len(triples),len(squares),b1


def primal_complex(n):
    m,edges=data(n)
    bad=[sum(1<<v for v in t) for t in combinations(range(m),3)
         if not connected_triple(t,edges)]
    full=(1<<m)-1
    faces={x for x in range(1<<m) if any((full^x)&b==b for b in bad)}
    return m,bad,faces


def matching(faces,m):
    remain=set(faces)
    pairs={}
    for v in range(m):
        bit=1<<v
        new=[(a,a|bit) for a in remain if a&bit==0 and a|bit in remain]
        for a,b in new:
            pairs[a]=b
            remain.remove(a)
            remain.remove(b)
    return pairs,remain


def acyclic(faces,pairs):
    degree={x:0 for x in faces}
    arcs={x:[] for x in faces}
    incidences=0
    for face in faces:
        rest=face
        while rest:
            bit=rest&-rest
            rest-=bit
            sub=face^bit
            if sub not in faces:continue
            incidences+=1
            if pairs.get(sub)==face:src,dst=sub,face
            else:src,dst=face,sub
            arcs[src].append(dst)
            degree[dst]+=1
    queue=deque(x for x,d in degree.items() if d==0)
    processed=0
    while queue:
        a=queue.popleft(); processed+=1
        for b in arcs[a]:
            degree[b]-=1
            if degree[b]==0:queue.append(b)
    assert processed==len(faces),(processed,len(faces))
    return incidences


def integral_attaching(faces,pairs,critical,m):
    dim=min(x.bit_count()-1 for x in critical)
    lower={x for x in critical if x.bit_count()-1==dim}
    upper=[x for x in critical if x.bit_count()-1==dim+1]
    assert len(lower)==1
    low_pairs={a:b for a,b in pairs.items() if a.bit_count()-1==dim}
    @lru_cache(None)
    def project(face):
        if face in lower:return 1
        coface=low_pairs.get(face)
        if coface is None:return 0
        verts=[v for v in range(m) if coface>>v&1]
        matched_vertex=(coface^face).bit_length()-1
        j=verts.index(matched_vertex)
        total=0
        for i,v in enumerate(verts):
            if i==j:continue
            total -= (-1)**(i+j)*project(coface^(1<<v))
        return total
    coefficients=[]
    for face in upper:
        verts=[v for v in range(m) if face>>v&1]
        coefficients.append(sum((-1)**i*project(face^(1<<v)) for i,v in enumerate(verts)))
    assert any(coefficients),(dim,coefficients)
    assert gcd(*coefficients)==1,(dim,coefficients)
    return dim,len(lower),len(upper),max(abs(c) for c in coefficients)


def main():
    for n in range(4,11):
        m,edges,tri,tet,b1=dual_counts(n)
        print('DUAL_OK',n,m,edges,tri,tet,b1,flush=True)
    for n in range(4,9):
        m,bads,faces=primal_complex(n)
        pairs,critical=matching(faces,m)
        assert len(pairs)*2+len(critical)==len(faces)
        num_arcs=acyclic(faces,pairs)
        d,lo,hi,unit=integral_attaching(faces,pairs,critical,m)
        assert d==2*n-5 and hi-lo==2*n*(n-4)+1
        print('MORSE_OK',n,'faces',len(faces),'incidences',num_arcs,
              'critical',(lo,hi),'attaching_unit',unit,flush=True)
    print('VERIFY_OK')


if __name__=='__main__':main()
