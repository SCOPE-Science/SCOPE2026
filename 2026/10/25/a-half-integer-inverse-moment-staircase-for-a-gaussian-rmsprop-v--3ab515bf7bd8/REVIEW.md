# Scientific review

## Correctness — PASS

For the exact scalar Gaussian accumulator, the infinite series defines the unique invariant distribution under a contractive affine recursion. The finite-startup inverse-moment cutoff follows from polar integration of a strictly positive Gaussian quadratic form. The stationary Mellin representation is justified by Tonelli and explicit Gaussian Laplace transforms. On each noncritical interval \(k/2<p<(k+1)/2\), rescaling the integral and using an integrable beta-function majorant proves the stated sharp coefficient. At \(p=k/2\), a log-coordinate change gives a plateau supported on an interval of unit length; three explicit integrable majorants establish the exact logarithmic coefficient. The analytic proof covers every \(p>0\) and every \(0<\beta<1\), including critical boundaries. Supplementary numerical quadrature completed 25 checks; it is not a replacement for the proof.

## Originality — PASS (provisional historical priority)

The source arXiv:2608.30382v1 introduces the relevant bias-corrected second-moment recursion and proves inverse-moment *bounds* in Section 4 after startup, but does not assert a sharp small-\(\beta\) stationary Gaussian asymptotic, its half-integer staircase, or its critical logarithmic constants. Its main optimization theorem concerns a different coupled process and a parameter range bounded away from zero. arXiv:1908.03265 uses a scaled inverse-chi-square approximation for adaptation variance; that approximation does not imply exact limits for the infinite geometrically weighted Gaussian sum. arXiv:2404.01436 concerns general optimization convergence, not these scalar invariant-law asymptotics. Targeted searches of earlier mathematical findings, Gaussian quadratic forms, reciprocal moments, and stationary adaptive accumulators identified no mathematically dominating statement. Negative searches are not proof of priority; possible older Mellin analyses of geometric quadratic forms remain a residual risk.

## Mathematical value — PASS

The reciprocal moments of second-moment accumulators are required to control adaptive denominators in stochastic optimization. The theorem supplies exact sharp constants and all phase transitions, distinguishes finite startup from stationary integrability, and quantifies why letting the memory parameter tend to zero is singular even though each positive value regularizes every inverse moment. The claim is mathematically motivated by an existing 2026 study of RMSprop inverse-moment control, not merely a numerical table or renaming.

## Scope and outstanding limitations

This is a scalar independent-Gaussian denominator theorem, not an optimization-convergence theorem. The archive of older geometric Gaussian quadratic-form results has not been exhausted. Numerical assertions are diagnostic only, and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
