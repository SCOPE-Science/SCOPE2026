# Scientific review: sharp Hölder Bergman exterior response

## Correctness — PASS

The positive disk weight is explicitly Hölder of exponent \(\alpha\). Fourier-mode orthogonality gives a tridiagonal moment matrix with \(\gamma_n=2\varepsilon B(2n+2,1+\alpha+i\tau)\). The resulting exact monic polynomial recursion yields both the nonzero \(n^{-\alpha-i\tau}\) exterior correction and the separate \(n^{-2\alpha}\) leading-coefficient change. Uniform exterior control follows from the decaying recursion coefficient. The accompanying reproducibility script tests the finite formulas and constants; the proof covers every positive degree.

## Originality — PASS under inspected evidence

Hübner, arXiv:2610.24693v1 (first public 2026-10-17), proves exterior asymptotics for positive Hölder weights with a quantitative bound for exponents strictly below \(\alpha\). The explicit nonzero sharp endpoint correction, normalization coefficient and log-periodic cluster circle are not supplied by its inspected theorem and relevant proof sections. Hedenmalm–Wennman, arXiv:2008.02682, treats analytic weights, excluding this boundary perturbation. published-finding corpus semantic searches for one-band angular moment matrices, Gamma/Beta corrections and log-periodic phases found no corresponding prior claim. Classical Suetin literature could conceivably contain an implicit specialization; full passages were not accessible, and search failure does not prove uniqueness.

## Mathematical value — PASS

The construction directly determines whether a general Hölder-error theorem can be sharpened beyond its natural regularity exponent. It supplies a positive, constant-boundary-data, minimally nonradial benchmark in which the pointwise response has sharp order \(n^{-\alpha}\) while its normalization responds only in second order. This is a motivated boundary case for strong planar orthogonal-polynomial asymptotics rather than just a numerically computed constant.

## Limitations

Only one angular Fourier mode is analyzed. The result is not a universal upper bound for arbitrary Hölder weights. There is a residual historical priority risk from inaccessible classical material, and there has been no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
