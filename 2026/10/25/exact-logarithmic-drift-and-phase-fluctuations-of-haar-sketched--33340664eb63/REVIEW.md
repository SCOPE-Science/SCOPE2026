# Independent mathematical audit

## correctness

PASS

PASS — Writing u=e^(iθ), z=re^(iψ), direct real projection produces z⁺/z=1+it(1−e^(2i(θ−ψ))); conditional rotational Haar invariance makes each factor iid for a fixed nonzero starting vector. Their circular support is entirely in upper half-plane, avoiding zero; uniform log-series about 1+it has coefficients w^j/j with |w|²=q, giving mean ln|1+it|+i atan t, complex second moment E[(L−EL)²]=0 and E|L−EL|²=Li₂(q). Thus equal log-radius and unwrapped-phase variance Li₂(q)/2 and zero cross covariance. E|multiplier|²=1+2t² and det(I+2tuuᵀJ)=1 checked. For gain 2, exact MSE formula and Taylor expansions give E error²/h→ω²T|z0|², while bounded triangular-array log increments satisfy Lindeberg and covariance ω²T/2. Independently checked four full-angle Fourier/log quadratures and three h→0 MSE cases; their finite-step deviations are O(h), not counterexamples.

## originality

PASS

PASS, qualified — Dong–Schwerdtner–Peherstorfer 2025 already defines the Haar-sketch integrator and provides generic bias and strong-error bounds, which are not new. General SL(2,R) Lyapunov and isotropic matrix-product machinery (Sturman–Thiffeault, Forrester–Zhang) is also prior, but inspected sources do not supply simultaneously the joint exact unwrapped phase/radial Fourier law and the sharp compensated time-integration MSE coefficient. A plausible 2026 Q. Dong rotational-invariance article was only abstract-readable; its exact exponent coverage is a residual priority risk, not a fabricated whole-document exclusion.

## value

PASS

PASS — Randomized projected integration of a conservative oscillator has potentially hidden geometric instability. The exact positive radial Lyapunov drift despite stepwise determinant one, isotropic phase/radial second-order law, and the sharp compensated mean-square integration error provide concrete analytical calibration beyond generic convergence bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
