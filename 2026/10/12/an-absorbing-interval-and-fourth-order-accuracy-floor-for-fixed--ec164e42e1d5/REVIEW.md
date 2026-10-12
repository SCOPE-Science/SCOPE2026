# Self-review

## Correctness — PASS

For a globally strongly convex \(C^3\) scalar objective, the centered derivative is strictly increasing with derivative at least \(\mu\), yielding a unique shifted zero. Taylor's theorem fixes the root shift and fourth-order objective gap. Between the shifted zero and the true minimizer, the approximate derivative has the wrong sign and the curvature-corrected proposal moves away from the minimizer; the two direct-sampling probes are uphill uniformly for sufficiently small radius. The explicit sine-modulated quadratic provides nonasymptotic inequalities through radius one. The reproducibility script checks finite instances, while the analytic proof covers every stated quantifier and boundary.

## Originality — PASS

The source CARS paper proves convergence to a prespecified tolerance under a radius bound of order \(\varepsilon^{1/4}\) and uses the original four-choice safeguard. It does not state the universal absorbing-interval mechanism, the signed third-derivative displacement, or a matched lower obstruction on required radius scaling. The STP precursor lacks CARS's extra Newton-style proposal, so fixed-step limitations of STP alone do not imply this obstruction. Targeted published-literature searches and accessible primary full text found no dominating statement. This is a provisional scientific priority assessment, not a proof against unindexed publications.

## Value — PASS

This is a structural boundary for a published zeroth-order optimizer under its natural smooth strongly convex hypotheses, not a small ad hoc numerical example. It establishes the necessity of the **exponent** in the source's accuracy-dependent radius regime by an attainable counterexample, identifies a continuum of permanent nonoptimal points, and explains a mechanism that remains after curvature correction and safeguarding. The scope is deliberately limited to fixed-radius scalar updates.

The CARS full-text algorithm and proof, the STP primary full text, and a 2023 thesis abstract/landing page were compared. The thesis full text was blocked by its landing-page access interstitial; specialized unindexed priority remains a disclosed residual risk. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
