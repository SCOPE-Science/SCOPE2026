"""Exact Frobenius fibre-profile and irreducible-place orbit checks."""
import collections,csv,json
from pathlib import Path
import sympy as sp
import verify_pencils as P
folder=Path(__file__).resolve().parent
x=sp.Symbol('x')
factor_types={}
for q in P.smooth:
    co=P.dec(q)
    f=sp.Poly(sum(a*x**i for i,a in enumerate(co)),x,modulus=3)
    factors=sp.factor_list(f,modulus=3)[1]
    degrees=sorted([ff.degree() for ff,m in factors for _ in range(m)]+([1] if co[-1]==0 else []))
    assert sum(degrees)==5
    factor_types[q]=tuple(degrees)
census=collections.Counter(tuple(sorted(factor_types[q] for q in pencil)) for pencil in P.Q)
assert len(census)==15 and sum(census.values())==1098
rows={}
for row in csv.DictReader((folder/'fiber_profiles.csv').open()):
    profile=tuple(sorted(tuple(map(int,b.split('+'))) for b in row['profile_of_four_fibres'].split(';')))
    rows[profile]=int(row['number_of_pencils'])
assert dict(census)==rows
num_inert=collections.Counter(sum(factor_types[q]==(5,) for q in p) for p in P.Q)
assert num_inert=={0:330,1:576,2:192}
I={q for q in P.smooth if factor_types[q]==(5,)}
assert len(I)==48
G=json.loads((folder/'inert_compatibility.json').read_text())
adj={v:set() for v in I}
for a,b in G['edges']:
    adj[a].add(b);adj[b].add(a)
assert collections.Counter(map(len,adj.values()))=={7:24,9:24}
orph=[];seen=set()
for q in sorted(I):
    if q in seen: continue
    orb={m[q] for m in P.GL}
    assert orb<=I
    orph.append(orb);seen|=orb
assert sorted(map(len,orph))==[24,24]
assert sorted(tuple(sorted(set(len(adj[v]) for v in o))) for o in orph)==[(7,),(9,)]
edge_types=collections.Counter(tuple(sorted((len(adj[a]),len(adj[b])))) for a,b in G['edges'])
assert edge_types=={(7,7):48,(7,9):72,(9,9):72}
print('ALL 15 FIBRE PROFILES AND INERT-PLACE ORBIT CLASSES VERIFIED')
