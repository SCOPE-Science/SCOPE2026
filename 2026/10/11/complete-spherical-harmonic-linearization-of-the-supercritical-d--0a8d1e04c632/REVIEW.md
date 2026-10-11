# Same-model review

## Correctness — PASS
The claim follows by differentiating the published support-function equation at the constant stationary solution. The curvature-quotient derivative is fixed by the published formula for \(\dot G^{ii}\) and isotropy. The resulting operator is
\[
L=\frac{k\binom nk}{n}\bar\Delta-\binom nk(\alpha-k-1).
\]
The degree-zero eigenvalue exactly matches the derivative of the source's homothetic logistic ODE, and degree one supplies a second check because \(\bar\nabla^2Y_1+Y_1\bar g=0\). The bundled exact-arithmetic checker verifies the combinatorial coefficient and low-mode reductions but is not used as the proof.

## Originality — PASS
The lead 2026 paper was inspected through its flow derivation, convergence proof, homothetic sharpness remark, and constant-data corollary. It gives the global rate \(\binom nk(\alpha-k-1)\) and homothetic saturation, but no spherical-harmonic linearization or spectral gap. The complete 2020 isotropic predecessor was also inspected; it proves spherical convergence and exponential gradient decay without a harmonic spectrum. Exact database searches for the source identifier, linearization, explicit eigenvalue pattern, and scale-to-shape gap found only results for different curvature flows. Residual risk remains that an equivalent calculation occurs in unindexed literature.

## Value — PASS
The finding explains the mechanism behind the newly explicit sharp global exponent: the homothetic direction is not merely one saturating example but the unique slow eigenspace. Every nonconstant infinitesimal deformation decays faster by at least the exact amount \(k\binom nk\). This mode separation is a natural structural fact for stability and refined asymptotics of the stationary sphere.

Closest literature: arXiv:2609.35241v1; DOI 10.1007/s12220-019-00169-4. Closest indexed comparisons concern different spherical/nonlocal flows and do not imply this Euclidean dual \(k\)-Minkowski spectrum.

Limitations: the result is linear and does not itself prove a nonlinear faster decay theorem after removal or modulation of the scale mode.

Same-model review: passed. Independent audit: not yet performed.
