# Strict v-number versus induced-matching gaps on 7-vertex edge ideals, and the complete labeled-tree (v, im) census

## Context

The v-number of a graded ideal, introduced via coding theory (Cooper et al.;
Jaramillo–Villarreal), is the least degree of a homogeneous colon element
yielding an associated prime. For the edge ideal of a graph, its comparison
with the induced matching number `im(G)` is an active program:
Grisalde–Reyes–Villarreal (arXiv:2109.14121) prove `v ≤ im` under
very-well-covered / simplicial-partition / well-covered-connected-no-C4-C5
hypotheses and classify cycles (C5 is the exception, `im=1 < 2=v`);
Saha–Sengupta (arXiv:2111.12881) prove `v ≤ im ≤ reg` for bipartite /
(C4,C5)-free vertex-decomposable / whisker graphs; Biswas–Mandal–Saha study
the related (reg, v) lattice-point program. Concrete small graphs locating
where `v < im` strictly, and whether the gap can occur outside all published
sufficient hypotheses, were missing.

## Definitions

Let `G` be a finite simple graph on `V = {0,…,6}` (0-indexed below;
add 1 for 1-indexed labels), `S = k[x_0,…,x_6]` over any field `k`, and
`I(G) = (x_u x_v : uv ∈ E(G))` its edge ideal.
The v-number is `v(I) = min{deg f : f` homogeneous`, (I:f) ∈ Ass(S/I)}`.
For edge ideals, `Ass(S/I(G)) = {P_C : C` minimal vertex cover`}`,
`P_C = (x_v : v ∈ C)`. A matching is induced if no further edge of `G`
lies among its endpoints; `im(G)` is the maximum size of one.
`V + 1 ≤ im` denotes a strict gap of at least 1.

## Result

**Headline witness H⋆ (outside all sufficient conditions).**
The connected 7-vertex graph with edges (0-indexed)

    01, 03, 15, 16, 23, 25, 36, 45, 56

(i.e. 1-indexed `12, 14, 26, 27, 34, 36, 47, 56, 67`) satisfies

    v(I(H⋆)) = 1,  im(H⋆) = 2,  so v + 1 ≤ im with equality,

and lies outside every published sufficient hypothesis for `v ≤ im`:
non-bipartite (triangle 1–5–6); not well-covered (minimal vertex covers of
sizes 3 and 5 coexist); contains induced C4's (`{0,1,3,6}` carrying exactly
`01,03,16,36`; `{2,3,5,6}` carrying exactly `23,25,36,56`) and an induced C5
(`{0,1,2,3,5}` carrying exactly `01,03,15,23,25`); no simplicial partition
(unique simplicial vertex 4, `N(4)={5}`); odd order 7, hence not a whisker or
very-well-covered graph.

**Tree witness G⋆ (gap 2).** The connected tree with edges (0-indexed)
`01, 23, 45, 16, 36, 56` (1-indexed `12, 34, 56, 27, 47, 67`: three disjoint
edges hung on hub 6/7) satisfies `v = 1`, `im = 3`, so `im − v = 2`.

**Labeled-tree census.** Over all `7^5 = 16807` labeled trees on 7 vertices,
the exact `(v, im)` distribution is

| (v, im) | count |
|---|---|
| (1,1) | 637 |
| (1,2) | 5250 |
| (1,3) | 840 |
| (2,2) | 10080 |

Hence 6090 labeled trees (36.2%) satisfy the strict gap `v + 1 ≤ im`, and no
tree has `v ≥ 3` or `im ≥ 4`.

## Proof / evidence

Squarefree colon lemma (proved in full): for monomial `f` with support `A`,
`(I(G):f)` depends only on `A`; with `x_A = ∏_{i∈A} x_i`,
`(I:x_A) = (x_v : v ∈ N(A)) + I(G − A)`. Thus `(I:x_A) = P_C` iff `A` is
stable, `N(A) = C` is a minimal vertex cover, and `V ∖ (A ∪ N(A))` is stable.
Hence `v(I(G)) = min{|A| : A` stable`, N(A)` minimal vertex cover`}`,
attained at a squarefree monomial.

- G⋆: `A = {6}` stable, `N(A) = {1,3,5}`, residual `{0,2,4}` edgeless, so
  `(I:x_6) = (x_1,x_3,x_5)`; minimality by private edges `01/23/45`-shifted
  (`12` private to 2, `34` to 4, `56` to 6 in 1-indexed form); `v = 1`.
  `{01,23,45}` pairwise disjoint with no chords among their endpoints gives
  `im = 3` (upper bound `⌊7/2⌋`).
- H⋆: `A = {6}` stable, `N(A) = {1,3,5}`, residual `{0,2,4}` edgeless, so
  `(I:x_6) = (x_1,x_3,x_5)`; private edges `16/36/45` give minimality;
  `v = 1`. `{03,45}` is induced (`04,05,34,35 ∉ E`), so `im ≥ 2`; all 7
  pairwise-disjoint edge-triples each carry a chord (enumerated), so
  `im = 2`. Boundary properties verified edge-by-edge (see Result above).
- Census: exhaustive Prüfer-sequence enumeration (`7^5 = 16807`), each tree
  processed by Lemma-based v-search and exhaustive edge-subset im-search
  with per-tree dual re-verification of `N(A)` and residual stability.

## Limitations

The authoritative McKay/OEIS A001349 count is 853 connected (1044 total)
unlabeled graphs on 7 vertices, not 104 as in the original topic text; the
full 853-graph connected unlabeled census is NOT claimed (no nauty-class
generation in this environment). The verified core is the two witnesses plus
the complete labeled-tree stratum. The simplicial-partition test uses the
closed-neighbourhood exact-cover formulation; the clique-block variant is
covered by the hand argument (unique simplicial vertex ⇒ at most one block
⇒ `V` not a clique). No regularity cross-checks beyond positioning are
claimed; `v ≥ 3` behaviour outside trees is not surveyed.

## Reproducibility

`output/artifacts/replay.py` (stdlib-only Python 3): verifies G⋆, runs the
complete 16807-tree Prüfer census (~2–5 s), and searches supersets for the
outside-all witness. Run: `python3 output/artifacts/replay.py`.
The census distribution and witness certificates were independently
re-executed during audit and matched exactly.

## References

- G. Grisalde, E. Reyes, R. H. Villarreal, Induced matchings and the v-number
  of graded ideals, arXiv:2109.14121.
- K. Saha, I. Sengupta, The v-number of Monomial Ideals, arXiv:2111.12881.
- K. Saha, A. Van Tuyl, Comparing the v-number and h-polynomials of edge
  ideals, arXiv:2507.05700.
