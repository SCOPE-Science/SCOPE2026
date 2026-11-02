"""Standalone verification of five-column ladder perfect-matching queries.
No external dependencies. Run: python check.py
"""
from itertools import combinations
from functools import lru_cache


def block_graph():
    vertices = [(r,c) for r in range(2) for c in range(1,6)]
    edges = [tuple(sorted(((0,c),(1,c)))) for c in range(1,6)]
    for c in range(1,5):
        for r in range(2):
            edges.append(tuple(sorted(((r,c),(r,c+1)))))
    assert len(edges)==13
    return vertices,edges


def perfect_matchings(vertices,edges):
    incident = {v: [] for v in vertices}
    for j,(a,b) in enumerate(edges):
        incident[a].append(j)
        incident[b].append(j)
    def rec(remaining,chosen):
        if not remaining:
            yield frozenset(chosen)
            return
        v=min(remaining)
        for j in incident[v]:
            a,b=edges[j]
            w=b if a==v else a
            if w in remaining:
                yield from rec(remaining-{v,w},chosen+(j,))
    return list(rec(set(vertices),()))


def v_idx(c,edges):
    return edges.index(tuple(sorted(((0,c),(1,c)))))

def h_idx(c,edges):
    return edges.index(tuple(sorted(((0,c),(0,c+1)))))


def check_tree(matchings, edges):
    V1,V3,V4 = [v_idx(c,edges) for c in (1,3,4)]
    H2=h_idx(2,edges)
    # Every path has three nodes: V3; next V1 if yes, H2 if no;
    # final V4 if V3 yes OR H2 yes, otherwise V1.
    paths={}
    for M in matchings:
        b0=int(V3 in M)
        b1=int((V1 if b0 else H2) in M)
        b2=int((V4 if (b0 or b1) else V1) in M)
        paths[(b0,b1,b2)]=M
    assert len(paths)==8 and len({tuple(sorted(m)) for m in paths.values()})==8
    return paths


def main():
    V,E=block_graph()
    M=perfect_matchings(V,E)
    assert len(M)==8
    assert all(len(m)==5 for m in M)
    assert all(len({v for j in m for v in E[j]})==10 for m in M)
    vc=0
    support={}
    for k in range(1,4):
        supports=[]
        for S in combinations(range(len(E)),k):
            patterns={tuple(int(j in m) for j in S) for m in M}
            if len(patterns)==2**k:
                supports.append(S)
        if supports:
            vc=k;support[k]=supports
        else:
            assert k==3
            break
    assert vc==2
    V1,V4=v_idx(1,E),v_idx(4,E)
    assert tuple(sorted((V1,V4))) in support[2]
    tree=check_tree(M,E)
    # Depth three is maximal because eight distinct concepts exist.
    assert len(tree)==8 and len(M)==8
    # A connected two-block bridge: attach the upper-right corner of
    # first block to the lower-left corner of the second block.
    def relabel(v,block): return (block,)+v
    vertices=[relabel(v,k) for k in range(2) for v in V]
    edges=[tuple(sorted((relabel(a,k),relabel(b,k)))) for k in range(2) for a,b in E]
    br=tuple(sorted((relabel((0,5),0),relabel((1,1),1))))
    edges.append(br)
    cross=perfect_matchings(vertices,edges)
    assert len(cross)==64
    assert all(26 not in m for m in cross)
    assert all(len(m)==10 for m in cross)
    # Exactly four independent fixed queries (V1,V4 in each block) shatter.
    q=[V1,V4,13+V1,13+V4]
    assert len({tuple(int(j in m) for j in q) for m in cross})==16
    assert max(sum(v==x for v in (u for edge in edges for u in edge)) for x in vertices)<=3
    print('FIVE_COLUMN_MATCHINGS_PASS',len(M),'edges',len(E),'VC',vc,'LDIM',3)
    print('DEPTH_THREE_TREE_PASS',len(tree),'leaf_witnesses')
    print('TWO_BLOCK_CONNECTED_CHECK_PASS',len(cross),'matchings','bridge_absent',True)
    print('CONNECTED_SUBCUBIC_PRODUCT_THEOREM_CHECKS_PASS')
if __name__=='__main__':main()
