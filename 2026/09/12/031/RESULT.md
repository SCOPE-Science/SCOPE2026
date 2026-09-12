# Mixed rotation-reflection rank-two Nichols infinitude over D8

## Record statement

Let k be algebraically closed of characteristic zero and
G = D_8 = <r,s | r^4 = s^2 = 1, srs = r^{-1}> (|G| = 8).
Let O_r = {r, r^3} with centralizer <r> ~= C_4 and character chi(r) = i,
and O_s = {s, r^2 s} with centralizer {1, r^2, s, r^2 s} ~= C_2 x C_2
and character psi(r^2) = psi(s) = -1.
Put V_1 = M(O_r, chi), W_1 = M(O_s, psi), V = V_1 (+) W_1.
Then B(V), the Nichols algebra of the 4-dimensional mixed
rotation-reflection Yetter-Drinfeld pair, is infinite-dimensional.

## Context and motivation

The admitted target asked for a dichotomy for exactly this pair:
either a certified minimal infinite Weyl-groupoid word (infinite case)
or a complete finite Cartan graph plus Nichols-relation ledger
(finite case). Finite-dimensional Nichols algebras over non-abelian
groups are sparsely classified (Heckenberger-Vendramin; Heckenberger-
Meir-Vendramin for prime dimension), so deciding a concrete D_8 pair
with an explicit obstruction is a natural classification datum.

## Definitions

- M(O, rho): simple Yetter-Drinfeld module induced from conjugacy
  class O with centralizer character rho; dim = |O| . dim(rho).
- Here dim V_1 = 2 . 1 = 2, dim W_1 = 2 . 1 = 2, dim V = 4.
- Yetter-Drinfeld braiding: c(x (x) y) = x_{(-1)} . y (x) x_{(0)}.
- Diagonal braiding matrix q = (q_{jl}), q_{jl} = eigenvalue of
  deg(e_j) acting on e_l.
- Heckenberger generalized Cartan entry:
  a_{ij} = -min{m >= 0 : (m+1)_{q_{ii}} (q_{ii}^m q_{ij} q_{ji} - 1) = 0}.
- Weyl-groupoid reflections s_1, s_2 on the root lattice; the
  alternating word (s_1 s_2)^infinity is reduced iff ord(s_1 s_2) = infinity.

## Result (headline)

1. V_1 has diagonal braiding q = [[i,-i],[-i,i]] with q_{12} q_{21} = -1.
2. Generalized Cartan matrix C = [[2,-2],[-2,2]], affine type A_1^{(1)},
   absent from the finite rank-two list.
3. With s_1 = [[-1,2],[0,1]], s_2 = [[1,0],[2,-1]],
   M = s_1 s_2 = [[3,-2],[2,-1]] satisfies
   M^k = [[2k+1,-2k],[2k,1-2k]] (!= id) for all k >= 1,
   so ord(s_1 s_2) = infinity and every prefix of (s_1 s_2)^infinity
   is reduced; minimal period 2.
4. Hence dim B(V_1) = infinity, and by braided-subspace inclusion
   B(V_1) hookrightarrow B(V_1 (+) W_1),
   dim B(V_1 (+) W_1) = infinity.

## Proof / evidence

Conjugacy data: O_r = {r, r^3}, C_G(r) = <r>; O_s = {s, r^2 s},
C_G(s) = {1, r^2, s, r^2 s}. Machine-checked from the D_8 presentation.
chi(r) = i is order 4 on <r>; psi(r^2) = psi(s) = -1 extends to the
Klein group since psi(r^2 s) = +1; both checked as homomorphisms over
all pairs.

Basis of V_1: e_0 of degree r (representative 1), e_1 of degree r^3
(representative s, since s r s^{-1} = r^3). YD action:
r . e_0 = chi(r) e_0 = i e_0; r s = s r^3 gives
r . e_1 = chi(r^3) e_1 = -i e_1; r^3 . e_0 = -i e_0;
r^3 s = s r gives r^3 . e_1 = i e_1. Braiding eigenvalues give
q_{11} = q_{22} = i, q_{12} = q_{21} = -i, product -1.

Cartan ledger (char 0 essential): m = 0: (1)_i = 1, i^0(-1)-1 = -2,
product -2 != 0; m = 1: (2)_i = 1+i != 0, i(-1)-1 = -1-i != 0,
product -2i != 0; m = 2: (3)_i = i != 0, i^2(-1)-1 = 0, product 0.
Thus min m = 2 on both rows: a_{12} = a_{21} = -2.

C is affine A_1^{(1)}, not among A_1 x A_1, A_2, B_2, G_2 (and
transposes), so the Weyl groupoid is infinite by Heckenberger's
classification of arithmetic root systems. Explicitly s_i^2 = id and
the closed form for M^k is proved by induction (base k = 1;
M^{k+1} = M M^k is elementary 2x2 algebra), giving infinite order and
13 pairwise distinct alternating prefixes of lengths 0..12, hence all
reduced. Minimality: one-letter words have order <= 2, so infinitude
needs both letters; (s_1 s_2)^infinity has smallest possible period 2.

Transfer: finite-dimensional diagonal Nichols implies finite Weyl
groupoid (Heckenberger 2009; Heckenberger-Schneider); contrapositive
forces dim B(V_1) = infinity (indeed infinite GK-dimension). The
inclusion V_1 -> V_1 (+) W_1 of braided spaces induces an injective
graded braided-Hopf map B(V_1) -> B(V_1 (+) W_1) via Nichols-ideal
functoriality (skew-derivation kernels restrict), so the sum is
infinite-dimensional.

## Limitations

The certificate proceeds via the diagonal rank-two subsystem V_1 and
monotonicity; no full rank-four Weyl-groupoid computation of the
non-diagonal sum and no cross-braidings with W_1 are needed or given.
Classification inputs (finite rank-two list; finite-dim implies finite
groupoid; Nichols functor preserves inclusions) are cited standard
theorems. Characteristic zero is essential: in characteristic 2 the
ledger (2)_i, (3)_i collapses.

## Reproducibility

`output/artifacts/verify_braiding.py` verifies from scratch: D_8
classes/centralizers, chi/psi homomorphisms, q-matrix, Cartan entries,
reflection involutions, M^k closed form for k = 1..8, and 13 distinct
alternating prefixes. Re-run: `python3 output/artifacts/verify_braiding.py`
(expected `ALL CHECKS PASSED`). The infinite-order conclusion uses the
analytic induction formula, not the finite numeric sample alone.

## References

- Heckenberger, Classification of arithmetic root systems, Adv. Math. 2006.
- Heckenberger, Weyl groupoids of rank-two Nichols algebras of diagonal type.
- Heckenberger-Schneider, Right coideal subalgebras of Nichols algebras, Math. Ann.
- Heckenberger-Vendramin, Classification of semisimple YD tuples, JEMS 19 (2017).
- Heckenberger-Meir-Vendramin, Prime-dimension simples, Adv. Math. 2024 (arXiv 2306.02989).
- Andruskiewitsch-Angiono-Heckenberger, finite GK-dimensional diagonal Nichols (affine Cartan infinite).
- Andruskiewitsch-Schneider survey on pointed Hopf algebras.
