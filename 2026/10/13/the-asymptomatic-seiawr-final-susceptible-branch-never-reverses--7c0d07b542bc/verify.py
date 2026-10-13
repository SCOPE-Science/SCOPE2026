#!/usr/bin/env python3
import mpmath as mp
import sympy as sp
mp.mp.dps=60
x,R=sp.symbols("x R", positive=True)
F=sp.log(1/x)-R*(1-x)
dx=sp.simplify(-sp.diff(F,R)/sp.diff(F,x))
assert sp.simplify(dx-(1-x)/(R-1/x))==0
Rv=mp.mpf("1.188808")
f=lambda z: mp.log(1/z)-Rv*(1-z)
root=mp.findroot(f, mp.mpf("0.7"))
assert abs(root-mp.mpf("0.7001358120286572180803376653146633")) < mp.mpf("1e-33")
assert abs(f(root)) < mp.mpf("1e-50")
assert abs(f(mp.mpf(1))) < mp.mpf("1e-50")
der=(1-root)/(Rv-1/root)
assert Rv*root < 1
assert der < 0
# For a representative seeded s0<1, verify the unique physical root lies below 1/R.
s0=mp.mpf("0.999")
g=lambda z: mp.log(s0/z)-Rv*(1-z)
r=mp.findroot(g, mp.mpf("0.69"))
assert 0 < r < s0 and Rv*r < 1
print("VERIFY_OK")
print("lower_root", mp.nstr(root,30))
print("lower_branch_derivative", mp.nstr(der,30))
print("seeded_root_s0_0_999", mp.nstr(r,30))
