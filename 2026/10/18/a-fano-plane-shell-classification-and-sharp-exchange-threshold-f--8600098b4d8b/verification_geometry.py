"""Geometric total-domination and reconfiguration certificate for the Coxeter graph.
Run in the same directory as certificate.json. Standard-library only.
"""
import itertools, collections, json
triples = [sum(1 << k for k in c) for c in itertools.combinations(range(1, 8), 3) if c[0] ^ c[1] ^ c[2]]
assert len(triples)==28
N=[sum(1 << j for j in range(28) if i!=j and not(triples[i]&triples[j])) for i in range(28)]
assert all(m.bit_count()==3 for m in N)
FULL=(1<<28)-1

def distance_from(source, adjacency):
    D={source:0};queue=collections.deque([source]);
    while queue:
        i=queue.popleft()
        for j in range(len(adjacency)):
            if adjacency[i]>>j&1 and j not in D:
                D[j]=D[i]+1;queue.append(j)
    return D

layers=[distance_from(i,N) for i in range(28)]
assert all(collections.Counter(D.values()) == {0:1,1:3,2:6,3:12,4:6} for D in layers)
# Explicitly verify every vertex has the known distance-regular intersection array.
for center,D in enumerate(layers):
    for i in range(28):
        d=D[i];counts=collections.Counter(D[j] for j in range(28) if (N[i]>>j)&1)
        expected=[{1:3},{0:1,2:2},{1:1,3:2},{2:1,3:1,4:1},{3:2,4:1}][d]
        assert counts==expected,(center,i,counts,expected)

S=[sum(1<<v for v in range(28) if layers[x][v] in (0,1,4)) for x in range(28)]
assert len(set(S))==28 and all(s.bit_count()==10 for s in S)
assert all(all((N[v]&s)!=0 for v in range(28)) for s in S)
# Every chosen optimum has precisely one triply covered vertex, identifying its center.
for x,s in enumerate(S):
    m=[(N[v]&s).bit_count() for v in range(28)]
    assert m[x]==3 and all(m[v]==1 for v in range(28) if v!=x)

cost={d:set() for d in range(1,5)};hist=collections.Counter()
for x in range(28):
    for y in range(x+1,28):
        c=(S[x]^S[y]).bit_count()//2
        cost[layers[x][y]].add(c);hist[c]+=1
assert cost=={1:{6},2:{9},3:{7},4:{4}}
assert hist=={4:84,6:42,7:168,9:84}
R=[sum(1<<j for j in range(28) if layers[i][j]==4) for i in range(28)]
assert all(m.bit_count()==6 for m in R)
RD=[distance_from(i,R) for i in range(28)]
assert all(collections.Counter(D.values())=={0:1,1:6,2:15,3:6} for D in RD)
assert sum(R[i].bit_count() for i in range(28))//2==84
triangles=sum(sum(1 for u in range(i+1,28) if R[i]>>u&1 for v in range(u+1,28) if (R[i]>>v&1) and (R[u]>>v&1)) for i in range(28))
assert triangles==56
certificate={'graph_construction':'noncollinear 3-subsets of Fano plane; adjacency iff disjoint',
             'vertex_triple_bitmasks':triples,'minimum_total_dominating_set_bitmasks':sorted(S),
             'graph_distance_sphere_sizes':[1,3,6,12,6],
             'exchange_cost_by_graph_distance':{'1':6,'2':9,'3':7,'4':4},
             'exchange_cost_histogram':{'4':84,'6':42,'7':168,'9':84},
             'four_exchange_graph_degree':6,'four_exchange_graph_edges':84,
             'four_exchange_distance_profile':[1,6,15,6],
             'four_exchange_diameter':3,'four_exchange_triangles':56}
try:
    with open('certificate.json',encoding='utf-8') as stream:
        actual=json.load(stream)
except FileNotFoundError:
    import sys
    if len(sys.argv)==2 and sys.argv[1]=='--make-certificate':
        with open('certificate.json','w',encoding='utf-8') as output:
            json.dump(certificate,output,indent=2,ensure_ascii=False,sort_keys=True)
            output.write('\n')
    else:
        raise
else:
    assert actual==certificate
print('graph=coxeter_28_42 intersection_array=(3,2,2,1;1,1,1,2)')
print('distance_spheres=1,3,6,12,6')
print('minimum_total_dominating_sets=28 all_of_form_S0+S1+S4')
print('exchange_costs_by_distance=6,9,7,4')
print('four_exchange_graph=28_vertices 84_edges degree_6 diameter_3 triangles_56')
print('GEOMETRY_CERTIFICATE_OK')
