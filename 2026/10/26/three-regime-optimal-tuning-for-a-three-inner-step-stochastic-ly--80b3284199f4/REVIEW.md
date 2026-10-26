# Scientific review

## Correctness — PASS
The stated operator is realized by a mean-square-stable two-state multiplicative-noise process; conjugation by the swap matrix is a self-adjoint involution on the symmetric Frobenius space. The exact three-inner-stage polynomial separates into two nonzero eigenspaces, reducing the worst-case contraction to the maximum of two explicit quadratic polynomials in the tuning parameter. Their sum, difference and derivatives yield a complete global minimax proof over every real parameter, including negative parameters and both transition endpoints. The actual packaged `check.py` confirms the critical symbolic identities and reproducible finite cases; numerical cases do not substitute for the universal proof.

## Originality — PASS
The closest primary source, He et al. (arXiv:2607.00451), already supplies the general polynomial recurrence and the second-step parameter analysis, but not the optimized three-inner-step signed-spectrum classification. Their Remark 2 explicitly leaves higher-degree parameter optimization for further analysis. The present result includes a nontrivial two-transition global minimax analysis, rather than merely substituting eigenvalues into their spectral-radius formula. Comparisons with mathematical records and related claims did not identify a covering result. The multi-step Smith–inner–outer paper by Tian et al. (2020) is relevant but its full text was unavailable; this is a residual originality risk, not evidence of absence.

## Mathematical value — PASS
The signed pair is the smallest natural spectrum that includes both positive and negative eigenmodes of a positive stochastic Lyapunov map. The exact regime switch distinguishes balanced eigenmode constraints, a one-mode stationary optimum, and ordinary Smith iteration, and quantifies an extra asymptotic power of improvement in weak coupling with a single parameter. This is a complete rate-optimal classification for a motivated minimal stochastic matrix equation; no extension to general operators or independent certification is claimed.

## Closest literature and limitations
He et al. (2026), equations (12), (14), (18), Theorem 2, Remark 2 and Section 4, is the closest accessible source. Chen et al. (2025 online, 2026 volume) study a separate one-step explicit recurrence; Tian et al. (2020) study multi-step Smith iterations in a different continuous coupled setting. Only the first source's complete mathematical paper was inspected; the others leave explicit bibliographic risk. The theorem covers two-state swapping dynamics, three inner stages, a common real parameter, symmetric Frobenius error, and exact arithmetic, not general spectra or stagewise-positive approximations.

Self-review: passed. Independent audit: not yet performed.
