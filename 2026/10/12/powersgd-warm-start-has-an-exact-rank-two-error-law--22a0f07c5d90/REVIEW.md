# Review

## Correctness

PASS. Repeated rank-one PowerSGD reuse makes the left factor proportional to \(M(M^\top M)^{t-1}q_0\). In singular coordinates, the residual is an explicit ratio of two Gaussian quadratic forms. Rotational invariance reduces the expectation to a one-angle integral whose elementary evaluation gives the stated finite-step formula. The packaged verifier reproduces both the pointwise and expected identities.

Scientific risk: the theorem is for a fixed rank-two matrix and squared Frobenius compression error.

## Originality

PASS. The defining PowerSGD paper gives Gaussian initialization, warm-start, empirical approximation gains, and asymptotic fixed-matrix subspace convergence. Classical randomized low-rank theory gives general probabilistic bounds. The inspected sources do not state the exact finite-step rank-two expectation or its condition-number law.

Residual risk: an unindexed randomized-linear-algebra note may contain the same two-dimensional integral outside PowerSGD terminology.

## Value

PASS. Warm-start is central to PowerSGD's practical design. The formula shows exactly why it can matter: a fresh random start is a factor \(\kappa\) above the optimal residual, whereas one reuse has only \(O(1/\kappa)\) relative excess at large gap. This is a sharp and interpretable compressor benchmark rather than a generic asymptotic observation.

Self-review: passed. Independent audit: not yet performed.
