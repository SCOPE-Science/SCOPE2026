#!/usr/bin/env python3
"""Exact enumeration of smooth binary plane quartics with tangent filling.
Enumerates projective orbits, tangent and blocking masks, verifies smoothness via Groebner basis.
No external mathematical data inputs.
"""
import itertools,json,collections,functools
from sympy import symbols, groebner, Poly
X,Y,Z=symbols('X Y Z')
exps=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
assert len(exps)==15
vars=(X,Y,Z)
points=tuple(range(1,8))
xyz=lambda p: tuple((p>>i)&1 for i in range(3))
dot=lambda p,l:(p & l).bit_count()%2
linepts={l:sum(1<<(p-1) for p in points if dot(l,p)==0) for l in points}
bitpar=lambda n:n.bit_count()&1
valmask=[]; gradmasks=[]
for p in points:
 v=xyz(p); valmask.append(sum((1<<i) for i,(a,b,c) in enumerate(exps) if (not a or v[0]) and (not b or v[1]) and (not c or v[2])))
 gs=[]
 for j in range(3):
  gs.append(sum((1<<i) for i,ee in enumerate(exps) if ee[j]%2 and all((not ee[k] + (0 if k!=j else -1)) or v[k] for k in range(3))))
 gradmasks.append(tuple(gs))
def profile(mask):
 Q=[]; tang=[]
 for t,p in enumerate(points):
  if not bitpar(mask&valmask[t]):
   Q.append(p)
   g=sum((bitpar(mask&gradmasks[t][j])<<j) for j in range(3))
   if not g: return {'rational_singular':True}
   tang.append(g)
 loc=0
 for t in tang: loc|=linepts[t]
 return {'rational_singular':False,'N':len(Q),'tangent_count':len(set(tang)), 'tangent_filling':loc==127, 'missing_count':7-loc.bit_count(), 'blocking': all(any(dot(l,p)==0 for p in Q) for l in points), 'tangent_mask':sum(1<<(t-1) for t in set(tang)), 'point_mask':sum(1<<(p-1) for p in Q)}
def galois_matrices():
 result=[]
 for rows in itertools.product(points,repeat=3):
  ax,ay,az=rows
  # rank 3 iff XOR span size 8
  if len({0,ax,ay,az,ax^ay,ax^az,ay^az,ax^ay^az})==8: result.append(rows)
 assert len(result)==168
 return result
def poly_mul(P,Q):
 R=set()
 for a in P:
  for b in Q:
   c=tuple(a[i]+b[i] for i in range(3))
   if c in R:R.remove(c)
   else:R.add(c)
 return R
def action_matrix(rows):
 linear=[set((tuple(1 if j==k else 0 for j in range(3))) for k in range(3) if rows[i]>>k&1) for i in range(3)]
 aa=[{(0,0,0)} for _ in range(3)]
 powers=[[{(0,0,0)}] for _ in range(3)]
 for i in range(3):
  for j in range(4):powers[i].append(poly_mul(powers[i][-1],linear[i]))
 out=[]
 for e in exps:
  terms=poly_mul(poly_mul(powers[0][e[0]],powers[1][e[1]]),powers[2][e[2]])
  out.append(sum((1<<exps.index(m)) for m in terms))
 return out
transforms=[action_matrix(rows) for rows in galois_matrices()]
def transform_mask(mask, trans):
 m=0
 while mask:
  bit=mask&-mask;m^=trans[bit.bit_length()-1];mask^=bit
 return m
def polynomial(mask):
 return sum((X**a*Y**b*Z**c for i,(a,b,c) in enumerate(exps) if mask>>i&1),0)
def geometrically_smooth(mask):
 P=polynomial(mask)
 tests=[]
 for V in (X,Y,Z):
  pp=P.subs(V,1)
  other=[v for v in vars if v!=V]
  derivs=[pp.diff(v) for v in other]
  G=groebner([pp,*derivs],*other,order='lex',modulus=2)
  tests.append(len(G.polys)==1 and G.polys[0].is_one)
 return all(tests)
def main():
 visited=set(); rec=[]; n=0; count_smooth=0
 for mask in range(1,1<<15):
  if mask in visited: continue
  orb={transform_mask(mask,t) for t in transforms}
  visited.update(orb)
  assert mask==min(orb)
  p=profile(mask); smooth=geometrically_smooth(mask) if not p.get('rational_singular') else False
  p.update({'mask':mask,'orbit_size':len(orb),'geometric_smooth':smooth})
  rec.append(p)
  if smooth: count_smooth+=len(orb)
  if len(rec)%50==0:print('orbits',len(rec),'visited',len(visited),flush=True)
 assert len(visited)==32767
 all_smooth=[r for r in rec if r['geometric_smooth']]
 cand=[r for r in all_smooth if r['tangent_filling']]
 print('all_orbits',len(rec),'smooth_orbits',len(all_smooth),'smooth_eq',count_smooth,'tangent_filling_orbits',len(cand),'tangent_filling_eq',sum(r['orbit_size'] for r in cand))
 print('distribution',(sorted(collections.Counter((r['N'],r['tangent_count'],r['blocking']) for r in cand for _ in range(r['orbit_size'])).items())))
 print('candidate_orbits',[(r['mask'],r['orbit_size'],r['N'],r['tangent_count'],r['blocking']) for r in cand])
 print('all_rational_tangent_filling',sum(r['orbit_size'] for r in rec if r.get('tangent_filling') and not r.get('rational_singular')))
 with open('tangent_quartics_result.json','w') as f:json.dump({'exponents':exps,'orbits':rec},f,indent=2)
if __name__=='__main__':main()
