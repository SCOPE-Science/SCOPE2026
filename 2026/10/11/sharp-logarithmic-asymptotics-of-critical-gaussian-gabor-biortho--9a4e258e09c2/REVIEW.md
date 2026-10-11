# Review of Sharp logarithmic asymptotics of critical Gaussian Gabor biorthogonals

## Correctness — PASS

The normalization \(g(t)=e^{-\pi t^2}\) matches the 2026 primary source. The 2025 full-text Zak formula for the unit-norm Gaussian has derivative \(2^{1/4}\pi\theta_1'(0,e^{-\pi})\); dividing by \(2^{1/4}\) gives the derivative used here. Its simple, isotropic zero at \((1/2,1/2)\) is fully controlled. The numerator of the dual Zak quotient vanishes there, and orthogonality of the remaining lattice characters proves the exact biorthogonal formula.

The local reciprocal-square difference is at most \(A/r\), so multiplication by the bounded numerator has an integrable, **uniform** error. Angular averaging gives exactly \(4\pi\int(1-J_0(t))dt/t\), where the standard stationary-phase decay of \(J_0\) yields \(\log R+O(1)\). The leading coefficient is therefore \(4/(\pi|\theta_1'(0,e^{-\pi})|^2)\), not a normalization-dependent guess. Integer lattice covariance gives exact norm equality for arbitrary deleted atoms. The optional numerical probe agrees with the coefficient; no finite sample is used as proof.

## Originality — PASS

The lead 2026 source explicitly labels the logarithmic growth of squared biorthogonal norms **Conjecture 4.1** and says the estimates are not verified. The 2025 primary full text supplies the dual Zak quotient, the uniqueness of the Zak zero and its nonzero derivative, but only uses these to establish exactness and the absence of Schauder and reproducing-pair properties. It does not state a uniform norm-growth estimate or a leading constant. The new proof performs the nontrivial radial-frequency asymptotic, proves a bounded error uniform in lattice direction and transfers the result to every deleted atom.

Searches of published results and semantic mathematical records under the source ID, Gaussian Gabor biorthogonality, dual-norm asymptotics, Zak/theta localization, and sharp logarithmic coefficients found no equivalent covering result. The 2025 source contains nearly all of the analytic infrastructure, so the genuine novelty is explicitly limited to the quantitative asymptotic and its uniform sharp coefficient; an unindexed independent derivation remains possible.

## Value — PASS

The theorem proves a named, newly stated open quantitative conjecture in time-frequency analysis. It computes the universal constant controlling the exact dual cost at large critical-lattice separation, not merely a coarse comparison, and turns an implicit sufficient norm condition for weighted lower semi-frames into an explicit logarithmic summability test. The direction-independent asymptotic distinguishes a genuine two-dimensional logarithmic singularity from an artifact of finitely many numerical experiments.

The theorem neither claims a Schauder basis nor a necessary classification of all weights. The lack of an explicitly computed additive constant is a scientific limitation but does not weaken the claimed sharp leading law.

Same-model review: passed. Independent audit: not yet performed.
