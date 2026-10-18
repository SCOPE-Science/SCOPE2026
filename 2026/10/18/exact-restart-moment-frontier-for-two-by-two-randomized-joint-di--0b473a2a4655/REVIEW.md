# Scientific review: exact restart-moment frontier

## Correctness — PASS

The specified algorithm and output loss are those of the Gaussian best-of-trials orthogonal RJD method. The proof derives the eigenvector rotation from the actual Gaussian matrix pencil, computes both off-diagonal Frobenius residuals without linearization, and obtains the exact minimum-order-statistic law. An elementary arctangent integral gives the one-trial identity. Uniform Taylor control gives the two-trial logarithmic asymptotic with its coefficient. Dominated convergence is valid only for three or more trials; for three, integration by parts yields the exact constant. The global optimum \(2\varepsilon^2\) is independently found by minimizing over all planar orthogonal rotations. The standalone exact-rational checker, explicit numerical eigenbasis reconstruction and quadrature reproduce the identities; neither finite tests nor numerical integration are used to assert the infinite-parameter theorem.

## Originality — PASS, with residual priority risk

He and Kressner's arXiv:2212.07248, Algorithm 1 is the exact preexisting algorithm and loss, and Theorems 6 and 8 give probabilistic upper bounds. Section 3.4 explicitly predicts and observes the \(L\)-dependent tail exponent. These results make the sufficiency of three trials for bounded mean-square error inferable from tail integration and do not count as new here. The inspected main results, analysis and experiments do not give the exact two-by-two loss distribution, the leading one-/two-/three-trial expectation constants, or a proved two-trial logarithmic lower obstruction for a fixed simple pair. The random congruence-diagonalization paper arXiv:2402.16557 considers a different transformation; the joint-eigenvalue paper arXiv:2409.00500 derives different Rayleigh-quotient error guarantees. Published mathematical searches for equivalent orders of Cauchy-ratio singularities, near-commuting random diagonalization and restart-moment thresholds did not identify a covering exact theorem. Such an equivalent formulation may nevertheless exist outside the inspected material, and independent priority validation is outstanding.

## Value — PASS

The squared-residual expectation is a meaningful numerical accuracy metric but cannot be read directly from high-probability statements at the mean-square scale. The explicit smallest-dimensional near-commuting example proves that two independent restarts are inadequate for a constant-factor expected squared loss despite asymptotically small input perturbations, while three suffice, and gives exact leading constants. This provides a quantitative stress test and a tight example explaining the relationship between the published tail phenomenon and expected solver quality. The result is not a theorem about all RJD inputs, other sampling rules, deflation, floating-point arithmetic or runtime.

## Evidence and remaining limitations

Primary source: He--Kressner, *Randomized Joint Diagonalization of Symmetric Matrices*, arXiv:2212.07248, Algorithm 1, Theorems 6 and 8, Section 3.4. Related full text: arXiv:2402.16557 and arXiv:2409.00500. Reproducibility: `verify.py` (standard-library-only exact rational tests and deterministic integration). The full theorem is supported by the written proof and not certified by independent formal or expert review. The possibility of equivalent results in uninspected specialized literature remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
