"""Independent verifier for K(4,9) minimum-genus witnesses.
Convention: rotation at each vertex = cyclic list of neighbors (counterclockwise).
Face tracing (standard rotation-system rule): traverse dart (tail->head); at head,
leave by the successor of the incoming edge in head's rotation list."""
import json

U = list(range(4)); W = list(range(4,13))

def check_rots(rots):
    assert set(rots.keys()) == set(U+W), "vertex set must be 0..12"
    for u in U:
        assert sorted(rots[u]) == W, f"rotation at {u} must list all of W"
    for w in W:
        assert sorted(rots[w]) == U, f"rotation at {w} must list all of U"
    # proper cyclic orders: no repeats
    for v in U+W:
        assert len(set(rots[v])) == len(rots[v])

def trace_faces(rots):
    pos = {(v, nb): i for v, lst in rots.items() for i, nb in enumerate(lst)}
    remaining = set()
    for a in U:
        for b in W:
            remaining.add((a, b)); remaining.add((b, a))
    faces = []
    while remaining:
        d0 = next(iter(remaining))
        cur = d0; cyc = []
        while True:
            remaining.discard(cur)
            cyc.append(cur)
            t, h = cur
            nxt = rots[h][(pos[(h, t)] + 1) % len(rots[h])]
            cur = (h, nxt)
            if cur == d0:
                break
            assert len(cyc) <= 72, "face walk too long"
        faces.append(cyc)
    return faces

def verify(name, rots):
    check_rots(rots)
    faces = trace_faces(rots)
    F = len(faces)
    V, E = 13, 36
    chi = V - E + F
    g = (2 - chi) // 2
    assert V - E + F == 2 - 2*g, "Euler check"
    vlens = sorted(len(f) for f in faces)
    assert sum(vlens) == 2*E, "face-edge double count"
    # each directed edge in exactly one face; each undirected edge twice
    from collections import Counter
    darts = Counter(d for f in faces for d in f)
    assert len(darts) == 2*E and all(v == 1 for v in darts.values()), "dart partition"
    # bipartite evenness + girth bound
    for f in faces:
        assert len(f) % 2 == 0 and len(f) >= 4, f"bad face {f}"
    return {"F": F, "g": g, "lens": vlens, "faces": faces}

def vseq(face):
    return [face[0][0]] + [h for (_, h) in face]

if __name__ == "__main__":
    with open("scratch/witnesses.json") as f:
        WIT = json.load(f)
    # keys are str of tuple; map back
    for k, rec in WIT.items():
        rots = {int(v): lst for v, lst in rec["rots"].items()}
        r = verify(k, rots)
        print(f"multiset {k} seed={rec['seed']}: F={r['F']} g={r['g']} lens={r['lens']}")
        for i, f in enumerate(r["faces"]):
            print(f"  face {i}: len={len(f)} verts={vseq(f)}")
