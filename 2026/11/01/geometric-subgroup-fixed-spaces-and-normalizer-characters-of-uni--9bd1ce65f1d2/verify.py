#!/usr/bin/env python3
"""Independent finite checks for fixed spaces of uniform multiclique complexes.

The tests enumerate invariant labelled cells in the original poset and
independently enumerate cells in the orbit-inflation model. They also compute
cellular mod-two homology of the latter complex by direct boundary reduction.
No finite test replaces the general group-orbit and flabby-sheaf proofs.
"""
from itertools import combinations, product


def closure(n, generators):
    ident = tuple(range(n))
    group = {ident}
    frontier = [ident]
    while frontier:
        a = frontier.pop()
        for g in generators:
            h = tuple(a[g[i]] for i in range(n))
            if h not in group:
                group.add(h)
                frontier.append(h)
    return tuple(sorted(group))


def orbits(items, group, action):
    remaining = set(items)
    out = []
    while remaining:
        x = min(remaining)
        orbit = frozenset(action(g,x) for g in group)
        assert orbit <= remaining
        out.append(tuple(sorted(orbit)))
        remaining.difference_update(orbit)
    return tuple(sorted(out))


def model(n, group):
    V = orbits(range(n), group, lambda g,x:g[x])
    E = list(combinations(range(n),2))
    O = orbits(E, group, lambda g,e:tuple(sorted((g[e[0]],g[e[1]]))))
    membership = {v:i for i, vs in enumerate(V) for v in vs}
    support = tuple(frozenset({membership[e[0][0]], membership[e[0][1]]}) for e in O)
    return V,O,support


def predicted_cells(n,q,group):
    V,O,support = model(n,group)
    cells = {}
    for k in range(1,len(V)+1):
        out = []
        for J in combinations(range(len(V)),k):
            I = frozenset(J)
            E = tuple(j for j,s in enumerate(support) if s<=I)
            S = tuple(sorted(v for j in J for v in V[j]))
            pair_list = tuple(combinations(S,2))
            edge_to_orbit = {e:j for j,orb in enumerate(O) for e in orb}
            for labels in product(range(q),repeat=len(E)):
                mp = dict(zip(E,labels))
                full = tuple(mp[edge_to_orbit[e]] for e in pair_list)
                out.append(((J,tuple(zip(E,labels))), (S,full)))
        cells[k-1] = out
    return cells


def direct_invariant_cells(n,q,group):
    result=set()
    for k in range(1,n+1):
        for S in combinations(range(n),k):
            Sset=set(S)
            if any({g[v] for v in S}!=Sset for g in group):
                continue
            edges=tuple(combinations(S,2))
            ei={e:i for i,e in enumerate(edges)}
            for colors in product(range(q), repeat=len(edges)):
                if all(colors[ei[tuple(sorted((g[u],g[v])))]]==colors[j]
                       for g in group for j,(u,v) in enumerate(edges)):
                    result.add((S,colors))
    return result


def ranks_and_betti(cells):
    levels = {k:[key for key, _ in vals] for k,vals in cells.items()}
    indices = {k:{key:i for i,key in enumerate(vals)} for k,vals in levels.items()}
    max_dim=max(levels)
    ranks={0:0,max_dim+1:0}
    for k in range(1,max_dim+1):
        basis={}
        for (J,colored),_ in cells[k]:
            assignments=dict(colored)
            bits=0
            for skip in range(len(J)):
                small=J[:skip]+J[skip+1:]
                # Restrict the labels to the edges supported in remaining cycles.
                V,O,support = cached_model
                I=frozenset(small)
                sub=tuple((j,label) for j,label in colored if support[j]<=I)
                face=(small,sub)
                bits ^= 1<<indices[k-1][face]
            while bits:
                pivot=bits.bit_length()-1
                if pivot in basis:
                    bits ^= basis[pivot]
                else:
                    basis[pivot]=bits
                    break
        ranks[k]=len(basis)
    betti = {k:len(levels[k])-ranks[k]-ranks[k+1] for k in levels}
    betti[0]-=1
    return betti, ranks


def wedge_count(n,q,group):
    V,O,support=model(n,group)
    c=len(V)
    s=0
    for k in range(c+1):
        for J in combinations(range(c),k):
            I=frozenset(J)
            e=sum(1 for p in support if p<=I)
            s+=(-1)**k*q**e
    return (-1)**c*s


def perm_from_cycles(n,cycles):
    p=list(range(n))
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):p[a]=b
    return tuple(p)



def permutation_sign(images):
    return -1 if sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))%2 else 1


def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))


def normalizes(g,group):
    inv=tuple(g.index(i) for i in range(len(g)))
    return all(compose(g,compose(h,inv)) in group for h in group)


