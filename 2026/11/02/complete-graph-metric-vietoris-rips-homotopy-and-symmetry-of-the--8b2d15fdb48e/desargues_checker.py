#!/usr/bin/env python3
"""Standalone exact check of Desargues-graph Rips Morse certificates and characters.
Run: python desargues_checker.py morse_certificate.json
Only the Python 3 standard library is required.
"""
import json, sys, itertools, collections
from itertools import combinations, permutations

V=[(k,tuple(t)) for k in (2,3) for t in combinations(range(5),k)]
assert len(V)==20
label={x:i for i,x in enumerate(V)}
edges=[(i,j) for i,a in enumerate(V) for j,b in enumerate(V) if i<j and ( (len(a[1])==2 and len(b[1])==3 and set(a[1])<set(b[1])) or (len(a[1])==3 and len(b[1])==2 and set(b[1])<set(a[1])))]
assert len(edges)==30
adj=[set() for _ in V]
for i,j in edges:adj[i].add(j);adj[j].add(i)
D=[]
for src in range(20):
 dist={src:0}; q=collections.deque([src])
 while q:
  i=q.popleft()
  for j in adj[i]:
   if j not in dist:dist[j]=dist[i]+1;q.append(j)
 assert len(dist)==20
 D.append([dist[j] for j in range(20)])
assert max(map(max,D))==5
# Degree profile from any fixed vertex: 1,3,6,6,3,1.
assert collections.Counter(D[0])=={0:1,1:3,2:6,3:6,4:3,5:1}

def faces(r):
 nbr=[{j for j in range(i+1,20) if D[i][j]<=r} for i in range(20)]
 out=set()
 def visit(s,candidates):
  for k,i in enumerate(candidates):
   t=s+(i,);out.add(t)
   visit(t,[j for j in candidates[k+1:] if j in nbr[i]])
 visit((),list(range(20)))
 return out

def mask(s):return sum(1<<i for i in s)
def from_mask(m):return tuple(i for i in range(20) if m>>i&1)

def check_morse(r,data):
 F=faces(r); allm={mask(s) for s in F};pairs=data['pairs'];crit=data['critical']
 assert len(pairs)==(len(F)-len(crit))//2
 assert allm==set(crit)|{x for a,b in pairs for x in (a,b)}
 assert len(allm)==len(crit)+2*len(pairs)
 matched={(a,b) for a,b in pairs}
 for a,b in pairs:assert a&b==a and (b^a).bit_count()==1
 # Directed face-poset Hasse diagram: all down-arrows, except reversed matches.
 incoming=collections.Counter();successors=collections.defaultdict(list)
 for t in F:
  big=mask(t)
  if len(t)<2:continue
  for k in range(len(t)):
   small=big^(1<<t[k])
   if (small,big) in matched:src,dst=small,big
   else:src,dst=big,small
   successors[src].append(dst); incoming[dst]+=1
 q=collections.deque(m for m in allm if incoming[m]==0);removed=0
 while q:
  m=q.popleft();removed+=1
  for n in successors[m]:
   incoming[n]-=1
   if incoming[n]==0:q.append(n)
 assert removed==len(F),'Morse matching must be acyclic'
 dims=collections.Counter((x.bit_count()-1) for x in crit)
 print('scale',r,'faces',len(F),'pairs',len(pairs),'critical',dict(dims),'acyclic OK')
 return F

def parsign(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def gmap(p,flip):
 out=[]
 for k,s in V:
  t=set(p[i] for i in s)
  if flip:t=set(range(5))-t
  out.append(label[(len(t),tuple(sorted(t)))])
 return out

def lef(F,gm):
 val=0
 for t in F:
  image=[gm[i] for i in t]
  if sorted(image)==list(t):val+=(-1)**(len(t)-1)*parsign(image)
 return val


def main():
 assert len(sys.argv)==2,'Supply morse_certificate.json'
 with open(sys.argv[1],encoding='utf-8') as fh:cert=json.load(fh)
 assert cert['schema_version']==1
 F1=faces(1); F2=check_morse(2,cert['2']);F3=check_morse(3,cert['3'])
 assert collections.Counter(map(len,F1))=={1:20,2:30}
 assert collections.Counter(map(len,F2))=={1:20,2:90,3:120,4:30}
 assert collections.Counter(map(len,F3))=={1:20,2:150,3:540,4:1000,5:960,6:450,7:80}
 assert collections.Counter(map(int.bit_count,cert['2']['critical']))=={1:1,3:19}
 assert collections.Counter(map(int.bit_count,cert['3']['critical']))=={1:1,4:1}
 # At scale 4 the only excluded edges are the ten complementary pairs.
 missing=[(i,j) for i in range(20) for j in range(i+1,20) if D[i][j]==5]
 assert len(missing)==10 and {i for pair in missing for i in pair}==set(range(20))
 # Hence scale 4 is the boundary of a 10-dimensional crosspolytope: S^9.
 # Scale 5 is the full 19-simplex; scale 0 is 20 isolated points.
 print('r0, r1, r2, r3, r4, r5 homotopy: 20 points; wedge11 S1; wedge19 S2; S3; S9; point')
 # Natural action of S5 x C2: permutations of labels, with central complementation.
 for p in permutations(range(5)):
  e=parsign(p);w=sum(p[i]==i for i in range(5))-1
  p2=[p[p[i]] for i in range(5)];w2=sum(p2[i]==i for i in range(5))-1
  a=(w*w-w2)//2 # wedge^2 standard, six-dimensional [3,1,1]
  b=e*((w*w+w2)//2-1-w) # sign-twisted [3,2], five-dimensional [2,2,1]
  c=e*w # sign-twisted standard, four-dimensional [2,1,1,1]
  induced=[]
  pairs2=list(combinations(range(5),2)); axes={s:i for i,s in enumerate(pairs2)}
  for t in pairs2:induced.append(axes[tuple(sorted(p[i] for i in t))])
  assert parsign(induced)==e
  for flip in (False,True):
   gm=gmap(p,flip)
   for i in range(20):
    for j in range(20):assert D[gm[i]][gm[j]]==D[i][j]
   obs=[-(lef(F1,gm)-1),lef(F2,gm)-1,-(lef(F3,gm)-1)]
   expected=[a+((-1 if flip else 1)*b),b+c+((-1 if flip else 1)*(a+c)),e]
   assert obs==expected,(p,flip,obs,expected)
   # At r=4 central complementation reverses all 10 axes (even parity).
   r4det=parsign(induced)*((-1)**(10*int(flip)))
   assert r4det==e
 print('ALL 240 GROUP ELEMENTS: signed Lefschetz characters and S5 x C2 decomposition OK')
 print('r2: (sign-twisted standard + [2,2,1])^+ plus (wedge2 standard + sign-twisted standard)^-')
 print('r1: (wedge2 standard)^+ plus [2,2,1]^-; r3,r4: sign_S5 x trivial_C2')
 print('DESARGUES_ALL_SCALES_MORSE_AND_240_CHARACTERS_OK')

if __name__=='__main__':main()
