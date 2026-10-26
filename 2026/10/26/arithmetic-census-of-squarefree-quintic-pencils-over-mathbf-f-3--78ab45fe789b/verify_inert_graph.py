from pathlib import Path
"""Independent graph verification from row-reduced pencil catalogue and factorization."""
import sympy as S,collections,json
x=S.Symbol('x'); q3=3

def dec(z):return [(z//(3**i))%3 for i in range(6)]
I=set()
for t in range(1,3**6):
 c=dec(t)
 if next((v for v in c if v),0)!=1 or c[-1]==0:continue
 f=S.Poly(sum(v*x**i for i,v in enumerate(c)),x,modulus=3)
 if f.is_irreducible:I.add(t)
print('irreducible forms',len(I))
assert len(I)==48
adj={x:set() for x in I};l=0
for s in open(Path(__file__).resolve().parent/'pencils.txt'):
 g=set(map(int,s.split()));both=list(g&I)
 assert len(both)<=2
 if len(both)==2:
  a,b=both;adj[a].add(b);adj[b].add(a);l+=1
print('edges',l,'degrees',collections.Counter(map(len,adj.values())))
z=json.load(open(Path(__file__).resolve().parent/'inert_compatibility.json'))
assert sorted([sorted([a,b]) for a in I for b in adj[a] if a<b])==z['edges']
print('all independent edges matched')
