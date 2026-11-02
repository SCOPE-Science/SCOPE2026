"""Exhaustive independent finite-ring checks for an involution geometry theorem.

Run with Python 3; networkx is optional for the maximal-clique check.
"""
import itertools
from collections import Counter


def make_ring(q, kind):
    if q not in (2,4) or kind not in ('split', 'witt'):
        raise ValueError((q,kind))
    f = {2:1, 4:2}[q]
    n=q*q
    def fldmul(a,b):
        out=0
        for i in range(f):
            for j in range(f):
                if (a>>i)&1 and (b>>j)&1:
                    out ^= 1<<(i+j)
        if f==2 and (out & 4):
            out ^= (1<<2)|(1<<1)|1  # x^2=x+1 in F4
        return out
    if kind=='split':
        def add(x,y):return (x%q)^(y%q) | (((x//q)^(y//q))<<f)
        def mul(x,y):
            a,b=x%q,x//q
            c,d=y%q,y//q
            return fldmul(a,c)+q*(fldmul(a,d)^fldmul(b,c))
        def neg(x):return x
        one=1
    elif q==2:
        def add(x,y):return (x+y)%4
        def mul(x,y):return x*y%4
        def neg(x):return -x%4
        one=1
    else:
        def add(x,y):return (x+y)%4 +4*((x//4+y//4)%4)
        def mul(x,y):
            a,b=x%4,x//4
            c,d=y%4,y//4
            return ((a*c-b*d)%4) + 4*((a*d+b*c-b*d)%4)
        def neg(x):return (-x%4)+4*(-(x//4)%4)
        one=1
    add_table=[[add(x,y) for y in range(n)] for x in range(n)]
    mul_table=[[mul(x,y) for y in range(n)] for x in range(n)]
    neg_table=[neg(x) for x in range(n)]
    assert len(set(add(x,neg(x)) for x in range(n)))==1
    assert len(set(mul(one,x) for x in range(n)))==n
    return n,add_table,mul_table,neg_table,one


def census(q, kind):
    n,A,M,N,one=make_ring(q,kind)
    Z=0
    eye=(one,Z,Z,one)
    def determinant(x):
        a,b,c,d=x
        return A[M[a][d]][N[M[b][c]]]
    def prod(x,y):
        a,b,c,d=x; e,f,g,h=y
        return (A[M[a][e]][M[b][g]],A[M[a][f]][M[b][h]],
                A[M[c][e]][M[d][g]],A[M[c][f]][M[d][h]])
    groups=[x for x in itertools.product(range(n),repeat=4) if determinant(x)==one]
    invol=[x for x in groups if prod(x,x)==eye]
    assert len(groups)==q**4*(q*q-1), (q,kind,len(groups))
    expected=q**3 if kind=='witt' else q**4+q**3-q*q
    assert len(invol)==expected,(q,kind,len(invol),expected)
    cts=[]
    comm={}
    for i,x in enumerate(invol):
        friends=[j for j,y in enumerate(invol) if prod(x,y)==prod(y,x)]
        cts.append(len(friends));comm[i]=set(friends)
    actual=Counter(cts)
    if kind=='witt':
        expected_spectrum={q**3:q**3}
        pairs=q**6
    else:
        expected_spectrum={q**4+q**3-q*q:q, 2*q**3-q*q:q**3-q,
                           q**3:q**4-q*q}
        pairs=q**4*(q**3+2*q*q-q-1)
    assert actual==expected_spectrum, (q,kind, actual,expected_spectrum)
    assert sum(cts)==pairs
    result={'q':q,'type':kind,'group_size':len(groups),'involution_count':len(invol),
            'involution_commuting_spectrum':dict(sorted(actual.items())),
            'ordered_commuting_involution_pairs':sum(cts)}
    try:
        import networkx as nx
        graph=nx.Graph()
        graph.add_nodes_from(range(len(invol)))
        graph.add_edges_from((i,j) for i in comm for j in comm[i] if j>i)
        cliques=[frozenset(c) for c in nx.find_cliques(graph)]
        expected_cliques=1 if kind=='witt' else q+2
        assert len(cliques)==expected_cliques,(q,kind,list(map(len,cliques)))
        assert all(len(c)==q**3 for c in cliques)
        result['maximal_elementary_abelian_2_subgroups']=len(cliques)
        result['maximal_subgroup_order']=q**3
    except ImportError:pass
    return result

if __name__=='__main__':
    for q in (2,4):
        for kind in ('split','witt'):
            print(census(q,kind))
    print('VERIFY_OK: 4 exhaustive special-linear group censuses and commuting-involution graphs.')
