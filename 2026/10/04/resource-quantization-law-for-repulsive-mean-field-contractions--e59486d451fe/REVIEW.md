# Same-model scientific review

## Correctness
PASS. The claim was reconstructed from the definitions. The resource-targeted coupling is strictly increasing, the atomless quantile update is exact, and the common resource term cancels in the pre-map \(W_1\) distance. The derivative bounds on \(T\) give the contraction factor \(L(1-\varepsilon)\). The fixed-point increment inequality was solved algebraically on both sides, and its cellwise integral gives the two-sided resource-quantization law. Ordered particle ranks, preservation of order, and the transient recurrence were checked directly. No finite experiment is used to infer an infinite theorem.

## Originality
PASS. The closest primary source, arXiv:2609.28664v1, treats homogeneous resources and states its finite-particle bounds in the uniform-grid scale. Full-text comparison found no arbitrary-resource theorem, and the source lower bound does not contain the denominator \(1-\tau(1-\varepsilon)\). A broader self-consistent-transfer-operator review was also checked and did not supply a dominating theorem. Statement-level searches for nonuniform resources, target quantiles, resource quantization, and finite-particle equilibrium found no equivalent result. Residual risk remains that the target-quantile extension is implicit folklore because the transport substitution is natural.

## Value
PASS. The result addresses a motivated modeling gap: heterogeneous resource availability. It identifies \(e_N(\rho)=W_1(\rho_N,\rho)\) as the finite-size control parameter and separates this discretization scale from the dynamical contraction. The homogeneous specialization also yields a strictly stronger lower equilibrium estimate than the motivating source, so the contribution is not only a change of notation or target measure.

## Closest literature and limitations
The closest work is R. Castorrini, S. Galatolo and M. Tanzi, arXiv:2609.28664v1, together with M. Tanzi's 2023 review (DOI 10.1007/s40574-023-00350-2). The theorem is restricted to one-dimensional strictly monotone contractions and a continuous strictly increasing bi-Lipschitz resource quantile. It does not cover atomic resource distributions, higher-dimensional rank couplings, or uniqueness among arbitrary atomic invariant measures.

Same-model review: passed. Independent audit: not yet performed.
