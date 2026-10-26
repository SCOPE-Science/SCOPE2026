import itertools, collections, csv
MON=[e for e in itertools.product(range(4),repeat=4) if sum(e)==3]
TRI=[e for e in itertools.product(range(3+1),repeat=3) if sum(e)==3]

def form_bits(f):return [MON[i] for i in range(20) if f>>i&1]
def val_monom(ex,p):return int(all((p>>i&1) for i,v in enumerate(ex) if v))
def val(f,p):return sum(val_monom(e,p) for e in form_bits(f))%2
def gradient(f,p):
 return sum(((sum((e[i]%2)*val_monom(tuple(e[k]-(i==k) for k in range(4)),p) for e in form_bits(f))%2)<<i) for i in range(4))
def dot(a,b):return (a&b).bit_count()%2

def expand_product(ex,basis):
 cur={(0,0,0):1}
 for i,mult in enumerate(ex):
  for _ in range(mult):
   new={}
   for tup,v in cur.items():
    for k in range(3):
     if (basis[k]>>i)&1:
      tt=tuple(tup[j]+(j==k) for j in range(3))
      new[tt]=new.get(tt,0)^v
   cur={key:v for key,v in new.items() if v}
 return cur

def tangent_form(f,basis):
 c={}
 for ex in form_bits(f):
  for tup,v in expand_product(ex,basis).items():c[tup]=c.get(tup,0)^v
 return {k:v for k,v in c.items() if v}

def classify_eckardt(f,p):
 g=gradient(f,p);assert g and not dot(g,p)
 hp=[q for q in range(1,16) if not dot(g,q)]
 for a,b in itertools.combinations(hp,2):
  if len({0,p,a,b,p^a,p^b,a^b,p^a^b})==8:break
 else:raise ValueError('no tangent basis')
 t=tangent_form(f,[p,a,b])
 if any(key[0]>0 for key in t):return None
 # coefficients u^3,u^2v,uv^2,v^3
 A=t.get((0,3,0),0);B=t.get((0,2,1),0);C=t.get((0,1,2),0);D=t.get((0,0,3),0)
 assert A*D ^ B*C,('not squarefree',f,p,t)
 rat_roots=sum((sum(coeff*pow(u,e[0])*pow(v,e[1]) for coeff,e in [(A,(3,0)),(B,(2,1)),(C,(1,2)),(D,(0,3))])%2==0) for u,v in [(1,0),(0,1),(1,1)])
 return rat_roots
rows=list(csv.DictReader(open('orbit_cubic.tsv'),delimiter='\t'))
output=[];agg=collections.defaultdict(lambda:[0,0])
for r in rows:
 if r['geometric_smooth']!='1':continue
 f=int(r['representative']); counts=collections.Counter()
 for p in range(1,16):
  if val(f,p)==0:
   e=classify_eckardt(f,p)
   if e is not None:counts[e]+=1
 assert sum(counts.values())<=int(r['points'])
 key=(int(r['points']),int(r['rational_lines']),counts[0],counts[1],counts[3]);weight=int(r['orbit_size']);agg[key][0]+=1;agg[key][1]+=weight
 output.append({'f':f,'orbit':weight,'points':int(r['points']),'lines':int(r['rational_lines']),'E0':counts[0],'E1':counts[1],'E3':counts[3]})
with open('eckardt_orbits.tsv','w') as ff:
 d=csv.DictWriter(ff,fieldnames=output[0].keys(),delimiter='\t');d.writeheader();d.writerows(output)
print('total orbits',len(output),'total equations',sum(r['orbit'] for r in output))
for k,v in sorted(agg.items()):print(k,v)
print('marginal', dict(sorted(collections.Counter({i:sum(r['orbit'] for r in output if r['E0']+r['E1']+r['E3']==i) for i in set(r['E0']+r['E1']+r['E3'] for r in output)}).items())))
