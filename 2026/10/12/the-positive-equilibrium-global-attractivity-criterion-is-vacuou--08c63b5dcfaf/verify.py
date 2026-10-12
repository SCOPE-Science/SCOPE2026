#!/usr/bin/env python3
import sympy as sp

a,b,h,m,r0,d,eps = sp.symbols('a b h m r0 d eps', positive=True)
Ux = (r0-d)/a + eps
Uy = h*(m+Ux) + eps

gap = sp.expand(b*Uy-(r0-d))
certificate = b*h*m + (b*h-a)*(r0-d)/a + b*(h+1)*eps
assert sp.simplify(gap-certificate) == 0

# Abstract sign certificate after the theorem implications D=r0-d>0 and P=bh-a>0.
D,P = sp.symbols('D P', positive=True)
positive_form = b*h*m + P*D/a + b*(h+1)*eps
assert positive_form.is_positive is True

# The theorem's stronger inequality h>(1+a)/b implies bh-a>1.
t = sp.symbols('t', positive=True)
# Write h=(1+a)/b+t. Then bh-a = 1+b*t > 0.
h_param = (1+a)/b + t
assert sp.simplify((b*h_param-a) - (1+b*t)) == 0

print('VERIFY_OK')
print('gap_identity', sp.factor(gap))
print('sign_certificate', positive_form)
print('bh_minus_a_under_theorem', sp.simplify(b*h_param-a))
