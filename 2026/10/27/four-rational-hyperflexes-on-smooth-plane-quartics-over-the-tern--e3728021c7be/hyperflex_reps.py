import json,itertools,numpy as np
M=json.load(open('hyperflex_flags.json'))['monomials'];flags=json.load(open('hyperflex_flags.json'))['flags'];orbs=json.load(open('hyperflex_orbits.json'))
for o in orbs:
 if o['rep'] not in (83262,78741,78754):continue
 idx=o['rep'];vec=[]
 for _ in M:vec.append(idx%3);idx//=3
 P=set()
 for flag in flags:
  if sum(a*b for a,b in zip(flag['transverse'],vec))%3==0:continue
  if all(sum(a*b for a,b in zip(row,vec))%3==0 for row in flag['rows']):P.add(tuple(flag['P']))
 Q=set()
 for v in itertools.product(range(3),repeat=3):
  if not any(v):continue
  a=next(x for x in v if x)
  v=tuple(x*pow(a,-1,3)%3 for x in v)
  if sum(c*np.prod([pow(v[i],m[i],3) for i in range(3)]) for m,c in zip(M,vec))%3==0:Q.add(v)
 print(o['rep'],'orbit',o['size'],'rational points',len(Q),sorted(Q),'hyperflexes',len(P),sorted(P),'non-hyperflex points',sorted(Q-P))
