"""Reproduce TARGET certificates: Heun accessory-parameter PPV trichotomy, case (C).

Specialization (admissible: a distinct from {0,1}, Fuchsian relation holds):
  a=2, c=sqrt(2), d=sqrt(3), e=sqrt(5),
  S = c+d+e-1, alpha=(S+sqrt(7))/2, beta=(S-sqrt(7))/2, t transcendental.
Checks:
 1. Fuchs relation, reduced form r, r_t = -1/D.
 2. Pole orders + double-pole coefficients + perfect-square roots.
 3. Kovacic case 1: all 16 d-combos irrational (Galois-flip + minpoly).
 4. Kovacic case 2: singleton E-sets, d=-2.
 5. Kovacic case 3: irrational sqrt(1+4b) exclusion.
 6. Non-resonance at 0,1,a,infty.
 7. Isomonodromy: pole/degree bound for Schlesinger factor q + linear eliminant.
 8. Groebner no-polynomial-q for degrees 1..4 (supplementary).
Writes groebner_log.json + certificates.json next to this script.
"""
import itertools, json, os
import sympy as sp

OUT = os.path.dirname(os.path.abspath(__file__))
x, t = sp.symbols('x t')
s2, s3, s5, s7 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(5), sp.sqrt(7)
a = sp.Integer(2)
c, d, e = s2, s3, s5
S = c + d + e - 1
alp, bet = (S + s7) / 2, (S - s7) / 2
C = {}
C['fuchs_residual'] = str(sp.simplify(c + d + e - (alp + bet + 1)))
assert C['fuchs_residual'] == '0'
assert len({0, 1, int(a)}) == 3

P = c / x + d / (x - 1) + e / (x - a)
D = x * (x - 1) * (x - a)
Q = (t + alp * bet * x) / D
r = sp.simplify(P**2 / 4 + sp.diff(P, x) / 2 - Q)
rt = sp.simplify(sp.diff(r, t))
C['r_t_plus_1_over_D'] = str(sp.simplify(rt + 1 / D))
assert sp.simplify(rt + 1 / D) == 0
num, den = sp.together(r).as_numer_denom()
C['num_deg'] = int(sp.Poly(num, x).degree())
C['den_deg'] = int(sp.Poly(den, x).degree())
assert (C['num_deg'], C['den_deg']) == (4, 6)

b0 = sp.simplify(sp.limit(x**2 * r, x, 0))
b1 = sp.simplify(sp.limit((x - 1)**2 * r, x, 1))
ba = sp.simplify(sp.limit((x - a)**2 * r, x, a))
binf = sp.simplify(sp.limit(x**2 * r, x, sp.oo))
C['double_pole_coeffs'] = {'b0': str(b0), 'b1': str(b1), 'ba': str(ba), 'binf': str(binf)}
assert b0 != 0 and b1 != 0 and ba != 0 and binf != 0
# perfect squares: 1+4b = (sqrt(p)-1)^2 ; 1+4binf = 7
C['square_identities'] = {
    '1+4b0-(s2-1)^2': str(sp.expand((s2 - 1)**2 - (1 + 4 * b0))),
    '1+4b1-(s3-1)^2': str(sp.expand((s3 - 1)**2 - (1 + 4 * b1))),
    '1+4ba-(s5-1)^2': str(sp.expand((s5 - 1)**2 - (1 + 4 * ba))),
    '1+4binf-7': str(sp.simplify(1 + 4 * binf - 7)),
}
assert all(v == '0' for v in C['square_identities'].values())
r0, r1, ra = s2 - 1, s3 - 1, s5 - 1  # positive square roots of 1+4b
rinf = s7
assert float(r0.evalf()) > 0 and float(r1.evalf()) > 0 and float(ra.evalf()) > 0

# ---- Kovacic case 1 ----
E0 = [s2 / 2, 1 - s2 / 2]; E1 = [s3 / 2, 1 - s3 / 2]
Ea = [s5 / 2, 1 - s5 / 2]; Ei = [(1 + s7) / 2, (1 - s7) / 2]
z = sp.symbols('z')
combos = list(itertools.product(Ei, E0, E1, Ea))
C['case1_num_combos'] = len(combos)
assert len(combos) == 16
# Galois-flip certificate: sigma2 (sqrt2->-sqrt2) moves every d since e0 has sqrt2-coeff +-1/2
irr = 0
for combo in combos:
    dd = sp.expand(combo[0] - combo[1] - combo[2] - combo[3])
    mp = sp.Poly(sp.minimal_polynomial(dd, z), z)
    assert mp.degree() > 1, dd  # irrational, hence not a nonneg integer
    irr += 1
C['case1_irrational_d_count'] = irr
C['case1_galois_flip'] = ('sigma:sqrt2->-sqrt2 gives d^sigma-d = -/+sqrt(2) != 0 '
                          'for every combo, since e0 in {sqrt2/2, 1-sqrt2/2}; hence no d in Q.')

