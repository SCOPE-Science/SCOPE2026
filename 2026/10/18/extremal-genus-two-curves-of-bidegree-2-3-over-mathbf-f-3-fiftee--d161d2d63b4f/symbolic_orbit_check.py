"""A second implementation of the smoothness test on every orbit representative."""
import csv
import sympy as sp
x=sp.Symbol('x')
rows=list(csv.DictReader(open('orbit_reps.csv',encoding='utf-8')))

def coeff(n): return [(n//(3**i))%3 for i in range(12)]

def branch(n):
 v=coeff(n)
 A=sum(v[i]*x**(3-i) for i in range(4))
 B=sum(v[4+i]*x**(3-i) for i in range(4))
 C=sum(v[8+i]*x**(3-i) for i in range(4))
 return sp.Poly(B**2-4*A*C,x,modulus=3)

sizes=0
for row in rows:
 n=int(row['rep']);f=branch(n)
 # Affine discriminant polynomial; also check the root at infinity separately.
 if sp.degree(sp.gcd(f,f.diff()))!=0:raise AssertionError(('non-squarefree',n))
 p=coeff(n)
 if (p[4]**2-p[0]*p[8])%3==0:
  # at infinity: use leading two homogeneous terms via symbolic f coefficient x^6,x^5
  assert f.nth(6)%3==0 and f.nth(5)%3!=0, n
 sizes+=int(row['orbit_size'])
assert len(rows)==286 and sizes==139392
print('symbolic_smooth_orbit_representatives',len(rows))
print('weighted_smooth_models',sizes)
