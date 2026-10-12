"""Verify representative codes with direct Hamming distances and composition."""
from itertools import product
v = [x for x in product(range(3),repeat=3) if any(x) and x[next(i for i,a in enumerate(x) if a)]==1]
assert len(v)==13
lines = [tuple(p for p,x in enumerate(v) if sum(v[l][k]*x[k] for k in range(3))%3==0) for l in range(13)]
assert all(len(x)==4 for x in lines)
count=0
seen=set()
for row in open('orbit_representatives.txt',encoding='utf-8'):
 parts=row.split()
 assert parts[0]=='class' and parts[6]=='colors_hex'
 bits=bytes.fromhex(parts[-1]); assert len(bits)==13
 code=[]
 for l,z in enumerate(bits):
  c=[0]*13
  for j,p in enumerate(lines[l]):c[p]=1+((z>>(2*j))&3)
  assert sorted(c)==[0]*9+[1,2,3,4]
  code.append(tuple(c))
 assert len(set(code))==13
 assert all(sum(a!=b for a,b in zip(x,y))>=7 for i,x in enumerate(code) for y in code[i+1:])
 assert parts[-1] not in seen
 seen.add(parts[-1]);count+=1
assert count==20
print('VERIFY_CODES_OK representatives=20 words_per_code=13 min_distance_at_least=7')
