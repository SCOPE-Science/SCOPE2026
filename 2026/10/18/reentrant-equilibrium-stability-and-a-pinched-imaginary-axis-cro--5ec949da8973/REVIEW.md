# Scientific review

## Correctness — PASS

The state-space and parameter quantifiers are explicit. Eliminating the equilibrium equations yields the two real symmetry-related points exactly for \(k<a/c\); the full Jacobian gives coefficients \(Q,R,S\) and a two-factor Routh determinant. Positivity of \(Q,S\), the exact Routh first column and a complete sign analysis imply the full stable/index-two regions. At an equality, \(p=(\lambda+Q)(\lambda^2+R)\) is the exact spectral certificate. A second-order perturbation establishes the positive contact coefficient. The standalone symbolic checker reconstructs the characteristic polynomial, determinant and quadratic coefficient; nineteen numerical cases are only corroboration, not the proof.

## Originality — PASS, with risks

The original Dong (2022) full text was examined in sections 2 and 3.4, including its fixed-parameter Routh calculation and numerical scans. The earlier 2010 Yang–Wei–Chen model is the \(k=0\) source and cannot establish the whole negative-feedback interval. published-finding corpus searches targeted exact model terms, aliases, controller stability and the reentrant parameter thresholds. None of the returned papers states or dominates the full Dong family result. Risk remains from an unindexed equivalent controller calculation; this assessment is not a claim of unique global priority. The general Routh criterion is acknowledged, and novelty is specifically the complete system-dependent factorization and pinched spectral topology.

## Mathematical value — PASS

The family exhibits an analytically sharp, \(b\)-independent, bounded stability interval for \(a>c\), although both parameter extremes are index-two unstable. At \(a=2c\) the entire interval collapses into a quadratic imaginary-axis contact; no stable parameter survives. This is a structural distinction not supplied by sampled bifurcation diagrams. It permits exact exploration and interpretation of feedback-controlled equilibrium coexistence.

## Scientific limitations

The statement concerns local Jacobian spectra and local exponential stability on hyperbolic stable branches, not global attraction. Imaginary eigenvalues do not prove a nonlinear Hopf bifurcation; there is no first Lyapunov coefficient or existence theorem for nearby cycles. Residual unindexed-literature priority risk is acknowledged.

Self-review: passed. Independent audit: not yet performed.
