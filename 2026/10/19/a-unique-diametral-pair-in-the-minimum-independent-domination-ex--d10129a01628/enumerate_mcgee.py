#!/usr/bin/env python3
"""Exhaustive independent-dominating-set and exchange certificate for the McGee graph.
Requires only Python 3 standard library. Run: python3 enumerate_mcgee.py > primary_output.txt
"""
import collections
import hashlib
import itertools
import json
from collections import deque
from pathlib import Path

N = 24
FULL = (1 << N) - 1

def graph():
    edges = set()
    increments = (-12, 7, -7)
    for u in range(N):
        for v in ((u + 1) % N, (u + increments[u % 3]) % N):
            edges.add(tuple(sorted((u, v))))
    nb = [0] * N
    for u, v in edges:
        nb[u] |= 1 << v
        nb[v] |= 1 << u
    assert len(edges) == 36 and all(z.bit_count() == 3 for z in nb)
    return nb, sorted(edges)

def graph_distances(nb):
    dist = []
    for u in range(N):
        d = [-1] * N
        d[u] = 0
        q = deque([u])
        while q:
            v = q.popleft()
            for w in range(N):
                if nb[v] >> w & 1 and d[w] < 0:
                    d[w] = d[v] + 1
                    q.append(w)
        assert all(x >= 0 for x in d)
        dist.append(d)
    return dist

def independent_sets(nb):
    sets = []
    def rec(v, mask):
        if v == N:
            sets.append(mask)
            return
        rec(v + 1, mask)
        if not (mask & nb[v]):
            rec(v + 1, mask | (1 << v))
    rec(0, 0)
    assert len(sets) == len(set(sets))
    return sets

def exchange_graph(opt, nb):
    lookup = {s:i for i,s in enumerate(opt)}
    es = set()
    for i, s in enumerate(opt):
        x = s
        while x:
            z = x & -x
            a = z.bit_length() - 1
            x -= z
            ys = nb[a] & ~s
            while ys:
                zz = ys & -ys
                b = zz.bit_length() - 1
                ys -= zz
                t = (s ^ (1 << a)) | (1 << b)
                j = lookup.get(t)
                if j is not None and i < j:
                    es.add((i, j))
    h = [[] for _ in opt]
    for i, j in sorted(es):
        h[i].append(j)
        h[j].append(i)
    for arr in h: arr.sort()
    return sorted(es), h

