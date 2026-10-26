# Scientific review: paired extreme-error transition

## Correctness — PASS

The exact least-squares normal equation reduces both rowwise errors to coupled Gaussian ratios. Conditional independence of the shared residual sketch from the two row regressors follows from orthogonality. For distinct row directions, rescaling the two Gaussian regressors gives a bounded-domain integral; Gaussian density at the origin and a finite radial moment yield the explicit \(t^{-q}\) coefficient. At coincident directions the two squared errors are identical and the sharp decay is \(t^{-q/2}\). Direct algebra, the spherical integral and all boundary conditions were rechecked. The numerical verifier ran 2,759 finite assertions, which do not substitute for proof.

## Originality — PASS under accessible comparisons

Gallmeier–Otto (2026, arXiv:2610.07513), Algorithm 1/Theorem 1, establishes rowwise reconstruction and an expected error guarantee. Amsel et al. (2024, arXiv:2402.09379) give the related fixed-coordinate subspace result and a Markov bound. Browne–Andrews (2023, arXiv:2306.03593), following earlier statistics work, supplies Student regression-sketch laws and prevents claiming novelty for an individual row's heavy tail. What is newly asserted is the exact *two-row simultaneous* asymptotic with nonaligned angle coefficient and exponent collapse at alignment. Related published probability and numerical records were compared by scientific implication rather than title. An earlier specialized theorem on dependent self-normalized Gaussian ratios could still imply the result; priority is not independently certified.

## Mathematical value — PASS

The direction correlation does not affect either row's mean squared error or marginal failure tail, yet controls the probability of simultaneous numerical failures, with a discontinuous extreme-tail exponent at exact alignment. Such risk dependence is relevant to simultaneous reliability of a forward-only approximation assembled from rows sharing one Gaussian query batch. The theorem is a natural sharp two-row boundary case rather than a general algorithmic convergence statement.

## Limitations

Two rows only, single known direction per row, the same unit residual orthogonal to both, Gaussian query entries, fixed angle and exact arithmetic. The asymptotic is not uniform in near-coincident directions, and no claim is made about arbitrary matrices, all error tolerances, or finite precision. Source comparison is limited to accessible relevant material.

Self-review: passed. Independent audit: not yet performed.
