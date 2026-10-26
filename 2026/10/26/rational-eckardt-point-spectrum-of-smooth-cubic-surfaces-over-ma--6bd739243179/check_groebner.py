import sympy as S,csv,itertools,time
X=S.symbols('x0:4')
M=[e for e in itertools.product(range(4),repeat=4) if sum(e)==3]
rows=list(csv.DictReader(open('orbit_cubic.tsv'),delimiter='\t'))
start=time.time();good=0;bad=[]
for r in rows:
 if r['geometric_smooth']!='1':continue
 f=int(r['representative']);pol=sum(S.prod(X[j]**v for j,v in enumerate(e)) for i,e in enumerate(M) if f>>i&1)
 deriv=[S.diff(pol,x) for x in X]
 for i in range(4):
  g=S.groebner(deriv+[X[i]-1],*X,modulus=2,order='grevlex')
  if list(g.polys)!=[S.Poly(1,*X,modulus=2)]:bad.append((f,i,str(g)))
 good+=1
print('verified representatives',good,'failure count',len(bad),'elapsed',time.time()-start)
if bad: print(bad[:3]);raise SystemExit(1)
