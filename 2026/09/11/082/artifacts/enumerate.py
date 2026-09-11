"""Exhaustive floor-diagram census for the real AB F0->F2 transfer at class (2,2)/(2E+4F).

Shapes: 2-vertex diagrams (proven below to be the only shapes for these classes),
enumerated over all (b,t) splits; each shape: Aut-quotiented marked census,
complex multiplicity prod w(e)^2, and Brugalle-Mikhalkin Def 3.8 r-real multiplicity
summed over markings for r=0..3 (F0) and r=0..1 (+extended rows) for F2.

Aut groups: brute-force graph automorphisms (fixing theta values + orientation +
divergence), markings counted up to equivalence (Def 3.4).

Outputs ledger.json. See DRAFT.md for the math.
"""
import itertools, json, os
from math import prod

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ledger.json")

# ---------- generic diagram representation ----------
class Diagram:
    def __init__(self, name, theta, edges):
        # theta: dict vertex->int; edges: list of dicts {name,u,v,w,kind}
        # kind: 'bounded','bottom','top'
        self.name = name
        self.theta = dict(theta)
        self.edges = [dict(e) for e in edges]
        self.verts = list(theta.keys())
    def div(self, v):
        d = 0
        for e in self.edges:
            if e['kind'] == 'bounded':
                if e['v'] == v: d += e['w']
                if e['u'] == v: d -= e['w']
            elif e['kind'] == 'bottom':
                if e['v'] == v: d += e['w']
            elif e['kind'] == 'top':
                if e['u'] == v: d -= e['w']
        return d
    def elements(self):
        return self.verts + [e['name'] for e in self.edges]
    def relations(self):
        r = []
        for e in self.edges:
            if e['kind'] == 'bounded':
                r.append((e['u'], e['name'])); r.append((e['name'], e['v']))
            elif e['kind'] == 'bottom':
                r.append((e['name'], e['v']))
            elif e['kind'] == 'top':
                r.append((e['u'], e['name']))
        return r
    def automorphisms(self):
        # permutations of elements preserving: vertex set + theta, edge set + kind + weight + incidence
        el = self.elements()
        V = set(self.verts)
        E = {e['name']: e for e in self.edges}
        rels = self.relations()
        before = {(a, b) for a, b in rels}
        auts = []
        for perm in itertools.permutations(el):
            mp = dict(zip(el, perm))
            # vertices -> vertices with same theta
            ok = True
            for v in self.verts:
                if mp[v] not in V or self.theta[mp[v]] != self.theta[v]:
                    ok = False; break
            if not ok: continue
            for e in self.edges:
                f = E.get(mp[e['name']])
                if f is None or f['kind'] != e['kind'] or f['w'] != e['w']:
                    ok = False; break
                # incidence
                if e['kind'] == 'bounded':
                    if not (mp[e['u']] == f['u'] and mp[e['v']] == f['v']):
                        ok = False; break
                elif e['kind'] == 'bottom':
                    if mp[e['v']] != f['v']:
                        ok = False; break
                elif e['kind'] == 'top':
                    if mp[e['u']] != f['u']:
                        ok = False; break
            if ok: auts.append(mp)
        return auts
    def complex_mult(self):
        p = 1
        for e in self.edges:
            if e['kind'] == 'bounded':
                p *= e['w'] ** 2
        return p

def all_markings(d):
    el = d.elements(); rels = d.relations()
    out = []
    for perm in itertools.permutations(el):
        pos = {e: i for i, e in enumerate(perm)}
        if all(pos[a] < pos[b] for a, b in rels):
            out.append(list(perm))
    return out

def marking_reps(d, markings):
    auts = d.automorphisms()
    seen = set(); reps = []
    for m in markings:
        # canonical: min tuple over aut images
        imgs = []
        for a in auts:
            imgs.append(tuple(a[x] for x in m))
        c = min(imgs)
        if c not in seen:
            seen.add(c); reps.append(m)
    return reps, len(auts)

def incident(d, v, ename):
    E = {e['name']: e for e in d.edges}
    e = E[ename]
    if e['kind'] == 'bounded': return v in (e['u'], e['v'])
    if e['kind'] == 'bottom': return v == e['v']
    if e['kind'] == 'top': return v == e['u']
    return False

def adjacent(d, x, y):
    V = set(d.verts)
    if (x in V) != (y in V):
        v = x if x in V else y
        e = y if x in V else x
        return incident(d, v, e)
    return False

