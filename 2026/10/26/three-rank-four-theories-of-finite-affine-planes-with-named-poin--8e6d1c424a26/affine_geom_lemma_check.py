"""Exhaustive checks of finite geometric-diagram extension tables; finite check, not universal proof."""
from affine_sorted_check import plane

def key(t,A,sort):
 # list t length<=3
 d=len(t)
 atoms=(tuple(sort[x] for x in t),tuple((t[i]==t[j],int(t[j] in A[t[i]])) for i in range(d) for j in range(i+1,d)))
 l=[x for x in t if sort[x]==1]
 pts=[x for x in t if sort[x]==0]
 par=tuple(not bool(A[x]&A[y]) for i,x in enumerate(l) for y in l[i+1:] if x!=y)
 col=len(pts)==3 and len(set(pts))==3 and bool(A[pts[0]]&A[pts[1]]&A[pts[2]])
 con=len(l)==3 and len(set(l))==3 and bool(A[l[0]]&A[l[1]]&A[l[2]])
 return (atoms,par,col,con)

def build(q):
 A,S=plane(q);n=len(A)
 keys1={a:key((a,),A,S) for a in range(n)}
 keys2={(a,b):key((a,b),A,S) for a in range(n) for b in range(n)}
 keys3={(a,b,c):key((a,b,c),A,S) for a in range(n) for b in range(n) for c in range(n)}
 E2={}
 for (a,b),k in keys2.items():
  E2.setdefault(k,set()).update(keys3[a,b,x] for x in range(n))
 E3={}
 for (a,b,c),k in keys3.items():
  z=E3.setdefault(k,set())
  for x in range(n):
   if x==a or x==b or x==c:z.add(('equal',next(i for i,v in enumerate((a,b,c)) if v==x)));continue
   z.add((S[x],int(a in A[x])+2*int(b in A[x])+4*int(c in A[x])))
 E1={}
 for a,k in keys1.items():E1.setdefault(k,set()).update(keys2[a,x] for x in range(n))
 return tuple(map(len,(keys1,keys2,keys3,E1,E2,E3))),E1,E2,E3

if __name__=='__main__':
 r4=build(4);r5=build(5)
 for i in (1,2,3):
  a,b=r4[i],r5[i]
  print('stage',i,'states',len(a),len(b),'same',a==b)
  if a!=b:
   print('only4',list(set(a)-set(b))[:4],'only5',list(set(b)-set(a))[:4])
  assert a==b
 print('GEO_EXTENSIONS_MATCH')
