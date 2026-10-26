"""Independent affine Groebner verification for six-point blocking quartics over F3.
Creates its own 9-dimensional coefficient kernel rather than using the other verifier.
"""
import sympy as sp
from itertools import product,combinations
from collections import Counter
x,y=sp.symbols('x y')
points=sorted({tuple(z*pow(next(w for w in p if w),-1,3)%3 for z in p)
               for p in product(range(3),repeat=3) if any(p)})
lines={sum(1<<i for i,p in enumerate(points) if sum(a[j]*p[j] for j in range(3))%3==0)
       for a in points}
assert len(lines)==13
B6=[]
for t in combinations(range(13),6):
 s=sum(1<<i for i in t)
 if all(s&L for L in lines) and all(s&L!=L for L in lines):B6.append(s)
assert len(B6)==234
for n in range(1,6):
 for t in combinations(range(13),n):
  s=sum(1<<i for i in t)
  assert not (all(s&L for L in lines) and all(s&L!=L for L in lines))
mask=311
E=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
A=[[int(pow(p[0],e[0])*pow(p[1],e[1])*pow(p[2],e[2])%3) for e in E]
   for i,p in enumerate(points) if mask>>i&1]
# Independent row-reduced null basis.
R=[row[:] for row in A];piv=[];r=0
for j in range(15):
 k=next((k for k in range(r,len(R)) if R[k][j]),None)
 if k is None:continue
 R[r],R[k]=R[k],R[r]
 R[r]=[(v*pow(R[r][j],-1,3))%3 for v in R[r]]
 for i in range(len(R)):
  if i!=r:
   f=R[i][j];R[i]=[(R[i][t]-f*R[r][t])%3 for t in range(15)]
 piv.append(j);r+=1
 if r==len(R):break
free=[j for j in range(15) if j not in piv]
assert len(free)==9
basis=[]
for j in free:
 b=[0]*15;b[j]=1
 for i,v in enumerate(piv):b[v]=(-R[i][j])%3
 basis.append(b)
ev=[[int(pow(p[0],e[0])*pow(p[1],e[1])*pow(p[2],e[2])%3) for e in E] for p in points]
# Each chart is (X_i=1, remaining 2 variables x,y).
monomial_chart=[]
for i in range(3):
 keep=[j for j in range(3) if j!=i]
 monomial_chart.append([x**e[keep[0]]*y**e[keep[1]] for e in E])
# Derivative chart arrays: 3 charts x 3 partials x 15 forms.
deriv=[]
for i in range(3):
 keep=[j for j in range(3) if j!=i]
 deriv.append([[e[k]* x**(e[keep[0]]-int(k==keep[0])) * y**(e[keep[1]]-int(k==keep[1])) if e[k] else sp.S.Zero
                for e in E] for k in range(3)])
# Derivative exponents can be negative with zero multiplier? e[k] nonzero ensures exponents >=1 for var k, so safe.
counts=Counter()
projective=0
reps=[]
for code in range(1,3**9):
 q=code;digits=[]
 for _ in range(9):q,d=divmod(q,3);digits.append(d)
 # representative up to scalar: first nonzero base-3 digit must equal 1
 if next(z for z in digits if z)!=1:continue
 coeff=tuple(sum(digits[t]*basis[t][j] for t in range(9))%3 for j in range(15))
 zeros=sum(1<<i for i,evalrow in enumerate(ev) if sum(coeff[j]*evalrow[j] for j in range(15))%3==0)
 if zeros!=mask:continue
 projective+=1
 chart_ok=True
 for i in range(3):
  G=[]
  for k in range(3):
   f=sum((coeff[j]*deriv[i][k][j] for j in range(15)), sp.S.Zero)
   G.append(f)
  gb=sp.groebner(G,x,y,modulus=3)
  if not gb.is_zero_dimensional and not gb.contains(sp.S.One):
   chart_ok=False;break
  # A unit ideal iff groebner basis contains 1. More robust direct check:
  if not (len(gb.polys)==1 and gb.polys[0].total_degree()==0):
   chart_ok=False;break
 if chart_ok:counts['smooth']+=1;reps.append(coeff)
 else:counts['singular']+=1
print('projective quartics rational-set-exact=',projective)
print('geometrically smooth=',counts['smooth'],'singular=',counts['singular'])
assert projective==567 and counts['smooth']==222 and counts['singular']==345
with open('verification/groebner_smooth_coefficients.txt','w') as out:
 for c in sorted(reps):out.write(''.join(map(str,c))+'\n')
