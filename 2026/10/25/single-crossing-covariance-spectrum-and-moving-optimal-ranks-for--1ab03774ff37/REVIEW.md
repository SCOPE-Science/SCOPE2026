# Scientific review

## Correctness — PASS

The covariance follows from one fixed Gaussian error propagated through the finite Landweber geometric sum. For any two distinct positive normal eigenvalues, differentiation of their covariance ratio shows a strictly decreasing ratio: the function \(s/(e^{st}-1)\) decreases strictly in \(s>0\). The ratio starts at the eigenvalue ratio greater than one and converges to its reciprocal below one, so there is exactly one crossing. The scaled finite-iteration covariance filter has a unique maximum because \(\sum_{h=0}^{K-1}q^{-h}\) decreases strictly with \(q\) and crosses \(2K\) once. Strict one-crossing excludes leftward motion of the consecutive variance-optimal rank blocks. Exact two-level covariance limits prove the stated arbitrary trace loss. The companion checker passed 6,254 finite comparisons, supporting rather than replacing these proofs.

## Originality — PASS, subject to historical priority risk

Abhishek–Holman (arXiv:2610.00882v1), especially equations (3.6), (3.26) and (3.27) and Section 3.6, already provide Landweber covariance formulas, leading eigenspace approximations, and the importance of small singular directions. The assessed result is specifically the exact all-pairs once-only variance-rank crossing and the consequent globally contiguous, one-way covariance-optimal spectral windows, together with the exact loss fraction for the fixed leading-normal subspace. Neither that source's inspected sections and appendices, nor the additional inspected spectral-filter material, supplied these global ordering assertions. The 1994 Vogel–Wade work on truncated SVD is historically relevant; its full primary text could not be materially inspected, so independent priority is still uncertain.

## Mathematical value — PASS

Iterative inverse-problem uncertainty quantification requires selecting a low-dimensional representation of propagated uncertainty. This theorem explains why a leading-normal-operator subspace optimal at the first iteration need not remain appropriate for the covariance and supplies a complete, predictable moving-window structure rather than just a numerical counterexample. It gives an arbitrarily poor trace-retention worst case for a fixed leading-normal subspace, a quantitatively motivated failure mode. It does not assert failure of methods accounting for residual covariance, nor make claims about reconstruction fidelity, higher Landweber stepsizes, correlated noise, or confidence coverage.

Self-review: passed. Independent audit: not yet performed.
