#!/usr/bin/env python3
"""Exhaustive finite-field check of smooth genus-one (2,2) divisors and pencils."""
import itertools, collections, json
from pathlib import Path
POLY=0x13

def gf_mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  a<<=1
  if a&16:a^=POLY
  b>>=1
 return r

def gf_pow(a,n):
 r=1
 for _ in range(n):r=gf_mul(r,a)
 return r

Q=[(1,a) for a in range(16)]+[(0,1)]
MON=[(i,j) for i in range(3) for j in range(3)]
T=[]
for x0,x1 in Q:
 for y0,y1 in Q:
  vals=[];dx=[];dy=[]
  X=[gf_mul(gf_pow(x0,2-i),gf_pow(x1,i)) for i in range(3)]
  Y=[gf_mul(gf_pow(y0,2-j),gf_pow(y1,j)) for j in range(3)]
  for i,j in MON:
   vals.append(gf_mul(X[i],Y[j]))
   dx.append(Y[j] if i==1 else 0)
   dy.append(X[i] if j==1 else 0)
  T.append((vals,dx,dy))

def evaluation(vals,a):
 r=0
 for i in range(9):
  if (a>>i)&1:r ^= vals[i]
 return r

def smooth(a):
 for v,dx,dy in T:
  if not evaluation(v,a) and not evaluation(dx,a) and not evaluation(dy,a):return False
 return True
S={a for a in range(1,512) if smooth(a)}
P={tuple(sorted((a,b,a^b))) for a in S for b in S if a<b and a^b in S}
assert len(P)==sum(1 for a in S for b in S if a<b and a^b in S)//3
Z={a:frozenset(k for k,(v,dx,dy) in enumerate(T) if k//17 in (0,1,16) and k%17 in (0,1,16) and not evaluation(v,a)) for a in S}
# separate basepoint count with full explicit affine projective coordinate evaluation
# Our F16 coordinate order: (1,0) index0, (1,1) index1, (0,1) index16
PTS=[(i,j) for i in (0,1,16) for j in (0,1,16)]
zeros={a:frozenset((i,j) for i,j in PTS if evaluation(T[i*17+j][0],a)==0) for a in S}
profile=collections.Counter((tuple(sorted(len(zeros[a]) for a in p)),len(set.intersection(*(set(zeros[a]) for a in p)))) for p in P)
# Independent orbit calculation via a unique finite-field interpolation map at 9 rational grid points.
# Each (2,2) form gives a 3x3 evaluation array; this is bijective in characteristic two.
point_vals={a:sum((1<<i) for i,(u,v) in enumerate(PTS) if evaluation(T[u*17+v][0],a)) for a in range(512)}
assert len(set(point_vals.values()))==512
back={v:k for k,v in point_vals.items()}
perms=list(itertools.permutations(range(3)))
# action on value table by row/col permutations and transpose
TMs=[]
for sig in perms:
 for tau in perms:
  for swap in (False,True):
   def transform(t):
    out=0
    for i in range(3):
     for j in range(3):
      row,col=(j,i) if swap else (i,j)
      if t>>(3*sig[row]+tau[col])&1:out |= 1<<(3*i+j)
    return out
   TMs.append([back[transform(point_vals[a])] for a in range(512)])
assert len({tuple(t) for t in TMs})==72
remaining=set(P);orbit=[]
while remaining:
 rep=min(remaining)
 orb={tuple(sorted(Tm[x] for x in rep)) for Tm in TMs}
 assert orb <=P
 remaining.difference_update(orb)
 orbit.append((rep,len(orb)))

result={'smooth_count':len(S),'pencil_count':len(P),'orbit_count':len(orbit),'orbit_sizes':dict(sorted(collections.Counter(k for rep,k in orbit).items())),'basepoint_counts':dict(sorted(collections.Counter(b for (pr,b),n in profile.items() for _ in range(n)).items())),'profile_by_base':[{'fibre_points':list(pr),'rational_basepoints':b,'pencils':n} for (pr,b),n in sorted(profile.items())], 'orbit_representatives':[{'pencil':list(rep),'size':size,'profile':sorted(len(zeros[a]) for a in rep),'rational_basepoints':len(set.intersection(*(set(zeros[a]) for a in rep)))} for rep,size in sorted(orbit)],'smooth_forms':sorted(S),'pencils':[list(p) for p in sorted(P)]}
if __name__=='__main__':
 print('smooth_sections',len(S))
 print('qualifying_pencils',len(P))
 print('orbits',len(orbit),sorted(collections.Counter(n for p,n in orbit).items()))
 print('basepoint_counts',sorted(collections.Counter(b for (pr,b),n in profile.items() for _ in range(n)).items()))
 for (pr,b),n in sorted(profile.items()): print('fibre_profile',pr,'basepoints',b,'count',n)
 with open(Path(__file__).with_name('pencil_catalogue.json'),'w') as f:json.dump(result,f,indent=2,sort_keys=True)
