## Correctness — PASS

The lower bound for orders five and seven follows from the incidence bound \(s+\binom{s}{2}(p-2)\). For order seven, the five-point case is excluded analytically: either a collinear triple leaves at least five points uncovered by the at-most-39-point bound, or ten secants have 50 external incidences with at least seven forced duplicated incidences. Explicit five- and six-point witnesses cover the two tori. The exact-arithmetic program independently checks witness coverage and all 1,906,884 five-subsets for order seven.

## Originality — PASS

The closest primary source is Aichholzer–Eppstein–Hainzl, *Geometric Dominating Sets* (arXiv:2203.13170). It gives general bounds and asks for exact torus domination numbers, but does not state these two values. The similarly titled Fowler–Groot–Pandya–Snapp paper (arXiv:1203.6604) solves the maximum no-three-in-line problem, not the minimum line-pair covering problem. published-finding corpus searches returned only adjacent torus-homology and abstract graph-domination results, with no implication covering these exact values. Global novelty is not certified; unindexed or differently phrased prior work remains possible.

## Value — PASS

Exact values of the natural geometric domination number are explicitly identified as an open direction in the motivating paper. The values \(D_5=5\) and \(D_7=6\) give exact calibration points for the first odd-prime orders not covered by the paper's four-point upper bound. The order-seven value requires a structural incidence obstruction, rather than only a computed witness.

## Closest literature and limitations

The claim concerns only \(T_5\) and \(T_7\), where \(T_p=\mathbb{F}_p^2\) and lines are affine lines. It does not assert a general-prime formula. Searches and a reproducible checker reduce, but do not eliminate, the risk of unindexed prior coverage.

Self-review: passed. Independent audit: not yet performed.
