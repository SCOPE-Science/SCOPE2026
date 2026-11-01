# Review of the chorded-ring majority two-cycle theorem

## Correctness

**PASS.** The proof examines every possible flipping set. Flipping at a degree-two vertex forces both neighbors to flip, so an interior arc is entirely flipping or entirely stable; an endpoint cannot be the unique flipping vertex. Endpoint-only orbits require opposite endpoint phases and opposite stable neighbors from the two paths. One-path-flipping orbits require an odd active path; full alternation requires even cycle length. Stable arc interiors are classified exactly by compositions into runs of length at least two, with a separately checked length-two exception. These cases are disjoint and exhaustive. The Fibonacci/six-periodic rewriting follows from rational run generating functions. Complete small-parameter direct dynamics separately agrees in all three classes for 66 parameter pairs and 327,696 states; finite experiments corroborate rather than replace the proof.

## Originality

**PASS, with stated residual risk.** Targeted searches for majority dynamics on chorded cycles, theta graphs with a direct chord edge, and Fibonacci periodic-orbit counts found no equivalent census. Goles–Olivos establishes period boundedness but not exact numbers. Benjamini et al. arXiv:1405.2486v1 treat period two and random/unimodular graphs; its relevant full-text sections contain no chorded-cycle exact enumeration. Nakar–Ron arXiv:2205.08972 concerns a degree-two cyclic rule, not the two degree-three chord endpoints. The distinction is substantive because every bare odd ring has zero primitive two-cycles while every single-chord odd ring has at least four. No assertion is made that failed searches prove novelty; the full 1980 original paper could not be inspected, and differently named graph families could conceal overlap.

## Mathematical value

**PASS.** The problem isolates the minimal nontrivial topology change to synchronous majority dynamics on a ring. Its sharp qualitative effect on odd rings is accompanied by a complete infinite-family integer census depending on both arc lengths, with a three-mechanism classification. The generating-function reduction yields Fibonacci growth and a six-periodic correction, giving a usable invariant for a natural perturbation of a classical cellular automaton rather than a computed table.

## Scope and residual limitations

No basin or transient-time classification is claimed. The theorem is not asserted for arbitrary theta graphs, other update rules, or multiple chords. A possible earlier equivalent theorem in inaccessible or differently indexed literature is an originality risk. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
