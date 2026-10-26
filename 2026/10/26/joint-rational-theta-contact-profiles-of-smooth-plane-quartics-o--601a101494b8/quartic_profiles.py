import collections, itertools, json
from pathlib import Path
T=[(4,0,0),(3,1,0),(3,0,1),(2,2,0),(2,1,1),(2,0,2),(1,3,0),(1,2,1),(1,1,2),(1,0,3),(0,4,0),(0,3,1),(0,2,2),(0,1,3),(0,0,4)]
D={e:i for i,e in enumerate(T)}
P=[(1,y,z) for y,z in itertools.product(range(2),repeat=2)]+[(0,1,z) for z in range(2)]+[(0,0,1)]
L=[(a,b,c) for a,b,c in P]

def mul(A,B):
 C=collections.defaultdict(int)
 for (i,j,k),a in A.items():
  if a:
   for (u,v,w),b in B.items():
    if b:C[i+u,j+v,k+w]^=1
 return {k:v for k,v in C.items() if v}

def polyprod(A,exponent):
 B={(0,0,0):1}
 for _ in range(exponent): B=mul(B,A)
 return B

def image_cols(cols):
 xs=[{(1 if i==0 else 0,1 if i==1 else 0,1 if i==2 else 0):x for i,x in enumerate(col) if x} for col in cols]
 basis=[]
 for a,b,c in T:
  H=mul(mul(polyprod(xs[0],a),polyprod(xs[1],b)),polyprod(xs[2],c))
  v=0
  for exp in H:v^=1<<D[exp]
  basis.append(v)
 return basis

def mapform(m,basis):
 r=0
 while m:
  low=m&-m;r^=basis[low.bit_length()-1];m^=low
 return r

def apply_point(M,p):
 return tuple(sum(M[i][j]*p[j] for j in range(3))%2 for i in range(3))

def det(M):
 x=M;return (x[0][0]*(x[1][1]*x[2][2]-x[1][2]*x[2][1])-x[0][1]*(x[1][0]*x[2][2]-x[1][2]*x[2][0])+x[0][2]*(x[1][0]*x[2][1]-x[1][1]*x[2][0]))%2

def mono_eval(t,p):
 return int(all(not e or x for e,x in zip(t,p)))
point_basis=[sum(1<<i for i,t in enumerate(T) if mono_eval(t,p)) for p in P]

# three variable linear changes describing line restrictions via (s,t)
def lines_data():
 ret=[]
 for lam in L:
  span=[p for p in P if (sum(a*b for a,b in zip(lam,p))%2)==0]
  A,B=span[0],span[1]
  assert len(span)==3 and tuple(a^b for a,b in zip(A,B))==span[2]
  rows=[0]*5
  for i,(a,b,c) in enumerate(T):
   H=mul(mul(polyprod({(1,0,0):A[0],(0,1,0):B[0]},a),polyprod({(1,0,0):A[1],(0,1,0):B[1]},b)),polyprod({(1,0,0):A[2],(0,1,0):B[2]},c))
   for (s,t,_),v in H.items():
    if v:rows[t]|=1<<i
  ret.append({'line':lam,'points':span,'rows':rows})
 return ret

lines=lines_data()
forms=[int(x) for x in Path(__file__).resolve().with_name('smooth_quartics.txt').read_text().splitlines()]
profiles=collections.Counter(); perN=collections.Counter(); per_t=collections.Counter(); configs=collections.Counter(); formprofiles={}
for mask in forms:
 N=sum((mask&row).bit_count()%2==0 for row in point_basis)
 countcontact=[0,0,0];line_indices=[];types=[]
 for li,line in enumerate(lines):
  R=line['rows']; v=[(mask&row).bit_count()%2 for row in R]
  if v[1] or v[3]:continue
  assert v[0] or v[2] or v[4], (mask,li)
  q0,q1,q2=v[0],v[2],v[4]
  n=(q0==0)+(q2==0)+(q0^q1^q2==0)
  assert n in (0,1,2)
  countcontact[n]+=1;line_indices.append(li);types.append(n)
 prof=(N,*countcontact)
 profiles[prof]+=1;perN[N]+=1;per_t[len(line_indices)]+=1
 if len(line_indices)==3:
  # is concurrent iff 3 lines meet rational same point
  concur=int(any(all(sum(a*b for a,b in zip(lines[i]['line'],p))%2==0 for i in line_indices) for p in P))
  configs[(N,concur)]+=1
 formprofiles[mask]={'N':N,'contact':countcontact,'lines':line_indices,'types':types}

# projective action on plane quartics
G=[]
for vals in itertools.product(range(2),repeat=9):
 M=[vals[3*i:3*i+3] for i in range(3)]
 if det(M):
  cols=[tuple(M[i][j] for i in range(3)) for j in range(3)]
  G.append((M,image_cols(cols)))
assert len(G)==168
formset=set(forms);seen=set();orbits=[]
for f in forms:
 if f in seen:continue
 orbit={mapform(f,b) for M,b in G}
 assert orbit<=formset
 seen|=orbit
 orbits.append({'rep':f,'size':len(orbit),'N':formprofiles[f]['N'],'contact':formprofiles[f]['contact'],'lines':formprofiles[f]['lines']})
assert len(seen)==len(formset)
results={'smooth_count':len(forms),'orbit_count':len(orbits),'N_counts':dict(sorted(perN.items())),'bitangent_count':dict(sorted(per_t.items())),'profiles':{'/'.join(map(str,k)):v for k,v in sorted(profiles.items())},'three_lines_concurrency':{'/'.join(map(str,k)):v for k,v in sorted(configs.items())},'orbits':orbits,'terms':T,'point_order':P,'lines':lines}
print('SMOOTH',len(forms),'ORBITS',len(orbits)); print('N distribution',perN)
print('RATIONAL BITANGENTS',per_t)
print('CONTACT PROFILES',len(profiles),profiles)
print('3-LINE CONCURRENCY',configs)
Path(__file__).resolve().with_name('quartic_profiles.json').write_text(json.dumps(results,indent=2))