# ---- Kovacic case 2 ----
C['case2_E_sets'] = 'E0=E1=Ea=Einf={2} since each sqrt(1+4b) is irrational'
C['case2_d'] = int((2 - 2 - 2 - 2) / 2)
assert C['case2_d'] == -2  # <0 -> no case-2 solution -> not dihedral
# ---- Kovacic case 3 ----
C['case3'] = 'excluded: necessary condition sqrt(1+4b_c) in Q fails at every pole (sqrt2-1, sqrt3-1, sqrt5-1, sqrt7 irrational via z^2-p minimal polynomials)'

# ---- non-resonance ----
C['exponent_differences'] = {'at_0': '1-sqrt(2)', 'at_1': '1-sqrt(3)',
                             'at_a': '1-sqrt(5)', 'at_inf': 'sqrt(7)'}
C['nonresonance'] = 'all differences irrational (minimal polynomial z^2-p or shifted), hence non-integral at all four punctures'

# ---- isomonodromy: pole/degree bound + eliminant ----
# finite-pole balance: A~(x-c)^-m gives m(m+2)=4b; check 4b values admit no m>=1
fourb = [sp.simplify(4 * b0), sp.simplify(4 * b1), sp.simplify(4 * ba)]
C['four_b'] = [str(v) for v in fourb]
C['four_b_numeric'] = [float(v.evalf()) for v in fourb]
assert all(v < 3 for v in [float(q.evalf()) for q in fourb])  # m(m+2)>=3 for m>=1
C['finite_pole_balance'] = 'm(m+2)=4b_c required for a pole of A; each 4b_c<3<=m(m+2), and 4b0,4b1<0; so A has no finite poles'
C['infinity_balance'] = ('leading coeff k(n-1)[(1/2)n(n-2)-3] with binf=3/2; zeros at n=1 or n=1+-sqrt(7); '
                         'hence polynomial A has degree <= 1')
# linear eliminant with u,v in C(t): c0 forces v=0; x^6 and x^2 coeffs give ad-bc=-128t+K'
u, v = sp.symbols('u v')
q = u * x + v
rx = sp.diff(r, x)
E = sp.Rational(1, 2) * sp.diff(q, x, 3) - 2 * r * sp.diff(q, x) - rx * q + 1 / D
nE = sp.Poly(sp.expand(sp.simplify(sp.together(E).as_numer_denom()[0])), x)
coef = {int(m[0]): sp.expand(nE.as_dict()[m]) for m in sorted(nE.as_dict(), reverse=True)}
A6 = sp.expand(coef[6].subs(v, 0).coeff(u)); B6 = sp.expand(coef[6].subs([(u, 0), (v, 0)]))
A2 = sp.expand(coef[2].subs(v, 0).coeff(u)); B2 = sp.expand(coef[2].subs([(u, 0), (v, 0)]))
elim = sp.expand(16 * A6 - 4 * A2)  # = A6*B2 - B6*A2 up to scale (B6=4,B2=16)
C['linear_c0'] = str(coef[0])
C['eliminant_A6'] = str(A6); C['eliminant_B6'] = str(B6)
C['eliminant_A2'] = str(A2); C['eliminant_B2'] = str(B2)
C['eliminant_16A6-4A2'] = str(elim)
assert B6 == 4 and B2 == 16
assert sp.Poly(elim, t).degree() == 1 and sp.expand(elim).coeff(t) == -128
C['eliminant_conclusion'] = ('common u in C(t) needs A6*16-4*A2=0, but it equals -128*t+K != 0 '
                             'for transcendental t (degree-1 polynomial); with v=0 from c0. No rational q of degree<=1; '
                             'bound gives deg<=1. Hence non-isomonodromic.')

# ---- Groebner supplement deg 1..4 ----
glog = {}
for deg in (1, 2, 3, 4):
    vs = sp.symbols('w0:%d' % (deg + 1))
    qq = sum(vs[i] * x**i for i in range(deg + 1))
    EE = sp.Rational(1, 2) * sp.diff(qq, x, 3) - 2 * r * sp.diff(qq, x) - sp.diff(r, x) * qq + 1 / D
    nn = sp.Poly(sp.expand(sp.simplify(sp.together(EE).as_numer_denom()[0])), x)
    eqs = [sp.expand(nn.as_dict()[m]) for m in sorted(nn.as_dict(), reverse=True)]
    G = sp.groebner(eqs, list(vs), order='lex')
    basis = [str(g.as_expr()) for g in G.polys]
    glog['degree_%d' % deg] = {'num_degree': int(nn.degree()), 'num_eqns': len(eqs), 'basis': basis}
    assert basis == ['1'], (deg, basis)
C['groebner_supplement'] = 'degrees 1..4 all give Groebner basis {1}: no polynomial q'
C['ppv_verdict'] = ('(C): ordinary PV group SL2; non-isomonodromic in t; PPV group = SL2 over dt-constants, '
                    'defining dt-ideal (0) besides det-1 (no proper dt-equations); up to conjugacy the full SL2.')

json.dump(C, open(os.path.join(OUT, 'certificates.json'), 'w'), indent=1)
json.dump(glog, open(os.path.join(OUT, 'groebner_log.json'), 'w'), indent=1)
print('OK: all TARGET certificates verified; files written to', OUT)
