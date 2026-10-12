"""Reproduce exact algebra and witness for a two-feedback epidemic equilibrium.
Requires Python 3 and SymPy. The mathematical proof is in RESULT.md.
"""
import sympy as sp
m,be,al,de,ga,si,k1,k2,z=sp.symbols('m be al de ga si k1 k2 z',positive=True)
a=de*(1+k1*z); b=ga*(1+k2*z)
d=be*z+m+b; e=si*be*z+m+b
D=sp.expand(m*d+a*e); N=sp.expand(d+(1-si)*a)
P=sp.Poly(D,z);T=sp.Poly(N,z)
d0,d1,d2=(P.nth(i) for i in range(3));n0,n1=(T.nth(i) for i in range(2))
A0,A1,B0,B1=de,de*k1,ga,ga*k2
Q=m*(be+B1)**2+A0*(be+B1)*(si*be+B1)+(1-si)*A1*(be*(m+B0)+m*(be+B1)+A1*(m+B0))
assert sp.simplify(n1*d1-n0*d2-Q)==0
assert sp.simplify(sp.diff(z*N/D,z)*D**2 -(n0*d0+2*n1*d0*z+Q*z*z))==0
A,B=sp.symbols('A B',positive=True)
dv=be*z+m+B;ev=si*be*z+m+B
Nv=dv+(1-si)*A;Dv=m*dv+A*ev
assert sp.simplify(sp.diff(Nv/Dv,A) + dv*(B+si*(be*z+m))/Dv**2)==0
assert sp.simplify(sp.diff(Nv/Dv,B) +(1-si)*A*(be*z+m+A)/Dv**2)==0
# Exact example m=al=de=ga=1, be=4, si=1/2, zero feedback.
subs={m:1,al:1,de:1,ga:1,be:4,si:sp.Rational(1,2),k1:0,k2:0}
L=sp.Rational(1,2)
base=sp.factor((z+al*z*N/D-L).subs(subs))
assert sp.simplify(base - (20*z*z+7*z-4)/(4*(3*z+2)))==0
root=(3*sp.sqrt(41)-7)/40
assert sp.simplify(base.subs(z,root))==0
# Only the R-to-C feedback tends to infinity, with the C-to-S feedback fixed at zero.
lim1=sp.factor(z+sp.Rational(1,2)*z/(2+2*z)-L)
root1=(sp.sqrt(41)-3)/8
assert sp.simplify(lim1.subs(z,root1))==0
# Only C-to-S feedback diverges: R survives, I=1/3.
lim2=z+z/2-L
assert sp.simplify(lim2.subs(z,sp.Rational(1,3)))==0
assert 0<root<root1<L and root<sp.Rational(1,3)<L
# Reconstruct one asymmetric finite equilibrium and check every derivative equation.
example={m:1,al:1,de:1,ga:1,be:4,si:sp.Rational(1,2),k1:3,k2:7}
F=sp.together((z+al*z*N/D-L).subs(example))
positive_roots=[float(sp.re(r)) for r in sp.nroots(sp.fraction(F)[0]) if abs(float(sp.im(r)))<1e-10 and 0<float(sp.re(r))<.5]
assert len(positive_roots)==1
zz=positive_roots[0]
vals={z:zz,**example}
rr=float((al*z*d/D).subs(vals));cc=float((al*z*a/D).subs(vals));ss=0.5-0.5*cc
m0,be0,al0,de0,ga0,si0,k10,k20=1.,4.,1.,1.,1.,.5,3.,7.
aa=de0*(1+k10*zz);bb=ga0*(1+k20*zz)
rates=[m0*(1-ss)-be0*ss*zz+bb*cc,
       be0*ss*zz+si0*be0*cc*zz-(m0+al0)*zz,
       (1-si0)*be0*cc*zz+al0*zz-m0*rr-aa*rr,
       aa*rr-be0*cc*zz-m0*cc-bb*cc]
assert all(abs(v)<1e-10 for v in rates) and abs(ss+zz+rr+cc-1)<1e-10
print('VERIFY_OK')
