#!/usr/bin/env python3
"""Exact coefficient-space and projective-orbit census over F2.

Binary Macaulay elimination tests *geometric* smoothness, not just rational
singularity. No external packages are required.
"""
from collections import Counter

def mons(n,d):
 if n==1:return [(d,)]
 return [(a,)+b for a in range(d,-1,-1) for b in mons(n-1,d-a)]
M3=mons(3,3);M2=mons(3,2);M4=mons(3,4)
M43=mons(4,3);M42=mons(4,2);M45=mons(4,5)

def rankbin(rows):
 B={}
 for z in rows:
  while z:
   k=z.bit_length()-1
   if k in B:z ^=B[k]
   else:B[k]=z;break
 return len(B)

def smooth_ternary(F):
 deriv=[]
 for j in range(3):
  z={tuple(a):1 for k,a in enumerate(M3) if (F>>k)&1 and a[j]%2}
  z2={tuple(t-1 if i==j else t for i,t in enumerate(a)):1 for a in z}
  deriv.append(z2)
 idx={a:i for i,a in enumerate(M4)}
 rows=[]
 for D in deriv:
  for m in M2:
   row=0
   for v in D:
    s=tuple(i+j for i,j in zip(v,m));row^=1<<idx[s]
   rows.append(row)
 return rankbin(rows)==15

def smooth_quaternary(F):
 deriv=[]
 for j in range(4):
  z={tuple(a):1 for k,a in enumerate(M43) if (F>>k)&1 and a[j]%2}
  z2={tuple(t-1 if i==j else t for i,t in enumerate(a)):1 for a in z}
  deriv.append(z2)
 idx={a:i for i,a in enumerate(M45)}
 rows=[]
 for D in deriv:
  for m in M43:
   row=0
   for v in D:
    s=tuple(i+j for i,j in zip(v,m));row^=1<<idx[s]
   rows.append(row)
 return rankbin(rows)==56

# choose kernel basis by bit lex
planes=[]
for normal in range(1,16):
 V=[a for a in range(1,16) if (a&normal).bit_count()%2==0]
 basis=[];span={0}
 for v in V:
  if v not in span:
   basis.append(v);span|={s^v for s in list(span)}
  if len(basis)==3:break
 assert len(basis)==3
 planes.append(tuple(basis))

# restriction: each x_j linear form in u/v/w, powers product
# poly ints representing monomial masks in 3 variables
def mul2(A,B):
 out={}
 for a in A:
  for b in B:
   c=tuple(i+j for i,j in zip(a,b));out[c]=out.get(c,0)^1
 return {k for k,v in out.items() if v}
remainder=[]
for basis in planes:
 v=[]
 for j in range(4):
  v.append({tuple(1 if i==r else 0 for i in range(3)) for r in range(3) if (basis[r]>>j)&1})
 res=[]
 for m in M43:
  p={(0,0,0)}
  for j,k in enumerate(m):
   for _ in range(k):p=mul2(p,v[j])
  mask=0
  for a in p:mask^=1<<M3.index(a)
  res.append(mask)
 remainder.append(res)

SM={x for x in range(1,1024) if smooth_ternary(x)}

def sections(F):
 out=[]
 for r in remainder:
  z=0; bits=F
  while bits:
   lsb=bits&-bits; k=lsb.bit_length()-1
   z^=r[k];bits^=lsb
  out.append(z)
 return out

def transform_table(A):
 imgs=[]
 for a in M43:
  p={(0,0,0,0)}
  for j,k in enumerate(a):
   for _ in range(k):p=mul2(p,A[j])
  mask=0
  for b in p:mask^=1<<M43.index(b)
  imgs.append(mask)
 lo=[0]*1024;hi=[0]*1024
 for x in range(1,1024):
  b=x&-x;k=b.bit_length()-1
  lo[x]=lo[x^b]^imgs[k]
  hi[x]=hi[x^b]^imgs[k+10]
 return lo,hi

I=[{tuple(int(i==j) for i in range(4))} for j in range(4)]
swap=I.copy(); swap[0],swap[1]=swap[1],swap[0]
cycle=[I[(j+1)%4] for j in range(4)]
trans=[s.copy() for s in I];trans[0]=I[0]|I[1]

def rational_points(F):
    count=0
    for point in range(1,16):
        z=0
        for i,a in enumerate(M43):
            if F & (1<<i) and all(not a[j] or point & (1<<j) for j in range(4)):
                z ^= 1
        count += not z
    return count

def compute():
    tables=[transform_table(A) for A in (swap,cycle,trans)]
    visited=bytearray(1<<20)
    records=[]
    for F in range(1,1<<20):
        if visited[F]:continue
        queue=[F];visited[F]=1
        n=0
        while n<len(queue):
            q=queue[n];n+=1
            for lo,hi in tables:
                value=lo[q&1023]^hi[q>>10]
                if not visited[value]:
                    visited[value]=1;queue.append(value)
        smooth=smooth_quaternary(F)
        rows=(F,len(queue),int(smooth),sum(z in SM for z in sections(F)) if smooth else -1,rational_points(F) if smooth else -1)
        records.append(rows)
    return records

if __name__=='__main__':
    import json,sys
    from collections import Counter
    records=compute()
    assert len(records)==141
    assert sum(r[1] for r in records)==(1<<20)-1
    smooth=[r for r in records if r[2]]
    assert len(smooth)==36 and sum(r[1] for r in smooth)==322560
    assert len(SM)==336 and len(planes)==15
    histogram={i:sum(r[1] for r in smooth if r[3]==i) for i in range(16)}
    assert histogram=={0:1708,1:0,2:0,3:0,4:11340,5:0,6:68320,7:10080,8:94500,9:60480,10:64512,11:10080,12:1540,13:0,14:0,15:0}
    assert [(r[0],r[1]) for r in smooth if r[3]==0]==[(10760,28),(10792,1680)]
    assert all((r[3]==0)==(r[4]>=13) for r in smooth)
    with open('orbit_representatives.tsv','w',encoding='utf8',newline='\n') as f:
        f.write('mask\torbit_size\tsmooth\tsmooth_sections\trational_points\n')
        for r in records:f.write('\t'.join(map(str,r))+'\n')
    result={'total_equations':1048575,'projective_classes':141,'smooth_equations':322560,'smooth_classes':36,
       'smooth_ternary_cubics':336,'hyperplanes':15,'smooth_section_histogram':histogram,
       'orbit_histogram':dict(sorted(Counter(r[3] for r in smooth).items())),
       'no_smooth_section_representatives':[{'mask':r[0],'orbit_size':r[1],'rational_points':r[4]} for r in smooth if r[3]==0]}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
