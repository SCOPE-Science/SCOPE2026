# Scientific review

## Correctness — PASS
The claim uses the standard synchronous degree-threshold chip-firing update on labelled \(K_{a,b}\), with nonnegative integer loads and primitive temporal period exactly two. Two-step conservation forces complementary firing sets on a connected graph, giving necessary *and sufficient* vertex intervals. Their positive-width classification produces the exact mass polynomial, including pure-shore boundary cases. The balanced sum equals the trace of a binomial transition kernel, whose eigenvalues follow from a triangular polynomial basis. Gaussian Riemann-sum domination proves the total-count asymptotic; a two-kernel local central limit estimate plus an explicit global binomial point-mass bound proves the arcsine weak limit. Exact arithmetic and full small-case simulation agree, but do not certify the limit on their own.

## Originality — PASS (qualified)
Jiang (arXiv:1003.0943, inspected through the relevant proofs and discussion) gives the possible *period lengths* for complete bipartite chip-firing. This does not imply exact counts of already-periodic primitive-two-cycles, chip-mass coefficients, or the limiting shore firing fraction. The existing complete-graph mass census concerns a different graph and a Gaussian phase law; the graph-cut parametrization and Wright–Fisher spectral method are background, not claimed novelties. Hansen–Jaworski's bipartite random mapping paper was inspected by abstract only; its component-limit theorem might provide a related probabilistic route, but no direct equivalence to this three-part chip-firing statement was established. Jung's 2026 middle-stair preprint proves eventual period two in a mass band, not the asserted periodic-state census, according to the accessible abstract; its full text was unavailable. Unindexed earlier equivalents remain a real risk, not a proof of uniqueness.

## Value — PASS
The biclique's two populated shores model coupled populations with distinct firing groups. The exact periodic mass polynomial is a natural invariant at every conserved energy; the factorial-square trace identity makes total counts effectively computable; the non-Gaussian arcsine firing fraction is a structural contrast to concentration around half seen in complete-graph dynamics. This is an all-size classification and a limiting law, not a marginal parameter tweak or a mere verification benchmark. It does not claim attraction-basin distributions.

## Closest sources and limits
- Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first posted 2010-03-04), Sections 2–5.
- Lionel Levine, *Parallel Chip-Firing on the Complete Graph*, arXiv:0811.2800 (2008).
- Jennie Hansen and Jerzy Jaworski, *Large components of bipartite random mappings*, Random Structures & Algorithms 17 (2000), 317–342. Only the abstract was accessible; equivalence risk retained.
- Minkyu Jung, *The Middle Stair for Complete Bipartite Parallel Chip-Firing*, arXiv:2608.01350 (2026). The abstract was accessible; full text was not, and independent confirmation of noncoverage is unavailable.

Self-review: passed. Independent audit: not yet performed.
