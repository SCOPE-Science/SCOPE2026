"""Independent finite forward-activation and exchange-graph verification.

Run: python3 verify_forward.py [certificate.json]
Only Python standard-library modules are required.
"""
import collections
import hashlib
import itertools
import json
import sys
from collections import deque

N = 16
VERTICES = range(N)

def adjacency(which):
    out = [set() for _ in VERTICES]
    D = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    for v in VERTICES:
        x, y = divmod(v, 4)
        for w in VERTICES:
            if w == v:
                continue
            a, b = divmod(w, 4)
            if (x == a or y == b) if which == 'rook' else ((a-x)%4, (b-y)%4) in D:
                out[v].add(w)
    assert all(len(out[v]) == 6 for v in VERTICES)
    return out

def activate(adj, selected):
    active = set(selected)
    time = 0
    while True:
        new = {v for v in VERTICES if v not in active and len(adj[v]&active) >= 3}
        if not new:
            return len(active) == N, time, tuple(sorted(active))
        active |= new
        time += 1

def affine_rook_automorphisms():
    perms = list(itertools.permutations(range(4)))
    for p in perms:
        for q in perms:
            for swap in [0, 1]:
                yield tuple(4*p[x]+q[y] if not swap else 4*q[y]+p[x]
                    for x, y in (divmod(v, 4) for v in VERTICES))

def affine_shrikhande_automorphisms():
    D = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    for a,b,c,d in itertools.product(range(4), repeat=4):
        if (a*d-b*c) % 2 != 1:
            continue
        if {((a*x+b*y)%4,(c*x+d*y)%4) for x,y in D} != D:
            continue
        for dx,dy in itertools.product(range(4), repeat=2):
            yield tuple(4*((a*x+b*y+dx)%4)+(c*x+d*y+dy)%4
                for x,y in (divmod(v,4) for v in VERTICES))

def vertices(mask):
    return tuple(i for i in VERTICES if mask >> i & 1)

def masks_from_vertices(z):
    return sum(1 << i for i in z)

def all_dist(neighbors, source):
    ds = {source:0}
    parents = {source:None}
    q = deque([source])
    while q:
        v=q.popleft()
        for w in sorted(neighbors[v]):
            if w not in ds:
                ds[w] = ds[v]+1
                parents[w] = v
                q.append(w)
    return ds, parents

def characterize(which):
    adj=adjacency(which)
    # Verify both have common-neighbour multiplicities (16,6,2,2).
    for x,y in itertools.combinations(VERTICES, 2):
        assert len(adj[x]&adj[y]) == 2
    # Distinctness of graph models follows from their local graph types.
    all_pairs = list(itertools.combinations(VERTICES,2))
    triple_max = max(len(activate(adj,s)[2]) for s in itertools.combinations(VERTICES,3))
    optimum = {}
    for combo in itertools.combinations(VERTICES,4):
        yes, rounds, _ = activate(adj,combo)
        if yes:
            optimum[masks_from_vertices(combo)]=rounds
    assert len(optimum) == (864 if which=='rook' else 720)
    assert triple_max == (5 if which=='rook' else 7)
    automorphisms=list(affine_rook_automorphisms() if which=='rook'
                        else affine_shrikhande_automorphisms())
    assert len(automorphisms)==(1152 if which=='rook' else 192)
    assert len(set(automorphisms))==len(automorphisms)
    assert all({p[w] for w in adj[v]}==adj[p[v]]
               for p in automorphisms for v in VERTICES)
    unseen=set(optimum)
    orbits=[]
    while unseen:
        r=min(unseen)
        orbit={masks_from_vertices(p[i] for i in vertices(r)) for p in automorphisms}
        assert orbit.issubset(optimum)
        unseen-=orbit
        orbits.append((r,orbit))
    networks={}
    for mode in ('jump','slide'):
        ne={s:set() for s in optimum}
        for s in optimum:
            for removed in vertices(s):
                for added in (adj[removed] if mode=='slide' else VERTICES):
                    if not s>>added&1:
                        t=(s^(1<<removed))|(1<<added)
                        if t in ne:
                            ne[s].add(t)
        assert all(s in ne[t] for s in ne for t in ne[s])
        eccentricities={}
        for s in optimum:
            ds,_=all_dist(ne,s)
            assert len(ds)==len(optimum), f'{which} {mode} disconnected'
            eccentricities[s]=max(ds.values())
        rad=min(eccentricities.values());diam=max(eccentricities.values())
        edge_count=sum(map(len,ne.values()))//2
        networks[mode]=(ne,eccentricities,edge_count,rad,diam)
        print(f'{which} {mode} states={len(optimum)} edges={edge_count} '
              f'components=1 radius={rad} diameter={diam} '
              f'eccentricity={dict(sorted(collections.Counter(eccentricities.values()).items()))}')
    orbit_report=[]
    for r,orbit in orbits:
        row=dict(representative=list(vertices(r)),orbit_size=len(orbit),
                 rounds=optimum[r],induced_edges=sum(w in adj[v]
                 for v,w in itertools.combinations(vertices(r),2)))
        for mode in ('jump','slide'):
            ne,ec,_,_,_=networks[mode]
            assert all(len(ne[s]) == len(ne[r]) and ec[s] == ec[r] and optimum[s]==optimum[r]
                       for s in orbit)
            row[mode+'_degree']=len(ne[r]);row[mode+'_eccentricity']=ec[r]
        orbit_report.append(row)
        print('orbit',which,json.dumps(row,sort_keys=True))
    assert sum(x['orbit_size'] for x in orbit_report)==len(optimum)
    cert={'graph':which, 'threshold':3,'order':16,'degree':6,'parameters':[16,6,2,2],
          'lower_bound':4,'explicit_automorphism_action_size':len(automorphisms),
          'size_three_largest_closure':triple_max,
          'minimum_seeds':sorted(optimum),
          'activation_rounds':[optimum[s] for s in sorted(optimum)],
          'orbits':orbit_report,'moves':{}}
    for mode in ('jump','slide'):
        ne,ec,edges,rad,diam=networks[mode]
        source=min(x for x in optimum if ec[x]==diam)
        distances,parents=all_dist(ne,source)
        end=min(x for x in distances if distances[x]==diam)
        path=[]
        while end is not None:
            path.append(list(vertices(end)))
            end=parents[end]
        path.reverse()
        cert['moves'][mode]={'edges':edges,'radius':rad,'diameter':diam,
           'eccentricity_distribution':dict(sorted(collections.Counter(ec.values()).items())),
           'edge_pairs':[[x,y] for x in sorted(ne) for y in sorted(ne[x]) if x<y],
           'diameter_witness':path}
    return cert

def main():
    both={g:characterize(g) for g in ('rook','shri')}
    if len(sys.argv)>1:
        data=(json.dumps(both,indent=2,ensure_ascii=False,sort_keys=True)+'\n').encode()
        with open(sys.argv[1],'wb') as f:f.write(data)
        print('certificate sha256',hashlib.sha256(data).hexdigest(),'bytes',len(data))
    print('OK independent forward-activation verification')
if __name__=='__main__':main()
