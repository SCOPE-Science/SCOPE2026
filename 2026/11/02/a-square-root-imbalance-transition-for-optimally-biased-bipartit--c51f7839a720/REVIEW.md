# Scientific assessment

## Correctness — PASS

The optimality claim follows from a common-uniform coupling of visited-count processes at each alternating part arrival. The full cover-time law follows from independent geometric waiting times for successive discoveries on the two parts; parity supplies the final offset. With fixed positive control probability, these waiting times have uniformly bounded moments, and triangular-array normal limits, uniform integrability and Chebyshev bounds establish the distributional, expectation and last-part limits. The standalone exact rational checker passed 6250 finite assertions, supplementary to the analytic proof. Boundary conditions include one initially visited vertex and the forced first arrival in the opposite part.

## Originality — PASS, qualified

Haslegrave, Sauerwald and Sylvester (arXiv:2006.02475) establish the controlled walk, general cover-time inequalities and algorithmic results but not the exact bipartite factorization or square-root imbalance terminal law in the inspected primary text. The conference predecessor (doi:10.4230/LIPIcs.ITCS.2020.76) and the two-choice paper (arXiv:1911.05170) likewise do not state this result; the two-choice transition kernel is mathematically different. Broad coupon-assignment theory is a potential source of the greedy-policy subclaim, which is not claimed separately as an independent foundational novelty. Ross and Wu (2013) was identifiable only through abstract-level material; fuller historical priority assessment remains outstanding.

## Value — PASS

The exact finite-sample representation converts a difficult-looking history-dependent controlled cover problem into two independent completion clocks. The resulting sharp imbalance window and explicit expected-time correction quantify when control changes which part is likely to be visited last. This is a natural statistic for network exploration and distinguishes controlled motion from uncontrolled bipartite coupon collecting; neither an arbitrary finite parameter slice nor an isolated textbook normal approximation is the claimed contribution.

## Scope and residual risks

Fixed positive control probability, full graph completeness, independent decisions and a starting vertex in the first part are essential to the proof. Varying control probabilities and more general graphs require new analysis. An inaccessible general stochastic-assignment source may bear on policy optimality, though its abstract does not imply the joint distributional theorem. Definitive historical priority and independent mathematical verification remain open.

Self-review: passed. Independent audit: not yet performed.
