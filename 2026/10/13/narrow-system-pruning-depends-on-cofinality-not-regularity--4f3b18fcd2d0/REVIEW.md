# Review

## Correctness

PASS. The proof replaces the source's regularity convention by explicit pruning ranks. If no well-pruned subtree exists, transfinite pruning empties the tree and assigns each node a successor removal rank. Every node then has a level after which all descendants have strictly smaller rank. The negation of the needed subsystem-level escape property gives at most \(\theta\) cones on each indexed level that cover every sufficiently high subsystem level. A recursion of length \(\lambda_\theta=\max(\omega,\theta^+)\) remains below \(\kappa\) because \(\lambda_\theta<\operatorname{cf}(\kappa)\). At one common high subsystem level, any fixed node can be above cones from only finitely many recursion stages, or else the removal ranks descend infinitely. At most \(\theta\) finite sets cannot cover \(\lambda_\theta\). Applying the resulting escape property to \(S_\alpha\) contradicts subsystem coherence.

## Originality

PASS. The primary paper states the well-pruned-subtree theorem under the explicit hypothesis that \(\kappa\) is regular. Its one-cardinal fanlike definitions also adopt that convention. The checked source does not formulate the theorem in terms of \(\operatorname{cf}(\kappa)\), nor does it treat singular tree heights. Targeted searches under singular-height, cofinality, well-pruned, fanlike, and narrow-subsystem terminology found no equivalent theorem. The closest broader narrow-system literature studies regular indexing cardinals and applications at successors of singulars, rather than trees whose own height is singular.

## Value

PASS. Regularity is a major structural hypothesis in tree-property arguments, so isolating its exact use is mathematically informative. The result shows that the recent pruning theorem survives at singular heights whenever the subsystem is sufficiently narrow relative to the cofinality, and it records the finite-width correction needed for the counting argument. This is a natural assumption-sharpening of the source's central one-cardinal theorem, rather than a parameter renaming or a routine special case.

## Closest literature and limitations

Adkisson's 2026 paper is the direct source: its Theorem 3.13 proves the regular-height result and its pruning section supplies the motivating mechanism. Lambie-Hanson's 2024 work is the closest broader narrow-system reference but focuses on generalized narrow-system properties at regular cardinals and their applications.

The sufficient cofinality bound is not claimed sharp, and no two-cardinal or branch-existence extension is asserted.

Self-review: passed. Independent audit: not yet performed.
