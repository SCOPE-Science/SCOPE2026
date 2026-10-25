# Scientific assessment

## Correctness — PASS

A four-endpoint Hermite reconstruction yields the stated residual polynomial exactly. For every finite residual exponent, differentiating its positive normalized integral proves the strict uniform sensitivity bound \(4<\nu_p<5\). Independently, elementary polynomial arithmetic locates a unit-modulus Runge–Kutta point with \(\mu>5\); the exact feedback Jacobian then has determinant larger than one at every positive controller gain and limiter operating-point slope. The argument holds analytically across the claimed quantifiers. The standalone exact-polynomial checker and representative numerical derivative tests passed; they are not substituted for the proof.

## Originality — PASS (best knowledge)

Ranocha and Giesselmann, arXiv:2307.12677, already derive the Hermite estimator and illustrate I-controller instability for selected parameters; these established observations are credited. The new assertion is a *common, exact, all-gain and all-finite-\(p\) instability arc*, with a strictly quantitative separation \(\mu>5>\nu_p\). The inspected primary paper's central cubic-Hermite section and stability discussion do not assert or imply that uniform bound as a stated theorem. The earlier adaptive RK/PI/PID treatment in arXiv:2104.06836 concerns different controller families/estimators. Published mathematical finding searches returned an embedded Fehlberg RK4(5) estimator resonance, which neither contains the central Hermite residual nor the I-controller Jacobian theorem. An uninspected earlier equivalent argument or a general stability theorem with the same implication remains a residual risk; no claim of exhaustive literature coverage is made.

## Value — PASS

A numerical instability plot at one gain need not rule out stabilizing the controller by changing its gain or the residual norm. This exact result proves that neither modification—and neither any ordinary smooth positive-slope limiter—can remove this particular local instability, within the specified I-type family. It supplies a concrete design exclusion boundary rather than a trivial local Taylor identity.

## Limits

Only the scalar complex equation, a fixed third-order stability polynomial, central cubic-Hermite residual, positive-gain I feedback, and local unrejected-step dynamics are covered. No PI/PID or step-rejection conclusion is made, and no independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
