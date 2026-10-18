# Self-review: inversion-graded Bruhat edge census

## Correctness — PASS
The exact cover criterion is derived from the inversion difference after a swap. Conditional Mallows projectivity for a consecutive block is proved by separating crossing inversions from internal inversions. Endpoint consecutive ranks yield precisely d choices, each of weight \(q^{d-1}[d-1]_q!\), so the gap-d factor follows. The finite polynomial enumerator is obtained by multiplying by \([n]_q!\), and the nonmonotone and fixed-parameter asymptotic corollaries are proved by expansions and exponential tails. The standalone independent Python verifier checked 1,246,964 position-pair candidates, \(2\le n\le8\), by actual swap and inversion recount, and all cross-multiplied polynomial equalities hold.

## Originality — PASS
The full q-inversion-rank Hasse-edge enumerator and the position-gap refinement were compared against the actual scope of the 2026 boxed-mesh/strong-Bruhat paper, the 2005 Adin–Roichman results, the Mallows positive-association work, and related research. The uniform mean, standard reciprocal symmetry, and covariance consequence are explicitly treated as known or implied, not novel. No prior source was found giving the claimed all-rank formula. Remaining risk: alternate or unindexed q-enumerators could supersede it.

## Value — PASS
The inversion-rank distribution of edges in the full strong Bruhat Hasse diagram is a canonical counting invariant beyond the previously determined total count and upward-degree maximum. The formula resolves every coefficient and refines further by position span. Its Mallows form displays two mathematically distinct effects: an interior global optimum for \(n\ge4\) and a fixed-\(q\) linear-versus-n log n transition. This is structurally informative for weighted sampling of Bruhat cover edges; it is not a mere reformulation of the uniform mean or of reciprocity.

## Closest sources and limitations
- Kitaev, Qiu and Xu (arXiv:2609.13764): boxed 12 / Bruhat equivalence, extremal and uniform first moment, degree-distribution insertion identity; the present rank-generating polynomial is a different invariant.
- Adin and Roichman (arXiv:math/0505020): original cover criterion and uniform expectation.
- Johnson, Leader and Long (arXiv:1909.03770): Mallows positive association, not a cover count.
- The proof applies to full symmetric groups; it does not settle full up-degree distributions, arbitrary Bruhat intervals, or uniqueness of an optimizing Mallows parameter.

Self-review: passed. Independent audit: not yet performed.
