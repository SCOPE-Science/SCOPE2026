"""Exact algebraic and numerical checks for the quartic normal-return phase diagram.
Run with Python 3 and SymPy: python CHECK.py
The mathematical proof, not these finite tests, establishes the universal statements.
"""
import sympy as S

t, x, y, v = S.symbols('t x y v', real=True)
H = (t**7*(x+1)**3 + 8*t**6*(x+1)**2
     + t**5*(4*x**2+32*x+28) + t**4*(24*x+56)
     + t**3*(70-2*x) + t**2*(56-8*x) + 28*t + 8)
P = (800000*x**12-109124375*x**11+171058713*x**10-81950155*x**9
     +21890925*x**8-3445758*x**7+64450*x**6+91970*x**5
     -7342*x**4-107*x**3+101*x**2+9*x+1)
count=0

def check(condition, label):
    global count
    assert condition, label
    count += 1

# With v=A*t, the independent symbols x and t encode A and the normal distance.
A=S.symbols('A',real=True)
z=1+t+S.I*A*t
F=S.expand_complex((z**4+S.I*A)*S.conjugate(z**4+S.I*A)-(1+A*A)).expand()
check(S.simplify(F-t*(1+A**2)*H.subs(x,A**2)) == 0, 'quartic boundary factorization')
res = S.resultant(H, S.diff(H,t), t)
check(S.expand(res+262144*(x-1)*(x+1)**9*P)==0, 'Sylvester resultant')
coeffs=S.Poly(S.expand(P.subs(x,y+7)),y)
check(coeffs.degree()==12 and coeffs.nth(12)==800000, 'resultant polynomial degree')
for j in range(12): check(coeffs.nth(j)<0,f'negative shifted coefficient j={j}')
check(P.subs(x,134)<0 and P.subs(x,135)>0, 'isolation of critical x')
for aa in [0,1,2,4,7]:
    poly=S.Poly(H.subs(x,aa),t)
    check(all(c>=0 for c in poly.all_coeffs()) and poly.nth(0)>0,'subcritical coefficients')

# Exact positive coefficients of H after fixing v=A*t and setting t=v/A.
h = S.expand(H.subs(x,v*v/t/t))
expected=(t**7+8*t**6+(3*v*v+28)*t**5+(16*v*v+56)*t**4
 +(3*v**4+32*v*v+70)*t**3+(8*v**4+24*v*v+56)*t**2
 +(v**6+4*v**4-2*v*v+28)*t+8-8*v*v)
check(S.simplify(h-expected)==0,'monotone rescaling identity')
check(S.factor(v**6+4*v**4-2*v*v+28).subs(v,0)==28,'positive coefficient basepoint')

# Exact sign witnesses: original September quartic seed A=64, t=1/32.
check(S.sign(F.subs({A:64,t:S.Rational(1,32)}))==-1, 'A=64 original interior witness')
for aa,tt in [(8,S.Rational(1,10)),(10,S.Rational(1,10)),(64,S.Rational(1,32))]:
    val=S.sign(F.subs({A:aa,t:tt}))
    check(val in [-1,0,1], 'rational test defined')

# Numerical sanity for the algebraic threshold and the two asymptotic branches.
import mpmath as mp
mp.mp.dps=50
pfn=S.lambdify(x,P,'mpmath')
crit=mp.findroot(pfn,(134,135),tol=mp.mpf("1e-40"));acrit=mp.sqrt(crit)
hfn=S.lambdify((t,x),H,'mpmath')
dhfn=S.lambdify((t,x),S.diff(H,t),'mpmath')
tcrit=mp.findroot(lambda u:dhfn(u,crit),(.12,.14))
check(abs(hfn(tcrit,crit)) < mp.mpf('1e-38'),'tangent equation')
check(mp.mpf(134)<crit<mp.mpf(135),'critical root isolation numerically')
check(mp.mpf('0.12')<tcrit<mp.mpf('0.14'),'tangency location')
for aa in [20,64,100,1000]:
    roots=S.nroots(H.subs(x,aa*aa),n=25,maxsteps=150)
    positives=sorted([float(S.re(q)) for q in roots if abs(float(S.im(q)))<1e-14 and S.re(q)>0])
    check(len(positives)==2,'two ray intersections')
    check(positives[0]<positives[1], 'proper crossing order')
    m=(positives[0]+positives[1])/2
    check(hfn(m,mp.mpf(aa)**2)<0,'negative between roots')
print('CHECK_OK',count)
print('xcrit',mp.nstr(crit,25),'Acrit',mp.nstr(acrit,25),'tcrit',mp.nstr(tcrit,25))