def all_graph_distances(h):
    rows = []
    for root in range(len(h)):
        d = [-1] * len(h)
        d[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in h[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    q.append(v)
        rows.append(d)
    return rows

def automorphisms(nb):
    distances = graph_distances(nb)
    nbs = [{v for v in range(N) if nb[u] >> v & 1} for u in range(N)]
    autos = []
    def extend(mapping, unused):
        if len(mapping) == N:
            autos.append([mapping[k] for k in range(N)])
            return
        chosen, values = None, None
        for u in range(N):
            if u in mapping: continue
            poss = [v for v in sorted(unused) if all(distances[u][w] == distances[v][mapped] for w, mapped in mapping.items())]
            if not poss: return
            if values is None or len(poss) < len(values):
                chosen, values = u, poss
            if len(values) == 1: break
        for v in values:
            mapping[chosen] = v
            extend(mapping, unused - {v})
            del mapping[chosen]
    src_neighbors = sorted(nbs[0])
    for dest in range(N):
        for perm in itertools.permutations(sorted(nbs[dest])):
            mp = dict(zip([0] + src_neighbors, [dest] + list(perm)))
            extend(mp, set(range(N)) - set(mp.values()))
    autos.sort()
    assert len(autos) == len(set(map(tuple, autos)))
    for a in autos:
        assert all(((nb[u] >> v) & 1) == ((nb[a[u]] >> a[v]) & 1) for u in range(N) for v in range(N))
    return autos

def orbit_data(opt, h, dists, autos):
    i_of = {s:i for i,s in enumerate(opt)}
    unvisited = set(opt)
    summary = []
    while unvisited:
        smallest = min(unvisited)
        orbit = set()
        for perm in autos:
            transformed = sum(1 << perm[v] for v in range(N) if smallest >> v & 1)
            assert transformed in i_of
            orbit.add(transformed)
        assert orbit <= unvisited
        unvisited -= orbit
        representative = min(orbit)
        r = i_of[representative]
        assert len({len(h[i_of[z]]) for z in orbit}) == 1
        assert len({max(dists[i_of[z]]) for z in orbit}) == 1
        summary.append({'representative_mask': representative, 'size': len(orbit), 'degree': len(h[r]), 'eccentricity': max(dists[r])})
    return sorted(summary, key=lambda x:x['representative_mask'])

def build():
    nb, edges = graph()
    sets = independent_sets(nb)
    face_counts = dict(sorted(collections.Counter(x.bit_count() for x in sets).items()))
    maximal = [x for x in sets if all((x >> i & 1) or (x & nb[i]) for i in range(N))]
    maximal_sizes = dict(sorted(collections.Counter(x.bit_count() for x in maximal).items()))
    optimum = sorted(x for x in maximal if x.bit_count() == min(maximal_sizes))
    swaps, h = exchange_graph(optimum, nb)
    all_d = all_graph_distances(h)
    assert all(min(row) == 0 and -1 not in row for row in all_d)
    ecc = [max(r) for r in all_d]
    diam_pairs = [[i,j] for i in range(len(optimum)) for j in range(i+1,len(optimum)) if all_d[i][j] == max(ecc)]
    autos = automorphisms(nb)
    orbits = orbit_data(optimum, h, all_d, autos)
    triangles = sum(len(set(h[i]) & set(h[j])) for i,j in swaps) // 3
    cert = {
        'graph': {'vertex_count':N,'edges':edges,'lcf_increments':[-12,7,-7],'lcf_repeat':8},
        'independence_face_sizes': {str(k):v for k,v in face_counts.items()},
        'maximal_independent_size_counts': {str(k):v for k,v in maximal_sizes.items()},
        'minimum_size':min(maximal_sizes),
        'minimum_masks':optimum,
        'exchange_edges':swaps,
        'exchange_degrees':[len(z) for z in h],
        'exchange_eccentricities':ecc,
        'exchange_radius':min(ecc),
        'exchange_diameter':max(ecc),
        'diametral_pairs':diam_pairs,
        'triangles':triangles,
        'automorphisms':autos,
        'orbits':orbits,
    }
    assert len(sets) == 34305 and maximal_sizes == {8:146,9:352,10:8}
    assert len(optimum) == 146 and len(swaps) == 216
    assert (min(ecc),max(ecc)) == (11,12)
    assert collections.Counter(ecc) == {11:144,12:2}
    assert triangles == 0 and len(diam_pairs) == 1
    assert len(autos) == 32 and sorted(z['size'] for z in orbits)==[2,16,16,16,32,32,32]
    assert diam_pairs == [[optimum.index(4793490),optimum.index(9586980)]]
    out = Path(__file__).with_name('mcgee_certificate.json')
    out.write_text(json.dumps(cert,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    raw = out.read_bytes()
    return cert, hashlib.sha256(raw).hexdigest(),len(raw)

if __name__ == '__main__':
    cert, sha, nbytes = build()
    print('McGee independent-domination certificate')
    print('independent_face_count:',sum(cert['independence_face_sizes'].values()))
    print('maximal_sizes:',cert['maximal_independent_size_counts'])
    print('minimum_size:',cert['minimum_size'],'minimum_sets:',len(cert['minimum_masks']))
    print('exchanges:',len(cert['exchange_edges']),'radius:',cert['exchange_radius'],'diameter:',cert['exchange_diameter'])
    print('degree_spectrum:',dict(sorted(collections.Counter(cert['exchange_degrees']).items())))
    print('eccentricity_spectrum:',dict(sorted(collections.Counter(cert['exchange_eccentricities']).items())))
    print('automorphisms:',len(cert['automorphisms']),'orbits:',[(x['size'],x['degree'],x['eccentricity']) for x in cert['orbits']])
    print('diametral_masks:',[(cert['minimum_masks'][i],cert['minimum_masks'][j]) for i,j in cert['diametral_pairs']])
    print('triangles:',cert['triangles'])
    print('certificate_bytes:',nbytes,'sha256:',sha)
