# Self-review

## Correctness — PASS

With two independent Gaussian evaluations, the scalar Anderson quotient reduces exactly to \(X=x-F_0^2/D\), where \((F_0,D)\) is a nonsingular jointly Gaussian pair. Conditional Gaussian integration gives a positive density at the denominator singularity and the exact \(t^{-1}\) tail coefficient; the tail-integral criterion gives the full moment threshold, including the logarithmic boundary. For ridge regularization, a rescaled one-dimensional Gaussian integral and uniform control of the regular remainder yield the exact positive \(\lambda^{-1/2}\) second-moment constant. All quantifiers, positivity, independence, and the special case \(a=0\) were checked. The standalone script passed 3,636 finite verification checks; finite tests do not prove the limiting theorem.

## Originality — PASS, with residual risk

The 2026 Adler–He–Hu–Lefebvre primary work was examined in its available full HTML form; it establishes deterministic Anderson/two-grid error propagation, not an independently Gaussian-noisy output distribution or a vanishing-ridge moment constant. Older Aitken extrapolation and Gaussian-ratio phenomena explain the rational mechanism and are not claimed as new. Toth et al. (2017) study inaccurate evaluations, including stochastic errors with unbounded support, which is the closest conceptual overlap. Its abstract/front matter was available, but a complete inspection was blocked by access; it remains a genuine bibliographic risk rather than evidence that the present constants were absent. Lupo Pasini–Laiu's 2024 approximate-calculation paper was available only through the abstract. Targeted publication and mathematical-record searches and accessible historical claim comparisons did not identify the combined exact result. An unsuccessful search cannot certify uniqueness.

## Value — PASS

The statement addresses a mathematically motivated stability gap in a widely used acceleration rule: Gaussian noise with all finite moments can create an accelerated output without even a first absolute moment, while ridge tuning has an exact singular risk cost. The coefficient-level result specifies the practical boundary between no safeguard and arbitrarily weak regularization, even for the zero map. It does not purport to settle stochastic multistep convergence or supersede existing bounded-error results.

## Remaining scientific and bibliographic limitations

The principal limitations are scalar affine dynamics, a single accelerated step, independent Gaussian oracle calls, and the absence of longer-horizon conclusions. The unavailable full 2017 source and equivalent classical stochastic Aitken analyses remain literature-comparison risks. The verification program is supplementary numerical evidence rather than independent certification.

Self-review: passed. Independent audit: not yet performed.
