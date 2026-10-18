# Scientific review

## Correctness — PASS
The molecule and polar constraints are specified in linear-dual coordinates. A beta integral over the first-part potential range gives the full polar volume. The primal volume is **credited** to a 2018 complete-bipartite symmetric-edge \(h^*\)-theorem; its normalization is independently checked with a signed-simplex slice integral. The strict balancing inequality follows from the exact Vandermonde sum, a single sign change in the weighted adjacent-split difference, and strict increase of \((k+1)\binom{2k}k/4^k\) for \(k\ge1\). This is a proof for every integer parameter, not extrapolation from finite checks. The package includes actual executable exact-arithmetic and finite-polytope checks.

## Originality — PASS, with residual bibliographic risk
Higashitani–Jochemko–Michałek, arXiv:1807.07678, already determines the primal volume and is expressly credited. Alexander–Fradelizi–García-Lirola–Zvavitch, arXiv:1911.10642, studies free-space Mahler products and Hanner equality cases. Neither inspected result evaluates the dual volume and its strict joint balancing across all complete bipartitions at fixed size. Targeted research-record queries and adjacent mathematical literature found a different signed-chain polytope and Banach–Mazur/skeleton/inradius results, but no covering partition-balancing theorem. The possibility of a differently named equivalent older result remains.

## Mathematical value — PASS
This is a natural volume-product extremal problem within a fundamental graph-metric family in every dimension. The exact optimizer and equality characterization distinguish previously understood Hanner-thin cases from all thicker bipartitions. A nontrivial single-crossing proof and a fixed-part asymptotic support the structural significance beyond mere computation.

## Literature and limits
Primary literature: arXiv:1705.09579 (extreme molecules; primary MSC 46B20), arXiv:1807.07678 (complete-bipartite \(h^*\), p. 2 and theorem), arXiv:1911.10642 (metric free-space Mahler products, sections 3 and 5); arXiv:1910.05193 provides related symmetric-edge context. No claim covers arbitrary graph metrics, weighted edges, or global metric-space optimization. Independent expert validation is not available.

Self-review: passed. Independent audit: not yet performed.
