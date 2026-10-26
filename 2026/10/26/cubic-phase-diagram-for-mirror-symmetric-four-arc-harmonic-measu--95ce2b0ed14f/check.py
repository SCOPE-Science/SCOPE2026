"""Independent reproducibility checks for four-arc harmonic-measure equilibria."""
from math import acos, pi
import cmath
import mpmath as mp
import numpy as np
import sympy as sp

z,t,A,B,c = sp.symbols('z t A B c')
Q = lambda x: sp.expand(z**2*((z+1/z)**2-4*x*c*(z+1/z)+4*(x*x+c*c-1)))
N = lambda x: x*(1+z*z)-2*c*z
P = sp.expand(N(A)*Q(B)+N(B)*Q(A))
h = [A+B,-4*c*(2*A*B+1),4*(A+B)*(A*B+3*c*c-1),-8*c*(A*A+B*B+2*c*c-2)]
H = sum(h[j]*t**(3-j) for j in range(4))
assert sp.simplify(P-sp.expand(z**3*H.subs(t,z+1/z)))==0
assert sp.simplify(sp.expand(z**6*P.subs(z,1/z))-P)==0
print('symbolic_joukowski_identity PASS')
print('symbolic_reciprocity PASS')

examples = [
    (sp.Rational(-3,4),sp.Rational(4,5),sp.Rational(9,10),'three-real'),
    (sp.Rational(-11,20),sp.Rational(3,5),sp.Rational(9,10),'one-real'),
]
for a0,b0,c0,label in examples:
    hh=sp.Poly(H.subs({A:a0,B:b0,c:c0}),t)
    Delta=sp.factor(sp.discriminant(hh.as_expr(),t))
    assert Delta!=0 and ((Delta>0)==(label=='three-real'))
    theta_a,theta_b,delta=acos(float(a0)),acos(float(b0)),acos(float(c0))
    assert 0<delta<theta_b and theta_b+2*delta<theta_a and theta_a+delta<pi
    roots=np.roots([float(x) for x in hh.all_coeffs()]); zw=[]
    for root in roots:
        discr=cmath.sqrt(root*root-4)
        opts=((root+discr)/2,(root-discr)/2)
        inside=min(opts,key=abs)
        assert abs(inside)<1 and abs(abs(opts[0]*opts[1])-1)<1e-9
        zw.append(inside)
    nreal=sum(abs(w.imag)<1e-9 for w in zw)
    assert nreal==(3 if label=='three-real' else 1)
    print(f'{label}_exact_discriminant {Delta} PASS; numerical roots:',[complex(round(q.real,8),round(q.imag,8)) for q in zw])

mp.mp.dps=70
for alpha,beta,delta0 in [(acos(-.75),acos(.8),acos(.9)),(acos(-.55),acos(.6),acos(.9))]:
    zz=mp.mpc('0.19','0.26')
    aa,bb,dd=mp.mpf(alpha),mp.mpf(beta),mp.mpf(delta0)
    cc=mp.cos(dd)
    def q(x):
        return (1-2*zz*mp.cos(x+dd)+zz**2)*(1-2*zz*mp.cos(x-dd)+zz**2)
    def nn(x): return mp.cos(x)*(1+zz**2)-2*cc*zz
    rational=4*mp.sin(dd)/mp.pi*(nn(aa)/q(aa)+nn(bb)/q(bb))
    series=4/mp.pi*sum(mp.sin(n*dd)*(mp.cos(n*aa)+mp.cos(n*bb))*zz**(n-1) for n in range(1,180))
    assert abs(rational-series)<mp.mpf('1e-45')
    print('independent_Fourier_rational_evaluation PASS',mp.nstr(abs(rational-series),5))

B0=sp.sqrt(2)/2; cs=sp.Rational(9,10)
square=sp.factor(P.subs({A:-B0,B:B0,c:cs}))
assert sp.simplify(square/z**3).free_symbols==set() and square!=0
print('square_triple_at_origin PASS')
print('ALL_CHECKS_PASSED')
