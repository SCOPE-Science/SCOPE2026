# Fukuda First-Layer Stabilization over Q(sqrt29) at p = 5

## Context

Greenberg's conjecture predicts that the p-primary parts of class groups in the
cyclotomic Z_p-extension of a totally real field are eventually bounded, i.e.
the Iwasawa invariants lambda_p and mu_p vanish. Fukuda's stabilization theorem
gives an economical route: if every prime above p is totally ramified in the
tower and the first two layers satisfy |A_0| = |A_1|, then |A_n| is constant for
all n and lambda_p = mu_p = 0. The tower over k = Q(sqrt29) at the split prime
p = 5 is a minimal natural odd-prime test case: k has class number 1, so the
entire question concentrates on a single certifiable first-layer computation.

## Definitions

- k = Q(sqrt29), O_k = Z[omega] with omega = (1+sqrt29)/2, m_k(y) = y^2 - y - 7.
- k_infty/k: cyclotomic Z_5-extension; k_n its n-th layer ([k_n:k] = 5^n).
- A_n: 5-primary part of Cl(k_n); |A_0| is the 5-part of h(k).
- Q_1: degree-5 subfield of Q(zeta_25), first layer of the cyclotomic Z_5-extension
  of Q, with m_{Q_1}(x) = x^5 - 10x^3 + 5x^2 + 10x + 1.
- k_1 = k Q_1, [k_1:Q] = 10, [k_1:k] = 5, cyclic of degree 5, with
  m_{k_1}(T) = T^10 - 5T^9 - 45T^8 + 220T^7 + 520T^6 - 2394T^5
    - 2150T^4 + 7635T^3 + 2985T^2 - 1445T - 107.
- epsilon = (5+sqrt29)/2 = 2 + omega, fundamental unit of k, N(epsilon) = -1.
- Fukuda hypothesis: every prime of k above 5 is totally ramified in k_infty/k.

## Result

Let k = Q(sqrt29), k_infty/k its cyclotomic Z_5-extension, k_n the n-th layer,
and A_n the 5-primary part of Cl(k_n). Then

  |A_0| = |A_1| = 1,

the two primes of k above 5 are totally ramified in k_infty/k, and consequently

  lambda_5(k) = mu_5(k) = 0,

i.e. the 5-parts stabilize from the base.

## Proof / Evidence

Base layer. The Minkowski bound M_k = sqrt(29)/2 < 2.7 forces every ideal class
of k to contain an integral ideal of norm <= 2. Since x^2 - x - 7 takes value 1
at 0 and 1 mod 2, it is irreducible mod 2, so 2 is inert in k and no ideal of
norm 2 exists. The only integral ideal of norm <= 2 is (1); hence h(k) = 1 and
|A_0| = 1. Replay: output/artifacts/minkowski_h1.py.

Q_1 certificate. With H = {5th powers mod 25} = {1,7,18,24} and Gaussian periods
eta_j = sum_{a in 2^j H} zeta_25^a, exact arithmetic in Z[x]/(Phi_25) gives
m_{Q_1}(x) = x^5 - 10x^3 + 5x^2 + 10x + 1. It is irreducible over Q (exact QQ
factorization singleton; independently irreducible mod 2), has polynomial
discriminant 5^8 * 7^2 (field discriminant 5^8, so only 5 ramifies), satisfies
m_{Q_1} = (x+1)^5 mod 5 (totally ramified at 5), and is totally real of Galois
group C_5. Replay: output/artifacts/period_Q1.py.

Compositum. Since k is ramified only at 29 and Q_1 only at 5, they are linearly
disjoint; [k_1:Q] = 10 and [k_1:k] = 5 cyclic. The resultant
Res_y(y^2-y-7, m_{Q_1}(T-y)) gives the irreducible degree-10 polynomial m_{k_1}
above, with m_{k_1} = (T+2)^5 (T-1)^5 mod 5. Replay:
output/artifacts/compositum_k1.py.

