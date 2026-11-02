"""Self-contained exact checks of strong-majority two-edge-colourings."""
from itertools import combinations


def edges_from_adj(n, E):
    E = sorted(tuple(sorted((u,v))) for u,v in E)
    assert len(E) == len(set(E))
    deg = [0]*n
    for u,v in E:
        assert 0 <= u < v < n
        deg[u]+=1; deg[v]+=1
    assert all(d==3 for d in deg)
    return E


def graph_prism(k):
    return edges_from_adj(2*k,[(i,(i+1)%k) for i in range(k)]+[(k+i,k+(i+1)%k) for i in range(k)]+[(i,k+i) for i in range(k)])


def graph_mobius(k):
    return edges_from_adj(2*k,[(i,(i+1)%(2*k)) for i in range(2*k)]+[(i,i+k) for i in range(k)])


def graph_cube(d):
    return edges_from_adj(1<<d,[(v,v^(1<<i)) for v in range(1<<d) for i in range(d) if v < (v^(1<<i))])


def graph_petersen():
    return edges_from_adj(10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)])


def graph_k33():
    return edges_from_adj(6,[(i,j) for i in range(3) for j in range(3,6)])


def check(n,E,direct=True):
    nbr=[[u] for u in range(n)]
    for u,v in E:
        nbr[u].append(v); nbr[v].append(u)
    efficient=sum(all(sum((mask>>x)&1 for x in nbr[v])==1 for v in range(n)) for mask in range(1<<n))
    if direct:
        around=[]
        for i,(u,v) in enumerate(E):
            around.append(tuple(j for j,(a,b) in enumerate(E) if j!=i and (u in (a,b) or v in (a,b))))
        assert all(len(L)==4 for L in around)
        strong=sum(all(sum((mask>>j)&1 for j in L)==2 for L in around) for mask in range(1<<len(E)))
        assert strong==2*efficient, (n,E,strong,efficient)
    return efficient


def main():
    tests=[('K4',4,edges_from_adj(4,list(combinations(range(4),2)))),
           ('K33',6,graph_k33()),('prism3',6,graph_prism(3)),
           ('cube3',8,graph_cube(3)),('prism4',8,graph_prism(4)),
           ('mobius4',8,graph_mobius(4)),('petersen',10,graph_petersen()),
           ('mobius6',12,graph_mobius(6))]
    for title,n,E in tests:
        p=check(n,E)
        print(title,'vertices',n,'efficient_codes',p,'two_named_colorings',2*p)
    # Exhaust every labelled cubic simple graph on six vertices (70 graphs).
    vertices=6
    universe=list(combinations(range(vertices),2))
    all_graphs=0
    for E in combinations(universe,9):
        if all(sum(u in edge for edge in E)==3 for u in range(vertices)):
            check(vertices,list(E)); all_graphs+=1
    assert all_graphs==70
    print('ALL_LABELED_CUBIC_ORDER6_OK',all_graphs)
    for k in range(2,9):
        p = check(2*k,graph_mobius(k),direct=False)
        assert p == (4 if k%4==2 else 0), (k,p)
    print('MOBIUS_CODE_COUNTS_OK k_2_to_8')
    assert check(8,graph_cube(3))>0
    print('VERIFY_OK')

if __name__ == '__main__': main()