def normalizer_character_formula(n,q,group,g):
    V,E,support=model(n,group)
    vindex={tuple(sorted(v)):i for i,v in enumerate(V)}
    eindex={tuple(sorted(e)):i for i,e in enumerate(E)}
    vp=tuple(vindex[tuple(sorted(g[v] for v in vs))] for vs in V)
    ep=tuple(eindex[tuple(sorted(tuple(sorted((g[a],g[b]))) for a,b in es))] for es in E)
    def perm_cycles(p):
        unseen=set(range(len(p)))
        result=[]
        while unseen:
            i=min(unseen); cyc=[]; j=i
            while j in unseen:
                unseen.remove(j); cyc.append(j);j=p[j]
            assert j==i
            result.append(tuple(cyc))
        return result
    vc=perm_cycles(vp)
    ec=perm_cycles(ep)
    total=0
    for k in range(len(vc)+1):
        for blocks in combinations(range(len(vc)),k):
            selected=frozenset(v for b in blocks for v in vc[b])
            b=sum(1 for cyc in ec if support[cyc[0]]<=selected)
            total+=(-1)**k*q**b
    return (-1)**len(V)*total


def direct_normalizer_trace(n,q,group,g,cells):
    V,E,support=model(n,group)
    vindex={tuple(sorted(v)):i for i,v in enumerate(V)}
    eindex={tuple(sorted(e)):i for i,e in enumerate(E)}
    vp=tuple(vindex[tuple(sorted(g[v] for v in vs))] for vs in V)
    ep=tuple(eindex[tuple(sorted(tuple(sorted((g[a],g[b]))) for a,b in es))] for es in E)
    tr=-1
    for k,collection in cells.items():
        for (J,colored),_ in collection:
            im=[vp[i] for i in J]
            if set(im)!=set(J):continue
            original=dict(colored)
            if any(original.get(ep[e])!=col for e,col in colored):continue
            sig=permutation_sign(im)
            tr+=(-1)**k*sig
    return (-1)**(len(V)-1)*tr


def run():
    tests=[]
    for n in range(2,6):
        idn=tuple(range(n))
        gs=[('identity',[]),('swap', [perm_from_cycles(n,[(0,1)])])]
        if n>=3:
            gs += [('3cycle',[perm_from_cycles(n,[(0,1,2)])]),
                   ('S3',[perm_from_cycles(n,[(0,1)]),perm_from_cycles(n,[(0,1,2)])])]
        if n>=4:
            gs += [('double_swap',[perm_from_cycles(n,[(0,1),(2,3)])]),
                   ('fourcycle',[perm_from_cycles(n,[(0,1,2,3)])]),
                   ('V4',[perm_from_cycles(n,[(0,1),(2,3)]),perm_from_cycles(n,[(0,2),(1,3)])])]
        if n>=5:
            gs += [('fivecycle',[perm_from_cycles(n,[(0,1,2,3,4)])]),
                   ('S5',[perm_from_cycles(n,[(0,1)]),perm_from_cycles(n,[(0,1,2,3,4)])])]
        for name,generators in gs:
            for q in (2,3):
                group=closure(n,generators)
                V,O,support=model(n,group)
                c=len(V)
                top=q**len(O)
                if top>900:continue
                tests.append((n,q,name,group))
    checked=0
    direct_faces=0
    characters_checked=0
    for n,q,name,group in tests:
        global cached_model
        cached_model=model(n,group)
        pred=predicted_cells(n,q,group)
        direct=direct_invariant_cells(n,q,group)
        inferred={v for cells in pred.values() for _,v in cells}
        assert inferred==direct,(n,q,name,'fixed cell discrepancy',len(inferred),len(direct))
        betti,ranks=ranks_and_betti(pred)
        B=wedge_count(n,q,group)
        c=len(cached_model[0])
        assert B>=0
        for degree,rank in betti.items():
            expected=B if degree==c-1 else 0
            assert rank==expected,(n,q,name,degree,rank,expected)
        checked+=1
        direct_faces+=len(direct)
        all_normalizer=[g for g in __import__('itertools').permutations(range(n)) if normalizes(g,group)]
        # Include identity, nontrivial sample and terminal elements.
        sample=all_normalizer[:3]+all_normalizer[-3:]
        for g in dict.fromkeys(sample):
            actual=direct_normalizer_trace(n,q,group,g,pred)
            expected=normalizer_character_formula(n,q,group,g)
            assert actual==expected,(n,q,name,g,actual,expected)
            characters_checked+=1
    print('VERIFY_OK cases=',checked,'invariant_cells=',direct_faces,'normalizer_characters=',characters_checked)
    print('examples S4 q=2:',wedge_count(4,2,closure(4,[perm_from_cycles(4,[(0,1)]),perm_from_cycles(4,[(0,1,2,3)])])))
    print('examples C4 q=2:',wedge_count(4,2,closure(4,[perm_from_cycles(4,[(0,1,2,3)])])))
    print('examples C2 double swap q=2:',wedge_count(4,2,closure(4,[perm_from_cycles(4,[(0,1),(2,3)])])))
    c5=closure(5,[perm_from_cycles(5,[(0,1,2,3,4)])])
    mul2=tuple((2*i)%5 for i in range(5))
    assert normalizes(mul2,c5)
    print('examples C5 q=2 normalizer multiplier2 trace:',normalizer_character_formula(5,2,c5,mul2))

if __name__=='__main__':
    run()