Splitting and ramification. 29 = 4 mod 5 is a square, so (29/5) = +1 and 5
splits in k: 5 O_k = p_1 p_2, with x^2-x-7 splitting distinctly mod 5 (roots
2,4; derivative nonzero, hence unramified). In k_1 = k Q_1 with Q_1/Q totally
ramified at 5 of degree 5 and k/Q unramified at 5, each p_i has ramification
index dividing 5 but cannot be 1, so e = 5 for each; the mod-5 shape of m_{k_1}
confirms exactly two totally ramified primes above 5. Since the only ramified
prime of Q is 5, every ramified prime of k_infty/k is totally ramified: the
Fukuda hypothesis holds.

Chevalley step. For cyclic k_1/k of prime degree 5 with G = Gal(k_1/k), the
Chevalley-Gras formula with h_k = 1 and two ramified places of e = 5 gives
|Cl(k_1)^G| = (1*5*5)/(5*j) = 5/j with j = [E_k : E_k cap N(k_1^x)] in {1,5}.
Minimality of epsilon is certified by an exact diophantine scan (no unit in
(1,epsilon) among (a+b sqrt29)/2 with (a^2-29b^2)/4 = +-1), so E_k = {+-eps^n}.

Local norm lemma (proved in DRAFT): for totally ramified cyclic degree-5
L_w/K_v with K_v/Q_5 unramified, N(U_{L_w}) = (U_{K_v})^5, so a unit is a local
norm iff it is a local 5th power; for K_v = Q_5 this is u^4 = 1 mod 25. Each
k_{p_i} ~= Q_5 (residue degree 1). Hensel-lifting the mod-5 roots {2,4} gives
omega -> {12,14} mod 25, so epsilon = 2+omega -> {14,16} mod 25. But
14^4 = 16 != 1 and 16^4 = 11 != 1 mod 25, while 5th powers in (Z/25)^x are
exactly {1,7,18,24} (enumerated). Hence epsilon is not a local norm at either
place, so not a global norm; since N(epsilon) = -1 has order prime to 5, j = 5.
Replay: output/artifacts/unit_obstruction.py.

Thus |Cl(k_1)^G| = 1. For a finite 5-group with 5-group action, trivial fixed
points force the group trivial (|A_1| = |Cl(k_1)^G| mod 5), so |A_1| = 1 = |A_0|.

Fukuda stabilization (Fukuda, Proc. Japan Acad. 70A (1994)): total ramification
plus |A_0| = |A_1| implies all |A_n| bounded, so lambda_5(k) = mu_5(k) = 0.

## Limitations

The proof uses standard black-box theorems (Minkowski bound, Dedekind-Kummer,
Hensel lifting, Chevalley ambiguous class number formula, local class field
theory for the norm lemma, Fukuda stabilization). It determines only the
5-primary parts at layers 0-1 and their stabilization; it does not compute full
class groups of k_1 or higher layers, other primes, or neighboring
discriminants.

## Reproducibility

All numerical facts replay with stdlib + sympy exact arithmetic; no class-group
software was used:
  python3 output/artifacts/minkowski_h1.py
  python3 output/artifacts/period_Q1.py
  python3 output/artifacts/compositum_k1.py
  python3 output/artifacts/unit_obstruction.py
Each prints its certificate and writes a JSON log (minkowski_h1.json, m_Q1.json,
m_k1.json, unit_obstruction.json). Polynomial identities, discriminant
factorizations, mod-p shapes, Hensel roots, and fourth/fifth-power enumerations
above were independently re-executed by the auditor with exit 0.

## References

- K. Fukuda, Remarks on Z_p-extensions of number fields, Proc. Japan Acad. Ser. A 70 (1994).
- T. Fukuda & H. Taya, The Iwasawa lambda-invariants of Z_p-extensions of real quadratic fields, Acta Arith. 69 (1995), 277-292.
- T. Fukuda & K. Komatsu, capitulation/Greenberg criteria for real quadratics; Ozaki-Taya, Mizusawa Z_2 studies (method context; different pairs).
- G. Gras, Class Field Theory: From Theory to Practice, Thm. II.4.3.1 (Chevalley-Gras formula).
- LMFDB 2.2.29.1 for base-field cross-check (class number 1; no tower-layer data).
