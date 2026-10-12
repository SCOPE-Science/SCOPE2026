import sympy as sp

p,S=sp.symbols('p S')
f=p**4-p**3+2*p**2+p+1
q=(p-1)/(p+1)

# Irreducibility over Q.
assert sp.Poly(f,p,domain=sp.QQ).is_irreducible

# The three nontrivial Möbius maps preserve the four roots.
T1=-1/p
T2=(1-p)/(1+p)
T3=(p+1)/(p-1)
for T,scale,den in [(T1,1,p**4),(T2,4,(p+1)**4),(T3,4,(p-1)**4)]:
    num,den0=sp.together(f.subs(p,T)).as_numer_denom()
    assert sp.expand(num-scale*f)==0
    assert sp.expand(den0-den)==0
assert sp.simplify(T1.subs(p,T1)-p)==0
assert sp.simplify(T2.subs(p,T2)-p)==0
assert sp.simplify(T1.subs(p,T2)-T3)==0
assert sp.simplify(T2.subs(p,T1)-T3)==0

# The quadratic subfield fixed by T1.
s=(2*p**2-p-2)/p
num=sp.together((s**2+15)*p**2).as_numer_denom()[0]
assert sp.rem(sp.Poly(num,p),sp.Poly(f,p)).as_expr()==0
for T,sign in [(T1,1),(T2,-1),(T3,-1)]:
    num=sp.together(sp.cancel(s.subs(p,T))-sign*s).as_numer_denom()[0]
    assert sp.rem(sp.Poly(num,p),sp.Poly(f,p)).as_expr()==0

# Factorization over Q(S), under S^2=-15.
fac=(p**2-(1+S)*p/2-1)*(p**2-(1-S)*p/2-1)
diff=sp.together(fac-f).as_numer_denom()[0]
assert sp.rem(sp.Poly(diff,S),sp.Poly(S**2+15,S)).as_expr()==0

# If u^2=(1+S)/2 and v=2/u, then v^2=(1-S)/2,
# (u+v)^2=5, (u-v)^2=-3, and (u+v)(u-v)=S.
u,v=sp.symbols('u v', nonzero=True)
a=(1+S)/2
b=(1-S)/2
assert sp.rem(sp.Poly(sp.expand(a*b-4),S),sp.Poly(S**2+15,S)).as_expr()==0
assert sp.rem(sp.Poly(sp.expand(a+b+4-5),S),sp.Poly(S**2+15,S)).as_expr()==0
assert sp.rem(sp.Poly(sp.expand(a+b-4+3),S),sp.Poly(S**2+15,S)).as_expr()==0
assert sp.rem(sp.Poly(sp.expand(a-b-S),S),sp.Poly(S**2+15,S)).as_expr()==0

# Relative involution on q.
assert sp.simplify(q.subs(p,T1)+1/q)==0

# Veniani's displayed quartic coefficient vector is preserved up to a scalar.
A=2*p**2*q**2
B=(p**4+1)*(q**4+1)
C=-2*q**2*(p**4+1)
D=-2*p**2*(q**4+1)
qp=sp.cancel(q.subs(p,T1))
Ap=sp.cancel(2*T1**2*qp**2)
Bp=sp.cancel((T1**4+1)*(qp**4+1))
Cp=sp.cancel(-2*qp**2*(T1**4+1))
Dp=sp.cancel(-2*T1**2*(qp**4+1))
scale=1/(p**4*q**4)
for x,y in [(Ap,A),(Bp,B),(Cp,C),(Dp,D)]:
    assert sp.simplify(x-scale*y)==0

print('VERIFY_OK irreducible=4 galois=V4 roots=p,-1/p,-q,1/q fixed=sqrt(-15) field=Q(sqrt5,sqrt(-3)) descent_scale=1/(p^4*q^4)')
