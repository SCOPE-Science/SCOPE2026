# Self-review

## Correctness
**PASS.** The support-two identity follows directly from the finite-population formulas and leaves no admissible possibility for a strict reversal. For three sorted incomes, exact algebra gives \(G=2(\ell+\nu)/3\) and \(P=\max\{\ell,\nu\}\). The displayed equal-total witness has exact fractions \(1/3,13/48,7/24,7/24\), giving opposite strict rankings. The packaged exact-rational verifier returns `VERIFY_OK`.

Risk: the support notion is for equally weighted households; weighted empirical distributions require a different formulation.

## Originality
**PASS.** Prior literature already states that Gini and Pietra rankings are not identical in general, so disagreement existence is not claimed as new. The accepted contribution is the sharp empirical-support boundary and exact three-household sum-versus-maximum criterion. Full-text treatments of Gini and Pietra were inspected, targeted semantic searches did not locate the support-two impossibility/support-three sharpness statement, and a directly relevant 2026 Hoover–Gini preprint was identified but its full text was inaccessible through the available route.

Risk: because the proof is elementary, an unindexed exercise or software test could contain the same witness.

## Value
**PASS.** Gini and Pietra are standard inequality summaries with distinct interpretations: average pairwise spread versus the one-shot redistribution share needed for equality. Knowing the smallest population size at which they can make opposite inequality judgments is a natural structural calibration. The three-household formula pinpoints the mechanism rather than merely supplying a numerical example.

Self-review: passed. Independent audit: not yet performed.
