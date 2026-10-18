import sympy as s,time,json,itertools,collections
x,y=s.symbols('x y'); t=time.time()
charts=[(i,j) for i in (0,1) for j in (0,1)]
exprs=[]
for ii,jj in charts:
 exprs.append([x**(2-a if ii else a)*y**(2-b if jj else b) for a in range(3) for b in range(3)])
# Coeff ordering a=0..2 b=0..2 : U^a V^(2-a) S^b T^(2-b)
def is_smooth(mask):
 for ms in exprs:
  f=s.Add(*(ms[k] for k in range(9) if (mask>>k)&1))
  fx=s.diff(f,x);fy=s.diff(f,y)
  gb=s.groebner([f,fx,fy],x,y,order='lex',modulus=2)
  if not (len(gb.polys)==1 and gb.polys[0].as_expr()==1):return False
 return True
smooth=[i for i in range(1,512) if is_smooth(i)];assert len(smooth)==144,len(smooth)
sm=set(smooth);pens=sorted({tuple(sorted((a,b,a^b))) for a,b in itertools.combinations(smooth,2) if a^b in sm});print('SMOOTH',len(smooth),'PENCILS',len(pens),'TIME',round(time.time()-t,3),flush=True)
# Automorphism on (U,V) substitution U->V,V->U or U->U+V,V->V. two factors+ factor swap.
def side_action(t):
 # t one of 3x3 matrix over F2 on Sym^2 binary forms
 forms=[]
 for e in range(3):
  if t=='swap': q=(y**e*x**(2-e)).expand()
  else: q=((x+y)**e*y**(2-e)).expand()
  out=0
  for k in range(3):
   if s.Poly(q,x,y).coeff_monomial(x**k*y**(2-k))%2:out|=1<<k
  forms.append(out)
 return forms
sw=side_action('swap'); sh=side_action('shear')
def act(mask,side,method):
 if method=='factor_swap':
  return sum(1<<(a*3+b) for a in range(3) for b in range(3) if mask&(1<<(b*3+a)))
 im=sw if method=='swap' else sh
 out=0
 for a in range(3):
  for b in range(3):
   if mask>>(a*3+b)&1:
    t=im[a if side==0 else b]
    for k in range(3):
     if t>>k&1:
      z=(k*3+b) if side==0 else (a*3+k)
      out^=1<<z
 return out

G=[lambda m:act(m,0,'swap'),lambda m:act(m,0,'shear'),lambda m:act(m,1,'swap'),lambda m:act(m,1,'shear'),lambda m:act(m,0,'factor_swap')]
for m in smooth:
 for g in G:assert g(m) in sm,('bad smooth action',m,g(m))
seen=set();rows=[]
for pen in pens:
 if pen in seen:continue
 orbit={pen};q=[pen]
 while q:
  a=q.pop()
  for g in G:
   b=tuple(sorted(map(g,a)))
   if b not in orbit:orbit.add(b);q.append(b)
 for item in orbit:assert item in pens
 seen.update(orbit);rows.append({'rep':pen,'size':len(orbit)})
assert len(seen)==len(pens)
print('ORBITS',len(rows),'sizes',collections.Counter(r['size'] for r in rows),'sum',sum(r['size'] for r in rows),flush=True)
with open('pencil_census.json','w') as f:json.dump({'smooth':smooth,'pencils':pens,'orbits':rows},f)
