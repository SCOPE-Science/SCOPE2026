# Scientific review

## Correctness — PASS

The hypotheses specify independent uniform parent choices in a rooted increasing tree, labels and outdegree-zero leaves. The event that the final birth labels are leaves is exactly a product of independent restricted-parent choices, yielding the stated factorial tail law. Conditioning converts those choices to independent uniform throws on the early vertices; the survivor probability and known Eulerian leaf mean give the regression. The tail-sum identity and strict Bernoulli inequality give the sign for every permitted integer. Eulerian recursion and 1-dependence give a Gaussian leaf CLT; an independent early-tree/late-parent decomposition gives the joint limit. Uniform bounds on the tail and regression remainder justify dominated Riemann-sum convergence to the mixed covariance constant. Exhaustive verification through nine vertices passed, and three numerical limit tests passed. No finite computation is used in place of an infinite proof.

## Originality — PASS (qualified by historical risk)

The nearest comparable published results concern global counts of prescribed outdegrees (Janson 2004/2005; Najock–Heyde 1982), fringe-subtree counts (Holmgren–Janson 2014), high-degree vertex depths (Eslava 2022), or fixed-label high-degree behavior (Lodewijks 2022). The new claim concerns the **largest birth label with nonzero outdegree**, and proves its exact conditional leaf regression, all-size positive covariance, joint independent Rayleigh–Gaussian limit, and precise smaller-order covariance constant. None of the accessible statements supplies this mixed age-extremal law by direct implication. Eslava's full 2022 paper was searched and inspected as a primary contrast: its random variables concern high-degree depths, not the present statistic. General functional degree-evolution theorems might imply some limit by further specialization; this is an acknowledged residual risk. The Janson, Najock–Heyde, and Lodewijks full texts could not be conclusively inspected, so this is a best-knowledge comparison, not a priority certificate.

## Value — PASS

A terminal age run is an intrinsic cutoff of the growth process, distinct from root height and maximum degree. Its Rayleigh scale contrasts with the Gaussian aggregate leaf count. The exact survivor regression and mixed covariance constant reveal a nonzero second-order association despite independent principal fluctuations. This resolves a natural joint-structure question at all finite sizes and at two asymptotic scales, rather than merely obtaining a small change to a known expectation.

## Remaining limitations and prior work

The theorem is restricted to uniform recursive attachment and birth-label order; the latest-nonleaf event differs from depth and chronological last attachment to a specified old vertex. The actual daily online date of the selected verified baseline, Janson 2004-11-16, is available; older 1982 terminal-vertex work is cited by its printed month/year without inventing a day. An independently established equivalent joint theorem would supersede the originality assessment. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
