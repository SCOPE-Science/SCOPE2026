"""Check identities for regular-hexagon Fourier lattice nodal geometry."""
import sympy as S
import mpmath as mp
from math import gcd
mp.mp.dps=55
pi=mp.pi
s,t=S.symbols('s t',real=True)
m,n=S.symbols('m n',integer=True)
x,y=S.symbols('x y',real=True)
N=(s-t)*S.cos(2*S.pi*(s-t))+t*S.cos(2*S.pi*t)-s*S.cos(2*S.pi*s)
print('Analytic sympy Hessian checks:')
for mi,ni in [(1,2),(2,1),(1,-1),(2,3),(-3,2),(5,8)]:
 H=S.hessian(N,(s,t)).subs({s:mi,t:ni});expected=4*S.pi**2*S.Matrix([[ni,mi-ni],[mi-ni,-mi]])
 assert S.simplify(H-expected)==S.zeros(2)
 assert S.simplify(H.det()+16*S.pi**4*(mi*mi-mi*ni+ni*ni))==0
 A=S.Matrix([[1,S.Rational(1,2)],[0,S.sqrt(3)/2]])
 PH=S.simplify(A*H*A.T)
 assert S.simplify(S.trace(PH))==0
 assert S.simplify(PH.det())<0
 print(mi,ni,'H normalized=',[S.simplify(v/(4*S.pi**2)) for v in H], 'trace physical=',S.trace(PH))

def I(s,t):
    # Direct quadrature in the aperture coordinates, no use of the cosine quotient.
    st=mp.mpc(s); tt=mp.mpc(t)
    if abs(tt)>mp.mpf('1e-20'):
        def inner(x,yl,yu):
            return mp.exp(-2j*pi*st*x)*(mp.exp(-2j*pi*tt*yl)-mp.exp(-2j*pi*tt*yu))/(2j*pi*tt)
        ob=mp.quad(lambda xx: inner(xx,-1-xx,1),[-1,0])+mp.quad(lambda xx:inner(xx,-1,1-xx),[0,1])
    else:
        ob=mp.quad(lambda xx: mp.exp(-2j*pi*st*xx)*(2-abs(xx)),[-1,0,1])
    return mp.sqrt(3)/2*ob

def formula(s,t):
    st=mp.mpf(s);tt=mp.mpf(t)
    num=(st-tt)*mp.cos(2*pi*(st-tt))+tt*mp.cos(2*pi*tt)-st*mp.cos(2*pi*st)
    return (mp.sqrt(3)/2)*num/(2*pi**2*st*tt*(st-tt))
for si,ti in [('0.41','0.67'),('1.12','-0.39'),('0.31','0.18')]:
    q=I(si,ti);f=formula(si,ti)
    assert abs(q-f)<mp.mpf('1e-45')
print('Direct quadrature versus closed form: PASS (3 generic points)')
for si,ti in [(1,2),(-3,2),(2,1),(0,2),(3,3),(mp.mpf(2)/3,mp.mpf(1)/3),(mp.mpf(1)/3,mp.mpf(2)/3)]:
    assert abs(I(si,ti))<mp.mpf('1e-45'),(si,ti,I(si,ti))
print('Direct quadrature reciprocal lattice zeros: PASS (7 nodes)')

for mi,ni in [(1,2),(2,1),(1,-1),(2,3),(-3,2)]:
    xi=mp.mpf(mi);eta=(mp.mpf(2*ni-mi))/mp.sqrt(3)
    eps=mp.mpf('1e-4')
    h1=eps*mp.mpf('.8');h2=eps*mp.mpf('1.1')
    sn=mi+h1;tn=ni+(h1+mp.sqrt(3)*h2)/2
    num=(xi*(h1*h1-h2*h2)-2*eta*h1*h2)
    leading=(3*mp.sqrt(3)/8)/(mi*ni*(mi-ni))*num
    exact=I(sn,tn)
    assert abs(exact-leading)<mp.mpf('0.001')*eps**2,(mi,ni,abs(exact-leading)/eps**2)
print('Physical traceless quadratic jets against direct quadrature: PASS (5 nodes)')

# Exact dual-lattice residue identities. For noninteger cosets, derivatives of the numerator cannot both vanish.
for k in range(-8,9):
 for ell in range(-8,9):
    a=S.Rational(2*k+ell,3);b=S.Rational(k+2*ell,3)
    if (k,ell)==(0,0):continue
    val=S.trigsimp(N.subs({s:a,t:b}));assert S.simplify(val)==0,(k,ell,val)
    if a.q!=1:
       gx=S.trigsimp(S.diff(N,s).subs({s:a,t:b})); gy=S.trigsimp(S.diff(N,t).subs({s:a,t:b}))
       assert gx!=0 or gy!=0
print('All 288 nonorigin reciprocal lattice nodes in a finite 17x17 grid: PASS')
print('All checks passed.')
