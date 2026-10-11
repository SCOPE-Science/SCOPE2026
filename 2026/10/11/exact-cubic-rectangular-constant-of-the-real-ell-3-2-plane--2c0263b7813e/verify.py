import sympy as sp
u,h=sp.symbols('u h')
N=u**2*(1+u)+h**3*(1+u**2)
D=(u+h)**3+u**2*(h-1)**3
R=sp.cancel(N/D)
fu=sp.factor(sp.together(sp.diff(R,u))).as_numer_denom()[0]
fh=sp.factor(sp.together(sp.diff(R,h))).as_numer_denom()[0]
# normalize the h derivative by its harmless factor 3*u
fh0=sp.factor(fh/(3*u))
P=u**10-12*u**9-59*u**8-104*u**7-350*u**6-368*u**5-334*u**4+40*u**3+77*u**2+60*u-7
Q=27*u**6+81*u**5+170*u**4+270*u**3+259*u**2+81*u+8
res=sp.factor(sp.resultant(fu,fh0,h))
expected=4*u**13*(u+1)**4*Q*P
assert sp.expand(res-expected)==0
Pp=sp.Poly(P,u,domain=sp.ZZ)
# Cauchy bound puts every root inside |u|<369; exact Sturm count leaves one root above 1.
assert Pp.count_roots(1,369)==1
lo=sp.Rational(161428,10000); hi=sp.Rational(161429,10000)
assert Pp.count_roots(lo,hi)==1 and Pp.eval(lo)<0<Pp.eval(hi)
A=8482484*u**9+35056168*u**8+66754285*u**7+196108143*u**6+203704837*u**5+173520417*u**4-23602937*u**3-42303003*u**2-31205429*u+3667499
B=167282621*u**9+692749853*u**8+1317595314*u**7+3874778514*u**6+4024515932*u**5+3430463796*u**4-466156426*u**3-835826554*u**2-616943313*u+72501863
for poly in [A,B-16*A,20*A-B]:
    pp=sp.Poly(poly,u,domain=sp.ZZ)
    assert pp.count_roots(lo,hi)==0
    assert pp.eval(lo)>0 and pp.eval(hi)>0
H=sp.cancel(B/(4*A))
# Verify the reduced subresultant relation.
subs=sp.subresultants(fu,fh0,h)
lin=sp.Poly(subs[-2],h)
# Common stationary roots must satisfy the linear subresultant; modulo P it is proportional to 4Ah-B.
rem_h=sp.Poly(lin.coeff_monomial(h),u,domain=sp.QQ).rem(Pp).as_expr()
rem_c=sp.Poly(lin.coeff_monomial(1),u,domain=sp.QQ).rem(Pp).as_expr()
assert sp.Poly(sp.together(lin.as_expr().subs(h,H)).as_numer_denom()[0],u,domain=sp.QQ).rem(Pp).is_zero
for expr in [fu,fh0]:
    num=sp.together(expr.subs(h,H)).as_numer_denom()[0]
    assert sp.Poly(num,u,domain=sp.QQ).rem(Pp).is_zero
assert sp.simplify((R.subs(h,1)-1)+u*(u+3)/(u+1)**3)==0
assert sp.simplify((R.subs(u,1)-1)+(3*h-1)/(h*(h**2+3)))==0
root=sp.CRootOf(P,3)
h0=H.subs(u,root)
rho=R.subs({u:root,h:h0})
mu=rho**sp.Rational(1,3)
assert 4<float(sp.N(h0,30))<5
print('VERIFY_OK', 'u0='+str(sp.N(root,18)), 'h0='+str(sp.N(h0,18)), 'rho='+str(sp.N(rho,18)), 'mu3='+str(sp.N(mu,18)), 'resultant_degree=10')
