#!/usr/bin/env python3
"""Exact combinatorial/lattice verification for a five-vertex graphical fan.

The graph has all edges except {0,1} and {2,3}. Each cone is the
sign-compatible order cone on integer potentials modulo constants.
No floating point arithmetic or third-party packages are used.
"""
from collections import Counter
from itertools import combinations, permutations, product

N = 5
VERTICES = tuple(range(N))
EDGES = tuple((i,j) for i,j in combinations(VERTICES,2)
              if (i,j) not in {(0,1),(2,3)})
ALL = (1 << N) - 1


def determinant(rows):
    if len(rows) == 0:
        return 1
    if len(rows) == 1:
        return rows[0][0]
    return sum((-1)**j * rows[0][j] * determinant(
        [row[:j]+row[j+1:] for row in rows[1:]])
        for j in range(len(rows)))


def cc(edge_set):
    remaining = set(VERTICES)
    result = []
    while remaining:
        component = {min(remaining)}
        todo = list(component)
        for u in todo:
            for i, j in edge_set:
                if i == u and j not in component:
                    component.add(j); todo.append(j)
                if j == u and i not in component:
                    component.add(i); todo.append(i)
        remaining -= component
        result.append(tuple(sorted(component)))
    return tuple(result)


def connected(mask):
    verts = {i for i in VERTICES if mask >> i & 1}
    if not verts:
        return False
    done = {min(verts)}
    while True:
        grown = done | {v for i,j in EDGES for v,u in [(i,j),(j,i)]
                        if u in done and v in verts}
        if grown == done:
            return done == verts
        done = grown


def sign_of(potential):
    return tuple((potential[j]>potential[i])-(potential[j]<potential[i])
                 for i,j in EDGES)


def all_signs_by_scores():
    return set(sign_of(t) for t in product(range(N),repeat=N))


def all_signs_by_ordered_partitions():
    result = set()
    for order in permutations(VERTICES):
        for cuts in product((0,1), repeat=N-1):
            values = [0]*N
            rank = 0
            for k,vertex in enumerate(order):
                if k: rank += cuts[k-1]
                values[vertex] = rank
            result.add(sign_of(values))
    return result


def ray_masks():
    return frozenset(s for s in range(1,ALL) if connected(s) and connected(ALL^s))


def permitted(s, signs):
    for (i,j), sign in zip(EDGES,signs):
        delta = ((s>>j)&1)-((s>>i)&1)
        if sign and sign*delta < 0:
            return False
        if sign == 0 and delta:
            return False
    return True


def integer_ray(s, components):
    last = components[-1][0]
    return tuple(((s>>c[0])&1)-((s>>last)&1) for c in components[:-1])


def primitive_relation(cols):
    d = len(cols[0])
    assert len(cols) == d+1
    coeffs = [(-1)**j * determinant([
        [cols[k][i] for k in range(d+1) if k!=j]
        for i in range(d)]) for j in range(d+1)]
    from math import gcd
    g = 0
    for k in coeffs:
        g = gcd(g,abs(k))
    assert g>0
    return tuple(k//g for k in coeffs)


def run():
    signs_a=all_signs_by_scores()
    signs_b=all_signs_by_ordered_partitions()
    assert signs_a==signs_b, (len(signs_a),len(signs_b))
    assert len(signs_a)==389
    rays0=ray_masks()
    assert len(rays0)==26
    cones = []
    for signs in signs_a:
        zeros = [e for e,s in zip(EDGES,signs) if s==0]
        components = cc(zeros)
        dim=len(components)-1
        rays=frozenset(mask for mask in rays0 if permitted(mask,signs))
        if len(rays)==dim:
            mat=[integer_ray(s,components) for s in sorted(rays)]
            det=abs(determinant(mat))
            regular=(det==1)
        else:
            assert len(rays)>dim
            det=None; regular=False
        cones.append(dict(signs=signs,dim=dim,rays=rays,regular=regular,det=det,components=components))
    assert Counter((c['dim'],len(c['rays'])) for c in cones)=={
        (0,0):1,(1,1):26,(2,2):116,(3,3):160,(3,4):8,
        (4,4):58,(4,5):20}
    assert all(c['det']==1 for c in cones if c['det'] is not None)
    bad=[c for c in cones if not c['regular']]
    minimal=[c for c in bad if not any(d['dim']<c['dim'] and
           d['rays']<c['rays'] for d in bad)]
    assert Counter(c['dim'] for c in minimal)=={3:8,4:4}
    curves=[c for c in minimal if c['dim']==3]
    isolated=[c for c in minimal if c['dim']==4]
    fixed=[c for c in cones if c['dim']==4]
    assert len(fixed)==78
    assert len([c for c in fixed if not c['regular']])==20
    # Independent fixed-point check through acyclic orientations and Hasse covers.
    acyclic_orientations = set()
    for ordering in permutations(VERTICES):
        position = {v:i for i,v in enumerate(ordering)}
        acyclic_orientations.add(tuple(position[i]<position[j] for i,j in EDGES))
    cover_counts = Counter()
    for oriented_signs in acyclic_orientations:
        arcs = [(i,j) if b else (j,i)
                for (i,j),b in zip(EDGES,oriented_signs)]
        out = {i:[] for i in VERTICES}
        for u,v in arcs:
            out[u].append(v)
        cover_count=0
        for u,v in arcs:
            seen={u}; todo=[u]
            for x in todo:
                for y in out[x]:
                    if (x,y)==(u,v):
                        continue
                    if y not in seen:
                        seen.add(y);todo.append(y)
            cover_count += (v not in seen)
        cover_counts[cover_count]+=1
    assert len(acyclic_orientations)==78
    assert cover_counts=={4:58,5:16,6:4}
    for c in curves:
        endpoints=[m for m in fixed if c['rays'] < m['rays']]
        assert len(endpoints)==2
        comp=c['components']
        col=[integer_ray(s,comp) for s in sorted(c['rays'])]
        rel=primitive_relation(col)
        assert sorted(rel)==[-1,-1,1,1],rel
        assert all(abs(determinant([col[j] for j in ix]))==1 for ix in combinations(range(4),3))
    for c in isolated:
        comp=c['components']
        col=[integer_ray(s,comp) for s in sorted(c['rays'])]
        rel=primitive_relation(col)
        assert sorted(rel)==[-1,-1,1,1,1],rel
        assert all(abs(determinant([col[j] for j in ix]))==1 for ix in combinations(range(5),4))
    for u,v in combinations(curves,2):
        assert not any(u['rays'] < m['rays'] and v['rays'] < m['rays'] for m in fixed)
    for isolated_point in isolated:
        assert not any(c['rays'] < isolated_point['rays'] for c in curves)
    print('VERIFY_OK')
    print('fan_cones=',len(cones),'rays=',len(rays0),'fixed_points=',len(fixed))
    print('cone_shapes=',sorted(Counter((c['dim'],len(c['rays'])) for c in cones).items()))
    print('minimal_singular_cones=',len(minimal),'curves=',len(curves),'isolated=',len(isolated))
    print('singular_orbits=',len(bad),'singular_fixed_points=',len([c for c in fixed if not c['regular']]))

if __name__=='__main__':
    run()
