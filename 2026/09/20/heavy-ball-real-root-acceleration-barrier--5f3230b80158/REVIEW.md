# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces the real-root constraint to a connected-interval dichotomy for
\(s_\lambda=1+\beta-\alpha\lambda\): the whole spectral interval must lie either above \(2\sqrt\beta\) or below \(-2\sqrt\beta\). On the positive branch, monotonicity of the larger positive root reduces the best case to \(\alpha L=(1-\sqrt\beta)^2\); direct evaluation of the characteristic polynomial at \(1-\mu/L\) then gives a strict lower bound for every positive momentum. On the negative branch, the endpoint \(L\) gives a lower bound after substituting \(\kappa=L/\mu\), and evaluation at the optimal gradient-descent factor proves the same strict obstruction. The zero-momentum case reduces exactly to the standard two-endpoint minimax calculation for gradient descent. The nonnegative-root frontier follows from the same positive branch. Representative deterministic calculations reproduce the formulas and the classical Polyak endpoint/interior root structure.

A central scope point was checked explicitly: the theorem is an interval-robust statement. It would be false if rephrased as saying that every individual finite-dimensional matrix accelerated by heavy ball must possess an eigenvalue with complex characteristic roots, because a spectrum supported only at the interval endpoints can avoid the complex-curvature interior.

## Originality

**PASS, to the best of our knowledge.** Polyak (1964) gives the classical accelerated parameters. Qian (1999) analyzes individual-mode roots and critical damping. Torii--Hagan (2002) study momentum stability; Zhang (2015) studies globally optimal double parameters. Danilova--Kulakova--Polyak (2018/2020) explicitly document repeated endpoint roots and complex interior roots for the classical optimal heavy-ball choice. Hagedorn--Jarre (2023/2024) provide an explicit modern spectral-radius formula separating real and complex root regimes, and Ugrinovskii--Petersen--Shames (2023) prove quadratic worst-case asymptotic optimality by robust-control methods.

No checked source stated the constrained minimax theorem proved here: among fixed heavy-ball parameters whose characteristic roots remain real for every curvature in the entire interval \([\mu,L]\), the smallest possible interval worst-case spectral radius is exactly the optimal gradient-descent factor, attained only at zero momentum. The associated exact nonnegative-root frontier was likewise not located. The theorem is elementary enough that independent rediscovery is plausible. Full theorem-level text of Torii--Hagan (2002) and Zhang (2015) was not available in the checked sources, so these are the principal residual coverage risks.

## Value

**PASS.** The result converts the familiar observation that classical optimal heavy ball has complex interior roots into a converse structural boundary: interval-robust acceleration over optimal fixed-step gradient descent is impossible while all curvatures remain in the real-root regime. The additional nonnegative-root frontier quantifies the stronger cost of forbidding modal sign reversal. These statements give a compact interpretation of why accelerated heavy-ball tuning must cross a damping-regime boundary, while separating that interval-level necessity from claims about any one discrete spectrum.

## Scientific limitations

- Fixed parameters, exact gradients, nonnegative momentum, and strongly convex quadratics only.
- The criterion is uniform over a continuous spectral interval and does not imply that every finite matrix instantiated with accelerated parameters contains an eigenvalue in the complex-root subinterval.
- The spectral radius is asymptotic; no monotonic finite-time norm bound is asserted.
- Complex roots are necessary under the theorem's interval-robust criterion, not sufficient for acceleration.
- Adaptive momentum, negative momentum, line-search methods, stochastic methods, nonlinear objectives, Nesterov acceleration, and conjugate-gradient methods are outside the claim.
- Torii--Hagan (2002) and Zhang (2015) were not inspected at full theorem level, leaving residual originality uncertainty.
