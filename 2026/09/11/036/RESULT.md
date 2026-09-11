# Certified single-field extremal: a 3-uniform clutter with (τ, ν, reg_Q) = (4, 1, 4)

## Context

For a (simple) 3-uniform clutter (3-uniform hypergraph) H, let S = k[x_v : v ∈ V(H)]
and I(H) = (x_i x_j x_k : {i,j,k} ∈ E(H)) be its edge ideal.
Write τ(H) for the covering (transversal) number (minimum vertex-cover size),
ν(H) for the induced matching number (maximum size of a set of pairwise disjoint
edges with no third edge contained in their union; so ν = 1 iff every disjoint
pair is "witnessed"), and reg(S/I(H); k) for the Castelnuovo–Mumford regularity
of S/I(H) over the field k.

For quadratic (graph) edge ideals the sandwich
reg ≤ min-match ≤ τ governs the landscape. In degree 3 it fails, and
characteristic-free 2-collage upper bounds (Ha–Woodroofe type:
reg(S/I) ≤ 2·|C| for a 2-collage C) leave a wide interior window.
The question is which exact triples (τ, ν, reg) actually occur for cubic
edge ideals, and where. The triple (4, 1, 4) is strictly above the
induced-matching lower bound (2 at ν = 1 in cubic scaling) and strictly below
the collage cap, hence a genuine interior extremal point constraining
conjectured 3-uniform uniformity. No source records it.

## Definitions

- V = {0,…,8}, n = 9. Edges (14 triples):
  e1={0,2,5}, e2={0,2,6}, e3={1,2,7}, e4={1,3,4}, e5={1,4,5}, e6={1,5,8},
  e7={2,3,4}, e8={2,5,7}, e9={3,6,7}, e10={3,6,8}, e11={4,6,8},
  e12={4,7,8}, e13={5,6,8}, e14={6,7,8}.
- S = Q[x_0,…,x_8], I(H1) = (x_ix_jx_k : {i,j,k} ∈ E).
- Δ(H1): independence complex (F ⊆ V is a face iff no edge e ⊆ F).
- Hochster's formula (equality): β_{i,W}(S/I) = dim H̃_{|W|−i−1}(Δ_W; k),
  so reg(S/I; k) = max{h+1 : H̃_h(Δ_W; k) ≠ 0 for some W}.
- A 2-collage is C ⊆ E with every edge sharing ≥ 2 vertices with some c ∈ C;
  Ha–Woodroofe cap for 3-uniform: reg(S/I) ≤ 2|C|.

## Result (headline claim)

There exists an explicit 3-uniform clutter H1 on 9 vertices (hence ≤ 10) with

- τ(H1) = 4,
- induced matching number ν(H1) = 1,
- reg(S/I(H1)) = 4 over Q,

certified by a logged minimal graded Betti table (exact-rational Hochster
computation) and explicit attaining Hochster induced-subcomplex homology classes.

## Proof / evidence

**3-uniformity.** All 14 listed edges have exactly 3 vertices.

**τ = 4.** C = {0,4,7,8} meets every edge:
e1∋0, e2∋0, e3∋7, e4∋4, e5∋4, e6∋8, e7∋4, e8∋7, e9∋7, e10∋8,
e11∋4,8, e12∋4,7,8, e13∋8, e14∋7,8. Hence τ ≤ 4.
Exhaustive check of all C(9,3) = 84 triples: none is a vertex cover.
Hence τ ≥ 4. So τ = 4 (minimum attained e.g. at (0,4,7,8)).

**ν = 1.** Of C(14,2) = 91 edge pairs, exactly 25 are disjoint. Each is
witnessed by a third edge contained in the pair union (so no induced pair):

- e1&e4→e5; e1&e9→e2; e1&e10→e2; e1&e11→e2; e1&e12→e8; e1&e14→e2
- e2&e4→e7; e2&e5→e1; e2&e6→e1; e2&e12→e11
- e3&e10→e9; e3&e11→e12; e3&e13→e6
- e4&e8→e3; e4&e13→e5; e4&e14→e9
- e5&e9→e4; e5&e10→e4; e5&e14→e6
- e6&e7→e4; e6&e9→e10
- e7&e13→e10; e7&e14→e9
- e8&e10→e9; e8&e11→e12

