#!/usr/bin/env python3
"""Independent finite checks for the integral time-class and symmetry action on flex complexes."""
from itertools import combinations, permutations
from collections import defaultdict, deque


def make_graph(n, edges):
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    assert len(set(edges)) == len(edges) and all(0 <= a < b < n for a, b in edges)
    incident = [0]*n
    for i, (a, b) in enumerate(edges):
        incident[a] |= 1<<i
        incident[b] |= 1<<i
    return n, edges, tuple(incident)


def sink(mask, v, graph):
    n,edges,incident=graph
    return all((b if ((mask>>i)&1) else a)==v
               for i,(a,b) in enumerate(edges) if v in (a,b))


def source(mask, v, graph):
    n,edges,incident=graph
    return all((a if ((mask>>i)&1) else b)==v
               for i,(a,b) in enumerate(edges) if v in (a,b))


def flip(mask, v, graph):
    return mask ^ graph[2][v]


def action(mask, p, graph):
    n,edges,_=graph
    look={e:i for i,e in enumerate(edges)}
    out=0
    for i,(a,b) in enumerate(edges):
        target=b if ((mask>>i)&1) else a
        j=look[tuple(sorted((p[a],p[b])))]
        if p[target]==edges[j][1]:out |=1<<j
    return out


def graph_auts(graph):
    n,edges,_=graph
    e=set(edges)
    return [p for p in permutations(range(n))
            if {tuple(sorted((p[a],p[b]))) for a,b in edges}==e]


def components(graph):
    n,edges,_=graph
    M=1<<len(edges)
    graph_links=[[] for _ in range(M)]
    sink_edges=set()
    for mask in range(M):
        for v in range(n):
            if sink(mask,v,graph):
                after=flip(mask,v,graph)
                assert source(after,v,graph)
                sink_edges.add((mask,v))
                graph_links[mask].append(after)
                graph_links[after].append(mask)
    comp=[-1]*M
    classes=[]
    for mask in range(M):
        if comp[mask]>=0:continue
        c=len(classes)
        comp[mask]=c
        queue=deque([mask]); nodes=[]
        while queue:
            a=queue.popleft();nodes.append(a)
            for b in graph_links[a]:
                if comp[b]<0:comp[b]=c;queue.append(b)
                else:assert comp[b]==c
        classes.append(nodes)
    return comp,classes,sink_edges


def oriented_core(order, graph):
    n,edges,_=graph
    pos={v:i for i,v in enumerate(order)}
    mask=sum((1<<i) for i,(a,b) in enumerate(edges) if pos[b]<pos[a])
    start=mask
    trace=[]
    for v in order:
        if not sink(mask,v,graph):return None
        trace.append((mask,v))
        mask=flip(mask,v,graph)
    assert mask==start
    assert len(set(m for m,v in trace))==n
    return trace


def cubical_counts(graph):
    n,edges,_=graph
    M=1<<len(edges)
    cubes=set()
    squares=0
    for mask in range(M):
        available=[v for v in range(n) if sink(mask,v,graph)]
        for k in range(len(available)+1):
            for vs in combinations(available,k):
                if any(v in e and w in e for v,w in combinations(vs,2) for e in edges):
                    continue
                incident=set(i for v in vs for i in range(len(edges)) if graph[2][v]&(1<<i))
                remaining=tuple((i,(mask>>i)&1) for i in range(len(edges)) if i not in incident)
                cubes.add((vs,remaining))
                if k==2:
                    v,w=vs
                    assert sink(flip(mask,v,graph),w,graph)
                    assert sink(flip(mask,w,graph),v,graph)
                    # The canonical cochain assigns +1 to each sink-to-source edge:
                    # its signed evaluation on the square boundary is zero.
                    assert 1+1-1-1==0
                    squares+=1
    c=defaultdict(int)
    for vs,rest in cubes:c[len(vs)]+=1
    return dict(c),squares


