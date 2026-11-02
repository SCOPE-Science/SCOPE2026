"""Reproducible exact arithmetic for the Paley-23 directed flag complex.
Dependencies: Python 3.10+ and SymPy. Run: python paley23_equivariant_check.py
The script reconstructs its face poset, a full acyclic matching, the integral
Morse boundary, finite-group invariant chains, and characteristic-23 eigenspaces.
"""
import itertools, collections, functools, os, time
P = 23
Q = {pow(i, 2, P) for i in range(1, P)}

def beat(a, b):
    return (b - a) % P in Q
cyclic = [1 << a | 1 << b | 1 << c for a, b, c in itertools.combinations(range(P), 3) if beat(a, b) == beat(b, c) == beat(c, a) or beat(a, c) == beat(c, b) == beat(b, a)]
per = [[] for j in range(P)]
for q in cyclic:
    per[q.bit_length() - 1].append(q ^ 1 << q.bit_length() - 1)
faces = {0}
for s in range(1, 1 << P):
    j = s.bit_length() - 1
    low = s ^ 1 << j
    if low in faces and (not any((low & v == v for v in per[j]))):
        faces.add(s)
faces.discard(0)
bydim = [sorted((s for s in faces if s.bit_count() == k + 1)) for k in range(5)]

def action(s, a, b):
    v = [(a * i + b) % P for i in range(P) if s >> i & 1]
    z = sum((1 << i for i in v))
    inversions = sum((v[i] > v[j] for i in range(len(v)) for j in range(i + 1, len(v))))
    return (z, -1 if inversions % 2 else 1)

def rankmod(cols, p):
    piv = {}
    for col in cols:
        z = {k: v % p for k, v in col.items() if v % p}
        while z:
            i = max(z)
            coef = z[i]
            if i not in piv:
                inv = pow(coef, -1, p)
                piv[i] = {k: v * inv % p for k, v in z.items()}
                break
            for k, v in piv[i].items():
                vv = (z.get(k, 0) - coef * v) % p
                if vv:
                    z[k] = vv
                elif k in z:
                    del z[k]
    return len(piv)

def groupcomplex(group, p=1009):
    orbitspaces = []
    maps = []
    kstats = []
    for d, original in enumerate(bydim):
        visited = set()
        orbits = []
        face_map = {}
        for s in original:
            if s in visited:
                continue
            coeff = {}
            conflict = False
            for a, b in group:
                t, z = action(s, a, b)
                if t in coeff and coeff[t] != z:
                    conflict = True
                coeff[t] = z
            for t in coeff:
                visited.add(t)
            if conflict:
                for t in coeff:
                    face_map[t] = None
            else:
                z = len(orbits)
                orbits.append(coeff)
                for t in coeff:
                    face_map[t] = z
        orbitspaces.append(orbits)
        maps.append(face_map)
    ranks = []
    for d in range(1, 5):
        cols = []
        for orb in orbitspaces[d]:
            out = {}
            for s, coeff in orb.items():
                j = 0
                for v in range(P):
                    if s >> v & 1:
                        t = s ^ 1 << v
                        index = maps[d - 1][t]
                        if index is not None and t == min(orbitspaces[d - 1][index]):
                            out[index] = out.get(index, 0) + coeff * (-1) ** j
                        j += 1
            cols.append(out)
        ranks.append(rankmod(cols, p))
    betti = [len(orbitspaces[i]) - (ranks[i - 1] if i else 0) - (ranks[i] if i < 4 else 0) for i in range(5)]
    return ([len(o) for o in orbitspaces], ranks, betti)

def eigencomplex(lam, p=23):
    assert pow(lam, 11, p) == 1
    orbitspaces = []
    maps = []
    for d, original in enumerate(bydim):
        visited = set()
        orbits = []
        face_map = {}
        for s in original:
            if s in visited:
                continue
            coeff = {}
            j = 0
            while True:
                t, sgn = action(s, pow(2, j, 23), 0)
                if t in coeff:
                    break
                coeff[t] = sgn * pow(lam, -j, p) % p
                j += 1
            if pow(lam, j, p) != 1:
                for x in coeff:
                    visited.add(x)
                    face_map[x] = None
            else:
                idx = len(orbits)
                orbits.append(coeff)
                for x in coeff:
                    visited.add(x)
                    face_map[x] = idx
        orbitspaces.append(orbits)
        maps.append(face_map)
    ranks = []
    for d in range(1, 5):
        cols = []
        for orb in orbitspaces[d]:
            out = {}
            for s, coeff in orb.items():
                j = 0
                for v in range(P):
                    if s >> v & 1:
                        t = s ^ 1 << v
                        idx = maps[d - 1][t]
                        if idx is not None and t == min(orbitspaces[d - 1][idx]):
                            out[idx] = out.get(idx, 0) + coeff * (-1) ** j
                        j += 1
            cols.append(out)
        ranks.append(rankmod(cols, p))
    return ([len(o) for o in orbitspaces], ranks, [len(orbitspaces[i]) - (ranks[i - 1] if i else 0) - (ranks[i] if i < 4 else 0) for i in range(5)])


