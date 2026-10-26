# Scientific review: complete fifth-order binary universal-cycle deletion spectrum

## Correctness — PASS

A universal cycle exists exactly when the retained length-five edge graph is weakly connected on active vertices, integer-balanced, and has at least five edges. The rank-15 binary incidence matrix has a 17-dimensional nullspace. `verify_parity.py` exhausts all 131072 parity-feasible edge-deletion masks; it retains exactly 6600 integer-balanced masks and evaluates connectivity. `verify_mitm.py` independently joins every two half-mask divergence vectors and uses disjoint-set connectivity, again obtaining every coefficient. Both checkers were executed from the included source paths. This proves the finite classification without extrapolation.

## Originality — PASS, with residual risk

The closest primary source is Chen, Kitaev, and Sun (arXiv:1908.01116; *Mathematics* 8 (2020), 778). Its Tables 1–3 give binary orders 2–4, its Theorem 6 gives general exact two-deletion probabilities, and its Theorem 5 gives a binary order-at-least-five lower bound. In contrast the present result calculates the complete order-five set for every deletion count; already at five forbidden words the published lower-bound construction supplies four versus the exact fourteen. Public scholarly-record and literature searches under universal-cycle, Eulerian-subgraph, and forbidden-edge aliases yielded no equivalent or dominating table. Unindexed specialized data remains a genuine uncertainty.

## Mathematical value — PASS

The table fills the natural first missing order of an existing exact enumeration program. It counts 33 nontrivial deletion probabilities and separates local Eulerian balance from global connectivity in a small but complete graph, with independent finite certificates and an explicit gap from published sufficient constructions. No arbitrary restriction on number of deletions is imposed at the fixed order.

## Limits

Binary order five and circular existence only; no all-order law, q-ary classification, linear universal-word spectrum, or circuit-multiplicity claim. This is a self-review, not independent certification.

Self-review: passed. Independent audit: not yet performed.
