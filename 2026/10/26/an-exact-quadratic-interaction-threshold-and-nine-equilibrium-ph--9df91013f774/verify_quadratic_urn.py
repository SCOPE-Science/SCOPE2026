"""Exact algebra checks for the quadratic two-urn phase transition.

Uses SymPy. These symbolic checks complement the continuum argument in RESULT.md.
"""
import sympy as S

a,b,s,t,p=S.symbols('a b s t p', real=True)
count=0
def check(condition,name):
    global count
    if not condition:
        raise AssertionError(name)
    count+=1

# For x=(1+a)/2 and y=(1+b)/2, these are the clearing-of-denominators equations.
F=lambda z: z*(z*z+2*p-1)*(4+(a+b)**2)-4*p*(a+b)*(1+z*z)
F1,F2=F(a),F(b)
D=a*a*b*b+(a+b)**2-2*p*a*b+2*p-1
fa=lambda z:z*(z*z+2*p-1)/(1+z*z)
check(S.factor((fa(a)-fa(b))*(1+a*a)*(1+b*b)-(a-b)*D)==0,'difference identity')
K=s**4+s*s*(3-3*t-2*p)+(8*p-12)*t-4
sym_sum=(a+b)*K.subs({s:a+b,t:a*b})
check(S.expand(F1+F2-sym_sum)==0,'sum identity')
pp=S.factor((1-s*s-t*t)/(2*(1-t)))
check(S.factor(D.subs({a*a*b*b:t*t,a+b:s,a*b:t}).subs(p,pp))==0 or S.factor((s*s+t*t-2*p*t+2*p-1).subs(p,pp))==0,'difference elimination')
Q=s*s*(t-2)-2*t*t+4*t+2
check(S.factor(K.subs(p,pp)-(s*s-2*t+2)*Q/(t-1))==0,'factorization of eliminated sum')
s2=S.factor(2*(t*t-2*t-1)/(t-2))
pt=S.factor(pp.subs(s*s,s2))
check(S.factor(pt-t*(t*t-5)/(2*(t-2)*(t-1)))==0,'off-anti-diagonal parameter')
check(S.factor((1+t)**2-s2-t*(t-1)**2/(t-2))==0,'admissibility margin')
dp=S.factor(S.diff(pt,t))
check(S.factor(dp-(t**4-6*t**3+11*t*t-10)/(2*(t-2)**2*(t-1)**2))==0,'monotonicity derivative')
t0=1-S.sqrt(2)
pc=1-S.sqrt(2)/2
check(S.simplify(pt.subs(t,t0)-pc)==0,'critical value')
# On the anti-diagonal, t=-z^2, p=(1-z^2)/2.
z=S.symbols('z',real=True)
pad=(1-z*z)/2
hpz=2*(1-z*z)/(1+z*z)**2
lambda_minus=S.factor(-1+(1-pad)*hpz)
lambda_plus=S.factor(lambda_minus+2*pad)
check(S.factor(lambda_minus+2*z*z/(1+z*z))==0,'anti-diagonal eigenvalue')
check(S.factor(lambda_plus-(1-2*z*z-z**4)/(1+z*z))==0,'diagonal eigenvalue')
check(S.simplify(lambda_plus.subs(z,S.sqrt(S.sqrt(2)-1)))==0,'critical eigenvalue zero')
# Direct substitution of a nontrivial off-anti-diagonal equilibrium for rational t.
for tv in [S.Rational(-2,5),S.Rational(-1,3),S.Rational(-1,4),S.Rational(-1,10)]:
    sv=S.sqrt(s2.subs(t,tv))
    av=(sv-S.sqrt(sv*sv-4*tv))/2
    bv=(sv+S.sqrt(sv*sv-4*tv))/2
    pv=pt.subs(t,tv)
    residual1=F1.subs({a:av,b:bv,p:pv})
    residual2=F2.subs({a:av,b:bv,p:pv})
    check(abs(complex(S.N(residual1,45)))<1e-30,f'off-axis residual a t={tv}')
    check(abs(complex(S.N(residual2,45)))<1e-30,f'off-axis residual b t={tv}')
    check(-1<float(S.N(av))<0<float(S.N(bv))<1,f'off-axis physical roots t={tv}')
    check(0<float(S.N(pv))<float(S.N(pc)),f'off-axis p range t={tv}')
print(f'PASS: {count} exact symbolic and high-precision algebra checks')
print('p_c = 1 - sqrt(2)/2 =',S.N(pc,16))
print('p_off(t) =',pt)
print('dp_off/dt =',dp)
