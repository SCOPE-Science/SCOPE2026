"""Reproducible algebraic and numerical checks of the two-district Huff-share theorem."""
import math
import random
import sympy as sp

x = sp.symbols('x', positive=True)
S = (sp.Rational(3, 5) * 2*x/(1 + 2*x)
     + sp.Rational(2, 5) * 2/(x + 2))
assert sp.simplify(S - 2*(3*x*x + 10*x + 2)/(5*(x + 2)*(2*x + 1))) == 0
poly = sp.factor(sp.together(S - sp.Rational(27,40)))
assert sp.factor(sp.fraction(poly)[0]) == -(6*x*x - 25*x + 22)
roots = ((25-sp.sqrt(97))/12, (25+sp.sqrt(97))/12)
assert all(float(t)>1 for t in roots)
assert all(sp.simplify(S.subs(x,t)-sp.Rational(27,40))==0 for t in roots)
critical = (2*sp.sqrt(3)-sp.sqrt(2))/(2*sp.sqrt(2)-sp.sqrt(3))
assert sp.simplify(critical-(2+3*sp.sqrt(6))/5)==0
max_share = sp.Rational(4,3)-4*sp.sqrt(6)/15
assert sp.simplify(S.subs(x,critical)-max_share)==0
assert float(max_share)>27/40

rng = random.Random(917301)
for _ in range(5000):
    lam = math.exp(rng.uniform(.04, 3.0))
    w = rng.random()
    ratio = math.exp(rng.uniform(.03, 2.0))
    cutoff = lam*lam/(1+lam*lam)
    def market(beta):
        t = beta * math.log(ratio)
        # Stable for all beta used here.
        z = math.log(lam)
        first = 1/(1+math.exp(-(z+t)))
        second = 1/(1+math.exp(-(z-t)))
        return w*first+(1-w)*second
    def deriv_x(xx):
        return lam*(w/(1+lam*xx)**2-(1-w)/(xx+lam)**2)
    if w <= .5:
        assert deriv_x(1.2)<0 and deriv_x(2.0)<0 and deriv_x(12.0)<0
        assert market(0)>market(.5)>market(1.0)>market(5.0)
    elif w >= cutoff:
        assert deriv_x(1.2)>0 and deriv_x(2.0)>0 and deriv_x(12.0)>0
        assert market(0)<market(.5)<market(1.0)<market(5.0)
    else:
        a=math.sqrt(w); b=math.sqrt(1-w)
        xm=(lam*a-b)/(lam*b-a)
        bm=math.log(xm)/math.log(ratio)
        assert xm>1 and bm>0
        assert deriv_x((xm+1)/2)>0
        assert deriv_x(xm*2)<0
        peak=market(bm)
        exact_peak=lam*(lam-2*math.sqrt(w*(1-w)))/(lam*lam-1)
        assert abs(peak-exact_peak)<1e-11
        assert peak>max(market(0),w)
print('PASS: exact rational inverse ambiguity, critical point and 5000 classifications')
