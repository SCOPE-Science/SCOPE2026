#!/usr/bin/env python3
"""Exact finite-model two-round relational-group game computation and partition analysis."""
import itertools, math, collections, json, sys

def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def ctype(p):
 n=len(p);seen=[False]*n;out=[]
 for i in range(n):
  if not seen[i]:
   j=i;k=0
   while not seen[j]:seen[j]=True;k+=1;j=p[j]
   out.append(k)
 return tuple(sorted(out,reverse=True))
def alt_group(n):
 for p in itertools.permutations(range(n)):
  inv=sum(1 for i in range(n) for j in range(i+1,n) if p[i]>p[j])
  if inv%2==0:yield p

def point_signature(x, group, e):
 # Complete atomic diagrams of (x,y) in ternary multiplication language.
 # All equations in e,x,y, including reversed products, are encoded explicitly.
 n=len(e); invx=[0]*n
 for a,b in enumerate(x):invx[b]=a
 invx=tuple(invx);xx=compose(x,x)
 sig=set()
 for y in group:
  yy=compose(y,y)
  xe=x==e; ye=y==e; eq=x==y
  ixy=y==invx
  code=(xe,ye,eq,
     xx==e,xx==x,xx==y,
     yy==e,yy==x,yy==y,
     ixy,ye,xe,ixy,ye,xe)
  sig.add(code)
 return frozenset(sig)

def part(n,lo=1):
 if n==0:
  yield ()
 else:
  for j in range(lo,n+1):
   for t in part(n-j,j):yield (j,)+t

def even_partition(q):return (sum(v-1 for v in q)%2)==0

def order(q):
 a=1
 for x in q:a=math.lcm(a,x)
 return a

def is_square_in_alt(q):
 ctr=collections.Counter(q)
 if any(c%2 for l,c in ctr.items() if l%2==0):return False
 epairs=sum(c//2 for l,c in ctr.items() if l%2==0)
 return epairs%2==0 or any(c>=2 for l,c in ctr.items() if l%2)

def category(q):
 z=order(q)
 if z==1:return 'e'
 if z==2:return 'i+' if is_square_in_alt(q) else 'i-'
 if z==3:
  c=collections.Counter(q)
  return '3+' if (c[3]//2+c[1]//2)>=2 else '3-'
 if z==4:return '4+' if is_square_in_alt(q) else '4-'
 return 'L+' if is_square_in_alt(q) else 'L-'

def perm_from_parts(q):
 n=sum(q);p=list(range(n));j=0
 for k in q:
  for i in range(k):p[j+i]=j+(i+1)%k
  j+=k
 return tuple(p)

def finite(n):
 group=list(alt_group(n));e=tuple(range(n)); d={}
 for x in group:
  q=ctype(x)
  if q not in d:d[q]=x
 square_roots=collections.Counter(compose(y,y) for y in group)
 summary={}
 for q,x in d.items():
  assert (square_roots[x]>0)==is_square_in_alt(q), (n,q,"square criterion")
  if order(q)==3:
   c=collections.Counter(q)
   assert (square_roots[x]>1)==(c[3]//2+c[1]//2>=2),(n,q,"extra-root criterion")
  s=point_signature(x,group,e)
  summary[q]=(category(q),s)
 rev=collections.defaultdict(set)
 for q,(c,s) in summary.items():rev[c].add(s)
 print('n',n,'elements',len(group),'conjugacy_partitions',len(d),'pointed_categories',sorted(rev),'pointed_types',len({v[1] for v in summary.values()}),'category_collisions',[(c,len(s)) for c,s in rev.items() if len(s)>1],flush=True)
 assert all(len(s)==1 for s in rev.values()), 'same abstract category maps to different pointed logical types'
 return set(s for c,s in summary.values()), {c:next(iter(s)) for c,s in rev.items()}

def expected_categories(n):
 a={'e'}
 if n<=7 or n in (9,10):a.add('3-')
 if n>=7:a.add('3+')
 if n>=4:a.add('i-') if n in [4,5] else a.add('i+')
 if n>=5:a.add('L+')
 if n>=6:a.add('4-')
 if n>=7:a.add('L-')
 if n>=10:a.add('4+')
 if n>=12 and n%8 in (4,5):a.add('i-')
 return a

def partcheck(nmax=40):
 signatures={}
 for n in range(3,nmax+1):
  cat={category(q) for q in part(n) if even_partition(q)}
  exp=expected_categories(n)
  if cat!=exp:
   print('CAT_MISMATCH',n, sorted(cat),sorted(exp));raise AssertionError
  signatures[n]=frozenset(cat)
  if n<=25 or n%8==0:print('PART',n,len(cat),','.join(sorted(cat)),flush=True)
 print('SYMBOLIC_CATEGORIES_OK n=3..'+str(nmax),'different=',len(set(signatures.values())))
 return signatures

if __name__=='__main__':
 P=partcheck(40)
 all_s={}
 mapping={}
 for n in range(3,10):
  sig,profile=finite(n)
  all_s[n]=frozenset(sig)
  for c,t in profile.items():
   if n<4: continue
   if c in mapping: assert mapping[c]==t, ('same category changes',n,c)
   else:
    for c0,t0 in mapping.items():
     if t==t0:print('CATEGORY_COLLISION',c,c0,n)
    mapping[c]=t
  assert len(sig)==len(P[n]),(n,len(sig),len(P[n]))
  print('FINITE_CLASS',n,'equiv_prev', [i for i in all_s if i<n and all_s[i]==all_s[n]],flush=True)
 print('DIRECT_ATOMIC_OK dimensions=3..9 model_classes=',len(set(all_s.values())))
 print('POINTED_TEMPLATE_OK',len(mapping),'templates:',','.join(sorted(mapping)))
 print('VERIFY_OK')
