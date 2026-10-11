import sympy as s
lam,gam,k,t=s.symbols("lam gam k t", positive=True)
c=(1-lam)/(1+lam)
d=(gam-1)/(gam+1)
# X corridor boundary polynomials from |(1+l)t^2-(1-l)| <= 2 l t
p_upper=s.factor((1+lam)*t**2-(1-lam)-2*lam*t)
p_lower=s.factor((1+lam)*t**2-(1-lam)+2*lam*t)
assert s.factor(p_upper-(t-1)*((1+lam)*t+(1-lam)))==0
assert s.factor(p_lower-(t-c)*((1+lam)*t+(1+lam)))==0
# Y corridor: (g+1)t^2+(g-1) <= 2 g t
p_y=s.factor((gam+1)*t**2+(gam-1)-2*gam*t)
assert s.factor(p_y-(t-1)*((gam+1)*t-(gam-1)))==0
# Alternating two-cycle.
xp,yp=-c,d
xm,ym=c,-d
assert s.simplify(lam*xp+(1-lam)-xm)==0
assert s.simplify(gam*yp-(gam-1)-ym)==0
assert s.simplify(lam*xm-(1-lam)-xp)==0
assert s.simplify(gam*ym+(gam-1)-yp)==0
# Both branch inequalities reduce to d+k*c>0.
assert s.simplify(yp-k*xp-(d+k*c))==0
assert s.simplify(k*xm-ym-(d+k*c))==0
print("VERIFY_OK")
