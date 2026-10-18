"""Independent symbolic tangent-section test on each smooth projective orbit."""
import sympy as sp, json,collections,sys
xs=sp.symbols('X0 X1 X2 X3'); s,t,u=sp.symbols('s t u')
exps=[]
for a in range(4):
 for b in range(4-a):
  for c in range(4-a-b):exps.append((a,b,c,3-a-b-c))
mon=[sp.prod(x**e for x,e in zip(xs,k)) for k in exps]
def rank(vecs):
 piv=[]
 for x in vecs:
  v=x
  for p in piv:v=min(v,v^p)
  if v:
   piv.append(v);piv.sort(reverse=True)
 return len(piv)
def vec(x):return {xs[i]: (x>>i)&1 for i in range(4)}
def gradient(F,p):return sum((int(sp.diff(F,x).subs(vec(p)))%2)<<i for i,x in enumerate(xs))
def tensor(F,p,g):
 w=[x for x in range(1,16) if (x&g).bit_count()%2==0]
 b=next(z for z in w if rank([p,z])==2)
 c=next(z for z in w if rank([p,b,z])==3)
 sub={x: ((p>>i&1)*s+(b>>i&1)*t+(c>>i&1)*u) for i,x in enumerate(xs)}
 P=sp.Poly(F.subs(sub, simultaneous=True).expand(),s,t,u,modulus=2)
 A={m: int(k)%2 for m,k in P.terms()}
 if any(a>0 for (a,b,c) in A):return None
 a=A.get((0,3,0),0);b_=A.get((0,2,1),0);c_=A.get((0,1,2),0);d=A.get((0,0,3),0)
 if (a*d+b_*c_)%2==0:return None
 rational_roots=(a==0)+(d==0)+((a+b_+c_+d)%2==0)
 return rational_roots
records=[]
for row in json.load(open(sys.argv[1])):
 if not row['smooth']: continue
 F=sum(mon[i] for i in range(20) if row['mask']>>i&1)
 points=[];types=collections.Counter()
 for p in range(1,16):
  if int(F.subs(vec(p)))%2:continue
  points.append(p)
  g=gradient(F,p)
  assert g!=0
  m=tensor(F,p,g)
  if m is not None:
   assert m in (0,1,3),(row['index'],p,m)
   types[str(m)]+=1
 count=sum(types.values())
 assert count==row['E'],(row,types)
 assert len(points)==row['N']
 records.append({**{k:v for k,v in row.items() if k!='gradients'},'ec_split_types':dict(types),'points':points})
summary=collections.defaultdict(lambda:[0,0])
for row in records:
 key=(row['N'],row['E'],row['ec_split_types'].get('0',0),row['ec_split_types'].get('1',0),row['ec_split_types'].get('3',0))
 summary[key][0]+=row['size'];summary[key][1]+=1
json.dump(records,open(sys.argv[2],'w'),indent=2)
print('checked classes',len(records))
print('JOINT',sorted([(k,v)for k,v in summary.items()]))
print('rational counts by types', {str(k):sum(r['size']*r['ec_split_types'].get(str(k),0) for r in records) for k in (0,1,3)})
