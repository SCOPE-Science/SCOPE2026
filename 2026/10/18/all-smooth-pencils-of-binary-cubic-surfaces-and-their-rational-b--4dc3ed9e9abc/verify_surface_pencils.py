#!/usr/bin/env python3
"""Independent full Walsh triple-check and rational-base weighted histogram."""
import numpy as np,csv
from pathlib import Path
base=Path(__file__).resolve().parent
s=np.fromfile(base/'cubic_surface_smooth.bin',dtype=np.uint8)
n=len(s);assert n==1<<20
f=s.astype(np.int64)
h=1
while h<n:
 a=f.reshape(-1,2*h);l=a[:,:h].copy();r=a[:,h:].copy();a[:,:h]=l+r;a[:,h:]=l-r;h<<=1
cube_sum=0
for k in range(0,n,128):
 z=f[k:k+128];cube_sum+=int((z*z*z).sum(dtype=np.int64))
assert cube_sum % n==0
triples=cube_sum//n
print('Walsh ordered triples',triples,'pencils',triples//6)
assert triples==30017433600
G=np.flatnonzero(s).astype(np.uint32)
mono=[]
for a in range(4):
 for b in range(4-a):
  for c in range(4-a-b):mono.append((a,b,c,3-a-b-c))
E=[]
for p in range(1,16):
 mask=sum((1<<i) for i,e in enumerate(mono) if all(e[j]==0 or (p>>j)&1 for j in range(4)))
 E.append(mask)
z=np.zeros(len(G),dtype=np.uint16)
for i,form in enumerate(G):
 z[i]=sum((1<<j) for j,mask in enumerate(E) if (int(form)&mask).bit_count()%2==0)
rows=list(csv.DictReader(open(base/'cubic_surface_orbits.tsv'),delimiter='\t'))
pc=np.fromiter((i.bit_count() for i in range(1<<15)),dtype=np.uint8,count=1<<15)
hist=np.zeros(16,dtype=np.int64)
for row in rows:
 rep=int(row['representative']); w=int(row['orbit_size'])
 filt=s[np.bitwise_xor(G,rep)].astype(bool)
 zr=sum((1<<j) for j,mask in enumerate(E) if (rep&mask).bit_count()%2==0)
 vals=pc[np.bitwise_and(z[filt],zr)]
 hist+=np.bincount(vals,minlength=16)*w
print('Ordered histogram',hist.tolist())
expected={0:164589376,1:635685120,2:1171931040,3:1292537400,4:956743200,5:504716688,6:198190720,7:59318280,8:15402240,9:3113600,10:493920,11:148680,12:30240,13:5040,15:56}
assert hist.sum()==triples
assert all(hist[i]==6*expected.get(i,0) for i in range(16))
print('Independent base-point distribution agrees at all 16 values')
