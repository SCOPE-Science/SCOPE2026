import verify_tangent_census as z
import itertools,collections,time
P=z.P; L=z.L; matchings=z.matching; comp=z.comp
pt_idx={p:i for i,p in enumerate(P)}
# generator symplectic transvections on F2^4: T_v(x)=x+B(x,v)v, v any nonzero
G=[]
for v in P:
 pv=[]
 for p in P:
  B=sum(p[j]*[v[1],v[0],v[3],v[2]][j] for j in range(4))%2
  pv.append(pt_idx[tuple(p[j]^ (B*v[j]) for j in range(4))])
 lv=[]
 for lm,i in sorted(L.items(),key=lambda x:x[1]):
  newlm=sum(1<<pv[j] for j in z.line_to_points[lm]);lv.append(L[newlm])
 G.append((pv,lv))

def action(t,G):
 pv,lv=G
 out=[0]*15
 for i,l in enumerate(t):out[pv[i]]=lv[l]
 return tuple(out)
remaining=set(matchings);orbits=[]
while remaining:
 r=min(remaining);orb={r};queue=[r]
 while queue:
  t=queue.pop()
  for g in G:
   tt=action(t,g)
   if tt not in orb:orb.add(tt);queue.append(tt)
 assert orb<=set(matchings)
 remaining-=orb;orbits.append((r,len(orb)))
print('orbits',len(orbits),[(leno, len([m for m in matchings if m==r])) for r,leno in orbits],flush=True)
for rep,size in orbits:
 gray=next(k for k,t in z.examples if t==list(rep)) if any(t==list(rep) for k,t in z.examples) else None
 # recompute direct gray by scanning all codes
 h=[0]*15;prev=0
 for n in range(1<<16):
  gr=n^(n>>1)
  if n:
   bit=(gr^prev).bit_length()-1
   for i in range(15):h[i]^=z.per_pt_grad[bit][i]
  prev=gr
  if tuple(z.tanmap[i,h[i]] for i in range(15))==rep:gray=gr;break
 poly=0
 for i,m in enumerate(comp):
  if gray>>i&1:poly^=m
 print('REP size',size,'gray',gray,'poly_int',poly,'monomials',[z.M[i] for i in range(35) if poly>>i&1],flush=True)
