#!/usr/bin/env python3
import sympy as sp

t = sp.symbols("t", real=True)
k, D, R0, Y0 = sp.symbols("k D R0 Y0", nonzero=True)
R = R0 * sp.exp(D*t)
Y = Y0 * sp.exp(-k*t)
Q = k*R + D*Y - 1
E = D*k/Q
r = sp.simplify(E*R)
y = sp.simplify(E*Y)
L = sp.simplify(r-y)
A = sp.simplify(k+L)
B = sp.simplify(D-L)
checks = {
    "Eprime": sp.simplify(sp.diff(E,t) + L*E),
    "rprime": sp.simplify(sp.diff(r,t) - r*B),
    "yprime": sp.simplify(sp.diff(y,t) + y*A),
    "Aprime": sp.simplify(sp.diff(A,t) - (r*B+y*A)),
    "Bprime": sp.simplify(sp.diff(B,t) + (r*B+y*A)),
    "sum": sp.simplify(A+B-(k+D)),
}

u,v,c,d = sp.symbols("u v c d")
kk = 1-u-v
DD = v-d
r0 = v-c
y0 = d
E0a = sp.expand(kk*r0 + DD*(y0-kk))
E0b = sp.expand(d*(kk+DD)-kk*c)
A0a = sp.expand(kk + r0-y0)
A0b = 1-u-c-d
B0a = sp.expand(DD-(r0-y0))
checks.update({
    "E0": sp.simplify(E0a-E0b),
    "A0": sp.simplify(A0a-A0b),
    "B0": sp.simplify(B0a-c),
})
failed={name:expr for name,expr in checks.items() if expr != 0}
if failed:
    for name,expr in failed.items():
        print(name, sp.factor(expr))
    raise SystemExit(1)
print("VERIFY_OK")
