"""Independent direct function census and explicit source/target symmetry quotient."""
from itertools import product,permutations
from collections import Counter
from s5_orbit_burnside import partitions,frame,auts

def count_direct(src,dst):
 A=frame(src);B=frame(dst);n=sum(src);m=sum(dst)
 target_blocks={y:j for j,b in enumerate(B) for y in b}
 source_profiles=set()
 for f in product(range(m),repeat=n):
  if len(set(f))<m:continue
  key=[]
  for a in A:
   j=target_blocks[f[a[0]]]
   if any(target_blocks[f[x]]!=j for x in a):break
   if {f[x] for x in a}!=set(B[j]):break
   key.append((len(a),j,tuple(f.count(y) if False else sum(f[x]==y for x in a) for y in B[j])))
  else:source_profiles.add(tuple(sorted(key)))
 target_aut=[(h,idx) for h,idx in auts(B)]
 orbits=set()
 for prof in source_profiles:
  reps=[]
  for h,idx in target_aut:
   transformed=[]
   for a,j,counts in prof:
    now={h[y]:c for y,c in zip(B[j],counts)}
    jj=idx[j]
    transformed.append((a,jj,tuple(now[y] for y in B[jj])))
   reps.append(tuple(sorted(transformed)))
  orbits.add(min(reps))
 return len(orbits)

if __name__=='__main__':
 cases=0
 for n in range(1,7):
  for src in partitions(n):
   for m in range(1,min(n,4)+1):
    for dst in partitions(m):
     from s5_orbit_burnside import orbits_burnside
     a=orbits_burnside(src,dst);b=count_direct(src,dst)
     assert a==b,(src,dst,a,b)
     cases+=1
 print('ALL PASS',cases,'source/target frame pairs, all functions checked up to six source worlds and four target worlds')
