# Scientific review

## Correctness — PASS

The exact generating identity \(H_n(z)=e^{-\lambda z}G(z/n)^n\) and Charlier–Parseval orthogonality convert the density's squared Poisson \(L^2\) distance into a weighted entire-function norm. Finite support provides an exponential-growth bound globally; analyticity of \(\log G\) gives a quadratic-Gaussian dominator on the expanding inner disk. Therefore the normalized densities converge strongly in \(L^2\), proving the chi-square and total-variation coefficients. A bounded entropy Taylor quotient and uniform integrability prove the half-chi-square entropy coefficient, including the infinite tail. The truncated-exponential family has exactly nonnegative rational masses and prescribed first nonzero factorial cumulant. The included standard-library checker passed 1368 finite assertions. Limiting results rely on the analytical arguments, not on finite tests.

## Originality — PASS, subject to historical-priority risk

Theorem 22 of Harremoës, Johnson and Kontoyiannis (arXiv:1601.04255) is the closest implication: it supplies the same-normalization *lower bound* on the all-order relative entropy rate, but not matching upper bounds or convergence in the finitely supported class. Kavvadias (arXiv:2608.02927, Proposition 3.20) supplies a general second-order *upper bound* under different density hypotheses, not exact all-order limits. Zacharovas and Hwang (arXiv:0810.4756) already prove the Charlier–Parseval identity and second-order Poisson-binomial estimates; the identity and generic expansion method are expressly credited rather than claimed as new. Accessible mathematical-record comparisons and literature searches did not locate the stated finite-support all-order exact entropy hierarchy. Older general asymptotic expansions could conceivably imply it implicitly; independent historical validation remains necessary.

## Value — PASS

The result closes a mathematically motivated gap between a published all-order information-divergence lower bound and an exact upper rate for a natural and explicitly characterized class. It establishes a complete classification of finite-support convergence exponents, computes the exact constants in three natural discrepancy metrics, and constructs fixed laws with arbitrarily strong polynomial information convergence. The variance-matched example has \(n^4\) rather than the generic \(n^2\) information rate, so the cancellation is not merely a reparametrization of the usual Poisson limit law.

## Scope and residual risks

Only fixed finite support, fixed positive mean, independent samples and independent unitwise thinning are treated. The result does not extend itself to unbounded support or varying inputs. The main historical risk is implicit coverage by older general Poisson–Charlier approximation literature, despite no directly matching statement identified in the primary works inspected. Independent validation has not yet been performed.

Self-review: passed. Independent audit: not yet performed.