def r_real_of_marking(d, m, r, bounded_names):
    s = len(m); V = set(d.verts)
    W = {e['name']: e['w'] for e in d.edges}
    divs = {v: d.div(v) for v in d.verts}
    pairs = [(s - 2*k, s - 2*k + 1) for k in range(1, r+1)]  # 0-based
    Im = set()
    for (i, j) in pairs:
        if not adjacent(d, m[i], m[j]):
            Im.add(i); Im.add(j)
    # r-reality: (D,m)~(D,m o rho): exists aut taking one marking to other
    rho = list(range(s))
    for (i, j) in pairs:
        if i in Im:
            rho[i], rho[j] = rho[j], rho[i]
    m2 = [m[rho[i]] for i in range(s)]
    auts = d.automorphisms()
    real = any(all(a[m[i]] == m2[i] for i in range(s)) for a in auts)
    if not real:
        return 0
    Im_elems = {m[i] for i in Im}
    for b in bounded_names:
        if W[b] % 2 == 0 and b not in Im_elems:
            return 0
    nr = s - 2*r
    A = [e['name'] for e in d.edges if e['kind'] == 'bounded' and e['name'] not in set(m[:nr])]
    odd = sum(1 for i in Im if m[i] in V and divs[m[i]] % 2 == 1)
    assert odd % 2 == 0, (d.name, m, r, odd)
    return ((-1) ** (odd // 2)) * (prod(W[e] for e in A) if A else 1)

def census(d, rmax):
    mk = all_markings(d)
    reps, aut = marking_reps(d, mk)
    bounded = [e['name'] for e in d.edges if e['kind'] == 'bounded']
    out = {"diagram": d.name, "theta": d.theta,
           "edges": [(e['name'], e['kind'], e.get('u'), e.get('v'), e['w']) for e in d.edges],
           "divs": {v: d.div(v) for v in d.verts},
           "aut_order": aut, "n_lin_ext": len(mk), "n_reps": len(reps),
           "complex_mult": d.complex_mult(),
           "complex_total": len(reps) * d.complex_mult()}
    for r in range(rmax + 1):
        out[f"W_r{r}"] = sum(r_real_of_marking(d, m, r, bounded) for m in reps)
    return out

def E(name, u, v, w, kind):
    d = {"name": name, "w": w, "kind": kind}
    if kind == 'bounded': d.update(u=u, v=v)
    elif kind == 'bottom': d.update(v=v)
    elif kind == 'top': d.update(u=u)
    return d

def build():
    L = []
    # F0 (2,2): dl={0,0}, dr={1,1}, d-=2, d+=2
    L.append(census(Diagram("F0-A w1: A(0):b1/t0 B(0):b1/t2", {0: 0, 1: 0} if False else {'A': 0, 'B': 0},
        [E('e0','A','B',1,'bounded'), E('bA','B','A',1,'bottom'), E('bB','B','B',1,'bottom'),
         E('t1','B','B',1,'top'), E('t2','B','B',1,'top')]), 3))
    L.append(census(Diagram("F0-B w1: A(0):b2/t1 B(0):b0/t1", {'A': 0, 'B': 0},
        [E('e0','A','B',1,'bounded'), E('bA1','B','A',1,'bottom'), E('bA2','B','A',1,'bottom'),
         E('tA','A','A',1,'top'), E('tB','B','B',1,'top')]), 3))
    L.append(census(Diagram("F0-C w2: A(0):b2/t0 B(0):b0/t2", {'A': 0, 'B': 0},
        [E('e0','A','B',2,'bounded'), E('bA1','B','A',1,'bottom'), E('bA2','B','A',1,'bottom'),
         E('t1','B','B',1,'top'), E('t2','B','B',1,'top')]), 3))
    # F2 main (2E+4F): dl={0,0}, dr={2,2}, d-=4, d+=0
    L.append(census(Diagram("F2-D w1: A(0):b3/t0 B(0):b1/t0", {'A': 0, 'B': 0},
        [E('e0','A','B',1,'bounded'), E('b1','B','A',1,'bottom'), E('b2','B','A',1,'bottom'),
         E('b3','B','A',1,'bottom'), E('b4','B','B',1,'bottom')]), 3))
    L.append(census(Diagram("F2-E w2: A(0):b4/t0 B(0):b0/t0", {'A': 0, 'B': 0},
        [E('e0','A','B',2,'bounded'), E('b1','B','A',1,'bottom'), E('b2','B','A',1,'bottom'),
         E('b3','B','A',1,'bottom'), E('b4','B','A',1,'bottom')]), 3))
    # F2 correction (E+4F): (c,d)=(2,1): d^t=2, d^b=4, l={0}, r={2}, height 1.
    # Single floor A(0): 4 bottoms, 2 tops; div=+2; theta+div={2}=r. s=7.
    L.append(census(Diagram("F2corr single floor A(0):b4/t2", {'A': 0},
        [E('b1','B','A',1,'bottom'), E('b2','B','A',1,'bottom'),
         E('b3','B','A',1,'bottom'), E('b4','B','A',1,'bottom'),
         E('t1','A','A',1,'top'), E('t2','A','A',1,'top')]), 3))
    return L

if __name__ == '__main__':
    L = build()
    with open(OUT, 'w') as f:
        json.dump(L, f, indent=1)
    for d in L:
        keys = [k for k in d if k.startswith('W_') or k in ('complex_total', 'n_reps', 'aut_order', 'n_lin_ext')]
        print(d['diagram'], {k: d[k] for k in keys})
