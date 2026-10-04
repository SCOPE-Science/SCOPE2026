# Same-model review

## Correctness
PASS. The last equation has the exact bounded-complete-trajectory representation
\[
z(t)=\int_{-\infty}^t e^{-\alpha(t-u)}x(u)^2\,du,
\]
which proves \(z\ge0\) on every compact invariant support and forces the origin if \(z=0\) occurs on such a trajectory. For arbitrary continuous \(\varphi(z)\), stationarity of an antiderivative gives
\[
\int\varphi(z)(x^2-\alpha z)\,d\mu=0.
\]
This is exactly
\[
\mathbb E[x^2\mid z]=\alpha z.
\]
The localized Borel-set identity, size-bias formulation, and moment hierarchy follow directly.

Risk: the proof uses standard support invariance and conditional-expectation approximation on a compact coordinate range.

## Originality
PASS. The closest implication-level prior result is a published balance theorem for the linearly equivalent Rucklidge flow. Its full statement was inspected and it already covers integrated stationary moments after scaling. Those integrated consequences are explicitly excluded from the novelty claim. Same-object homoclinic, global-dynamics, and integrability sources were compared, and targeted searches for the conditional, heightwise, and size-bias formulations returned no coverage.

Risk: the full 2020 integrability paper was not securely available, so a hidden conditional-disintegration observation there remains a specific residual risk.

## Value
PASS. The result determines stationary \(x^2\)-energy separately at every height, rather than only after integrating over height. Equivalently, it identifies the complete \(x^2\)-weighted height distribution as the size-biased height marginal and fixes all moments \(\mathbb E[x^2z^k]\). This is a structural invariant-measure constraint that is strictly finer than the previously covered integrated balance.

Same-model review: passed. Independent audit: not yet performed.