def verify():
    from collections import Counter, deque
    from functools import lru_cache
    from sympy import MutableSparseMatrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    assert len(Q)==11 and pow(2,11,23)==1 and pow(2,1,23)!=1
    assert len(cyclic)==506
    assert all(sum(beat(a,c) and beat(b,c) for c in range(P)) == 5
               for a in range(P) for b in range(a+1,P))
    assert [len(a) for a in bydim]==[23,253,1265,2530,1518]
    for d in range(1,5):
        lo=set(bydim[d-1])
        assert all(s^(1<<v) in lo for s in bydim[d] for v in range(P) if s>>v&1)
    unmatched=set(faces); pairs=[]
    for v in range(P):
        bit=1<<v
        for s in sorted(unmatched):
            if not (s&bit) and (s|bit) in unmatched:
                unmatched.remove(s);unmatched.remove(s|bit)
                pairs.append((s,s|bit))
    assert len(pairs)==2681
    assert Counter(s.bit_count()-1 for s in unmatched)=={0:1,3:102,4:124}
    lower={a:b for a,b in pairs}; upper={b:a for a,b in pairs}
    indegree={s:0 for s in faces}; adjacency={s:[] for s in faces}; incidents=0
    for s in faces:
        if s.bit_count()==1: continue
        for v in range(P):
            if not s>>v&1: continue
            t=s^(1<<v); incidents+=1
            if upper.get(s)==t:
                adjacency[t].append(s);indegree[s]+=1
            else:
                adjacency[s].append(t);indegree[t]+=1
    ready=deque(s for s,d in indegree.items() if d==0)
    removed=0
    while ready:
        s=ready.popleft();removed+=1
        for t in adjacency[s]:
            indegree[t]-=1
            if indegree[t]==0:ready.append(t)
    assert removed==len(faces)
    crit3=sorted(s for s in unmatched if s.bit_count()==4)
    crit4=sorted(s for s in unmatched if s.bit_count()==5)
    rows={s:i for i,s in enumerate(crit3)}
    @lru_cache(None)
    def reduce3(s):
        if s in unmatched: return {s:1}
        if s not in lower: return {}
        parent=lower[s]
        if parent.bit_count()!=5:return {}
        vertices=[v for v in range(P) if parent>>v&1]
        k=vertices.index((parent^s).bit_length()-1)
        out={}
        for i,v in enumerate(vertices):
            if i==k:continue
            t=parent^(1<<v)
            for r,val in reduce3(t).items():
                out[r]=out.get(r,0)+(-1 if (k+i)%2==0 else 1)*val
        return {r:val for r,val in out.items() if val}
    morsecols=[]
    for s in crit4:
        col={}
        for j,v in enumerate([v for v in range(P) if s>>v&1]):
            for r,val in reduce3(s^(1<<v)).items():
                col[rows[r]]=col.get(rows[r],0)+(-1)**j*val
        morsecols.append({r:val for r,val in col.items() if val})
    m=MutableSparseMatrix(102,124,{(r,j):val for j,col in enumerate(morsecols) for r,val in col.items()})
    diag=smith_normal_form(m,domain=ZZ)
    factors=Counter(abs(int(diag[i,i])) for i in range(102) if diag[i,i])
    assert factors=={1:78,23:1}, factors
    # The exact integral homology is Z^23 + Z/23 in degree 3,
    # and Z^45 in degree 4; this classification is not a novelty claim.
    tgroup=[(1,b) for b in range(P)]
    mgroup=[(a,0) for a in sorted(Q)]
    fullgroup=[(a,b) for a in sorted(Q) for b in range(P)]
    for group, expected in [(tgroup,([1,11,55,110,66],[0,11,44,65],[1,0,0,1,1])),
                            (mgroup,([3,23,115,230,138],[2,21,94,133],[1,0,0,3,5])),
                            (fullgroup,([1,1,5,10,6],[0,1,4,5],[1,0,0,1,1]))]:
        assert groupcomplex(group,1009)==expected,(len(group),groupcomplex(group,1009))
    for lam in sorted(Q):
        chain,ranks,betti=eigencomplex(lam,23)
        expected=[1,0,0,3,5] if lam==1 else ([0,0,0,3,5] if lam==12 else [0,0,0,2,4])
        assert betti==expected,(lam,chain,ranks,betti)
    # Full C23 invariants in degrees 3,4 are (1,1); quotient C11 invariants (3,5).
    # Over F23 the extra pair of eigenspaces in degrees (3,4) both carry
    # eigenvalue 12. Naturality of tensor and Tor identifies the degree-3
    # extra eigenspace with H_3 integral 23-torsion, so multiplier 2 acts by 12.
    print('PAL23_AFFINE_FREE_MODULES_AND_23_TORSION_CHARACTER_OK')
    print('face_vector', [len(a) for a in bydim], 'matching_pairs',len(pairs),
          'Hasse_incidences',incidents,'integral_factors',dict(factors))
    print('rational_modules H3=1+W22 H4=1+2W22; torsion multiplier2=12(mod23)')

if __name__=='__main__': verify()
