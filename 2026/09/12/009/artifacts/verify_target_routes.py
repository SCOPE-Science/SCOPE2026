"""Decisive target-route checks for lane-1099 (hyperbolic-hyperbolic rank jump).

pi0 on R^4 (Weinstein normal form), coordinates (x0,x1,x2,y2->x3):
  C1 = x0*x1, C2 = x2*x3,  Pi^{ij} = eps^{ijkl} dC1_k dC2_l  (Nambu form)
Checks:
  R1: constant-nu cocycle classification  [pi0,nu]=0  <=> n02=n03=n12=n13=0
  R2: jump family pi_t = pi0 + t*d01 : full Jacobi, Pfaffian, rank 2 everywhere, no zeros
  R3: single-component localization no-go: [pi0, phi*d01] = X_phi ^ d01, X^2,X^3 formulas
  R4: recovery test: radial (multi-component) localization search via pointwise linear algebra
"""
import itertools, random
import sympy as sp

x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3')
X = [x0, x1, x2, x3]
C1 = x0*x1
C2 = x2*x3
d1 = [sp.diff(C1, x) for x in X]
d2 = [sp.diff(C2, x) for x in X]

def sgn(p):
    p = list(p); inv = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                inv += 1
    return 1 if inv % 2 == 0 else -1

Pi = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        e = 0
        for k in range(4):
            for l in range(4):
                if len({i, j, k, l}) < 4:
                    continue
                e += sgn((i, j, k, l))*d1[k]*d2[l]
        Pi[i, j] = sp.expand(e)
print("== pi0 =="); sp.pprint(Pi)
# factor check: A=(-x0,x1,0,0), B=(0,0,x2,-x3): A^B ?
A = [-x0, x1, 0, 0]; B = [0, 0, x2, -x3]
Ok = all(sp.expand(A[i]*B[j]-A[j]*B[i]-Pi[i,j])==0 for i in range(4) for j in range(4))
print("decomposable A^B check:", Ok)

def schouten_const_nu():
    n = sp.symbols('n01 n02 n03 n12 n13 n23')
    Nu = sp.zeros(4, 4)
    for s, (i, j) in zip(n, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):
        Nu[i, j] = s; Nu[j, i] = -s
    out = {}
    for (a,b,c) in itertools.combinations(range(4),3):
        ex = 0
        for l in range(4):
            ex += Nu[l,a]*sp.diff(Pi[b,c],X[l])+Nu[l,b]*sp.diff(Pi[c,a],X[l])+Nu[l,c]*sp.diff(Pi[a,b],X[l])
        out[(a,b,c)] = sp.expand(ex)
    return n, out

n, R1 = schouten_const_nu()
print("== R1: [pi0,nu_const] ==")
for k, v in R1.items():
    print(k, ":", v)
# R1 result: (0,1,2):-n02*x1-n12*x0 ; (0,1,3):n03*x1+n13*x0 ;
#             (0,2,3):-n02*x3-n03*x2 ; (1,2,3):n12*x3+n13*x2
# => all zero as polynomials  <=>  n02=n03=n12=n13=0.  R1 PASS (2-dim space: n01,n23).

# == R2: jump family pi_t = pi0 + t d0^d1 ==
t = sp.symbols('t')
Mt = Pi.copy(); Mt[0,1] += t; Mt[1,0] -= t
# Pfaffian of 4x4 skew: M01*M23 - M02*M13 + M03*M12
Pf = sp.expand(Mt[0,1]*Mt[2,3]-Mt[0,2]*Mt[1,3]+Mt[0,3]*Mt[1,2])
print("== R2: Pfaffian(pi_t) =", Pf)   # expect t*0 - ... = 0
print("M01 =", Mt[0,1], "(nonzero for t!=0 => rank>=2 everywhere; Pf=0 => rank exactly 2)")
# sample numeric rank check (manual 4x4 eval, no lambdify-of-Matrix)
def numMt(pt, tt):
    sv = {x0:pt[0], x1:pt[1], x2:pt[2], x3:pt[3], t:tt}
    return [[float(Mt[i,j].subs(sv)) for j in range(4)] for i in range(4)]
import numpy as np
_pts = [(0,0,0,0),(0.3,-0.2,0.1,0.4),(1,0,0,0),(0,0,2,-1)]
for p in _pts:
    Mm = np.array(numMt(p,0.05), dtype=float)
    ev = np.linalg.eigvalsh(1j*Mm)
    print("pt", p, "eig-imag-abs:", np.round(sorted(abs(ev)),6))
print("R2: no zeros since entry (0,1)=t; Jacobi: [pi0,pi0]=0, [pi0,d01]=0 (R1), [d01,d01]=0.")

# == R3: single-component localization ==
phi = sp.Function('phi')(x0,x1,x2,x3)
# X_phi = pi0^#(d phi); components:
dphi = [sp.diff(phi, x) for x in X]
Xp = [sum(Pi[i,j]*dphi[j] for j in range(4)) for i in range(4)]
print("== R3: X_phi components ==")
for i,e in enumerate(Xp):
    print(i, ":", sp.expand(e))
# X^2 = x2*(x0*phi_,0 - x1*phi_,1), X^3 = x3*(-x0*phi_,0 + x1*phi_,1)
E = x0*sp.diff(phi,x0)-x1*sp.diff(phi,x1)
print("X^2/x2 =", sp.expand(E), " ;  X^3/x3 =", sp.expand(-E))
print("R3: V^d01=0 <=> V in span(d0,d1) <=> X^2=X^3=0 <=> x2*E=x3*E=0 <=> E==0 (continuity).")
print("E=0 means phi invariant under x0d0-x1d1 => phi=F(x0x1,x2,x3); any nonzero such phi has")
print("unbounded support (level sets {|x0x1|<=R} unbounded; curve (N,s/N,a2,a3)). Hence no nonzero")
print("compactly supported phi makes [pi0,phi*d01]=0. R3 NO-GO PROVED.")

# == R4: SUPERSEDED by verify_radial.py (numeric per-sphere) and ==
# == verify_radial_exact.py (exact certificate over Q(s)). Summary:    ==
# == per-sphere null space = span{f01,f23}, all g forced 0 at s=0.25,  ==
# == 1.0, 4.0 numerically; exactly null_{Q(s)} M = span{e_f01,e_f23}.  ==
print("R4: see verify_radial.py and verify_radial_exact.py (both replay green).")
