#!/usr/bin/env python3
"""Reproducible symbolic checks for the quartic anharmonic-oscillator PPV trichotomy.

Equation: y'' = q*y, q = x^4 + t*x^2 + 1, over C(t,x), dx=d/dx, dt=d/dt.

Verifies exact polynomial identities behind:
 (R) Riccati cascade excluding the Borel/reducible case (Kovacic case 1);
 (S) symmetric-square P-equation leading obstruction excluding dihedral (case 2);
 (B) Lax-pair reduction to the scalar b-equation + its pole/degree obstructions
     (non-isomonodromy => full PPV group SL2).

All outputs are exact (SymPy). Run: python3 kovacic_ppv_checks.py
"""
import sympy as sp

x, t = sp.symbols('x t')
q = x**4 + t*x**2 + 1
qx = sp.diff(q, x)
qt = sp.diff(q, t)
print("== base ==")
print("q =", q, "| qx =", qx, "| qt (=dtA lower-left) =", qt)

# ---------- (R) Riccati cascade ----------
print("\n== (R) Riccati: Q = s*x^2 + a*x + b, s^2 = 1 ==")
s, a, b = sp.symbols('s a b')
Q = s*x**2 + a*x + b
R = sp.expand(sp.diff(Q, x) + Q**2 - q)
# R = x^4 + 2*s*a*x^3 + (2*s*b + a^2 - t)*x^2 + (2*a*b + 2*s)*x + (b^2 + a - 1)
for pw in (3, 2, 1):
    print(f"coeff of x^{pw} in Q'+Q^2-q:", sp.expand(R).coeff(x, pw))
print("with a=0: coeff x^2 =", sp.expand(R.subs(a, 0)).coeff(x, 2),
      "-> b = s*t/2; then coeff x^1 =", sp.expand(R.subs(a, 0)).coeff(x, 1))

# tail contribution of S = k/x + m1/x^2 + m2/x^3 (k = # finite poles, each residue 1)
k, m1, m2 = sp.symbols('k m1 m2')
S = k/x + m1/x**2 + m2/x**3
E = sp.diff(S, x) + 2*Q*S + S**2
z = sp.symbols('z')
Ez = sp.simplify(E.subs(x, 1/z))
print("residue at oo of tail E (= coeff of x^1):", sp.limit(Ez*z, z, 0))
print("constant term of tail E:", sp.limit(Ez - (2*s*k)/z, z, 0))
print("=> total x^1 coeff of u'+u^2-q is 2*s*(1+k) = 0  <=>  k = -1, impossible (k>=0).")

# formal Riccati series at oo has 1/x coefficient -1 (mismatch with k>=0)
c = sp.symbols('c')
u = s*(x**2 + t/2) + c/x
Ru = sp.expand(sp.diff(u, x) + u**2 - q)
print("formal series check: coeff of x^1 in u'+u^2-q:", sp.expand(Ru*x**2).coeff(x, 3),
      "-> c = -1, incompatible with rational k >= 0.")

# ---------- (S) symmetric square: no polynomial P of any degree ----------
print("\n== (S) L(P) = P'''-4*q*P'-2*qx*P for monomials ==")
for d in range(0, 7):
    Ld = sp.expand(sp.diff(x**d, x, 3) - 4*q*sp.diff(x**d, x) - 2*qx*x**d)
    P = sp.Poly(Ld, x)
    print(f"d={d}: deg={P.degree()}, LC={P.LC()}  (expect deg d+3, LC -(4d+8))")

# ---------- (B) Lax reduction + b-equation obstructions ----------
print("\n== (B) Lax pair: A=[[0,1],[q,0]], B=[[a,b],[c,-a]] ==")
bf = sp.Function('b')(x)
af = sp.diff(bf, x)/2
cf = bf*q - sp.diff(bf, x, 2)/2
E11 = sp.simplify(sp.diff(af, x) - (bf*q - cf))
E12 = sp.simplify(sp.diff(bf, x) - 2*af)
E21 = sp.diff(cf, x) - x**2 + 2*af*q
bxxx = sp.diff(bf, x, 3)
bx = sp.diff(bf, x)
check = sp.simplify(E21 + (bxxx - 4*q*bx - 2*qx*bf)/2 + x**2)
print("E11 =", E11, "| E12 =", E12, "| E21 + L(b)/2 + x^2 =", check)
print("=> (2,1)-entry vanishes iff L(b) := b'''-4*q*b'-2*qx*b = -2*x^2.")

print("\n== (B) pole obstruction: b = c0*(x-a0)^(-k), k=1..3 ==")
c0, a0 = sp.symbols('c0 a0')
for kk in (1, 2, 3):
    bk = c0*(x - a0)**(-kk)
    Lk = sp.diff(bk, x, 3) - 4*q*sp.diff(bk, x) - 2*qx*bk
    print(f"k={kk}: lim (x-a0)^(k+3)*L(b) =",
          sp.limit(Lk*(x - a0)**(kk + 3), x, a0),
          f"(expect -k(k+1)(k+2)*c0 = {-kk*(kk+1)*(kk+2)}*c0)")

print("\n== (B) degree obstruction: generic polynomial b of degree d ==")
for d in range(0, 5):
    coeffs = sp.symbols(' '.join(f'b{j}' for j in range(d + 1)))
    if d == 0:
        coeffs = (coeffs,)
    Bp = sum(coeffs[j]*x**j for j in range(d + 1))
    Lb = sp.expand(sp.diff(Bp, x, 3) - 4*q*sp.diff(Bp, x) - 2*qx*Bp)
    P = sp.Poly(Lb, x)
    print(f"d={d}: deg L(b)={P.degree()}, LC={P.LC()}  (RHS deg 2; never equal)")
print("\nALL CHECKS DONE")
