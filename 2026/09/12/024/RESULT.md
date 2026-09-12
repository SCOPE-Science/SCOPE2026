# 7-Maximality of Cyclotomic Units at the First Layer of the Cyclotomic Z_7-Extension of Q(sqrt(2))

## Context and motivation

Let k = Q(sqrt(2)) and let k_infty/k be the cyclotomic Z_7-extension with first layer k_1.
The base field has class number 1 and fundamental unit eps = 1+sqrt(2) of norm -1.
The prime 7 splits in k as (3+sqrt(2))(3-sqrt(2)), so exactly two primes ramify in
the degree-7 cyclic extension k_1/k, each totally ramified. A central Iwasawa question
(Greenberg's conjecture for this real base field and p=7) is whether the 7-primary
class groups stabilize trivially, equivalently whether the cyclotomic units already
generate the full units up to index prime to 7 at the first layer, and whether the
Iwasawa invariants lambda_7(k) and mu_7(k) vanish. The degree-14 field k_1 has
conductor lcm(8,49) = 392, a non-semisimple case (7 divides the degree) where
algebraic and arithmetic isotopic components can differ, so the 7-part must be
checked explicitly rather than quoted from a semisimple main conjecture.

## Definitions

- k = Q(sqrt(2)), O_k its ring of integers, disc(k) = 8, h(k) = 1.
- Q_infty/Q is the cyclotomic Z_7-extension with [Q_n:Q] = 7^n; k_n = k Q_n.
- G = Gal(k_1/k) is cyclic of order 7; [k_1:Q] = 14 with Gal(k_1/Q) cyclic of order 14.
- E(K) denotes the full unit group of a number field K.
- C(K) denotes the Sinnott-Washington group of cyclotomic (circular) units at a
  finite layer; Washington's group, Leopoldt's group F, and Sinnott's group differ
  pairwise by 2-powers at finite layers, and every 2-power is a 7-adic unit, so all
  three carry identical 7-part information.
- j = [E(k) : E(k) cap N_{k_1/k}(k_1^times)] is the unit-norm index.
- A_n is the 7-primary part of Cl(k_n); lambda_7, mu_7 are the cyclotomic Iwasawa
  invariants of k.

## Result

Theorem. Let k_1 be the first layer of the cyclotomic Z_7-extension of Q(sqrt(2)).
With fixed Sinnott-Washington conventions, 7 does not divide [E(k_1):C(k_1)].
Equivalently the cyclotomic units at k_1 are 7-maximal. Moreover 7 does not divide
h(k_1), and the Iwasawa invariants satisfy lambda_7(k) = mu_7(k) = 0.

## Proof and evidence

Setup. Since [k:Q] = 2 is prime to 7, k cap Q_infty = Q and [k_1:k] = 7 cyclic.
Kronecker and the explicit factorization 7 = (3+sqrt(2))(3-sqrt(2)) of norm 7 give
7 O_k = p_+ p_- with residue fields F_7. Minkowski bound (1/2)sqrt(8) approx 1.414 < 2
gives h(k) = 1. The extension k_1/k is the base change of Q_1/Q, hence ramified only
at the two primes above 7, each totally ramified with e = 7, so the product of
ramification indices is 49.

Chevalley step. For cyclic K/k of prime degree l = 7, Chevalley/Gras gives
|Cl(K)^G| = h(k) (prod e_v)/(l j). Here h(k) = 1, prod e_v = 49, l = 7, so
|Cl(k_1)^G| = 49/(7j) = 7/j.

Local norm step (j = 7). E(k) = {+-1} x <eps>, so j lies in {1,7} and j = 7 iff
eps is not a global norm. By Hasse, a global norm is a local norm at p_+, p_-.
At p = p_pm, k_p = Q_7 and (k_1)_p/Q_7 is totally ramified cyclic of degree 7 inside
Q_7(zeta_49), of conductor dividing 49. Local reciprocity gives unit norms of index
7; with 1+49 Z_7 contained in the norms, the norm subgroup of Z_7^times is the unique
index-7 subgroup containing 1+49 Z_7, detected mod 49. Since (Z/49)^times is cyclic
of order 42, its unique order-6 subgroup is H = {u : u^6 = 1 mod 49}
= {1,18,19,30,31,48}, equal to the 7th powers; on units of a totally ramified
extension the norm is congruent to the 7th power mod the maximal ideal, giving the
test u in N(L^times) iff u^6 = 1 mod 49. Now sqrt(2) mod 49 is 10 or 39, so eps
embeds as 11 or 40. Direct powers give 11^6 = 15 and 40^6 = 36 mod 49, neither 1,
so eps is not a local norm at either place, hence not a global norm. Thus j = 7.
Exact integer certificate: eps^3 = 7+5 sqrt(2), eps^6 = 99+70 sqrt(2), and
N(eps^6-1) = 98^2 - 2(70^2) = -196 = -4 x 49.

Class group. With j = 7, |Cl(k_1)^G| = 1. The G-fixed subgroup of the 7-Sylow is
trivial; a finite 7-group with trivial fixed points under a 7-group action is
trivial by the class equation, so 7 does not divide h(k_1).

Index-class bridge. Apply the real Gras chi-formula (Theorem 7.5 of
arXiv:2112.02865, Leopoldt analytic formula in chi-form):
#H^ar_chi = w_chi (E_{K_chi} : Eb_{K_chi} F_{K_chi}) with w = 1 for non-prime-power
character order, and w = 1 for prime-power order with prime-power conductor.
For K = k_1 of conductor 392 = 8 x 49, Gal(K/Q) is C_14 with rational character
census {1:1, 2:1, 7:6, 14:6}: order 2 (conductor 8, case iii'), order 7 (conductor 49,
case ii'), order 14 (non-prime-power, case i), all w = 1. Faithful components use
A_1 = 0; order-7 components use K_chi = Q_1 with Chevalley |Ambig| = 1 x 7/(7 x 1) = 1
(j = 1 since N(-1) = (-1)^7 = -1) giving trivial 7-class group; order-2 component uses
k = Q(sqrt(2)) of prime-power conductor with [E:C] = h = 1. Decomposition data
ord_49(2) = 21 with Frobenius order 7 (2 inert in Q_1), e/f/g at 2 and 7, and
Omega 7-unit psi(Omega) = 2 are logged. Summing 7-parts gives v_7[E_K:F_K] = 0, and
Sinnott/Washington/Leopoldt transfer preserves 7-parts, so 7 does not divide
[E(k_1):C(k_1)].

Iwasawa. A_0 = 0 (h = 1) and A_1 = 0 give two consecutive trivial coinvariants, so
Fukuda stabilization (Fukuda 1994) with Nakayama forces X_infty = 0, hence
lambda_7(k) = mu_7(k) = 0.

## Limitations

The lambda/mu vanishing invokes Fukuda stabilization from A_0 = A_1 = 0, cited
rather than re-proved. No PARI/Sage class-group computation of the degree-14 field
was needed because the Chevalley-norm route bypasses it. The bridge uses the
published chi-formula with per-character verification for this conductor; it does
not compute Sinnott's (R:U) module directly. Convention comparison is finite-layer
only; Kucera's projective-limit subtlety does not apply.

## Reproducibility

The pure-stdlib script output/artifacts/verify_target.py replays every integer:
Minkowski bound, splitting, sqrt(2) lifts {10,39}, eps residues {11,40}, sixth powers
{11:15, 40:36}, (Z/49)^times census (phi 42, |H| 6, 7th powers = H), N(eps^6-1) = -196,
Chevalley 49/(7 x 7) = 1, C_14 character census with w = 1 for all orders (V7a),
Q_1 Chevalley (V7b), ord_49(2) = 21 with Frobenius order 7 and e/f/g data (V7c),
Omega 7-unit (V7d), 2-powers prime to 7 (V7e); output VERIFY_OK.

## References

- Sinnott, On the Stickelberger ideal and the circular units of an abelian field,
  Invent. Math. 1980; Washington, Introduction to Cyclotomic Fields, Ch. 8.
- Chevalley 1933; Gras, Class Field Theory, Thm. IV.4; Hasse norm theorem; Serre,
  Local Fields, Ch. XIII-XV.
- Fukuda, Remarks on Z_p-extensions, 1994; Fukuda, Math. Comp. 1996.
- Gras, Application of the notion of Phi-object, arXiv:2112.02865, Theorem 7.5
  (= Leopoldt Satz 21 in chi-form), Remark 7.7; Gras, arXiv:2306.12836, Prop. 3.4.
- Leopoldt 1953 Satz 21 and 1962; Ouyang arXiv:math/9911031 Thm 1.2; Pagani
  arXiv:2202.02844 App. A; Kucera, JTNB 15 (2003), 223.
