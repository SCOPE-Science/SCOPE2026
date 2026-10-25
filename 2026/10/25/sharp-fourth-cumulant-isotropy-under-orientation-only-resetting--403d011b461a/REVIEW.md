# Scientific review

## Correctness — PASS

With stationary angular initialization the angular-reset generator is \(q\partial_\theta^2+r[f(\theta_*)-f(\theta)]\). Its order-two Fourier mode is a centered eigenfunction of decay rate \(r+4q\), giving an exact two-time covariance. Conditional on the orientation path, the projected displacement is normal with a random time-integrated variance, and its fourth cumulant equals three times that variance's variance. Integrating the exponential covariance gives the stated finite-time formula. Independently, the Fourier-mode generator hierarchy for \(\mathbb E[Z^2e^{ik\Theta}]\) and \(\mathbb E[Z^4]\) reproduces 90 numerical parameter/time/direction cases in `verify.py`. The sharp threshold follows from the proved factorization of the fourth harmonic, and strict positivity follows from the strictly positive invariant angular density. The finite-time statement is explicitly limited to stationary angular preparation; a nonstationary start gives an asymptotic growth-rate statement.

## Originality — PASS, with residual risk

The primary source, Chaki–Olsen–Löwen, arXiv:2406.17550v1, Section V, supplies the orientation-only reset model and second moments but does not explicitly give the fourth cumulant or its angular isotropy threshold in the complete available text. A related active-particle work, arXiv:2501.05149v1, Section III.3 and Appendix C, discusses first two displacement moments, while arXiv:1005.1343v1 examines fourth moments without orientation resetting. Position-only resetting and active-propulsion orientational dynamics have non-equivalent generators and distinct observables. Focused published-record and mathematical-database searches found no result implying the complete formula and unique \(r=2q\) fourth-cumulant cancellation. This is not a definitive priority certification: older modulated-diffusivity cumulant calculations might implicitly contain an equivalent case.

## Mathematical value — PASS

The second-order anisotropic effective diffusion tensor is known. The new exact fourth-order result distinguishes finite-time non-Gaussian displacement fluctuations from their Gaussian scaling limit and detects a counterintuitive state: an isotropic fourth-cumulant tensor coexisting with a strictly anisotropic second cumulant. The unique crossing rate and reversal of two experimentally measurable projection orderings make the statement a motivated, complete classification rather than an arbitrary parameter evaluation.

## Boundaries

No assertion is made about full positional stationarity, raw fourth-moment isotropy, orientation-dependent reset laws, active propulsion, or finite-time cancellation for a deterministic initial angle. Independent verification of publication priority is outstanding.

Self-review: passed. Independent audit: not yet performed.
