#!/usr/bin/env python3
"""Independent finite verification for the regular-nine-tournament neighborhood classification.
Usage: python3 verify.py, from the same directory as rt9_source.txt and certificate.json.
All mathematics checked over integers/rationals or exact mod-two arithmetic.
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'rt9_source.txt'
CERT=ROOT/'certificate.json'
EXPECT=[(1,0),(1,0),(2,0),(4,0),(1,0),(1,0),(1,0),(0,1),(0,3),(1,1),(3,0),(7,0),(2,0),(1,0),(1,0)]

def tournament_out(s):
 assert len(s)==36 and set(s)<={'0','1'}
 out=[0]*9
 t=0
 for i in range(9):
  for j in range(i+1,9):
   if s[t]=='1':out[i]|=1<<j
   else:out[j]|=1<<i
   t+=1
 assert t==36 and all(x.bit_count()==4 for x in out)
 return out


def graph_signature(out):
    allbits=(1<<9)-1
    sig=[]
    for i in range(9):
        plus=out[i]
        minus=(allbits^(1<<i))^plus
        sig.append((tuple(sorted((out[j]&plus).bit_count() for j in range(9) if plus>>j&1)),
                    tuple(sorted((out[j]&minus).bit_count() for j in range(9) if minus>>j&1))))
    return sig

def isomorphic(out1,out2):
    a=graph_signature(out1); b=graph_signature(out2)
    if sorted(a)!=sorted(b):return False
    cands={i:[j for j in range(9) if a[i]==b[j]] for i in range(9)}
    order=sorted(range(9),key=lambda i:(len(cands[i]),i))
    f={}
    def search(k,used):
        if k==9:return True
        i=order[k]
        for j in cands[i]:
            if used>>j&1:continue
            if any(((out1[i]>>ii)&1)!=((out2[j]>>jj)&1) for ii,jj in f.items()):continue
            f[i]=j
            if search(k+1,used|(1<<j)):return True
            del f[i]
        return False
    return search(0,0)

def get_faces(out):
 fs=set()
 for mask in out:
  x=mask
  while x:
   fs.add(x);x=(x-1)&mask
 assert all(any((a&mask)==a for mask in out) for a in fs)
 return fs

def covers(fs):
 edges=[]
 for b in fs:
  for i in range(9):
   if b>>i&1:
    a=b^(1<<i)
    if a in fs:edges.append((a,b))
 return edges

def check_matching(fs,pairs,critical):
 assert isinstance(pairs,list) and isinstance(critical,list)
 allset=set(); matched=set()
 for a,b in pairs:
  assert a in fs and b in fs and a.bit_count()+1==b.bit_count()
  assert (a&b)==a
  assert a not in allset and b not in allset
  allset.add(a);allset.add(b);matched.add((a,b))
 for c in critical:
  assert c in fs and c not in allset
  allset.add(c)
 assert allset==fs and len(set(critical))==len(critical)
 h=covers(fs)
 neighbors={v:[] for v in fs}
 indeg={v:0 for v in fs}
 for a,b in h:
  # Reversed matched edges, all other Hasse edges downward.
  x,y=(a,b) if (a,b) in matched else (b,a)
  neighbors[x].append(y);indeg[y]+=1
 queue=deque([v for v in fs if indeg[v]==0]);processed=0
 while queue:
  v=queue.popleft(); processed+=1
  for w in neighbors[v]:
   indeg[w]-=1
   if indeg[w]==0:queue.append(w)
 assert processed==len(fs),f'Directed Morse cycle detected: {processed}/{len(fs)}'
 return len(h)

def boundary(d,face_layers):
 # Integral simplicial boundary: rows in degree d-1 and columns in d.
 columns=[]
 low_index={m:j for j,m in enumerate(face_layers[d-1])}
 for face in face_layers[d]:
  vals={}
  verts=[i for i in range(9) if face>>i&1]
  for j,i in enumerate(verts):
   vals[low_index[face^(1<<i)]]= -1 if j%2 else 1
  columns.append(vals)
 return columns,len(face_layers[d-1])

def rank_mod2(cols):
 basis={}
 for col in cols:
  x=sum(1<<r for r in col)
  while x:
   pivot=x.bit_length()-1
   if pivot in basis:x^=basis[pivot]
   else:basis[pivot]=x;break
 return len(basis)

def rank_Q(cols):
 basis={}
 for col in cols:
  v={i:Fraction(a) for i,a in col.items() if a}
  while v:
   p=min(v)
   if p not in basis:
    a=v[p]
    basis[p]={i:val/a for i,val in v.items()}
    break
   mul=v[p]
   for i,val in basis[p].items():
    z=v.get(i,Fraction(0))-mul*val
    if z:v[i]=z
    else:v.pop(i,None)
 return len(basis)

def homology(fs):
 layers={d:sorted(x for x in fs if x.bit_count()==d+1) for d in range(4)}
 bdr={d:boundary(d,layers)[0] for d in range(1,4)}
 ranks={d:rank_mod2(bdr[d]) for d in bdr}
 br=[len(layers[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(4)]
 qranks={d:rank_Q(bdr[d]) for d in bdr}
 qbr=[len(layers[d])-qranks.get(d,0)-qranks.get(d+1,0) for d in range(4)]
 assert br==qbr
 assert br[0]==1
 return tuple(br[1:3]),tuple(len(layers[i]) for i in range(4)),ranks,qranks

def main():
 lines=SOURCE.read_text(encoding='ascii').splitlines()
 cert=json.loads(CERT.read_text(encoding='utf-8'))
 assert cert['schema_version']==1 and cert['n']==9
 assert len(lines)==len(cert['records'])==15 and len(set(lines))==15
 assert [r['index'] for r in cert['records']]==list(range(15))
 # Separate pairwise isomorphism check; exhaustive coverage uses the cited McKay catalogue.
 decoded=[tournament_out(s) for s in lines]
 for i in range(15):
  for j in range(i):
   assert not isomorphic(decoded[i],decoded[j])
 for i,(s,record) in enumerate(zip(lines,cert['records'])):
  outs=tournament_out(s)
  assert outs==record['facets']
  fs=get_faces(outs)
  assert len(fs)==record['face_count']
  hasse=check_matching(fs,record['pairs'],record['critical'])
  crit=Counter(x.bit_count()-1 for x in record['critical'])
  assert crit[0]==1 and crit[1]==EXPECT[i][0] and crit[2]==EXPECT[i][1] and crit[3]==0
  (bh1,bh2),fvec,rank2,qrank=homology(fs)
  assert (bh1,bh2)==EXPECT[i]
  assert rank2==qrank
  # The Morse CW dimension is at most two; one vertex and exactly
  # beta1 1-cells, beta2 2-cells. Both never exceed one simultaneously.
  # In the lone mixed case the exact rational H_2=1 forces its
  # 1-by-1 Morse boundary to vanish over Z, so a degree-zero map S1->S1.
  assert not (crit[1]>1 and crit[2]>0)
  print(f'{i:02} faces={len(fs):3} f={fvec} Hasse={hasse:3} pairs={len(record["pairs"]):2} critical={dict(sorted(crit.items()))} betti=(1,{bh1},{bh2},0)')
 print('PASS: all 15 source orientations pairwise nonisomorphic by direct backtracking. Catalogue completeness is externally sourced.')
 print('PASS: 15 regular nine-vertex tournaments; all integral sphere-wedge types via acyclic Morse certificates and exact rational boundary ranks.')
 print('PASS: independent simplicial boundary computation over GF(2) and exact Q, with no field-rank discrepancy.')
 print('CERTIFICATE: REGULAR_NINE_TOURNAMENT_NEIGHBORHOOD_FULL_HOMOTOPY_CENSUS_OK')
if __name__=='__main__':main()
