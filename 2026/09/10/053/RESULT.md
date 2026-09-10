# No multiplicity-2 nodal bitangent class on the central-parallelogram tropical quartic

## Context
The admitted target proposed a nodal wall-crossing splitting law: for a nodal
subdivision `S_nod` of `4Δ₂` with central unit parallelogram
`P* = conv{(1,1),(2,1),(1,2),(2,2)}`, the Lee–Len multiplicity-2 nodal
bitangent mother `B₀` at the 4-valent vertex `v₀` splits across the two
diagonal refinements `S₊/S₋` into smooth daughters with 4 vs 0 real lifts.
Admission assumed tropical genus `g = 2` with multiplicity pattern
`(1,2,2,2)`. The submitted report proves this premise is impossible as stated
for the named `P*`.

## Definitions
- `S_nod`: regular subdivision of `4Δ₂` that is honeycomb-unimodular except
  for one central unit parallelogram `P*` as above.
- `Γ₀`: dual nodal tropical plane quartic; `v₀` is the 4-valent vertex dual
  to `P*`.
- Vertex weight `w(v₀)`: number of interior lattice points of the dual face
  (Lee–Len Def. 2.3). Tropical edge weight = lattice length of the dual
  primal edge.
- Paired metric graph `Σ` with pairing morphism `φ : Σ → Γ₀` (Lee–Len
  Def. 2.4); `g_Σ = (d-1)(d-2)/2 = 3` for quartics.
- Bitangent multiplicity: number of effective theta preimages
  (Lee–Len Def. 2.8, Lemma 2.9).

## Result
For `S_nod` of the topic, the dual `Γ₀` has genus 3 with all edge weights 1.
By Lee–Len Lemma 2.9 / Theorem 4.4 its seven bitangent classes all have
multiplicity exactly 1: **no multiplicity-2 nodal class `B₀` exists at `v₀`
or anywhere**, and the target splitting law presupposing such a `B₀` is
impossible as stated. Both diagonal refinements `S₊/S₋` are regular,
unimodular, genus-3 smoothings (smooth daughters exist, but there is no
mult-2 mother to split).

## Proof / evidence
1. `P*` lattice data (Pick): normalized area 2, boundary 4, interior 0, so
   `w(v₀) = 0`; all four `P*` edges have lattice length 1, so every tropical
   edge at `v₀` has weight 1.
2. Existence: explicit integer heights `H₀` (e.g. `H₀(0,0)=1`,
   `H₀(1,1)=201`, `H₀(2,1)=501`, `H₀(1,2)=500`, `H₀(2,2)=800`) make `P*`
   exactly coplanar on the lower hull with all other cells unimodular
   triangles (lower-hull enumeration over all `C(15,3)` triples).
3. Genus: area counting `8 = n_tri/2 + 1` forces `n_tri = 14` unimodular
   triangles beside `P*`, so `V = 15` dual vertices; boundary edges of
   `4Δ₂` number 12; interior edges `E_int = (3·14 + 4 − 12)/2 = 17`;
   hence `b₁(Γ₀) = 17 − 15 + 1 = 3`. All weights 1, so `Σ = Γ₀` as graphs
   and `g_Σ = g_Γ₀ = 3`.
4. Lee–Len fiber sizes (Lemma 2.9 + Thm 4.4): pushforward fibers of size
   `2^{3−3} = 1`; exactly one of the 8 theta classes has `1 − 1 = 0`
   effective preimages, the other seven have 1 each: seven classes of
   multiplicity exactly 1, one of multiplicity 0. Maximum multiplicity is 1.
5. Smoothings: raising `{(2,1),(1,2)}` (resp. `{(1,1),(2,2)}`) by small
   `ε` gives regular refinements `S₊` (triangles ABD, ACD) and `S₋`
   (triangles ABC, BCD), each a 16-triangle unimodular triangulation with
   bounded Betti number 3.
6. The `(1,2,2,2)` pattern applies only under genuine genus drop
   (`I > 0` faces or higher-weight edges); the unit square has `I = 0`,
   so it is inapplicable here.

## Limitations
- Scoped to the named central unit square `P*` (`I = 0` parallelogram).
  Larger parallelograms (`I > 0`) or squares elsewhere with different
  global combinatorics are outside this claim; some genuinely
  genus-dropping nodal walls may host mult-2 mothers.
- Says nothing about real-lift behavior of the seven mult-1 classes or
  their smooth daughters; the 4/0 evaluations are moot without `B₀`.
- The earlier `target_exit.json` (USE_PRESET_FALLBACK) is superseded:
  fallback item (i) shares the same impossible premise.

## Reproducibility
Run `python3 output/artifacts/verify_disproof.py` (stdlib only) →
`DISPROOF_OK` (31 PASS, 0 FAIL): D1 Pick/weight data; D2 existence of
`S_nod`; D3 general area/Betti count; D4 Lee–Len fiber arithmetic;
D5 regularity, unimodularity, and genus of both refinements.

## References
- H. Lee, Y. Len, Bitangents of non-smooth tropical quartics,
  arXiv:1710.10126 (Portugaliae Math. 75 (2018) 67–78):
  Lemma 2.9, Thm 4.1/4.4, Def. 4.2; paired-graph genus 3 (p.3).
- M. Baker et al., Bitangents of tropical plane quartic curves
  (smooth 7-class theorem; background).
- M. A. Cueto, H. Markwig, Combinatorics and real lifts of bitangents
  (smooth 41 shapes, Tables 10–11; consulted only as evaluators).
- A. Geiger, Real tropical quartics and their bitangents
  (smooth 1278-triangulation × 2^14-sign census, polyDB smooth-only).
