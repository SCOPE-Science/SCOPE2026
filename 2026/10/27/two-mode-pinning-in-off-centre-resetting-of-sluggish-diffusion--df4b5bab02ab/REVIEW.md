# Scientific assessment

## Correctness — PASS

The canonical Bessel pair is normalized by its explicit origin value and derivative, has constant Wronskian, and satisfies the distributional reset equation. Integration gives unit mass, while exponential-reset regeneration identifies the unique invariant law. The nonstandard global peak-count step is derived from the strict decrease of the auxiliary energy \(E=q'^2-rx^\alpha q^2\), which forces strict log-concavity of the decaying branch; the growing branch is monotone. The scalar mode condition has a unique root. The opposite-side mass follows by integrating the ODE and identifying the standard hitting resolvent. An independent numerical implementation passed 112 assertions. All hypotheses and asymptotic boundaries are included in RESULT.md; the proof does not infer continuum uniqueness from numerical sampling.

## Originality — PASS, with residual risk

The 2026 originating paper already supplies the centered distribution, modified-Bessel reduction, and the hitting transform, and formally writes an off-origin source term. The 2022 heterogeneous-resetting Green function explicitly treats nonzero resets but uses \(\partial_x(D\partial_x\rho)\) rather than the Itô forward term \(\partial_x^2(D\rho)\). Neither inspected stationary analysis gives the displaced-source two-mode theorem, exact pinning threshold, or opposite-side mass law for the specified conservative generator. The general resolvent method is established background. A broader theorem might entail some part of the formulas without using the same vocabulary, so independent priority review remains necessary.

## Value — PASS

Moving the reset point while keeping the physical mobility centre fixed is a natural control dimension for anomalously slow searchers. The theorem gives a complete phase classification of all stationary maxima for every positive sluggishness and rate, including the exact pinning boundary; this is stronger than plotting profiles or calculating a single parameter case. The crossing-probability identity ties the satellite peak's total mass to an independently meaningful first-passage observable. Such structure distinguishes the nonhomogeneous Itô model from both ordinary Brownian restarting and other heterogeneous diffusion conventions.

## Limits and closest sources

The proof assumes one-dimensional nonsticky natural-scale diffusion, fixed positive rate, a point reset, and \(\alpha>0\). It does not cover alternative interface extensions, drifted heterogeneous diffusion, or random resetting sites. Closest primary sources: Frimpong–Bresque–Roldán (arXiv:2610.21962v1), §§3–5, 8; Lenzi et al. (arXiv:2201.05598v1), §§II–III. Potential implicit inclusion in a more general resolvent treatment is the main residual originality risk.

Self-review: passed. Independent audit: not yet performed.
