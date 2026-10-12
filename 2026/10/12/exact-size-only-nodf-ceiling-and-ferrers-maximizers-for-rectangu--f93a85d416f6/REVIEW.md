# Self-review

## Correctness
**PASS.** By the definition of NODF, a tied-degree within-guild pair contributes zero and every other pair at most one. When one guild has \(b\) vertices and the other has \(a\le b\), the larger guild has at most \(a\) positive degree values. Discrete convexity proves the exact unavoidable number of ties, \((a-r)\binom q2+r\binom{q+1}2\), with equality precisely for balanced multiplicities. A Ferrers incidence matrix with those multiplicities attains every remaining pair's maximum. At equality all shorter-guild pairs must be strict neighborhood inclusions, forcing the Ferrers form. The longer-side degree histogram uniquely identifies each Ferrers isomorphism type, giving \(\binom ar\). The accompanying integer verifier checks all 176554 nonisolated labeled matrices in ten small shapes and independently exercises larger constructions.

Risk: the theorem is not an optimum at prescribed edge count, and does not cover altered NODF conventions or isolated species.

## Originality
**PASS.** The original NODF paper supplies the index and its strict-degree condition. Britton, Almeida Neto, and Corso rigorously prove the square perfect-staircase and zero-index classifications; these existing endpoint theorems are acknowledged, not relabeled as new. Song, Rohr, and Saavedra and Hoeppke and Simmons treat the practically different maximum at fixed guild sizes **and fixed edge count**, with numerical optimization. The full texts and exact-result searches inspected did not provide the exact shape-only rectangular ceiling, its all-shapes equality classification, or the \(\binom ar\) count. The new theorem supplies a sharp intermediate bound not implied by the known endpoint statements.

Risk: some niche combinatorial note or unindexed package documentation could independently derive the same dimension-only formula; failed search is not a proof of novelty.

## Value
**PASS.** Network ecologists compare nestedness across unequal guild sizes, and size/connectance confounding is a documented problem. Here rectangular guild imbalance forces a nontrivial NODF deficit even with a completely nested architecture and no fixed link count. The exact closed form, complete Ferrers maximizer classification, and nonzero asymptotic shape penalty give a natural shape-specific baseline and a rigorous upper-bound check for fixed-link numerical optimization. This value does not depend on claiming a solution to the distinct fixed-link optimization task.

Self-review: passed. Independent audit: not yet performed.
