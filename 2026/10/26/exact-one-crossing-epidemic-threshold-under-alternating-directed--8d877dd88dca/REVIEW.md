# Review of exact one-crossing epidemic threshold under alternating directed contacts

## Correctness (PASS)

The monodromy is the product of two exact \(2\times2\) exponential matrices. Each off-diagonal generator squares to \(pqI\); the normalized product is symmetric positive definite of determinant one, with trace \(2+4\kappa^2\sinh^2(a\tau)\). Its principal eigenvalue therefore has logarithm \(2\operatorname{arsinh}(\kappa\sinh(a\tau))\). The explicit second derivative of this scalar function is negative exactly when \(p\ne q\), giving strict decrease of the dominant Floquet exponent on every positive duration. The endpoint limits, all equality cases, uniqueness, and the two asymptotic regimes follow analytically. The exact numerical example and standalone randomized checker agree with the formulas. No claim of stochastic persistence or critical nonlinear stability is made.

## Originality (PASS, with residual uncertainty)

Primary-source comparisons distinguish this exact theorem from general infection-propagator spectral criteria (Valdano et al., 2014/2015), the continuous-time SIS treatment of undirected contact snapshots (Speidel et al., 2016), the opposite-direction two-node Parrondo effect under mostly symmetric adjacency examples (Sejunti et al., 2024), the general Floquet criteria for periodically switched linear systems (Gökçek, 2004), and sufficient dwell-time stability criteria for positive systems (Lian and Liu, 2013). None of the materially inspected claims states the mirrored positive off-diagonal law, a strict all-duration monotonicity theorem, the full iff switching window, or the two critical-duration asymptotics. A full mathematical priority claim cannot be guaranteed: an algebraically equivalent result may exist in specialized positive-matrix-product literature.

## Mathematical value (PASS)

The theorem characterizes a meaningful, minimal mechanism: two individually disease-free-stable directed contact environments become invasion-capable when their directional asymmetry is reversed sufficiently quickly. It gives an exact quantitative intervention threshold and a complete sign diagram, rather than a numerical example or a reformulation of a generic Floquet criterion. The criterion separates geometric-mean, arithmetic-mean, and recovery scales, with sharp sensitivity near both boundaries. The two-group, equal-duty restriction and linearized interpretation are substantive limitations.

## Closest literature and limitations

Compare the precise statements in the literature review and references of `RESULT.md`. The strongest conceptual precedents are the temporal-network monodromy criterion, the general existence of instability under switching of stable generators, and the positive-systems dwell-time theory. These do not, in their inspected forms, resolve the exact strictness and one-crossing statement here. The residual risk of equivalent coverage is recorded in `AUDIT.json`. Computational tests are supplementary to the analytical proof.

Self-review: passed. Independent audit: not yet performed.
