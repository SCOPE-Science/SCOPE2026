import sympy as s, time,collections,json,sys
from pathlib import Path
xs=s.symbols('x0 x1 x2 x3'); exps=[]
for a in range(4):
 for b in range(4-a):
  for c in range(4-a-b):
   d=3-a-b-c;exps.append((a,b,c,d))
mons=[s.prod(x**e for x,e in zip(xs,exp)) for exp in exps]
rows=[]; t=time.time()
for n,line in enumerate(open(sys.argv[1])):
 idx,f,weight,N,E=map(int,line.split());
 F=sum(mon for i,mon in enumerate(mons) if f>>i&1)
 dF=[s.diff(F,x) for x in xs]
 sing=False
 for k,x in enumerate(xs):
  inds=[q for q in xs if q!=x]
  polys=[p.subs(x,1) for p in dF]
  G=s.groebner(polys,*inds,order='grevlex',modulus=2)
  if G.polys != [s.Poly(1,*inds,modulus=2)]:
   sing=True; break
 rows.append(dict(index=idx,mask=f,size=weight,N=N,E=E,smooth=not sing,gradients=[str(z) for z in dF]))
 if idx%20==0: print('processed',idx,'elapsed',round(time.time()-t,1),flush=True)
json.dump(rows,open(sys.argv[2],'w'),indent=2)
print('DONE',len(rows), 'smooth classes',sum(r['smooth'] for r in rows),'smooth eq',sum(r['size'] for r in rows if r['smooth']))
tab=collections.defaultdict(lambda:[0,0]);
for r in rows:
 if r['smooth']: tab[(r['E'],r['N'])][0]+=r['size'];tab[(r['E'],r['N'])][1]+=1
print('JOINT',sorted(tab.items()))
print('MARG', {k:sum(v[0] for (e,N),v in tab.items() if e==k) for k in sorted(set(k[0] for k in tab))})
print('END TIME',time.time()-t)
