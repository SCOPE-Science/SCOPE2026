# Splitting does not imply K-energy properness: an explicit F1 x elliptic counterexample

## Context

The admitted target asks whether, for pairs (X,[omega]) in the family F_en of compact
Kahler threefolds with -K_X nef whose Albanese map is a surjective locally trivial
fibration with Calabi-Yau or rationally connected nef-anticanonical fibre, the Mabuchi
K-energy (equivalently Ding functional) in [omega] is bounded below, respectively proper
modulo automorphisms, if and only if X splits after a finite etale cover as a product of
a torus with Calabi-Yau and rationally connected factors. A complete TARGET resolution is
either a proof of the iff or one fully computed pair refuting at least one direction.

## Definitions

- Y = Bl_1 P^2 = F_1, first Hirzebruch surface, L_Y = -K_Y ample.
- E = C/Lambda an elliptic curve, L_E ample (e.g. O(3.0)), omega_E = c_1(L_E).
- X = Y x E, L_X = pr_Y^*L_Y tensor pr_E^*L_E, [omega] = c_1(L_X).
- Splitting side: X is (after finite etale cover) a holomorphic product torus x RC factor.
- Energy side: Mabuchi K-energy M in [omega] bounded below / proper modulo Aut(X).

## Result

The pair (X,[omega]) lies in F_en, its splitting side is true (X = Y x E is literally a
product, and every connected finite etale cover is Y x E' for an isogenous E'), yet its
Mabuchi K-energy in [omega] is unbounded below with geodesic-ray slope DF_X = DF_Y < 0,
hence not proper modulo automorphisms. This refutes the direction
splitting => bounded-below/proper of the target equivalence. The converse direction is untouched.

## Proof / evidence

1. F_en membership: X is a compact Kahler 3-fold; -K_X = pr_Y^*(-K_Y) is nef (ample on Y,
trivial on E); Alb(X) = E since Y is simply connected, and a = pr_E : X -> E is a smooth
surjective locally trivial fibration with every fibre Y rationally connected with nef -K.

2. Fibre instability: the anticanonical polytope of Y is the quadrilateral
Q = {x >= -1, y >= -1, -1 <= x+y <= 1} with vertices (-1,0),(0,-1),(2,-1),(-1,2).
Writing Q = T \ S with T = conv{(-1,-1),(-1,2),(2,-1)} (area 9/2, centroid (0,0)) and
S = conv{(-1,-1),(-1,0),(0,-1)} (area 1/2, centroid (-2/3,-2/3)), exact arithmetic gives
area(Q) = 4 and centroid(Q) = (1/12,1/12) != (0,0), reproduced by the exact Fraction
script output/artifacts/compute_barycenter.py. By the toric Futaki-barycentre criterion
(Futaki-Ono; Donaldson), Fut(Y) != 0, so a product test configuration on Y has DF_Y < 0.

3. Product slope: from any test configuration (Y,L_Y) form X = Y x E over P^1 with E
constant and C*-action trivial on E. Since K_X-pullback comes from Y, intersection
theory gives (L_X^4)-type terms and (K_X . L_X^3)-type terms scaled by the common positive
factor (L_E), which cancels in the normalized Donaldson-Futaki invariant; independently,
mu_X = (2/3) mu_Y. Hence DF_X = DF_Y < 0. The Mabuchi slope formula
(Donaldson; Berman-Berndtsson-Sjostrand; Boucksom-Hisamoto-Jonsson) gives
lim M(phi_t)/t = DF_X < 0, so M(phi_t) -> -infinity linearly; infimum -infinity.
The metric splits as p_Y^*omega_{Y,t} + p_E^*omega_E with scalar curvature additive, so
M_X = (L_E).M_Y + const. Since properness implies bounded below, M is neither bounded
below nor proper modulo Aut; quotienting by Aut(X)^0 (containing E-translations) cannot
absorb a Y-direction linear decrease. The Ding functional shares the negative slope for
this Y-direction configuration; the Mabuchi conclusion alone suffices for the refutation.

4. Splitting verification: X is already torus x rationally connected; pi_1(X) = Lambda,
so connected finite etale covers are exactly Y x E', all products.

## Limitations

Refutes only the splitting-implies-energy direction for one explicit ample class
c_1(pr_Y^*(-K_Y) boxtimes L_E) on one explicit threefold. No verdict on the converse
(bounded/proper => splitting). DF negativity uses the classical toric criterion plus the
product intersection formula rather than a newly evaluated named 1-PS. The Aut-quotient
argument is qualitative; no explicit J^A estimate is computed.

## Reproducibility

Run python3 output/artifacts/compute_barycenter.py (exact fractions, asserts
area T = 9/2, S = 1/2, Q = 4 and centroid Q = (1/12,1/12)). The DF sign preservation is a
pencil-and-paper intersection computation checkable from the formulas in the DRAFT.

## References

Cao - Albanese maps of projective manifolds with nef anticanonical bundles; Naumann-Wu -
Albanese map for Kahler manifolds with nef anticanonical bundle; Li-Xu - special test
configurations and K-stability; Tian/Donaldson - K-stability and Futaki invariant;
Futaki-Ono, Wang-Zhu - toric Fano Futaki and solitons; Boucksom-Hisamoto-Jonsson and
Berman-Berndtsson-Sjostrand - non-Archimedean/Mabuchi slope formulas; product theorem
for K-stability; Cheltsov - Calabi problem for Fano threefolds (background survey).
