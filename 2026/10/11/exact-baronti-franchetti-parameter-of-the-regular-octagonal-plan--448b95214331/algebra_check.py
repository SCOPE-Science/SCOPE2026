"""Exact symbolic checks for the regular-octagon Lambda calculation."""
import sympy as sp
r=sp.symbols("r", real=True)
a=sp.sqrt(2)-1
s=sp.sqrt(1+a**2)
L=sp.sqrt(2)/(1+s)
h1=(1+r**2)/(sp.sqrt(2)*(1+a*r))
h2=(1+r**2)/((1+r)*(1+a*r))
r0=a/(1+s)
r1=s-a
assert sp.simplify(s**2-(4-2*sp.sqrt(2)))==0
assert sp.simplify(sp.together(sp.diff(h1,r)).as_numer_denom()[0].subs(r,r0))==0
assert sp.simplify(sp.together(sp.diff(h2,r)).as_numer_denom()[0].subs(r,r1))==0
assert sp.simplify(h1.subs(r,r0)-L)==0
assert sp.simplify(h2.subs(r,r1)-L)==0
assert sp.simplify(h1.subs(r,a)-1/sp.sqrt(2))==0
assert sp.simplify(h2.subs(r,a)-1/sp.sqrt(2))==0
assert sp.simplify(h2.subs(r,1)-1/sp.sqrt(2))==0
print("all symbolic identities verified")
