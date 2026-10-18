# Scientific review

## Correctness — PASS

The all-parameter statement has an integral primal construction and matching dual proof. The overlap graph is strongly connected, its only imbalanced vertices are classified exactly by the forbidden-run prefix and suffix, and the leftmost forbidden-near-run potential drops by at most one per legal edge. Every negative-imbalance vertex has a unique positive-imbalance counterpart obtained by reversing the prefix before its first maximal permitted run. The bijection balances all vertices with precisely the dual lower-bound number of repeated edges. An Euler tour then supplies a valid legal cycle. The generating-series derivation independently counts the leftmost-occurrence potential. A standalone checker tests the construction, formula, and cyclic coverage on 47 parameter combinations; small independent exhaustive bounds also agree. No finite test is used as an infinite proof.

## Originality — PASS within inspected evidence

The closest recent treatment, Sawada and Gabrić (arXiv:2510.16545, 2025), studies universal cycles of windows whose forbidden-run avoidance is *cyclic*, a rotation-closed balanced language. In contrast, our window language only avoids the run *linearly*; for example, the binary word `00100` is included here for the three-zero restriction but excluded from their family. Chee et al. (arXiv:2403.01454) maximize distinct run-limited windows, whereas Bernardini et al. (CPM 2022) describe general Eulerian-balancing algorithms without this explicit all-parameter formula. A previously established binary two-run restriction is a special case of our theorem and is not claimed separately. Searches for cyclic shortest common superstrings, directed postman augmentations, restricted de Bruijn sequences, and exact excess generating functions did not locate stronger coverage. Unindexed equivalent formulations and overlooked optimization results remain genuine risks.

## Value — PASS

Arbitrary-alphabet run-limited window sets are a natural constrained-channel and de Bruijn construction class. Their linear-window overlap graphs are generally not Eulerian, so standard cyclically restricted universal-cycle constructions do not solve the all-window coverage task. The theorem optimally covers the full language simultaneously for every alphabet size, forbidden-run length, and admissible window length; it gives an explicit construction, a sharp potential certificate, and a rational exact generating function. This is a structural infinite-family solution rather than a small finite increment.

## Limits

No assertion is made about multiple forbidden patterns, enumeration of all optimal cycles, or independent scientific validation. Novelty is assessed against the inspected sources and indexed comparisons rather than as an exhaustive assertion about all publications.

Self-review: passed. Independent audit: not yet performed.
