# Scientific review

## Correctness — PASS

The published mass function has the exact factorization \(P(X=x)/(C\tau)=(1+t)e^{-\theta t}\), with \(t=\tau x\) for nonnegative \(x\), and \(t=-x/\tau\) for negative \(x\). Strict concavity of \(\log(1+t)\) makes all ordered adjacent secant thresholds strictly decreasing, and the adjacent log-mass differences prove the exhaustive mode set for every \(\theta>0\). Positive grid intersections occur if and only if \(\tau^2\) is rational, and elementary divisibility gives the complete sign recurrence classification. No finite computation substitutes for the strict-concavity or infinitude arguments. The attached standard-library checker confirms selected probability ratios, normalization, unique modes, and equality boundaries.

## Originality — PASS, with priority risk

Salinas et al., *Symmetry* 18 (2026), 533, Section 2.4.6, establish half-line unimodality and suggest comparing a few candidates. That fact does not provide the exact global staircase or characterize infinitely many signed modal reversals. Alyami et al., *Symmetry* 17 (2025), 2148, study symmetric sign-magnitude laws, while Kozubowski–Inusah, *Ann. Inst. Stat. Math.* 58 (2006), 555–571, use geometric-only tails; neither statement logically covers the linear-geometric merged-grid DADL theorem. Searches for source title, modal aliases, rational-grid coincidence, and exact secant parameters in published finding records and research literature found no covering theorem; failed search is not proof of universal novelty. Remaining priority risk is an unindexed direct or reformulated result, rather than a known stronger covering theorem.

## Value — PASS

The paper's focus is modeling signed counts, and it explicitly discusses practical global mode location without an analytic global classification. The theorem gives every exact shape transition and tie, an explicit test for persistent two-sided modal multiplicity, and a sharp arithmetic criterion showing that even a fixed tail-asymmetry parameter need not fix the sign of the global mode as concentration changes. These are distributional shape constraints useful when calibrating or interpreting signed discrete outcomes; no claim is made about population skewness, sample inference, or sample-size effects.

## Limits and closest literature

The theorem applies to the particular DADL kernel with positive shape parameters and fixed \(\tau\); it does not generalize automatically to other linear-geometric families. The finite checker is illustrative. The cited 2026 source was read through its open full-text HTML presentation, and the classical skew discrete Laplace probability mass was checked from the original open-access paper. Independent priority and correctness review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
