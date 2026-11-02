# Scientific review

## Correctness — PASS

The sample is well-defined in mean square because the operator is Hilbert--Schmidt and the isotropic coordinates have unit variance. The projected-energy trace formula is exact. Exchangeability gives a valid two-coordinate swap identity, making \(r_i=\mathbb E(X_i/T)\) nondecreasing as singular values decrease; its weighted-average consequence proves all spectral prefix inequalities. A second symmetrization establishes that the expected shares are decreasing. The exact residual difference is a sum of nonnegative pair terms. For infinite rank, every interchange is justified by a finite absolute upper bound, not by experiments. The supplied checker directly verifies 1,984 enumerated iid assignments and additional dependent/equality examples, with rational arithmetic.

## Originality — PASS, with residual priority risk

The earlier two-coordinate Rademacher residual identity is acknowledged and does not itself assert the all-cutoff majorization relation or the convergence of the global pair sum for arbitrary positive exchangeable amplitudes in infinite rank. The motivating primary 2026 full text defines cylindrical sketches and supplies sub-Gaussian tail bounds, not an exact spectral-share theorem. Classical and later randomized SVD surveys and general-distribution analyses use different controls (sample covariance and overall error bounds). Searches for weighted normalized-share majorization found no decisive exact equivalent, but a general preexisting theorem on exchangeable normalized weights could still imply part of the claim. The comparison is based on mathematical implication, not on title differences.

## Mathematical value — PASS

The theorem answers a natural distribution-selection question simultaneously at every spectral cutoff rather than only for one scalar residual. It identifies a deterministic sketch that is optimal for all monotone spectral rewards in this model, quantifies the cost of amplitude randomness for all mode pairs, and remains valid when the input isotropic sketch is only cylindrical and the output is Hilbert--Schmidt. The three-mode exact witness demonstrates that the result has content beyond the two-dimensional special case. The scope deliberately excludes several practical randomized SVD regimes.

## Closest literature and limits

Lynch-Davies and Webb, arXiv:2610.31333v1, Theorem 3.15 and Section 4; Saibaba and Międlar, arXiv:2308.05814; Halko, Martinsson and Tropp, arXiv:0909.4061; Diouane et al., arXiv:2206.08793. An older normalized-weight comparison theorem, not found in the inspected material, remains a possible historical-priority risk. The result is a one-column, singular-basis, expected-squared-error statement and does not assert performance for arbitrary orientations or multiple sketch columns.

Self-review: passed. Independent audit: not yet performed.