(e-numbers 1-based; verified: each witness edge ⊆ union of the pair.)
0 unwitnessed of 25 disjoint pairs, E nonempty ⇒ ν = 1.

**reg = 4 over Q (exact).** Signed simplicial boundary matrices with exact
rational (Fraction) ranks on all 512 subsets:

- Lower bound: W = {0,…,8} (mask 511): 57 3-faces, r(∂_3) = 42, r(∂_4) = 14,
  so dim H̃_3(Δ_W; Q) = 57−42−14 = 1 (β_{5,9} ≥ 1, reg ≥ 4).
  Second class: W = {0,1,2,3,4,5,6,8} (mask 383): 33 3-faces,
  33−26−6 = 1, dim H̃_3 = 1.
- Upper bound: full 512-subset scan finds no nonzero H̃_h for any h ≥ 4.
  Hence reg ≤ 4. So reg(S/I(H1); Q) = 4.

Exact-QQ minimal graded Betti table of S/I(H1) (Hochster equality, (i,j) ↦ β_{i,j}):

| (i,j) | β | (i,j) | β |
|---|---|---|---|
| (1,2) | 14 | (4,2) | 1 |
| (2,2) | 15 | (4,3) | 24 |
| (2,3) | 27 | (4,4) | 1 |
| (3,2) | 4 | (5,3) | 3 |
| (3,3) | 47 | (5,4) | 1 |

Max j = 4 (rows β_{4,4} = β_{5,4} = 1), confirming reg = 4.
Cross-checks: identical reg = 4 over F_{1000000007}, F_{10007}, and F2
(Q-proxy + F2 agreement is corroboration; the Q verdict rests on exact ranks).

**Strictly interior.** Minimum 2-collage has size 5 (e.g. {e1,e3,e4,e5,e14}),
so the Ha–Woodroofe cap is 2·5 = 10, and reg = 4 lies strictly below it;
the induced-matching lower bound sits at 2, so reg = 4 exceeds it by 2.

## Limitations

- Betti numbers are obtained via Hochster's formula (a theorem giving exact
  Tor Betti numbers) plus exact Fraction ranks, not via explicit minimal
  differentials; the "minimal Betti table" status follows from Hochster's equality.
- ν = 1 uses the witnessed-disjoint-pair induced-matching definition for
  3-uniform clutters; the full 25-pair witness list makes the certificate
  definition-transparent.
- No characteristic gap is claimed for H1 (reg over F2 is also 4); this is the
  single-field extremal, not the two-field target (which was blocked with zero
  splits in ~4300 filtered evaluations and is not claimed here).

## Reproducibility

- `output/artifacts/engine.py` — combinatorics + homology engine
  (τ/ν/collage, signed boundary matrices, ranks over F2 / F_p / exact QQ).
- `output/artifacts/run_certH1.py` — τ, ν, two-prime + F2 regs, collage;
  writes H1_cert.json.
- `output/artifacts/run_exactQQ.py` — full 512-subset exact-rational Betti
  table and upper bound; writes H1_exactQQ.json.
- `output/artifacts/H1_cert.json`, `H1_exactQQ.json` — logged certificates.
- Independent audit re-verified all five qualification artifacts with a fresh
  exact-rational implementation: min cover 4, zero 3-covers, 25/25 disjoint
  pairs witnessed, H̃_3 = 1 on W = 511 and 383, no h ≥ 4 anywhere,
  Betti table match entry-for-entry, min 2-collage 5.

## References

- D. Bolognini, A. Macchia, F. Strazzanti, V. Welker, Powers of monomial ideals
  with characteristic-dependent Betti numbers, Res. Math. Sci. 9:26 (2022).
- M. Katzman, Characteristic-independence of Betti numbers of graph ideals,
  J. Combin. Theory Ser. A 113 (2006), 435–454.
- S. Morey, R. Villarreal, Edge Ideals: Algebraic and Combinatorial Properties
  (survey).
- H. T. Hà et al., Regularity of square-free monomial ideals / collage bound line.
- M. Hochster, Cohen-Macaulay rings, combinatorics, and simplicial complexes
  (Hochster's formula).
