#!/usr/bin/env python3
"""Independent bit-mask reconstruction of both deletion-packing inequalities."""
import json, math, pathlib
cert=json.loads(pathlib.Path(__file__).with_name('dual_certificates.json').read_text(encoding='utf-8'))
for m in range(1,7):
 n=2*m; degree=m+1; V=[x for x in range(1<<n) if x.bit_count()==m]
 def word(x,size):return format(x,'0%db'%size)
 def delbits(x,i):
  low=x&((1<<i)-1); high=x>>(i+1)
  return low|(high<<i)
 # Positions in bit encoding are indexed from least significant bit, not string order.
 D={int(y,2):v for y,v in cert[str(m)]['weights'].items()}; scale=cert[str(m)]['scale']
 U=0; sets=[set() for _ in range(degree)]
 for x in V:
  s=sum((k+1)*int(b) for k,b in enumerate(word(x,n)))%degree
  shadows={delbits(x,i) for i in range(n)}
  assert all(v not in sets[s] for v in shadows)
  sets[s].update(shadows)
  assert sum(D.get(z,0) for z in shadows)>=scale
  U+=1
 assert U==math.comb(n,m)
 assert sum(D.values())<(U//degree+1)*scale
 assert U%degree==0
P=json.loads(pathlib.Path(__file__).with_name('primal_gap_m4.json').read_text(encoding='utf-8'))
Q={int(x,2):v for x,v in P['weights'].items()}
assert sum(Q.values())>14*P['scale']
for y in range(1<<7):
    if y.bit_count() not in (3,4):continue
    load=0
    for x,v in Q.items():
        if y in {delbits(x,i) for i in range(8)}:load+=v
    assert load<=P['scale']
print('INDEPENDENT_VERIFY_OK')
