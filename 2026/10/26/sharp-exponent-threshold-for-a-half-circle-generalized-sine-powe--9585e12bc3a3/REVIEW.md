# Scientific review: half-circle generalized sine-power covariance

## Correctness — PASS
The exact cosine-integral identity is obtained by differentiating \(\sin^{\alpha+1}t\cos((n-1)t)\); the endpoint evaluation is valid for every \(\alpha>0\). The even-frequency recurrence has a constant negative sign for the admissible exponents. The odd-frequency recurrence yields the explicit fifth coefficient and an all-frequency two-step positivity induction. Beyond the threshold the fifth or fourth harmonic is strictly negative. Bochner's criterion and a consecutive-frequency Vandermonde argument complete the equivalence and strictness. The supplied checker independently verifies 384 Fourier integrals, symbolic coefficient identities, and an inadmissible finite witness; it does not substitute for the universal proof.

## Originality — PASS under bounded comparison
Gneiting's original 2011 preprint poses the generalized sine-power family as a parameter classification problem. The present result settles its natural half-circle support on \(\mathbb S^1\), giving a sharp exponent \(8-\sqrt{41}\) and exact Fourier support. The 2011 spherical Pólya paper supplies sufficient conditions under convexity, not the nonconvex exponent range up to the new threshold. The 2015 circle-product strictness criterion is an abstract Fourier-support condition and does not evaluate these coefficients. Multiple indexed mathematical searches, together with the accessible prior-claim ledger, did not return an equivalent threshold. Residual risk: an unindexed source, particularly earlier circle covariance literature, may have the same special-case classification; a relevant 1998 paper's full text was not available.

## Mathematical value — PASS
A natural fixed-radius section of an explicitly posed open parameter problem has a complete sharp answer, including a genuinely nonconvex admissible interval \(1<\alpha\le8-\sqrt{41}\), the exact obstructing harmonic, and strict endpoint interpolation. The threshold is not an arbitrary numerical slice: the support radius \(\pi/2\) is a symmetric intrinsic angular cutoff, and the exponent controls the kernel's local roughness. The recurrence also gives a reusable positivity method for related Fourier-sign questions.

## Independent status and limits
The result does not classify other support radii or higher-dimensional spheres. Accessible-source novelty checks are bounded; no independent proof verification has been performed.

Self-review: passed. Independent audit: not yet performed.
