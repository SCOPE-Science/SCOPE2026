#!/usr/bin/env python3
import itertools, json, hashlib, collections, pathlib
N=7
V=1<<N
WORDS=[format(i,f'0{N}b') for i in range(V)]

def descendants_delete_positions(w):
    return frozenset(''.join(w[k] for k in range(N) if k not in (i,j))
                     for i in range(N) for j in range(i+1,N))

def descendants_keep_positions(w):
    return frozenset(''.join(w[k] for k in I)
                     for I in itertools.combinations(range(N),N-2))

D=[]
for w in WORDS:
    a=descendants_delete_positions(w)
    b=descendants_keep_positions(w)
    assert a==b
    D.append(a)

adj=[0]*V
edges=0
for i in range(V):
    for j in range(i+1,V):
        if D[i].isdisjoint(D[j]):
            adj[i]|=1<<j
            adj[j]|=1<<i
            edges+=1

def enumerate_k(k):
    out=[]
    def rec(pref,cands,need):
        if need==0:
            out.append(tuple(pref)); return
        if cands.bit_count()<need: return
        while cands:
            bit=cands & -cands
            v=bit.bit_length()-1
            cands-=bit
            rec(pref+[v],cands & adj[v],need-1)
    rec([], (1<<V)-1, k)
    return out

def exists_k(k):
    def rec(cands,need):
        if need==0:return True
        if cands.bit_count()<need:return False
        while cands:
            bit=cands & -cands
            v=bit.bit_length()-1
            cands-=bit
            if rec(cands & adj[v],need-1):return True
        return False
    return rec((1<<V)-1,k)

maxima=enumerate_k(5)
assert len(maxima)==476
assert not exists_k(6)
assert all(all(D[a].isdisjoint(D[b]) for a,b in itertools.combinations(c,2)) for c in maxima)

mask=V-1
def rev(x):return int(format(x,f'0{N}b')[::-1],2)
def comp(x):return x^mask
def transforms(c):
    return {
        tuple(sorted(c)),
        tuple(sorted(rev(x) for x in c)),
        tuple(sorted(comp(x) for x in c)),
        tuple(sorted(rev(comp(x)) for x in c)),
    }
M=set(maxima)
seen=set(); orbit_sizes=[]
for c in maxima:
    if c in seen:continue
    o=transforms(c)
    assert o <= M
    seen |= o
    orbit_sizes.append(len(o))
assert seen==M
assert collections.Counter(orbit_sizes)=={4:115,2:8}

constants=collections.Counter((0 in c,(V-1) in c) for c in maxima)
assert constants=={(True,False):148,(False,True):148,(False,False):94,(True,True):86}
assert not set.intersection(*(set(c) for c in maxima))
coverage=collections.Counter(len(set().union(*(D[x] for x in c))) for c in maxima)
expected={17:4,19:6,20:12,21:16,22:30,23:48,24:64,25:72,26:80,27:78,28:44,29:16,30:6}
assert dict(sorted(coverage.items()))==expected
maxcov=[c for c in maxima if len(set().union(*(D[x] for x in c)))==30]
assert len(maxcov)==6
seen_cov=set(); cov_orbits=[]
for c in maxcov:
    if c in seen_cov:continue
    o=transforms(c) & set(maxcov)
    seen_cov |= o
    cov_orbits.append(len(o))
assert sorted(cov_orbits)==[2,4]

payload={
  'length':7,
  'deletions':2,
  'vertices':V,
  'compatibility_edges':edges,
  'maximum_size':5,
  'labeled_maxima_count':len(maxima),
  'natural_symmetry_group':['identity','reversal','global_complement','reversal_then_global_complement'],
  'orbit_size_histogram':{'2':8,'4':115},
  'constant_membership':{'both':86,'zero_only':148,'one_only':148,'neither':94},
  'common_intersection':[],
  'coverage_histogram':{str(k):v for k,v in sorted(coverage.items())},
  'maximum_coverage':30,
  'maximum_coverage_codes':6,
  'maximum_coverage_orbit_sizes':[2,4],
  'maxima':[[WORDS[x] for x in c] for c in maxima]
}
raw=(json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n').encode()
path=pathlib.Path(__file__).with_name('census.json')
if path.exists():
    assert path.read_bytes()==raw
else:
    path.write_bytes(raw)
sha=hashlib.sha256(raw).hexdigest()
print(f'VERIFY_OK vertices={V} edges={edges} maximum=5 labeled_maxima=476 orbits=123 orbit_hist=2x8,4x115 neither_constants=94 max_coverage=30 max_coverage_codes=6 max_coverage_orbits=2,4')
print('CENSUS_SHA256='+sha)
