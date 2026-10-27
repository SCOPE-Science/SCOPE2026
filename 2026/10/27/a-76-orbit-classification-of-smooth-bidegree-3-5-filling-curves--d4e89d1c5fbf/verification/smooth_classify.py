import sympy as s, json,time
from collections import Counter
D=json.load(open('orbits.json'));A,B=D['A'],D['B'];terms=D['terms']
u,v=s.symbols('u v')
def equation(mask,xchart,ychart):
 expr=0
 for k,(i,j) in enumerate(terms):
  if mask>>k&1:
   expr+=u**(i if xchart==0 else A-i)*v**(j if ychart==0 else B-j)
 return s.Poly(expr,u,v,modulus=2)
def smooth(mask):
 for xc,yc in [(0,0),(0,1),(1,0),(1,1)]:
  f=equation(mask,xc,yc)
  G=s.groebner([f,f.diff(u),f.diff(v)],u,v,order='grevlex',modulus=2)
  if len(G.polys)==1 and G.polys[0].is_one:continue
  return False,(xc,yc),[str(q.as_expr()) for q in G.polys]
 return True,None,None
start=time.monotonic();count=0;res=[]
for n,(size,mask) in enumerate(D['orbits']):
 ok,chart,basis=smooth(mask)
 res.append({'size':size,'mask':mask,'smooth':ok,'singular_chart':chart,'singular_basis':basis if not ok else None})
 if ok:count+=size
 if n%25==0:print('progress',n,'elapsed',round(time.monotonic()-start,2),'smooth_count',count,flush=True)
D['geom_smooth_orbits']=res;D['geom_smooth_total']=count;D['geom_smooth_orbit_count']=sum(r['smooth'] for r in res)
print('FINISHED',count,D['geom_smooth_orbit_count'],'time',round(time.monotonic()-start,3),'orbit_sizes',dict(Counter(q['size'] for q in res if q['smooth'])),flush=True)
json.dump(D,open('classification.json','w'))
