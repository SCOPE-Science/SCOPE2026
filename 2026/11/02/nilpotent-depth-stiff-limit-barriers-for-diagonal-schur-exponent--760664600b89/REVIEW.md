# Scientific review

## Correctness — PASS

The statement specifies \(d\ge1\), \(0<\rho<1\), \(h,\kappa>0\) and a fixed positive integer \(k\). Direct substitution of the standard scalar \(\varphi\)-functions into exponential Euler and the two-stage ETD2 corrector produces exact quadratic shift polynomials with coefficients \(p\), \(u=p^2/z\), and \(v=p(z-p)/z\). They satisfy \(0<p<z\), \(u,v>0\), and \(u+v=p\). Substochastic row and column bounds prove strict Euclidean contractivity, independently of the exact dissipativity inequality. The exact exponential is a finite polynomial times \(e^{-z}\). Matrix-power continuity and the exact norm of the truncated shift yield the two piecewise limits, including \(d=1\), \(d=2\), and equality at \(k=d\) or \(2k=d\). No finite computation is treated as a proof of these limits.

## Originality — PASS, qualified

The motivating 2023 Schur-decomposition paper presents diagonal exponentiation with explicitly handled triangular couplings and notes the potential for additional error; the relevant Schur discussion was inspected without finding an exact nilpotent-depth limit for the two specified steppers. The 2005 full-text exponential Runge–Kutta analysis supplies a more general stiff-order framework, but its fixed-operator/regularity setting does not yield the singular \(\kappa\)-dependent explicit residual estimate or the exact piecewise finite-horizon constants. The 2023 Jordan–Schur matrix exponential paper computes the full triangular matrix function rather than the diagonal-only split. Published research records on Lanczos positivity, Jordan norm pencils and Richardson stability concern different algorithms and do not imply the stated limit. Some specialized earlier analyses of nonnormal exponential integrators or equivalent explicit polynomial limits might exist; publication priority is not guaranteed.

## Value — PASS

The exact defect persists for a positive, norm-contracting and strongly dissipative family, ruling out two usual explanations for poor stiff behavior. The dimension thresholds \(d=2\) and \(d=3\), plus the sharp \(k\)-step nilpotent-depth cutoffs and algebraic post-threshold residue coefficients, make a reusable benchmark for how many explicit coupling edges a diagonal-Schur scheme resolves before fast modes vanish. This is a motivated structural classification for two widely used numerical schemes, not an arbitrary numerical parameter slice. The result does not claim universality across other methods or automatic failure of fixed-stiffness convergence.

## Remaining limitations

The operator is a particular Jordan-chain family and the limit fixes \(d,h,k,\rho\) before letting \(\kappa\) grow. General nonnormal matrices, adaptive controllers, arbitrary semilinear perturbations and practical floating-point stability are unproved. Priority relative to all specialized literature remains a risk. The accompanying 2838 checks are finite confirmations and not formal proof certificates.

Self-review: passed. Independent audit: not yet performed.
