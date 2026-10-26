import itertools,collections,time
from sympy import symbols,Poly,groebner
T=time.monotonic()
E=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
EM={e:i for i,e in enumerate(E)}
P=[p for p in range(1,8)]
def parity(x):return x.bit_count()%2
# rows are bit vectors, 3x3 invertible
MATS=[]
for rows in itertools.product(P,repeat=3):
 a,b,c=rows
 if len({parity(a&p) for p in P})==0: continue
 images={((parity(a&p))|(parity(b&p)<<1)|(parity(c&p)<<2)) for p in P}
 if len(images)==7:MATS.append(rows)
assert len(MATS)==168
ID=(1,2,4)

def lin_pow(row,k):
 d={(0,0,0):1}
 for _ in range(k):
  nd=collections.defaultdict(int)
  for e,v in d.items():
   for a in range(3):
    if (row>>a)&1:
     t=list(e);t[a]+=1;nd[tuple(t)]^=v
  d={e:v for e,v in nd.items() if v}
 return d

def transform_columns(rows):
 powtab=[[lin_pow(rows[a],k) for k in range(5)] for a in range(3)]
 cols=[]
 for e in E:
  cur={(0,0,0):1}
  for a,k in enumerate(e):
   nd=collections.defaultdict(int)
   for v in cur:
    for w in powtab[a][k]:nd[tuple(v[b]+w[b] for b in range(3))]^=1
   cur={v for v,c in nd.items() if c}
  cols.append(sum(1<<EM[v] for v in cur))
 return cols
CM={g:transform_columns(g) for g in MATS}
def apply(cols,m):
 v=0
 while m:
  z=m&(-m);v^=cols[z.bit_length()-1];m-=z
 return v
# orbit decomposition
seen={0};ors=[];by_orbit={}
for mask in range(1,1<<15):
 if mask in seen:continue
 orb={apply(CM[g],mask) for g in MATS}
 assert mask in orb
 for m in orb:by_orbit[m]=len(ors)
 seen|=orb;ors.append((mask,tuple(sorted(orb))))
print('orbits',len(ors),'sizes',collections.Counter(len(o) for _,o in ors),'time',round(time.monotonic()-T,1),flush=True)
x,y,z=symbols('x y z')
def smooth(m):
 terms=sum((x**a*y**b*z**c for j,(a,b,c) in enumerate(E) if (m>>j)&1),start=0)
 for primary,a,b in [(x,y,z),(y,x,z),(z,x,y)]:
  f=terms.subs(primary,1,simultaneous=True)
  f=Poly(f,a,b,modulus=2).as_expr()
  G=groebner([f,f.diff(a),f.diff(b)],a,b,order='grevlex',modulus=2)
  if not(G.is_zero_dimensional or len(G.polys)==1 and G.polys[0].as_expr()==1):
   # Positive-dimensional also singular: ignore true is_zero_dimensional possibly proper nontrivial ideal, need definitive [1]
   return False
  if not(len(G.polys)==1 and G.polys[0].as_expr()==1): return False
 return True

def image(g,p):
 return sum(parity(g[a]&p)<<a for a in range(3))
LINES=[m for m in P]
def on_line(line,p):return parity(line&p)==0
PENCIL={p:tuple(line for line in LINES if on_line(line,p)) for p in P}
# central line stabilizer check for each g
CENTERS={}
for g in MATS:
 if g==ID:continue
 centers=[]
 for p in P:
  if image(g,p)!=p:continue
  if all({image(g,q) for q in P if on_line(line,q)}=={q for q in P if on_line(line,q)} for line in PENCIL[p]):centers.append(p)
 if centers:CENTERS[g]=centers
print('center matrices',len(CENTERS), 'centers_counts',collections.Counter(c for v in CENTERS.values() for c in v),flush=True)

smooth_orbits=[];cnt=collections.Counter();rows=[]
for oi,(rep,orbit) in enumerate(ors):
 if not smooth(rep):continue
 smooth_orbits.append(oi)
 stab=[g for g in MATS if apply(CM[g],rep)==rep]
 ps={p for g in stab if g in CENTERS for p in CENTERS[g]}
 on={p for p in ps if (sum(1 for i,e in enumerate(E) if rep>>i&1 and all((not n or (p>>a)&1) for a,n in enumerate(e))))%2==0}
 # evaluate quartic at binary p: F(p) = parity of monomial hits
 N=sum((sum(((rep>>j)&1) for j,e in enumerate(E) if all((not n or ((p>>a)&1)) for a,n in enumerate(e)))%2)==0 for p in P)
 rows.append({'orbit_index':oi,'mask':rep,'size':len(orbit),'stab':len(stab),'P':len(ps),'Pin':len(on),'Pout':len(ps)-len(on),'N':N,'ps':sorted(ps)})
 cnt[(len(ps),len(on),N)]+=1
print('smooth orbits',len(rows),'smooth equations',sum(r['size'] for r in rows),'time',round(time.monotonic()-T,1),flush=True)
print('nonzero points:')
for r in rows:
 if r['P']>0:print(r)
print('summary',sorted(cnt.items()),flush=True)
import json
open('quasi_census.json','w').write(json.dumps({'rows':rows,'counter':{str(k):v for k,v in cnt.items()},'monomials':E},indent=2)+'\n')
