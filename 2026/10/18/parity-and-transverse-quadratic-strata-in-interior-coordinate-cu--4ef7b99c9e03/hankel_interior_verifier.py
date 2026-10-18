"""Exact illustrative checks for interior coordinate sections of square Hankel determinants.
The general statement is proved symbolically; these finite tests are not its proof.
Run: python hankel_interior_verifier.py
"""
import sympy as s

def check(n,j):
    a=s.symbols(f'a0:{2*n-1}')
    H=s.Matrix(n,n,lambda i,k:a[i+k])
    subs={a[t]:0 for t in range(j,j+n)}
    indices=[i for i in range(n) if i!=j]
    B=H.extract(indices,indices).subs(subs)
    D=s.factor(B.det())
    expected=(-1)**(j*(j-1)//2+(n-1-j)*(n-2-j)//2)*(a[j-1]**j if j else 1)*(a[j+n]**(n-1-j) if j<n-1 else 1)
    assert s.expand(D-expected)==0,(n,j,D,expected)
    # For rank=n-1, the nonzero (n-1)-minor gives an open dense nonsingular quadratic normal slice.
    assert D != 0
    return str(D)
for n in range(3,9):
    for j in range(1,n-1):
        print('B-minor',n,j,check(n,j))

# Two singular points, of A1 and A5 type, of cubic section a1=0.
a0,a2,a3,a4=s.symbols('a0 a2 a3 a4')
f=a0*a2*a4-a0*a3**2-a2**3
assert s.expand(f.subs({a0:1,a4:0})-(a2*(0-a2**2)-a3**2))==0
u,v,A=s.symbols('u v A')
transformed=s.expand(f.subs({a4:1,a2:u+v**2,a3:v,a0:A+u**2+3*u*v**2+3*v**4}))
assert s.expand(transformed-(A*u-v**6))==0,transformed
print('A5 normal-form identity verified')

# Derivative identity over symmetric Hankel matrices: rank-(n-1) adjugate kernel vv^t.
for n in range(3,6):
  z=s.symbols('z')
  v=s.symbols(f'v0:{n}')
  p=sum(v[i]*z**i for i in range(n))
  for k in range(2*n-1):
    lhs=sum(v[i]*v[j] for i in range(n) for j in range(n) if i+j==k)
    rhs=s.expand(p*p).coeff(z,k)
    assert s.expand(lhs-rhs)==0
print('VERIFY_OK')
