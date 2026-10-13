# Scientific review

## Correctness — PASS
Positivity, monotonicity and boundedness hold globally for every positive finite initial datum. A strictly positive limiting predator population would force an integrable, uniformly continuous numerical-response gap to vanish, hence prey convergence to the maximum-response point; its limiting negative prey derivative contradicts convergence. Once the predator goes to zero, two-sided logistic comparison forces prey to carrying capacity. The exact differential equation for the prey-deficit/predator-density quotient gives a limiting ratio, and the derivative of reciprocal squared predator density has a positive constant limit. These steps produce the exact critical coefficients without extrapolating finite computations. Symbolic rational-identity checks in `verifier.py` support the algebra.

## Originality — PASS
The 2026 motivating paper [1] already contains the response-maximizing density and the fold parameter, so **neither of those is claimed new**. Its Theorem 4 tests strict linear predator-free invasion signs but not equality. Its Theorem 8 has a positive coexistence cusp at \(\gamma=2/\sqrt b\), whereas the new result is at a predator-free boundary with \(\gamma=1/\sqrt b\). Its positive-coexistence global theorem cannot cover this no-positive-equilibrium regime. Prakash--Vamsi [2] analyzes AF Holling-IV with a positive predator self-competition term; that changes the leading decay equation. Exact/alias and stronger-coverage searches in prior records and indexed literature returned no covering statement. A related 2019 predecessor [3] was only accessible in abstract, and potential more general local critical normal forms remain bounded prior-art risks. No uniqueness guarantee is inferred from database partitioning.

## Mathematical value — PASS
Two independently natural equalities (maximal numerical response versus mortality, and coincidence of optimum prey density with carrying capacity) produce a genuine, degenerate invasion threshold. The finding resolves global extinction rather than just a local linear test, quantifies universal critically slow predator loss, and gives matching prey recovery with explicit dimensional parameters. Direct predator competition would change the leading balance, so the model choice has structural meaning. No wider robustness or applied intervention outcome is asserted.

## Sources and limitations
Main full-text comparison: Verma et al., arXiv:2606.26340v1, Secs 3--4 and 6 (https://arxiv.org/abs/2606.26340). Second full-text comparison: Prakash--Vamsi, arXiv:2504.09078v1 (https://arxiv.org/html/2504.09078v1). Abstract-only related predecessor: DOI 10.1007/s10441-019-09371-x. The result excludes initial zero prey or predator, off-threshold parameters, positive predator competition, and stochastic or spatial effects. The reviewer has not independently verified the literature exhaustively.

Self-review: passed. Independent audit: not yet performed.
