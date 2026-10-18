#!/usr/bin/env python3
import itertools, math
from collections import Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def run(n,r):
 H=set(range(r)); s=n-r
 vertices=[frozenset(t) for t in itertools.combinations(range(n),r) if set(t)!=H]
 facet_data=[]
 for i in range(n):
  for kind in ('0','1'):
   V=frozenset(j for j,v in enumerate(vertices) if (i in v)==(kind=='1'))
   normal=tuple((1 if t==i else 0)*(1 if kind=='1' else -1) for t in range(n))
   facet_data.append((f'{i}={kind}',V,normal))
 V=frozenset(j for j,v in enumerate(vertices) if len(v&H)==r-1)
 facet_data.append(('H=r-1',V,tuple(int(t in H) for t in range(n))))
 assert len(set(v for _,v,_ in facet_data)) == 2*n+1
 # BFS closure of faces under facet intersections
 faces={frozenset(range(len(vertices)))}
 q=list(faces)
 for u in q:
  for _,v,_ in facet_data:
   w=u&v
   if w and w not in faces:
    faces.add(w);q.append(w)
 singular=[]; by_dim=Counter();faces_sig=[]
 for f in faces:
  basis=vertices[next(iter(f))]
  dim=Matrix([[int(i in vertices[j])-int(i in basis) for i in range(n-1)] for j in list(f)[1:]]).rank() if len(f)>1 else 0
  codim=n-1-dim
  active=[(label,norm) for label,V,norm in facet_data if f<=V]
  rays=[tuple(v[i]-v[-1] for i in range(n-1)) for _,v in active]
  if len(rays)==codim:
   S=smith_normal_form(Matrix(n-1,codim,lambda i,j:rays[j][i]),domain=ZZ) if codim else Matrix([])
   smooth=all(abs(int(S[i,i]))==1 for i in range(codim))
  else:
   smooth=False
  by_dim[(dim,'smooth' if smooth else 'singular')]+=1
  if not smooth:
   singular.append((f,dim,codim,[lab for lab,_ in active]))
   if 'H=r-1' in [lab for lab,_ in active] and dim>0:
    faces_sig.append((dim,len(f),[lab for lab,_ in active]))
 # expected irreducible support components: A_h, B_j and isolated nonadjacent vertices
 Pred=[]
 for h in H:
  v=frozenset(j for j,B in enumerate(vertices) if (B&H)==H-{h})
  Pred.append(v)
 for j in range(r,n):
  v=frozenset(k for k,B in enumerate(vertices) if B-H=={j})
  Pred.append(v)
 for k,B in enumerate(vertices):
  if len(B&H)<=r-2: Pred.append(frozenset({k}))
 unexpected=[(f,d,labs) for f,d,codim,labs in singular if not any(f<=component for component in Pred)]
 missing=[component for component in Pred if component not in set(f for f,*_ in singular)]
 print('n,r',n,r,'verts',len(vertices),'faces',len(faces),'singular',len(singular),'expected components',len(Pred),'by_dim',dict(sorted(by_dim.items())),'unexpected',len(unexpected),'missing',len(missing))
 if unexpected:print('UNEXPECTED',unexpected[:5])
 if missing:print('MISSING',missing[:5])
 assert not unexpected and not missing
 return True
if __name__=='__main__':
 for args in [(6,3),(7,3),(7,4),(8,3),(8,4)]:run(*args)
 print('VERIFY_OK')
