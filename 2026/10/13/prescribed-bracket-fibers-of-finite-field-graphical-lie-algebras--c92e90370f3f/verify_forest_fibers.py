"""Independent exhaustive checks of prescribed Lie-bracket fibers for forests.

The bracket coordinate of an edge {u,v} (u<v) equals a[u]*b[v]-a[v]*b[u].
This stand-alone script uses only the Python standard library.
"""
from collections import Counter
from itertools import product


def mul(a,b,q):
    if q==4:
        aa,ab=a&1,(a>>1)&1
        ba,bb=b&1,(b>>1)&1
        return (aa*ba ^ ab*bb) | ((aa*bb ^ ab*ba ^ ab*bb)<<1)
    return a*b%q


def sub(a,b,q):
    return a^b if q==4 else (a-b)%q


def count_direct(n,edges,q):
    # Bracket map evaluated directly, without support-set reduction.
    out=Counter()
    domain=product(range(q),repeat=n)
    for a in domain:
        for b in product(range(q),repeat=n):
            z=tuple(sub(mul(a[u],b[v],q),mul(a[v],b[u],q),q) for u,v in edges)
            out[z]+=1
    return out


def count_formula(n,edges,q,z):
    nz={i for i,val in enumerate(z) if val!=0}
    forced=set()
    for i in nz:
        forced.update(edges[i])
    total=0
    for mask in range(1<<n):
        if any(not (mask>>v&1) for v in forced):
            continue
        verts=mask.bit_count()
        inside=sum((mask>>u&1) and (mask>>v&1) for u,v in edges)
        cc=verts-inside  # precisely because every induced subgraph is a forest
        total+=(q*q-1)**cc * q**len(nz) * (q-1)**(inside-len(nz))
    return total


def run():
    graphs=[('vertex',1,()),('edge',2,((0,1),)),
            ('path3',3,((0,1),(1,2))),
            ('edge_plus_isolate',3,((0,1),)),
            ('path4',4,((0,1),(1,2),(2,3))),
            ('star4',4,((0,1),(0,2),(0,3))),
            ('two_edges',4,((0,1),(2,3)))]
    tests=0
    for q in (2,3,4):
        for name,n,edges in graphs:
            if q==4 and n>4:continue
            table=count_direct(n,edges,q)
            assert sum(table.values())==q**(2*n)
            assert len(table)==q**len(edges), ('not surjective',q,name)
            for z in product(range(q),repeat=len(edges)):
                predicted=count_formula(n,edges,q,z)
                assert table[z]==predicted,(q,name,z,predicted,table[z])
                tests+=1
    P=((0,1),(1,2),(2,3)); S=((0,1),(0,2),(0,3))
    assert count_formula(4,P,2,(0,0,0))==76
    assert count_formula(4,S,2,(0,0,0))==88
    assert count_formula(4,P,2,(1,0,0))==36
    assert count_formula(4,P,2,(0,1,0))==24
    assert count_formula(4,S,2,(1,0,0))==24
    # Every possible target is attained and the total across them is q^(2n).
    for q in (2,3,4,5,7):
        for _,n,edges in graphs:
            total=sum(count_formula(n,edges,q,z) for z in product(range(q),repeat=len(edges)))
            assert total==q**(2*n),(q,n,edges,total)
    print(f'VERIFY_OK {tests} independent prescribed-target exhaustive tests, normalization tested')

if __name__=='__main__':run()
