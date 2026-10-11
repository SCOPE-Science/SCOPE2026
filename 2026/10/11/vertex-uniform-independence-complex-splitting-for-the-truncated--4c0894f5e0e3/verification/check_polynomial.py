#!/usr/bin/env python3
"""Independent polynomial recurrence using LEFT Cayley multiplication (value swaps)."""
from itertools import permutations
from functools import lru_cache
P=list(permutations((1,2,3,4)))
assert len(P)==24
pos={v:i for i,v in enumerate(P)}
near=[0]*24
for i,p in enumerate(P):
 for t in (1,2,3):
  q=tuple(t+1 if x==t else (t if x==t+1 else x) for x in p)
  near[i]|=1<<pos[q]
assert sum(a.bit_count() for a in near)==72
@lru_cache(None)
def poly(active):
 if active==0:return (1,)
 bits=[j for j in range(24) if active>>j&1]
 v=max(bits,key=lambda j:(active&near[j]).bit_count())
 a=poly(active&~(1<<v));b=poly(active&~(1<<v)&~near[v])
 out=[0]*max(len(a),len(b)+1)
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i+1]+=x
 return tuple(out)
full=(1<<24)-1
expected={
 'full': (1,24,240,1304,4218,8400,10356,7824,3555,960,168,24,2),
 'delete_vertex':(1,23,220,1141,3515,6650,7767,5542,2370,600,98,13,1),
 'delete_closed_neighborhood':(1,20,163,703,1750,2589,2282,1185,360,70,11,1),
}
# Left Cayley graph is canonically isomorphic to right Cayley graph under inversion.
for p in P:
 inv=tuple(p.index(x)+1 for x in (1,2,3,4))
 for k in (0,1,2):
  q=list(p);q[k],q[k+1]=q[k+1],q[k]
  iq=tuple(q.index(x)+1 for x in (1,2,3,4))
  assert (near[pos[inv]]>>pos[iq])&1
for name,allowed in [('full',full),('delete_vertex',full&~1),('delete_closed_neighborhood',full&~(1|near[0]))]:
 co=poly(allowed)
 assert co==expected[name],(name,co,expected[name])
 print(name, 'independence_polynomial=',co, 'evaluation_at_minus_one=',sum((-1)**i*x for i,x in enumerate(co)))
print('INDEPENDENT_POLYNOMIAL_OK memo_states=',poly.cache_info().currsize)
