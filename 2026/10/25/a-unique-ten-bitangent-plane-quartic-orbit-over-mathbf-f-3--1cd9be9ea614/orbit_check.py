import json,time,itertools,collections
from sympy import symbols,Poly,groebner
J=json.load(open('restriction_data.json'))
mon=list(map(tuple,J['monomials']));monidx={m:i for i,m in enumerate(mon)}
vecs={tuple(map(int,s.split()[0])):int(s.split()[1]) for s in open('high_forms.tsv')}
print('loaded',len(vecs))
G=[((1,1,0),(0,1,0),(0,0,1)),((1,0,0),(0,1,1),(0,0,1)),((1,0,0),(0,1,0),(1,0,1)),((0,1,0),(1,0,0),(0,0,1)),((2,0,0),(0,1,0),(0,0,1))]

def mul(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():
   e=tuple(i[k]+j[k] for k in range(3))
   c[e]=(c.get(e,0)+x*y)%3
 return {k:v for k,v in c.items() if v}

def matrices():
 mats=[]
 for gen in G:
  mat=[[0]*15 for _ in range(15)]
  for c,power in enumerate(mon):
   v={(0,0,0):1}
   for i,a in enumerate(power):
    linear={tuple(1 if j==k else 0 for j in range(3)):gen[i][k] for k in range(3) if gen[i][k]}
    for _ in range(a):v=mul(v,linear)
   for m,z in v.items():mat[monidx[m]][c]=z
  mats.append(mat)
 return mats
M=matrices()

def step(v,mat):
 out=[sum(mat[i][j]*v[j] for j in range(15))%3 for i in range(15)]
 for x in out:
  if x:
   if x==2:out=[2*k%3 for k in out]
   return tuple(out)
 raise Exception('zero')

def allorbits():
 notdone=set(vecs)
 orbits=[]
 while notdone:
  seed=min(notdone)
  O={seed};stack=[seed]
  while stack:
   v=stack.pop()
   for mat in M:
    u=step(v,mat)
    if u not in O:
     O.add(u);stack.append(u)
  assert O<=vecs.keys(),('not full',next(iter(O-vecs.keys())))
  notdone-=O
  orbits.append((seed,len(O),vecs[seed]))
 print('orbits',len(orbits),'sizes',collections.Counter((n,r) for _,n,r in orbits))
 json.dump([{'form':''.join(map(str,seed)),'size':n,'num_bitangents':r} for seed,n,r in orbits],open('orbit_certificate.json','w'),indent=2)
 return orbits

if __name__=='__main__':
 t=time.monotonic();o=allorbits();print('time',time.monotonic()-t)
 x,y,z=symbols('x y z')
 for seed,n,k in sorted(o,key=lambda r:-r[2]):
  f=sum(a*x**i*y**j*z**h for a,(i,j,h) in zip(seed,mon))
  good=True
  for a,b,c in [(x,y,z),(y,x,z),(z,x,y)]:
   ff=Poly(f.subs(a,1),b,c,modulus=3).as_expr() # substitution may simultaneously treat? no variable conflict? x->1 etc ok
   ff1=Poly(ff,b,c,modulus=3);dx=ff1.diff(b).as_expr();dy=ff1.diff(c).as_expr()
   gb=groebner([ff,dx,dy],b,c,order='grevlex',modulus=3)
   if not (len(gb.polys)==1 and gb.polys[0].is_one):good=False;break
  print('r',k,'orbit',n,'smooth',good,'form',str(f))

