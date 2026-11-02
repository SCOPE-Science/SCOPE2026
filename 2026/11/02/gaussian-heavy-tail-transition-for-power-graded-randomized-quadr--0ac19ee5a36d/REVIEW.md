# Review: Gaussian–heavy-tail transition for power-graded randomized quadrature

## Correctness — PASS

The claimed universal distributional laws reduce to a single independent centered series by an exact scaling identity. An explicit uniform-cell integral supplies the cell variance, Taylor expansion supplies the power exponent and coefficient, Kolmogorov's theorem and a sub-Gaussian remainder yield the non-Gaussian limit, and Lindeberg–Feller yields the two Gaussian limits. Differentiation proves the unique optimal fixed power exponent; polynomial identities give exactly \(3/(4n^3)\) in the cubic example. The executable exact-arithmetic verifier passed its finite-instance tests. Finite tests are corroborating evidence, not an infinite proof.

## Originality — PASS (qualified)

Chopin–Gerber (arXiv:2210.01554, 2022) analyzes smooth cubic stratification and Haber constructions; the endpoint singularity is outside that source's \(C^r\) hypotheses. Carpentier–Munos (arXiv:1210.5345, 2012) gives earlier optimal smooth-function oracle allocation; its continuous square-integrable gradient hypothesis is violated here. Their allocation principle is acknowledged and not claimed as new. Actual mathematical-record searches did not locate this singular three-regime distributional classification or exact all-n equal-variance identity. Earlier overlooked graded-quadrature work is a live residual priority risk; independent checking remains outstanding.

## Value — PASS

A precisely specified and natural Monte Carlo integration problem undergoes a sharp heavy-tail/log-Gaussian/Gaussian transition that controls reliability and confidence modeling. The power exponent maximizing asymptotic variance efficiency is unique, and a particularly natural singular exponent has an exact equal-variance mesh at every finite resolution. This yields concrete design guidance beyond existing differentiability-based guarantees, without any claim of new generic stratification methodology.

## Scope and limitations

One-dimensional power-law integrand, deterministic power mesh, independent uniform samples, fixed exponent. The variance theorem requires \(0<lpha<1/2\). Optimality is only within the fixed power-graded family. Complete global prior-art coverage is not established.

Self-review: passed. Independent audit: not yet performed.
