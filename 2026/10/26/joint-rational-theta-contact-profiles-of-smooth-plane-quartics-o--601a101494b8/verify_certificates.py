import collections
from pathlib import Path
TERMS=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
# Must match canonical order in the profile and enumerator.
assert TERMS==[(4,0,0),(3,1,0),(3,0,1),(2,2,0),(2,1,1),(2,0,2),(1,3,0),(1,2,1),(1,1,2),(1,0,3),(0,4,0),(0,3,1),(0,2,2),(0,1,3),(0,0,4)]
POLY={1:0b11,2:0b111,3:0b1011,4:0b10011}

def multiply(x,y,k):
 out=0;mod=POLY[k]
 while y:
  if y%2:out^=x
  y>>=1;x<<=1
  if x&(1<<k):x^=mod
 return out

def powg(a,d,k):
 o=1
 for _ in range(d):o=multiply(o,a,k)
 return o

def calc(mask,k,x,y,z):
 vals=[0]*4
 for i,(a,b,c) in enumerate(TERMS):
  if not(mask>>i&1):continue
  f=lambda A,B,C:multiply(multiply(powg(x,A,k),powg(y,B,k),k),powg(z,C,k),k)
  vals[0]^=f(a,b,c)
  if a%2:vals[1]^=f(a-1,b,c)
  if b%2:vals[2]^=f(a,b-1,c)
  if c%2:vals[3]^=f(a,b,c-1)
 return vals

cert=Path(__file__).with_name('nonsmooth_certificates.tsv')
smooth=Path(__file__).with_name('smooth_quartics.txt')
witnesses={}
for line in cert.read_text().splitlines():
 m,k,x,y,z=map(int,line.split())
 assert 1<=k<=4 and 0<=x<(1<<k) and 0<=y<(1<<k) and 0<=z<(1<<k)
 assert x==1 or x==0 and y==1 or x==y==0 and z==1
 assert m not in witnesses
 assert calc(m,k,x,y,z)==[0,0,0,0],(m,k,x,y,z,calc(m,k,x,y,z))
 witnesses[m]=k
smoothset={int(a) for a in smooth.read_text().splitlines()}
assert 0 not in smoothset and len(smoothset)==10920
assert set(witnesses).isdisjoint(smoothset)
assert set(witnesses)|smoothset==set(range(1,1<<15))
print('PASS 21847 certified geometrically singular quartics; 10920 remaining masks; independent GF evaluation')
print('witness extension degree counts',dict(sorted(collections.Counter(witnesses.values()).items())))
