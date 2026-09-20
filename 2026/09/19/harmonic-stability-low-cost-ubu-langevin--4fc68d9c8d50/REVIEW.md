# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For a quadratic target, orthogonal diagonalization reduces each scheme to independent scalar curvature modes.  Substitution of the LC-UBU, LCT-UBU, and LCP-UBU coefficients from arXiv:2609.20713 gives the three explicit 2 by 2 amplification matrices in `RESULT.md`.  Applying the classical Jury conditions to their characteristic polynomials yields the stated necessary-and-sufficient regions.  The Taylor condition `1 - trace + determinant > 0` forces the strict barrier z<2; the Padé determinant condition is either automatic or weaker than the displayed `1 + trace + determinant > 0` bound.  The derivative calculations give the exact minima 24/7 and 2+sqrt(2).  The stiff-friction limits then follow directly from the three threshold formulas.

Adversarial checks included the boundary cases z=2 and s equal to the threshold, whether the Padé determinant creates a hidden second restriction, the weak-friction Verlet limit, the sign of every Jury factor, and mode reduction for a general SPD Hessian.  The additive noises have positive-definite one-mode covariance because their two Brownian kernel functions are linearly independent, so no unstable deterministic direction is silently unforced.  The verification artifact compared the analytic classification with direct eigenvalue classification on 30,000 deterministic pseudo-random points for each scheme and found zero mismatches.

## Originality

**PASS, to the best of our knowledge.** The motivating preprint arXiv:2609.20713 was inspected at the method definitions and coefficient formulas for LC-UBU, LCT-UBU, and LCP-UBU, as well as its stated convergence results.  The paper introduces these low-cost schemes and establishes Wasserstein error rates, but the inspected text does not state the exact harmonic Schur regions, the hard Taylor friction barrier, the Padé minimum, or the three-way stiff-friction step-size scaling reported here.

Harmonic and linear stability analysis for Langevin integrators is not new.  Grønbech-Jensen, Journal of Statistical Physics 193, 12 (2026), was inspected as a close general reference: it develops a broad linear framework for stochastic Verlet-type integrators and gives harmonic stability criteria for established schemes.  Accordingly, the use of a harmonic oscillator, amplification matrices, and the Jury/Schur criterion is explicitly excluded from the novelty claim.

Searches used the exact names LCT-UBU and LCP-UBU, the source identifier 2609.20713, low-cost UBU plus harmonic/linear stability terminology, and the distinctive threshold forms.  No checked source stated the source-specific phase diagram.  The residual originality risk is that older stochastic-Verlet, splitting, or rational-approximation literature may imply individual formulas once the newly introduced schemes are translated into a different parameterization.  The claim is therefore restricted to the theorem package in `RESULT.md`, not to generic harmonic stability methodology.

## Value

**PASS.** The source paper shows that the three low-cost UBU variants share the same formal second-order convergence rate under its assumptions.  The exact phase diagram reveals a qualitatively different property that order analysis does not capture: in the stiff-friction regime the exponential method's stable step grows linearly with friction, the Taylor method's stable step collapses inversely with friction, and the Padé method approaches a curvature-controlled constant.  This gives a concrete criterion for choosing between exponential and exponential-free implementations and identifies a sharp failure boundary for the Taylor replacement.

## Limitations

The theorem is for quadratic potentials and Schur/finite-second-moment stability of the resulting affine Gaussian chain.  It does not establish nonlinear stability, sampling-bias superiority, or a global guarantee for nonquadratic targets.  The invariant covariance within the stable region is not analyzed.  General Hessian-based use outside the quadratic setting is diagnostic only unless additional assumptions control variation of the Hessian.