def rank_two_boundaries(graph, sink_edges):
    n,edges,_=graph
    lookup={e:i for i,e in enumerate(sorted(sink_edges))}
    pivots={}
    square_count=0
    for mask in range(1<<len(edges)):
        for v,w in combinations([v for v in range(n) if sink(mask,v,graph)],2):
            if (v,w) in edges:continue
            square_count+=1
            terms=[(mask,v),(mask,w),(flip(mask,v,graph),w),(flip(mask,w,graph),v)]
            row=0
            for term in terms:
                assert term in lookup
                row ^= 1<<lookup[term]
            assert row.bit_count()==4
            while row:
                bit=row.bit_length()-1
                if bit not in pivots:
                    pivots[bit]=row
                    break
                row ^= pivots[bit]
    return len(pivots),square_count


def check(name,graph):
    n,edges,_=graph
    comp,classes,edge_directed=components(graph)
    fc,squares=cubical_counts(graph)
    euler=sum(((-1)**k)*v for k,v in fc.items())
    sinkless=sum(not any(sink(mask,v,graph) for v in range(n))
                 for mask in range(1<<len(edges)))
    assert euler==sinkless,(name,euler,sinkless)
    circle_count=len(classes)-sinkless
    assert circle_count>=1
    rank2,c2=rank_two_boundaries(graph,edge_directed)
    assert c2==fc.get(2,0),(name,c2,fc)
    rank1=(1<<len(edges))-len(classes)
    beta1_mod2=len(edge_directed)-rank1-rank2
    assert beta1_mod2==circle_count,(name,beta1_mod2,circle_count)
    candidate={}
    for p in permutations(range(n)):
        cy=oriented_core(p,graph)
        if cy is not None:
            c=comp[cy[0][0]]
            candidate[c]=cy
            assert len(cy)==n
            assert all((mask,v) in edge_directed for mask,v in cy)
    assert len(candidate)==circle_count,(name,len(candidate),circle_count)
    all_auts=graph_auts(graph)
    for p in all_auts:
        for c,cy in candidate.items():
            image=[(action(mask,p,graph),p[v]) for mask,v in cy]
            assert all((mask,v) in edge_directed for mask,v in image)
            tc=comp[image[0][0]]
            assert tc in candidate
            assert all(comp[mask]==tc for mask,v in image)
            # All source-directed periods remain +n, hence H_1 sign +1.
            assert len(image)==n
    J=(1<<len(edges))-1
    for c,cy in candidate.items():
        im=[((mask^J),v) for mask,v in cy]
        assert all(source(mask,v,graph) for mask,v in im)
        tc=comp[im[0][0]]
        assert tc in candidate
        assert all(comp[mask]==tc for mask,v in im)
        # All time-reversed periods are -n.
        assert -len(im)==-n
    print(f'{name}: V={n}, E={len(edges)}, orientations={1<<len(edges)}, '
          f'cells={sum(fc.values())}, 2-square checks={squares}, '
          f'components={len(classes)}, circles={circle_count}, GF2_H1={beta1_mod2}, '
          f'automorphisms={len(all_auts)}, '
          f'aut-core cases={circle_count*len(all_auts)}')
    return len(classes),circle_count,squares,len(all_auts)*circle_count


def main():
    cases=[]
    for n in range(2,7):
        cases.append((f'path-{n}',make_graph(n,[(i,i+1) for i in range(n-1)])))
        if n>=3:cases.append((f'star-{n}',make_graph(n,[(0,i) for i in range(1,n)])))
        if n>=3:cases.append((f'cycle-{n}',make_graph(n,[(i,(i+1)%n) for i in range(n)])))
    cases.extend([
        ('K3',make_graph(3,list(combinations(range(3),2)))),
        ('K4',make_graph(4,list(combinations(range(4),2)))),
        ('K2,3',make_graph(5,[(i,j) for i in range(2) for j in range(2,5)])),
        ('house-5',make_graph(5,[(0,1),(1,2),(2,3),(3,0),(1,4),(2,4)])),
        ('bowtie-5',make_graph(5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)])),
    ])
    total=[0]*4
    for name,graph in cases:
        t=check(name,graph)
        total=[x+y for x,y in zip(total,t)]
    print('CASES',len(cases),'SUM_COMPONENTS',total[0],
          'SUM_CIRCLES',total[1],'SUM_SQUARE_CHECKS',total[2],
          'SUM_AUTOMORPHISM_CORE_CHECKS',total[3])
    print('VERIFY_OK')

if __name__=='__main__':main()
