# Exact ordinary chromatic number 3 for the verified-generating SL(3,Z) Cayley cell and a radius-1 local-rule no-go

## Context

Let Gamma = SL(3,Z), S_gen = {E12^+-1, E21^+-1, E23^+-1, E32^+-1} (8 distinct
symmetric elements), X = Free(2^Gamma) the free part of the Bernoulli shift,
G = G(S_gen, X) the 8-regular Schreier graph. KST gives chi_B(G) <= 9.
The admitted target sought chi_M(G) <= 4 < 5 <= chi_B(G) via a Marks game;
the preset fallback sought an explicit Borel 7-rule C0. Both Borel halves are
documented as blocked; this record claims only what is proved below.

## Definitions

- Right Cayley graph Cay(Gamma, S_gen): g ~ gs for s in S_gen.
  Left-Cayley version follows via the inversion isomorphism
  c'(g) = q(pi(g)^{-1}).
- pi: Gamma -> SL(3,F2) reduction mod 2; Gamma(2) = ker(pi), index 168.
- Radius-1 window W = {e} union S_gen (9 points); patterns in {0,1}^W.
  For s in S_gen, patterns p, q are s-consistent iff
  p(w) = q(sw) for all w in W cap s^{-1}W.

## Result

Theorem A (exact ordinary chromatic number).
chi(Cay(SL(3,Z), S_gen)) = 3.

Lemma B (radius-1 local Borel 7-rule no-go).
No coloring rule C0(x) = f(x|_{B_1(e)}) depending only on the 9-point
radius-1 window properly colors G(S_gen, X) with 7 colors.

## Proof / evidence

Generation (verified): [E12,E23] = E13 and [E32,E21] = E31 by exact 3x3
integer arithmetic (`gen_check.py` -> GEN_CHECK_OK); hence <S_gen> contains
all six elementary matrices, so <S_gen> = SL(3,Z). The 8 listed elements
are distinct, all det 1.

Theorem A lower bound: the word w = abAcaBcAC (a=E12, b=E21, c=E23,
A=E12^{-1}, B=E21^{-1}, C=E23^{-1}), length 9, evaluates exactly to I
(machine-checked integer multiplication in `quotient_exact_chi3.py`),
so the Cayley graph has a closed odd walk, is not bipartite: chi >= 3.

Theorem A upper bound: mod-2 images of the four base generators are 4
distinct nontrivial elements of SL(3,F2) (no loops); BFS closure has
exactly 168 = |SL(3,F2)| elements, so pi surjects onto the quotient Cayley
graph. That 168-vertex graph admits a proper 3-coloring found by exhaustive
search (169 search nodes; properness re-verified edge by edge in the same
script). Pullback c = q o pi is proper (pi(gs)=pi(g)pi(s)). Hence chi <= 3.

Lemma B: for fixed s, all patterns vanishing on O union J (O = W cap s^{-1}W,
J = sO cap W) are pairwise s-consistent, forming a clique in the pattern
graph. Exact computation gives |O|=2, |O union J|=3 for every s in S_gen,
hence a clique of size 2^6 = 64 in the 512-vertex pattern graph, verified
pairwise (`fallback_radius1_clique.py` -> verified=True for all 8).
A radius-1 rule into 7 colors would 7-color the pattern graph, impossible.

Consistent certificates: B_1 (n=9) chi=2, B_2 (n=57) chi=2, B_3 (n=325)
3-colorable, B_4 (n=1729) exact 3-coloring (1730 nodes), B_5 (n=8409)
3-coloring, B_3 max clique 2, no reduced odd identity word length <= 7
(1729 endpoints), length-9 witness above is shortest found.

Measurable remark (unproved, not claimed): the periodic 3-coloring q o pi
is Gamma(2)-invariant, but transfer to a measurable coloring of the shift
graph would need a measurable equivariant phi: X -> Gamma/Gamma(2), which
is unavailable (Gamma(2)-action on (X, product measure) is ergodic);
chi_M(G) <= 3 remains an explicitly unproved conjecture here.

## Limitations

- chi_B(G) remains open in [3,9]; nothing decides Borel 4-colorability.
- chi_M(G) <= 3 (and the target's chi_M <= 4) is unproved here; the proved
  chi=3 is ordinary and does not transfer to Borel or measurably.
- The length-9 odd word is shortest found (<=7 excluded), not proved
  globally shortest. Borel Brooks <= 8 quoted as context only.

## Reproducibility

Standard library Python only:
- python3 artifacts/gen_check.py -> GEN_CHECK_OK
- python3 artifacts/quotient_exact_chi3.py -> EXACT_CHI3_CERTIFIED
- python3 artifacts/fallback_radius1_clique.py -> verified=True x 8
- python3 artifacts/odd_girth_bounds.py -> ODD_BOUNDS_OK
- python3 artifacts/chi_balls_B4B5.py 4 -> BALLS_CERTIFIED

## References

- Kechris-Solecki-Todorcevic bound chi_B <= Delta+1 (here <= 9).
- Marks 2016 determinacy approach (existential n-regular acyclic chi_B=n+1).
- Bernshteyn 2105.11557 Borel fractional colorings (fractional only).
- Conley et al. 1611.02204 hyperfinite classification (elsewhere).
- Conley-Kechris 2013 measurable/property-(T) calibration.
- Gao et al. 2401.13866 abelian 2chi-1 (Z^n, not SL(3,Z)).
- Brandt et al. 2024 homomorphism-graph Sigma^1_2-completeness.
- Garcia-Marco/Knauer arXiv:2405.19543 minimal Cayley graphs (nilpotent/dihedral <=3; inapplicable to SL(3,Z)).
