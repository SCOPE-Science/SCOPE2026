#!/usr/bin/env python3
"""Direct finite-cell checks of the three-particle radial-tree character formula.

Usage: python3 verify_star_three.py
No external dependencies. Graph edges are radially oriented; all cube
orientation signs are evaluated by a genuine permutation of edge axes.
"""
import itertools
from collections import defaultdict
from math import comb


def permutations_by_type(m):
    found = {}
    for p in itertools.permutations(range(m)):
        ct = cycle_type(p)
        if ct not in found:
            found[ct] = p
    return found


def cycle_type(p):
    seen = set()
    lens = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lens.append(length)
    return tuple(sorted(lens))


def cubical_cells(m):
    # Vertices: 0 is the center, 1+2i the inner vertex, 2+2i the tip.
    ends = []
    names = []
    for v in range(2*m+1):
        names.append(('v',v))
        ends.append(frozenset((v,)))
    for i in range(m):
        names.append(('p',i))
        ends.append(frozenset((0,1+2*i)))
    for i in range(m):
        names.append(('q',i))
        ends.append(frozenset((1+2*i,2+2*i)))
    face_groups=defaultdict(list)
    for a,b,c in itertools.combinations(range(len(names)),3):
        if ends[a]&ends[b] or ends[a]&ends[c] or ends[b]&ends[c]:
            continue
        triple=(a,b,c)
        k=sum(names[x][0]!='v' for x in triple)
        face_groups[k].append(triple)
    return names, ends, face_groups


def remap(names,m,p):
    result=[]
    index={x:i for i,x in enumerate(names)}
    for kind,i in names:
        if kind=='v':
            if i==0:
                result.append(index[(kind,i)])
            else:
                result.append(index[(kind,1+2*p[(i-1)//2]+((i-1)%2))])
        else:
            result.append(index[(kind,p[i])])
    return result


def signed_trace(names, groups, mapping):
    signed=[]
    for dim in range(4):
        subtotal=0
        for cells in groups[dim]:
            image=tuple(mapping[x] for x in cells)
            if set(cells)!=set(image):
                continue
            edges=[mapping[x] for x in cells if names[x][0]!='v']
            inversions=sum(edges[a]>edges[b] for a in range(len(edges)) for b in range(a+1,len(edges)))
            subtotal+=(-1)**inversions
        signed.append(subtotal)
    return signed


def connectivity(names, groups):
    vertices = {cells:i for i,cells in enumerate(groups[0])}
    par=list(range(len(vertices)))
    def root(a):
        while par[a]!=a:
            par[a]=par[par[a]]
            a=par[a]
        return a
    for cells in groups[1]:
        edge=next(x for x in cells if names[x][0]!='v')
        i=names[edge][1]
        endpoints=((0,1+2*i) if names[edge][0]=='p' else (1+2*i,2+2*i))
        leftovers=tuple(x for x in cells if names[x][0]=='v')
        for j in endpoints:
            # Vertex-cell index equals the graph vertex number.
            assert tuple(sorted(leftovers+(j,))) in vertices
        a,b=(vertices[tuple(sorted(leftovers+(j,)))] for j in endpoints)
        par[root(a)]=root(b)
    return len({root(x) for x in range(len(par))})


def formula(m,parts):
    f=parts.count(1)
    t=parts.count(2)
    u=parts.count(3)
    return 1-f+comb(f,2)+2*comb(f,3)-t-u


def main():
    checked_classes=0
    checked_permutations=0
    for m in range(3,8):
        names,_,groups=cubical_cells(m)
        cell_vector=tuple(len(groups[k]) for k in range(4))
        assert connectivity(names,groups)==1
        euler=sum((-1)**k*cell_vector[k] for k in range(4))
        rank=(m-2)*(m-1)*(2*m+3)//6
        assert 1-euler==rank
        by_type=permutations_by_type(m)
        for ct,p in by_type.items():
            mapping=remap(names,m,p)
            traces=signed_trace(names,groups,mapping)
            value=1-sum((-1)**k*traces[k] for k in range(4))
            assert value==formula(m,ct),(m,ct,traces,value,formula(m,ct))
            checked_classes+=1
        if m<=5:
            for p in itertools.permutations(range(m)):
                traces=signed_trace(names,groups,remap(names,m,p))
                value=1-sum((-1)**k*traces[k] for k in range(4))
                assert value==formula(m,cycle_type(p))
                checked_permutations+=1
        print('m=%d cells=%s connected=YES beta1=%d conjugacy_classes=%d' % (m,cell_vector,rank,len(by_type)))
    print('verified_conjugacy_classes=%d verified_all_permutations_m3_to_m5=%d' % (checked_classes,checked_permutations))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
