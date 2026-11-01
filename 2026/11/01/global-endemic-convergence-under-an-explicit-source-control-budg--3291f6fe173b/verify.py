"""Independent symbolic arithmetic diagnostics for a specified NPI-coupled SIR theorem.
Run: python3 verify_npi_28.py (requires SymPy). These finite checks are not an infinite proof.
"""
import sympy as s
x, xs, beta, a, e, xi, mu, gamma, eps, S, I = s.symbols('x xs beta a e xi mu gamma eps S I', positive=True)
q=mu+gamma
T=lambda z:beta*(1-a*z)*(1-e*z)
A=lambda z:a*xi*beta*(1-e*z)
Ts=T(xs); Ss=q/Ts; Is=mu/q*(1-Ss); c=A(xs)*Is
Sp=mu*(1-S)-T(x)*S*I
Ip=T(x)*S*I-q*I
xp=eps*x*(1-x)*(A(x)*I-c)
VSIp=s.expand((1-Ss/S)*Sp+(1-Is/I)*Ip)
Uprime=-(q/(eps*Ts))*(T(x)-Ts)/(x*(1-x)*A(x))
Vprime=s.factor(VSIp+Uprime*xp)
form=-mu*(S/Ss-1)**2/(S/Ss) -q*Is/Ts*(T(x)-Ts)*(S/Ss-1)-q*Is/Ts*(T(x)-Ts)*(A(x)-A(xs))/A(x)
assert s.simplify(Vprime-form)==0, 'entropy derivative mismatch'
print('PASS entropy exact derivative')
ratio=s.factor((A(x)-A(xs))/(A(x)*(T(x)-Ts)))
expect=e/(beta*(1-e*x)*(a+e-a*e*(x+xs)))
assert s.simplify(ratio-expect)==0
print('PASS exact source-control damping ratio')
ex={mu:s.Rational(1,5), gamma:s.Rational(4,5),beta:s.Integer(4), a:s.Rational(3,10),e:s.Rational(9,10),xi:1,xs:s.Rational(3,10)}
exact={ 'T*':s.Rational(6643,2500),'S*':s.Rational(2500,6643),'I*':s.Rational(4143,33215),'A*':s.Rational(219,250),'c':s.Rational(12429,113750)}
for label,expr in [('T*',Ts),('S*',Ss),('I*',Is),('A*',A(xs)),('c',c)]:
    val=s.cancel(expr.subs(ex)); assert val==exact[label],(label,val,exact[label]);print('PASS',label,val)
L=s.cancel((e/(beta*(a+e))).subs(ex));R=s.cancel((Is/(4*mu)).subs(ex));assert L>R;print('PASS strict damping margin',L-R)
# Boundary invariant viability test: R=1-S-I obeys R'=gamma*I-mu*R.
assert s.simplify(-Sp-Ip-(gamma*I-mu*(1-S-I)))==0
print('PASS demographic simplex balance')
# Verify symbolic equilibrium from equations.
assert s.simplify(Sp.subs({S:Ss,I:Is,x:xs}))==0
assert s.simplify(Ip.subs({S:Ss,I:Is,x:xs}))==0
assert s.simplify(xp.subs({S:Ss,I:Is,x:xs}))==0
print('PASS equilibrium substitutions')
print('All verification checks passed; general proof requires analytic arguments.')
