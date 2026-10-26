"""Reproducibility checks for sharp polygon-boundary affine projection norms.

Requires Python 3, SymPy, and NumPy. Analytical proof is provided in RESULT.md;
finite checks do not certify infinite parameter ranges.
"""
import math
import sympy as sp
import numpy as np

checked = 0

def exact_formula(n):
    h = 2*math.pi/n
    c = 6/(2+math.cos(h))
    j = (n+2)//3
    a = 1+c*math.cos((j-1)*h)
    b = -(1+c*math.cos(j*h))
    assert a>0 and b>0
    return 1 + 2/n*(-(n-2*j+1)+c*math.sin((j-.5)*h)/math.sin(h/2)-a*b/(a+b))

def direct_edge_integrals(n):
    h = 2*math.pi/n
    c = 6/(2+math.cos(h))
    q = [1+c*math.cos(j*h) for j in range(n)]
    total = 0
    for j in range(n):
        x,y = q[j], q[(j+1)%n]
        if x*y>=0:
            total += (abs(x)+abs(y))/2
        else:
            total += (x*x+y*y)/(2*(abs(x)+abs(y)))
    return total/n

for n in range(3,1001):
    j=(n+2)//3
    q=[1+6*math.cos(2*math.pi*k/n)/(2+math.cos(2*math.pi/n)) for k in range(n)]
    assert all(q[k]<0 for k in range(j,n-j+1)), (n,'negative')
    assert all(q[k]>0 for k in list(range(j))+list(range(n-j+1,n))), (n,'positive')
    assert abs(direct_edge_integrals(n)-exact_formula(n))<2e-12,(n,direct_edge_integrals(n),exact_formula(n))
    checked+=3

# Independent moment matrix and kernel evaluation at each vertex for low orders.
for n in range(3,31):
    h=2*math.pi/n
    v=np.array([[math.cos(j*h),math.sin(j*h)] for j in range(n)])
    mat=np.zeros((3,3))
    for j in range(n):
        a=np.r_[1.,v[j]]
        b=np.r_[1.,v[(j+1)%n]]
        mat+=(np.outer(a,a)+np.outer(b,b))/3+(np.outer(a,b)+np.outer(b,a))/6
    mat/=n
    inv=np.linalg.inv(mat)
    assert np.linalg.norm(mat-np.diag([1.,(2+math.cos(h))/6,(2+math.cos(h))/6]))<2e-12
    # Independently compute all vertex-row integrals from Gram inverse.
    vals=[]
    for i in range(n):
        y=np.r_[1.,v[i]]
        tot=0.
        for j in range(n):
            a=float(y@inv@np.r_[1.,v[j]])
            b=float(y@inv@np.r_[1.,v[(j+1)%n]])
            if a*b>=0: tot+=(abs(a)+abs(b))/2
            else:tot+=(a*a+b*b)/(2*(abs(a)+abs(b)))
        vals.append(tot/n)
    assert max(abs(z-exact_formula(n)) for z in vals)<5e-12
    checked+=2

# Exact rational special cases, without floating-point approximation.
for n,expected in [(3,sp.Rational(16,9)),(4,sp.Rational(5,3)),(6,sp.Rational(277,180))]:
    h=2*sp.pi/n
    c=6/(2+sp.cos(h))
    j=(n+2)//3
    a=1+c*sp.cos((j-1)*h)
    b=-(1+c*sp.cos(j*h))
    expr=1+sp.Rational(2,n)*(-(n-2*j+1)+c*sp.sin((sp.Rational(2*j-1,2))*h)/sp.sin(h/2)-a*b/(a+b))
    assert sp.simplify(expr-expected)==0,(n,sp.simplify(expr),expected)
    checked+=1

# Full symbolic cubic expansion in the three congruence classes.
z=sp.symbols('z',positive=True)
d=sp.symbols('d',real=True)
k=6/(2+sp.cos(z))
t=2*sp.pi/3
S=-(2*sp.pi/(3*z)+1-2*d)+k*sp.sin(t+(d-sp.Rational(1,2))*z)/sp.sin(z/2)
a=1+k*sp.cos(t+(d-1)*z)
b=-(1+k*sp.cos(t+d*z))
L=1+z/sp.pi*(S-a*b/(a+b))
base=sp.Rational(1,3)+2*sp.sqrt(3)/sp.pi
expected=base+sp.sqrt(3)*z*z/(6*sp.pi)+d*(2*d-1)*(d-1)*z**3/(6*sp.pi)
for dd in [sp.Integer(0),sp.Rational(2,3),sp.Rational(1,3)]:
    assert sp.simplify(sp.series(L.subs(d,dd)-expected.subs(d,dd),z,0,4).removeO())==0
    checked+=1

# Verify large-n residuals tend to the predicted residue-dependent limits.
coeff=2*math.pi*math.sqrt(3)/3
cubic=8*math.pi*math.pi/81
circle=1/3+2*math.sqrt(3)/math.pi
for r,sgn in [(0,0),(1,-1),(2,1)]:
    for n in [900+r,1800+r,3600+r]:
        scale=n**3*(exact_formula(n)-circle-coeff/n**2)
        assert abs(scale-sgn*cubic)<0.03,(n,scale,sgn*cubic)
        checked+=1

print('PASS',checked,'assertion groups; infinite assertions come from the proof in RESULT.md')
