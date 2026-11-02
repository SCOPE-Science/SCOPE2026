# Mathematical review

## Correctness — PASS

The theorem concerns rooted full binary group-separable preference domains under the impartial-culture average of minimum Kendall distance. Every distinct pair of alternatives has a unique lowest common ancestor, so the minimum Kendall loss decomposes exactly into nodewise balanced-interleaving losses. The exact singleton cost yields \(F_m\). The universal bound \(g(a,b)\ge ab/4\) for \(a,b\ge2\) follows from the exact sample-without-replacement variance and Cauchy–Schwarz except for five explicit small pairs, which have been evaluated exactly. The comparison \(F_{a+b}-F_a-F_b\le ab/4-1/6\) has equality only for \((a,b)=(2,2)\). Telescoping proves the global lower bound, strict caterpillar-only equality, the uniform runner-up gap and every runner-up shape. This reasoning is finite and elementary at every local step and applies to every tree size; the exact verifier independently reproduces the finite calculations and sample domains.

## Originality — PASS (qualified)

The primary 2026 source, *Outer Diversity of Condorcet Domains* (arXiv:2610.00720v1), proves its finite-size optimization algorithm and reports the caterpillar maximizer empirically for up to one hundred alternatives, but does not supply the all-size analytic extremal characterization or second-best gap. Its earlier companion, *Outer Diversity of Structured Domains* (arXiv:2602.15708v1), explicitly poses the extremality question. The related *Nearly Group-Separable Elections* (arXiv:2609.33535v1) studies different multi-voter edit problems. Searches of relevant published research and mathematical claim records found no dominating or equivalent theorem; their absence is not proof of novelty. An unindexed equivalent result is the main remaining risk.

## Value — PASS

This resolves a publicly motivated structural extremal question for all numbers of alternatives, upgrades a finite experimental pattern to an exact theorem and identifies the sharp next-best shape and gap. The nodewise surcharge also explains why a true balanced branch is less diverse, a structural mechanism useful in further extremal questions about domain restrictions.

## Scope and limitations

The expectation is over a single uniformly random complete ranking and the permissible domains are exactly those represented by full binary group-separable trees. No claim is made for arbitrary domains, alternative distances, or correlated electoral profiles. The numerical checks are finite and are not substitutes for the universal proof. Equivalent independent earlier results might not be indexed.

Self-review: passed. Independent audit: not yet performed.
