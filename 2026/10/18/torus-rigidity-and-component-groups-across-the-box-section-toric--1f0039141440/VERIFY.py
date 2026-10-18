"""Exact small-parameter corroboration of a face-fan automorphism theorem.
No external packages required; mathematical proof is separate.
"""
from itertools import combinations, permutations, product
from fractions import Fraction
from math import comb,gcd

def vertices(n,a,b):
    d=n+1
    verts=set()
    for k in range(n+1):
        c=k*a-(n-k)*b
        if -a<=c<=b:
            v=(-a,)*k+(b,)*(n-k)+(c,)
            verts.update(permutations(v))
    return tuple(sorted(verts))

def root_test(n,vs,radius=2):
    for zs in product(range(-radius,radius+1),repeat=n):
        if all(z==0 for z in zs):continue
        m=(0,)+zs
        pairings=[sum(x*y for x,y in zip(m,v)) for v in vs]
        if pairings.count(-1)==1 and all(t>=0 for t in pairings if t!=-1):
            raise AssertionError(('unexpected root',n,m,pairings))
        if pairings.count(1)==1 and all(t<=0 for t in pairings if t!=1):
            raise AssertionError(('unexpected opposite root',n,m,pairings))

checked=0; tested=0; triples=[]
for n in range(2,7):
 for b in range(1,4):
  for a in range(b,n*b+1):
   if gcd(a,b)>1:continue
   vs=vertices(n,a,b); N=len(vs)
   assert all(sum(v)==0 for v in vs)
   assert all(gcd(*(abs(x) for x in v))==1 for v in vs)
   ss=sum(x*x for x in vs[0])
   assert all(sum(x*x for x in v)==ss for v in vs)
   assert all(sum(v[i]*v[j] for v in vs)==Fraction(N*ss,n)* (Fraction(n,n+1) if i==j else Fraction(-1,n+1)) for i in range(n+1) for j in range(n+1))
   # For interior at the only equality case n=3 a=b=1, n+1=4.
   if a<n*b:
    assert N>2*n or (n,a,b)==(3,1,1),(n,a,b,N)
   else:
    assert (a,b)==(n,1) and N==n+1
   if n<=4:
    root_test(n,vs,2);tested+=1
   triples.append((n,a,b,N));checked+=1
assert len(vertices(3,1,1))==6
print(f'VERIFY_OK isotropic_orbits={checked} exhaustive_bounded_character_cases={tested} exceptional_oct={len(vertices(3,1,1))} sample={triples[:6]}')
