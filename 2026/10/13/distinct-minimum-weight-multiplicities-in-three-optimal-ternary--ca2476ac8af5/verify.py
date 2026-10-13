from itertools import product
from collections import defaultdict
import sys

def field(m):
 q=3**m
 def enc(v):return sum(x*(3**i) for i,x in enumerate(v))
 def dec(k):return [(k//(3**i))%3 for i in range(m)]
 digit=[dec(k) for k in range(q)]
 plus=[[enc([(a+b)%3 for a,b in zip(digit[x],digit[y])]) for y in range(q)] for x in range(q)]
 neg=[enc([-t%3 for t in v]) for v in digit]
 def times(x,y,poly):
  v=[0]*(2*m-1)
  for i,a in enumerate(digit[x]):
   for j,b in enumerate(digit[y]):v[i+j]=(v[i+j]+a*b)%3
  for i in range(2*m-2,m-1,-1):
   t=v[i]
   for j in range(m):v[i-m+j]=(v[i-m+j]-t*poly[j])%3
  return enc(v[:m])
 for poly in product(range(3),repeat=m):
  if poly[0]==0:continue
  for a in range(3,q):
   pw=[1]
   for j in range(q-1):pw.append(times(pw[-1],a,poly))
   if len(set(pw[:-1]))==q-1 and pw[-1]==1:
    assert (m,poly,a)==(5,(1,0,0,0,2),3)
    print('FIELD_OK',m,poly,a,flush=True)
    return pw[:-1],plus,neg
 raise ValueError('no field')

def spectrum(pw,plus,neg,e):
 n=len(pw); y=[pw[(e*i)%n] for i in range(n)]
 pairs=defaultdict(list)
 for i in range(n):
  for j in range(i+1,n):
   for s,t in product((0,1),repeat=2):
    a=neg[pw[i]] if s else pw[i];b=neg[pw[j]] if t else pw[j]
    c=neg[y[i]] if s else y[i];d=neg[y[j]] if t else y[j]
    pairs[(plus[a][b],plus[c][d])].append((i,j))
 total=0
 for (a,b),z in pairs.items():
  for i,j in z:
   for k,l in pairs.get((neg[a],neg[b]),()):
    if i!=k and i!=l and j!=k and j!=l:total+=1
 assert total%6==0,total
 return total//6

def rank3(rows):
    a=[r[:] for r in rows]
    k=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(k,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        inv=1 if a[k][j]==1 else 2
        a[k]=[(v*inv)%3 for v in a[k]]
        for i in range(len(a)):
            if i!=k and a[i][j]:
                t=a[i][j]
                a[i]=[(u-t*v)%3 for u,v in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

if __name__=='__main__':
    pw,plus,neg=field(5)
    assert len(pw)==242 and len(set(pw))==242 and pw[0]==1
    for e,expected in [(2,24200),(16,33880),(20,43560)]:
        x=[pw[i] for i in range(242)]
        y=[pw[(i*e)%242] for i in range(242)]
        rows=[]
        for k in range(5):
            rows.append([v//(3**k)%3 for v in x])
        for k in range(5):
            rows.append([v//(3**k)%3 for v in y])
        assert rank3(rows)==10
        a4=spectrum(pw,plus,neg,e)
        assert a4==expected,(e,a4)
        print(f'e={e} n=242 k=232 A4={a4} four_supports={a4//2}',flush=True)
    print('VERIFY_OK',flush=True)
