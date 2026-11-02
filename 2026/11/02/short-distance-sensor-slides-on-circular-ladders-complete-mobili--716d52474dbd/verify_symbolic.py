"""Independent six-type formula for the 11n short-distance pair states."""
from collections import Counter

TYPES = {'S1':(2,4,8),'S2':(2,6,7),'S3':(2,2,1),
         'O0':(1,4,8),'O1':(2,6,12),'O2':(2,4,6)}

def test(n):
    # Vertex labels are pairs (row,column), not single integer indexes.
    adjacent=lambda v: { (v[0],(v[1]-1)%n),
                         (v[0],(v[1]+1)%n),(1-v[0],v[1]) }
    family={}
    for r in (0,1):
        for d in (1,2,3):
            for i in range(n):
                p=frozenset(((r,i),(r,(i+d)%n)))
                family[p]='S'+str(d)
    for d in (0,1,-1,2,-2):
        for i in range(n):
            p=frozenset(((0,i),(1,(i+d)%n)))
            family[p]='O'+str(abs(d))
    assert len(family)==11*n
    graph={p:set() for p in family}
    for p in family:
        for old in p:
            other=next(x for x in p if x!=old)
            for new in adjacent(old)-{other}:
                q=frozenset((other,new))
                if q in family:
                    graph[p].add(q)
    assert all(p in graph[q] for p in graph for q in graph[p])
    for shape,(multiplicity,degree,qcount) in TYPES.items():
        selected=[p for p in family if family[p]==shape]
        assert len(selected)==multiplicity*n
        for p in selected:
            neighbors=sorted(graph[p],key=lambda s: sorted(s))
            assert len(neighbors)==degree
            squares_at_p=sum(len(graph[u]&graph[v])-1
                for ia,u in enumerate(neighbors) for v in neighbors[ia+1:])
            assert squares_at_p==qcount,(n,shape,squares_at_p,qcount)
    assert sum(len(neighbors) for neighbors in graph.values())==48*n
    assert sum(multiplicity*n*quad
       for multiplicity,degree,quad in TYPES.values())==76*n
    return (len(family),sum(map(len,graph.values()))//2,19*n)

if __name__=='__main__':
    for n in (8,9,10,11,12,13,14,15,16,17,19,23,31):
        print('n',n,'(vertices, edges, squares)',test(n))
    print('SIX_LOCAL_TYPES_AND_SQUARE_TABLE_PASS')
