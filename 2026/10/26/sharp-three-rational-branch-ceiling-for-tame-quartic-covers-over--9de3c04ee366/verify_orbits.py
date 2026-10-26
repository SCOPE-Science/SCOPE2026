"""Projective equivalence verification for the equality-stratum degree-four maps."""
import itertools
from verify_fibers import accepted

mats=[]
for m in itertools.product(range(3),repeat=4):
 a,b,c,d=m
 if (a*d-b*c)%3 and next(i for i in m if i)==1:mats.append(m)
assert len(mats)==24

def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]=(c[i+j]+u*v)%3
 return c

def src_form(v,m):
 a,b,c,d=m;z=[0]*5
 for i,vi in enumerate(v):
  if not vi:continue
  h=[1]
  for j in range(4-i):h=mul(h,[b,a])
  for j in range(i):h=mul(h,[d,c])
  for j,t in enumerate(h):z[4-j]=(z[4-j]+vi*t)%3
 return tuple(z)

def canon(a,b):
 n=next(t for t in a+b if t)
 return (a,b) if n==1 else (tuple(2*i%3 for i in a),tuple(2*i%3 for i in b))

def orbit(rep):
 A,B=rep;o=set()
 for s in mats:
  a=src_form(A,s);b=src_form(B,s)
  for u,v,w,t in mats:
   c=tuple((u*aa+v*bb)%3 for aa,bb in zip(a,b))
   d=tuple((w*aa+t*bb)%3 for aa,bb in zip(a,b))
   o.add(canon(c,d))
 return o

reps=[
 ('dihedral A',((0,0,0,0,1),(1,0,1,0,0)),288),
 ('dihedral B',((0,0,0,0,1),(1,0,2,0,0)),288),
 ('Klein A',((0,0,1,0,0),(1,0,0,0,1)),72),
 ('Klein B',((0,1,0,2,0),(1,0,2,0,1)),24),
 ('symmetric',((0,0,1,0,1),(1,1,0,0,1)),192),
]
all_orbits=set()
for name,rep,expected in reps:
 o=orbit(rep)
 assert len(o)==expected, (name,len(o),expected)
 assert not o&all_orbits
 assert o<=accepted.keys()
 all_orbits|=o
 print(name,'orbit',len(o),'stabilizer',576//len(o))
assert all_orbits==accepted.keys()
print('EXACT FIVE ORBITS',len(all_orbits))
