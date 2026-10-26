#!/usr/bin/env python3
"""Finite-field exhaustive verification of commuting-idempotent tuple identities.

No dependencies beyond the Python standard library.
"""
from itertools import product


def path_basis(vertices, max_length):
    paths = [(i,) for i in range(vertices)]
    if vertices == 2:
        for degree in range(1, max_length):
            for source in (0, 1):
                paths.append(tuple((source + j) % 2 for j in range(degree + 1)))
    return paths


def path_table(paths, cutoff):
    position = {path: i for i, path in enumerate(paths)}
    table = {}
    for i, left in enumerate(paths):
        for j, right in enumerate(paths):
            if left[-1] == right[0] and len(left) + len(right) - 2 < cutoff:
                table[i,j] = position[left + right[1:]]
    return table


def incidence_basis(size):
    return [(i,j) for i in range(size) for j in range(i, size)]


def incidence_table(size):
    basis = incidence_basis(size)
    positions = {pair:i for i,pair in enumerate(basis)}
    table = {}
    for i,(a,b) in enumerate(basis):
        for j,(c,d) in enumerate(basis):
            if b == c:
                table[i,j] = positions[(a,d)]
    return basis, table


def multiply(left, right, table, q):
    out = [0] * len(left)
    for (i,j), k in table.items():
        out[k] += left[i] * right[j]
    return tuple(x%q for x in out)


def algebra_enumeration(basis, table, q, label, single, pair):
    idempotents=[]
    for x in product(range(q), repeat=len(basis)):
        if multiply(x,x,table,q)==x:
            idempotents.append(x)
    count_pairs=sum(multiply(a,b,table,q)==multiply(b,a,table,q)
                    for a in idempotents for b in idempotents)
    assert len(idempotents)==single, (label,q,'single',len(idempotents),single)
    assert count_pairs==pair, (label,q,'pair',count_pairs,pair)
    print(label,'q=',q,'dimension=',len(basis),'idempotents=',single,'commuting_pairs=',pair)


def potts(vertices, edges, colors, q):
    result=0
    for assignment in product(range(colors),repeat=vertices):
        result += q**sum(assignment[u]!=assignment[v] for u,v in edges)
    return result


def random_cluster(vertices, edges, colors, q):
    total=0
    for selected in product((0,1),repeat=len(edges)):
        parent=list(range(vertices))
        def root(x):
            while x!=parent[x]:
                x=parent[x]
            return x
        for bit,(u,v) in zip(selected,edges):
            if bit:
                parent[root(u)]=root(v)
        c=len({root(i) for i in range(vertices)})
        a=sum(selected)
        total += q**(len(edges)-a) * (1-q)**a * colors**c
    return total


def orbit_verification(q, cutoff):
    basis=path_basis(2,cutoff)
    table=path_table(basis,cutoff)
    units=[x for x in product(range(q),repeat=len(basis)) if x[0]!=0 and x[1]!=0]
    ids=[x for x in product(range(q),repeat=len(basis)) if multiply(x,x,table,q)==x]
    pairs=[(a,b) for a in ids for b in ids if multiply(a,b,table,q)==multiply(b,a,table,q)]
    weight=2*(cutoff//2) if cutoff%2==0 else 2*((cutoff-1)//2)
    assert weight==2
    for e,f in pairs:
        unequal=(e[0],f[0])!=(e[1],f[1])
        centralizer=sum(multiply(u,e,table,q)==multiply(e,u,table,q) and
                        multiply(u,f,table,q)==multiply(f,u,table,q) for u in units)
        assert len(units)//centralizer == q**(weight*unequal)
    print('ORBIT_INDEX_OK', 'q=',q,'cutoff=',cutoff,'pair_tuples=',len(pairs))


def main():
    for q in (2,3):
        # Two opposite arrows; truncation at lengths 2 and 3.
        graph_specs=((2,[(0,1),(0,1)]),(3,[(0,1),(0,2),(1,2)]))
        for vertices,edges in graph_specs:
            for r in (1,2):
                colors=2**r
                lhs=potts(vertices,edges,colors,q)
                rhs=random_cluster(vertices,edges,colors,q)
                assert lhs==rhs, (vertices,q,r,lhs,rhs)
        for cutoff in (2,3):
            paths=path_basis(2,cutoff)
            table=path_table(paths,cutoff)
            algebra_enumeration(paths,table,q,'2-cycle/J^'+str(cutoff),
                                2+2*q*q,4+12*q*q)
        for cutoff in (2,3): orbit_verification(q,cutoff)
        basis,table=incidence_table(3)
        algebra_enumeration(basis,table,q,'3-chain incidence',
                            2+6*q*q, 4+36*q*q+24*q*q*q)
    print('COMMUTING_IDEMPOTENT_POTTS_OK')


if __name__=='__main__':
    main()
