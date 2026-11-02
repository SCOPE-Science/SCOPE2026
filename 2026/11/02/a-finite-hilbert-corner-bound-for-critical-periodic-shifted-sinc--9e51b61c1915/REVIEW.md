# Review of the critical finite Hilbert-corner bound

## Correctness (C): PASS

For the explicitly normalized periodic Fourier matrix, same-sign columns are orthonormal, and the Gram matrix splits into identity diagonal blocks and one cross-sign block. Its minimum eigenvalue is exactly one minus the norm of that block. At the balanced sign junction, the selected \(\lfloor p/2\rfloor\)-by-\(\lfloor p/2\rfloor\) cross corner is, after separate row and column phase rotations, the positive Hankel matrix with entries \(1/[p\sin(\pi(j+k+1/2)/p)]\). Because \(0<j+k+1/2<p\), the sine is positive; the elementary inequality \(\sin x\le x\) then dominates the classical Hilbert corner entrywise. Testing its top nonnegative eigenvector proves the finite comparison. The 1962 de Bruijn–Wilf asymptotic, confirmed in Preissmann–Lévêque (2013, p. 201), gives the \(\pi^4/2\) upper-limit coefficient. No inference from finite experiments to an infinite-period limit is used. Floating-point checker: 343 finite assertions passed across 49 periods.

**Boundaries and risks:** The theorem gives only an upper bound, including a limsup, not equality or a matching lower bound. The Hilbert asymptotic is a cited theorem rather than reproved here. In particular, this review does not assert that the periodic cross norm has the same complete asymptotic expansion as the Hilbert finite-section norm.

## Originality (O): PASS, best-knowledge assessment

The most directly relevant 2026 paper, Vellucci–Samad, introduces the same periodic synthesis matrices and proves the cross-block representation (Theorems 5.1 and 6.1). Its Corollary 7.3 establishes degeneration only as an infimum over periods, while Conjecture 7.5 asks specifically for two-sided inverse-log-squared bounds. The inspected manuscript does not establish its upper estimate. The new proof uses the exact positive finite Hilbert corner, not an unproved identification of the periodic and infinite-step operators. The classical finite Hilbert asymptotic is fully credited to de Bruijn and Wilf; the 2013 Preissmann–Lévêque survey reproduces it and does not address these periodic shifted Fourier matrices. Searches for equivalent Riesz-bound and finite-Hilbert-section formulations found no dominating published mathematical statement. The result is therefore presented as a best-knowledge resolution of only one side of a new conjecture, not as a general Hilbert-matrix theorem.

**Residual risks:** Historical finite Cauchy–Vandermonde spectral estimates or perturbation-of-exponentials inequalities may imply the corner comparison in another guise. The original 1962 paper itself was not directly accessible, although its exact asymptotic formula was confirmed from the accessible 2013 journal text. These are publication-priority limitations, not evidence of independent validation.

## Value (V): PASS

The motivating paper singles out the critical logarithmic degeneration of the worst periodic lower synthesis bound as an explicit open two-sided inequality. Establishing its entire upper half in all periods gives a quantitative, nontrivial strengthening of the previously known limit-infimum zero statement, together with a computable finite-period comparison and an explicit universal leading limsup coefficient. The positive-corner argument bypasses an apparently necessary control of the rest of the periodized matrix and does not assume the separate balanced-pattern extremality conjecture. This supports further work on the harder matching lower bound and the exact asymptotic rather than merely recomputing a known table.

**Scope of contribution:** One-sided finite comparison and the asymptotic implication; no new claim about the exact Hilbert matrix asymptotic, complete extremizers, or the unrelated general Gram problem.

Self-review: passed. Independent audit: not yet performed.
