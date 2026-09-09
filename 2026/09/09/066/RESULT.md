# Triple-C5 one-vertex wedge gap: reg(S/I)=4, im=3

## Context
Bounding the Castelnuovo-Mumford regularity of squarefree edge ideals by the
induced matching number is a recognized frontier (Herzog-Hibi-Zheng chordal
equality; Banerjee-Beyarslan-Ha program; unicyclic Alilooee-Kara-Selvaraja and
bicyclic Cid-Ruiz et al. characterizations). Cyclomatic number 3 is the smallest
unclassified case. The admitted program targeted a tricyclic reg-vs-im
dichotomy with preset fallback T0: reg=im on all triple-wedge graphs (three
cycles through one common vertex plus arbitrary trees). The finding below arose
by probing that T0 wedge subfamily directly.

## Definitions
- `G0`: wedge (one-vertex bouquet) of three 5-cycles through common vertex 0:
  lobe 1 `0-1-2-3-4-0`, lobe 2 `0-5-6-7-8-0`, lobe 3 `0-9-10-11-12-0`.
  So `n=13`, `m=15`, connected, cyclomatic number `|E|-|V|+1=3`, no attached trees.
- `S = QQ[x_0..x_12]`, `I(G0)` = edge ideal. `reg = reg(S/I(G0))`
  (so `reg(I(G0)) = reg+1`).
- `im(G)` = induced matching number (pairwise disjoint edges, no cross-edges).

## Result
Over `QQ`, `G0` in class T0 satisfies:

- `im(G0) = 3`, e.g. edges `(0,1),(6,7),(10,11)`;
- `reg(S/I(G0)) = 4`;
- hence `reg - im = 1`.

Consequence: the triple-wedge subclass does **not** satisfy `reg = im`
identically; the preset T0 equality is false. `G0` is a certified gap
obstruction inside the one-vertex bouquet family that any complete tricyclic
obstruction list must account for.

## Proof / evidence
- Scope: edge list above gives `n=13, m=15`, connected, `cyc=3`; replay confirms.
- Induced matching: exhaustive check over all edge subsets; witness at `k=3`
  above is vertex-disjoint with no cross-edges; all `C(15,4)=1365` 4-sets checked,
  zero induced. Hence no induced matching of size >= 4, so `im=3`.
- Lower bound (Hochster, exact `QQ` arithmetic): independence complex of full
  vertex set has face sizes `{0:1, 1:13, 2:63, 3:148, 4:179, 5:108, 6:27}` and
  boundary ranks `{1:1, 2:12, 3:51, 4:97, 5:81, 6:27}`, giving
  `dim Htilde_3 = 179-97-81 = 1`. By Hochster
  `beta_{i,|W|} = dim Htilde_{|W|-i-1}`, so `beta_{9,13} >= 1`, hence
  `reg(S/I) >= 13-9 = 4`.
- Upper bound (standard vertex-deletion inequality
  `reg(G) <= max(reg(G-v), reg(G-N[v])+1)` for every `v`, applied as
  `R(V) = min_v max(R(G-v), R(G-N[v])+1)` with `R(edgeless)=0`): exact recursion
  over all `2^13-1 = 8191` subsets closes at `R(G0) = 4`. Lower and upper bounds
  meet, so `reg = 4` over `QQ`.
- Independent verifier reproduces `im=3`, deletion-UB `4`, `Htilde_3` rank 1,
  plus neighboring wedge values (`(5,5)`: im 2/reg 3; `(3,3,3)`: 3/3;
  `(4,4,4)`: 3/3), confirming the method and that the gap is not a mechanical
  wedge-additivity corollary.
- Replay: `python3 artifacts/replay_counterexample.py`
  and `python3 artifacts/verify.py` (exact rational arithmetic, stdlib only).

## Limitations
- Proved over `QQ` only; torsion/Smith analysis over other characteristics
  not done. The Hochster lower-bound ranks are `QQ` ranks.
- Proved for the single graph `G0` (no attached trees). Minimality of `G0`
  among bouquet gap graphs, behavior with trees attached, the full tricyclic
  iff list `L`, and a universal tricyclic gap bound are not claimed.
- Upper bound depends on the standard deletion inequality for `reg(S/I)` of
  edge ideals (used as cited theorem); no independent Macaulay2/Singular
  resolution cross-check in this audit environment.

## Reproducibility
- `artifacts/replay_counterexample.py`: scope, exhaustive im, exact-QQ
  Hochster homology, deletion recursion; log confirms output quoted above.
- `artifacts/verify.py`: independent brute-force im, QQ homology, deletion UB,
  wedge-family cross-checks.
- Both scripts are stdlib-only (`fractions`, `itertools`) and deterministic.

## References
- Alilooee-Kara-Selvaraja, Regularity of Powers of Unicyclic Graphs,
  https://arxiv.org/abs/1702.00916 (unicyclic base case, cyclomatic 1).
- Cid-Ruiz-Jafari-Nemati-Picone, Regularity of bicyclic Graphs and their powers,
  https://arxiv.org/abs/1802.07202 (bicyclic/dumbbell, cyclomatic 2).
- Moradi-Khosh-Ahang, On vertex decomposable simplicial complexes and their
  Alexander duals, https://arxiv.org/abs/1302.5947 (vertex-splittable method).
- Seyyedi-Rahmati, Regularity and projective dimension of generalized theta
  graphs, https://doi.org/10.3906/mat-1510-121 (disjoint two-vertex core).
- Jayanthan-Sarkar, Bound for regularity of binomial edge ideals of cactus
  graphs, arXiv:2005.08594 (different ideal).
- arXiv searches returning zero hits: tricyclic edge-ideal regularity;
  `"edge ideal" tricyclic`; bouquet / wedge-cycles / friendship / windmill
  edge-ideal regularity.
