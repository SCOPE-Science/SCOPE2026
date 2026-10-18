"""Reproduce exact covariance and turning-point certificates for a three-habitat linear model.
Run: python verify.py (requires SymPy). This is finite symbolic verification; the proof of the two-habitat universal assertion is in RESULT.md.
"""
import sympy as sp

d=sp.symbols('d',nonnegative=True)
L=sp.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
K=sp.diag(2,1,3)+d*L
Q=sp.diag(8,1,1)
u=sp.symbols('u0:6')
C=sp.Matrix([[u[0],u[1],u[2]],[u[1],u[3],u[4]],[u[2],u[4],u[5]]])
sol=sp.solve(list(K*C+C*K-Q),u,dict=True)
assert len(sol)==1
C=C.subs(sol[0])
assert all(sp.cancel(z)==0 for z in K*C+C*K-Q)
V=sp.factor(sp.together((sp.ones(1,3)*C*sp.ones(3,1))[0]))
N=180*d**5+1824*d**4+6021*d**3+8209*d**2+4764*d+960
H=(6*d*d+17*d+6)*(12*d**3+80*d*d+129*d+60)
assert sp.cancel(V-N/H)==0
P=(8208*d**8+72864*d**7+229944*d**6+245880*d**5-172079*d**4
    -584580*d**3-427134*d*d-87120*d+7200)
assert sp.cancel(sp.diff(V,d)+P/H**2)==0
assert P.subs(d,0)>0 and P.subs(d,sp.Rational(1,10))<0 and P.subs(d,3)>0
assert [sp.sign(c) for c in sp.Poly(P,d).all_coeffs()]==[1,1,1,1,-1,-1,-1,-1,1]
print('three-habitat covariance identity, derivative, sign witnesses and Descartes signs: PASS')
print('local minimum/maximum candidates:',[float(sp.re(z)) for z in sp.nroots(P,maxsteps=400) if abs(float(sp.im(z)))<1e-12 and float(sp.re(z))>0])

# Two-habitat normalized regression and coefficient-sign certificate.
a,b,A,B=sp.symbols('a b A B',positive=True)
H2=2*(a+b+2*d)*(a*b+(a+b)*d)
N2=(A*(a*b+a*d+b*b+5*b*d+4*d*d)
    +B*(a*a+a*b+5*a*d+b*d+4*d*d))
V2=N2/H2
P0=(a+b)*(B*a*a-A*b*b)
P1=4*(a+b)*(B*a-A*b)
P2=2*(B*(3*a+b)-A*(a+3*b))
R2=(P0+P1*d+P2*d*d)
assert sp.factor(sp.together(sp.diff(V2,d)+(a-b)*R2/(2*((a+b+2*d)*(a*b+(a+b)*d))**2)))==0
# For a<b the three A/B thresholds are r0 < r1 < r2.
assert sp.simplify(a/b-a*a/(b*b)-a*(b-a)/b**2)==0
assert sp.simplify((3*a+b)/(a+3*b)-a/b-(b-a)*(a+b)/(b*(a+3*b)))==0
print('two-habitat general derivative and strictly ordered coefficient thresholds: PASS')
print('All certificates reproduced.')
