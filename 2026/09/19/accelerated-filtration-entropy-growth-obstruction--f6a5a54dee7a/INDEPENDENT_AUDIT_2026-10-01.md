# Scientific audit — 2026-10-01

## Final claim

For the polynomial algebra \(k[x]\), the set of algebraic-entropy values of finite-dimensional exhaustive algebra filtrations is exactly \([0,\infty]\).

## Correctness — PASS

For every finite lambda, the degree cutoff f(n)=n+floor(exp(lambda*n)-1) is increasing and superadditive, so it defines a finite-dimensional exhaustive algebra filtration of \(k[x]\). Its successive quotient dimension is asymptotic to (exp(lambda)-1)exp(lambda*(n-1)), giving entropy lambda. The standard degree filtration gives zero, and replacing the exponential by \(e^{n^2}\) gives infinite entropy. Thus the extended nonnegative spectrum is exactly \([0,\infty]\).

## Originality — PASS

After narrowing the final claim to the exact entropy spectrum of \(k[x]\), no earlier source located implies all finite values together with infinity. The broader growth-detection and linear-control claims are credited as prior and removed from the contribution.

The structured originality comparison records equivalent formulations, broader coverage, exact database/table checks, claim-versus-prior implication, source inspections, checked sources and residual risks in the accompanying JSON file.

## Scientific value — PASS

Determining the complete range of a filtration-dependent invariant on the simplest infinite-dimensional affine algebra is a natural classification. It quantifies exactly how far the entropy can vary under the definition and is more informative than another isolated counterexample to filtration invariance.

## Disposition

REPAIRED. This is a mathematical assessment of the stated claim, not a formal-proof certificate.
