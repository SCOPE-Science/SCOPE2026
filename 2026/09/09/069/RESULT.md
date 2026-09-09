# No binary self-dual [48,24] code admits an order-15 automorphism of type 15-(3;3)

## Context
Classification of extremal binary doubly-even self-dual (Type II) codes is a
recognized benchmark (Mallows–Sloane bound, Conway–Sloane, Rains shadow
bounds, Harada–Kitazume program). At length 48 the extremal bound gives
d = 12; the extremal enumerator exists (quadratic-residue code q48) but the
automorphism-window classification is incomplete. The complete census of
doubly-even self-dual codes stops at length 40 (Betsumiya–Harada–Munemasa).
Order 15 = 3 × 5 was the hard gap-closer at length 96
(Bouyuklieva–Willems–Yankov). At n = 48 the arithmetically forced maximal
long-cycle order-15 window is three 15-cycles plus three fixed points
(3 × 15 + 3 = 48), type 15-(3;3).

## Definitions
- Binary self-dual [48,24]: subspace C ⊆ F_2^48 with dim C = 24 and C = C^⊥
  under the standard dot product. Includes singly- and doubly-even codes of
  any minimum distance; extremal Type II [48,24,12] is the special case.
- Type 15-(3;3): permutation with three cycles of length 15 and three fixed
  points.
- For a permutation τ preserving C, C(τ) = C ∩ Fix(τ) is the fixed subcode.

## Result (headline claim)
No binary self-dual [48,24] code — in particular no extremal doubly-even
self-dual [48,24,12] code — admits a permutation automorphism σ of order 15
with cycle type 15-(3;3).

The obstruction is uniform over all orbit-weight cases, hence stronger than
a per-case MacWilliams-shadow ledger: the window is infeasible in every case.

## Proof / evidence
Let σ of type 15-(3;3) preserve self-dual C ⊆ F_2^48 and put τ = σ^5.

1. **Descent of cycle type.** Each 15-cycle raised to the 5th power splits
   into 5 cycles of length 3 (residue classes mod 5, since gcd(15,5) = 5).
   Three 15-cycles give fifteen 3-cycles; the three σ-fixed points stay
   fixed. Hence τ has type 3-(15;3): fifteen 3-cycles plus three fixed
   points, order exactly 3. Cycle type is a conjugacy invariant, so checking
   one representative covers every σ of type 15-(3;3).

2. **Fixed-subcode self-duality (odd-order lemma).** Let τ be an odd-order
   permutation automorphism of a binary self-dual code, all of whose orbit
   lengths are odd. With m = order(τ) odd and
   π(v) = Σ_{i=0}^{m-1} τ^i v, π projects V onto Fix(τ), and for
   w ∈ Fix(τ), ⟨π(v),w⟩ = ⟨v,w⟩. Since each orbit length is odd, the orbit
   characteristic vectors satisfy ⟨e_O,e_O′⟩ = δ_{O,O′}, so the restriction
   to Fix(τ) is nondegenerate. Then C(τ) is self-orthogonal by inheritance
   and self-dual by the π-adjoint argument: any w ∈ Fix(τ) orthogonal to all
   of C(τ) satisfies ⟨x,w⟩ = ⟨π(x),w⟩ = 0 for all x ∈ C, so w ∈ C^⊥ = C.
   Here τ has order 3 with 15 + 3 = 18 odd-length orbits, so
   dim C(τ) = 18/2 = 9.

3. **Idempotent splitting.** With e = 1 + t + t² in F_2[⟨τ⟩], e² = e
   (each residue mod 3 occurs 9/3 = 3 times among the 9 pairs (i,j), and
   3 = 1 in F_2), te = e, e(1+e) = 0. Hence C = eC ⊕ (1+e)C with
   eC = C(τ) of dimension 9 and W = (1+e)C of F_2-dimension 24 − 9 = 15.

4. **Orbit-counting kill.** τ acts on W with eW = 0, so no nonzero w ∈ W is
   fixed (tw = w implies ew = 3w = w, forcing w = 0). Thus ⟨τ⟩ permutes the
   2^15 − 1 nonzero vectors of W in orbits of size exactly 3, so
   3 | (2^15 − 1). But 2^15 − 1 = 32767 = 3·10922 + 1 ≡ 1 (mod 3),
   since 2 ≡ −1 (mod 3) and 15 is odd. Contradiction.
   Equivalently, W is a vector space over F_2[t]/(1+t+t²) ≅ GF(4), so its
   F_2-dimension is even; 15 is odd.

**Independent second kill.** With ρ = σ³ of type 5-(9;3) (nine 5-cycles plus
three fixed points), the fixed subcode has dimension 12/2 = 6 and the
remainder has dimension 24 − 6 = 18; but 2^18 − 1 = 262143 ≡ 3 (mod 5), so
5 ∤ (2^18 − 1). Either descent alone suffices.

## Limitations
- Proves nonexistence only for the exact type 15-(3;3) window at n = 48.
- Says nothing about other orders/cycle types or about existence of
  extremal [48,24,12] codes (q48 is known to exist).
- Assumes permutation automorphisms acting on coordinates (not monomial or
  semilinear actions).

## Reproducibility
Stdlib-only Python replays, each printing VERIFY_OK:
- `artifacts/verify.py`: representative σ of type 15-(3;3); τ = σ^5 of type
  3-(15;3), order 3, fixed set exactly the 3 σ-fixed points; projector
  combinatorics (e² = e, t·e = e); dimension arithmetic 18/2 = 9, remainder
  15 odd; kill 3 | (2^d − 1) iff d even with 2^15 − 1 ≡ 1 (mod 3).
- `artifacts/verify_order5.py`: independent order-5 descent (ρ = σ³ of type
  5-(9;3), fixed dim 6, remainder 18, 2^18 − 1 ≡ 3 mod 5) plus irreducibility
  of x⁴+x³+x²+x+1 over F_2.
- `artifacts/verify_lemma2.py`: stress test of the fixed-subcode lemma on
  the small analogue n = 6, τ = (0 1 2)(3 4 5) — all 84 τ-stable ordered
  spanning triples (15 distinct codes, 3 τ-stable distinct) have fixed-subcode
  dimension exactly (2+0)/2 = 1 as predicted. (Docstring "420 codes" counts
  ordered generating triples; distinct-code count is 15.)

## References
- S. Bouyuklieva, W. Willems, N. Yankov, On the automorphisms of order 15
  for a binary self-dual [96,48,20] code, arXiv:1403.4735 (length-96
  order-15 exclusion; general pq method model, no length-48 statement).
- A. Guenther, G. Nebe, Automorphisms of doubly-even self-dual binary
  codes, arXiv:0810.3787 (Alt-group constraint; permits 15-(3;3), implies
  no enumerator exclusion).
- K. Betsumiya, M. Harada, A. Munemasa, A complete classification of doubly
  even self-dual codes of length 40, arXiv:1104.3727 (census stops at 40).
- M. Harada, On a 5-design related to a putative extremal doubly even
  self-dual code of length a multiple of 24, arXiv:1401.6254.
- Y. Cao et al., Self-dual binary [8m,4m]-codes from dihedral group algebra,
  arXiv:1902.07533 (extremal [48,24,12] via D48; distinct regular-scope
  construction, confirms existence frontier).
- S. T. Dougherty et al., Constructions of self-dual codes from group rings,
  arXiv:1604.07863 (constructible groups for lengths 24/48).
