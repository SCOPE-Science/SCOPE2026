# Self-review

## Correctness — PASS
The result specifies graph definition, integer domain, colouring semantics, and a necessary-and-sufficient transfer automaton. The full 41-state potential inequality is replayed on every directed arc and telescopes to the lower bound. The sole cyclic tight strongly connected component has a verified mod-four level, excluding exactly the forbidden equality case; explicit cyclic column words with checked two-column junctions attain all bounds. An independently implemented bipartiteness search checks all deletion sets through order \(n=12\). Finite searches are supporting tests, not substitutes for the infinite construction and finite certificate.

## Originality — PASS (best-knowledge, residual risk)
The primary comparison is with Wei–Li's *decycling* number (all cycles) and Fox–Gera–Stănică's independent-set formula. Neither statement implies the exact bipartite vertex-deletion number: a forest condition is strictly stronger than bipartiteness, while two independent classes need not be a single independent set. Other relevant sources concern edge deletion or global bipartiteness without deletion; Zhu’s universal ratio bound is strictly weaker than the sharp value here. Actual searches for odd-cycle-transversal aliases, induced-bipartite maxima, and the periodic formula returned no covering claim. An inaccessible plausible 2011 thesis about edge bipartization and possible unindexed equivalent results remain risks; snippets and abstracts were not treated as evidence of full-paper noncoverage.

## Value — PASS
The theorem determines a natural infinite-family vertex-bipartization invariant rather than just computing an isolated case. The mod-four exceptional class is a structural phenomenon not obtained from the elementary \(n/2\) lower bound; the finite-state potential explains it and supplies a reproducible proof certificate. It differentiates the odd-cycle deletion problem from feedback-vertex deletion in a familiar cubic family.

## Limitations and related work
The result is specific to inner step two; no classification of optimal deletion sets or claims for higher steps are offered. Earlier equivalent coverage, if found, would change the originality assessment. The checker is executable in standard Python; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
