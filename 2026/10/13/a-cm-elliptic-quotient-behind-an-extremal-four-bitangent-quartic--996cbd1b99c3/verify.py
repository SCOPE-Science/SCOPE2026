import sympy as sp
X,T,Z=sp.symbols('X T Z')
F=sp.expand((X**2+T**2+Z**2)**2 + T*(T+Z)*(T+2*Z)*Z)
# source equation dehomogenizes correctly
assert sp.expand(F.subs(Z,1) - ((X**2+T**2+1)**2 + T*(T+1)*(T+2))) == 0
# smoothness: affine patches Z=1 and T=1 cover all projective points except [1:0:0], which is not on curve.
def no_sing_patch(poly, vars):
    ideal=[poly]+[sp.diff(poly,v) for v in vars]
    G=sp.groebner(ideal,*vars,order='lex')
    return G == sp.groebner([1],*vars,order='lex')
fz=sp.expand(F.subs(Z,1))
assert no_sing_patch(fz,(X,T))
ft=sp.expand(F.subs(T,1))
assert no_sing_patch(ft,(X,Z))
assert F.subs({X:1,T:0,Z:0}) != 0
# involution and quotient
assert sp.expand(F.subs(X,-X)-F)==0
Y=sp.symbols('Y')
# Y = X^2+T^2+1 on Z=1 gives E: Y^2=-T(T+1)(T+2)
assert sp.expand(fz.subs(X**2, Y-T**2-1) - (Y**2+T*(T+1)*(T+2))) == 0
# quotient elliptic discriminant and j: shift s=T+1, equation Y^2=s-s^3 ~ y^2=x^3-x, so j=1728
s=sp.symbols('s')
cubic=sp.expand(-T*(T+1)*(T+2)).subs(T,s-1)
assert sp.expand(cubic - (s-s**3))==0
# For y^2=x^3+A x+B, A=-1,B=0 after y -> iY; j=1728*4A^3/(4A^3+27B^2)
A=sp.Integer(-1); B=sp.Integer(0)
j=sp.simplify(1728*4*A**3/(4*A**3+27*B**2))
assert j==1728
# fixed divisor X=0 is four distinct points
f0=sp.Poly(sp.expand(fz.subs(X,0)),T)
assert f0.degree()==4 and sp.discriminant(f0.as_expr(),T)==4257
# marked stabilizer. Any PGL transformation fixing p=[1:0:0] has matrix
# [aa bb cc; 0 d e; 0 f h]. Comparing X^3 coefficients forces bb=cc=0.
aa,bb,cc,d,e,f,h,lam=sp.symbols('aa bb cc d e f h lam')
Xp=aa*X+bb*T+cc*Z; Tp=d*T+e*Z; Zp=f*T+h*Z
Ftr=sp.Poly(sp.expand(F.subs({X:Xp,T:Tp,Z:Zp}, simultaneous=True)-lam*F),X,T,Z)
# coefficients X^4, X^3T, X^3Z
assert sp.expand(Ftr.coeff_monomial(X**4)) == aa**4-lam
assert sp.expand(Ftr.coeff_monomial(X**3*T)) == 4*aa**3*bb
assert sp.expand(Ftr.coeff_monomial(X**3*Z)) == 4*aa**3*cc
# after bb=cc=0 and lambda=aa^4, normalize N=M/aa. Need N preserve q=T^2+Z^2 and r=T Z(T+Z)(T+2Z).
a,b,c,dd=sp.symbols('a b c dd')
Tp2=a*T+b*Z; Zp2=c*T+dd*Z
q=T**2+Z**2; r=T*Z*(T+Z)*(T+2*Z)
eq_q=sp.Poly(sp.expand(Tp2**2+Zp2**2-q),T,Z).coeffs()
eq_r=sp.Poly(sp.expand(Tp2*Zp2*(Tp2+Zp2)*(Tp2+2*Zp2)-r),T,Z).coeffs()
G=sp.groebner(eq_q+eq_r,a,b,c,dd,order='lex')
expected=sp.groebner([a-dd,b,c,dd**2-1],a,b,c,dd,order='lex')
assert G==expected
print('VERIFY_OK')
print('smooth=PASS quotient_genus=1 quotient_j=1728 fixed_points=4 marked_stabilizer=C2 fixed_binary_discriminant=4257')
