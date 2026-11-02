# Self-review

**Final claim assessed:** three equally spaced observations of one stable planar rotation through a scalar output; exact Gram determinant, globally sharp high-damping envelope and the unique high-damping optimal-spacing expansion. Noise variance normalized to one.

## Correctness: PASS

The 3x2 Cauchy--Binet expansion proves the exact determinant for arbitrary positive frequencies and intervals. The inequality \(\sin^2 x\le x^2\) gives a universal finite-parameter envelope; the scaled limit at fixed \(u=ah\) proves the constant is sharp. Derivative reduction to \(1/u-m(u)\), together with the exact quartic polynomial identity bounding \(v\), proves a unique nondegenerate envelope peak. Uniform localization and strict concavity prove uniqueness of the true design for all sufficiently small \(\omega/a\); the analytic implicit-function theorem gives the stated second-order spacing and determinant constants. The zero-information resonant times are explicitly included in the quantifiers. The standalone checker validates the algebra and numerical expansions without being substituted for proof.

## Originality: PASS, with priority limits

Direct statement/implication comparison to the closely aligned full-text complex-OU D-optimal design in arXiv:1704.05719 shows a different random-process model, observed coordinates, unknown parameters and objective determinant; its precise formulae do not contain this initial-condition estimator as a corollary. General Gramian sparsification (arXiv:2005.03143) and randomized sensor-selection Kalman covariance bounds (arXiv:2303.07903) likewise neither dominate the sharp three-time theorem nor imply the asymptotic optimizer coefficients. Semantic research-record searches for damped-rotation three-sample Fisher optimization, high-damping sampling asymptotics and alternate Gramian formulations returned closest but mathematically distinct results (including an arithmetic-spectrum flow with amplitude-and-slope observations). prior claim inventory includes random-phase observability tails and greedy Kalman scheduling, but not this fixed deterministic design. An uncatalogued earlier exact experimental-design calculation remains a residual priority risk; this is not independent publication certification.

## Value: PASS

Three samples of a rapidly decaying oscillatory output must balance phase separation against signal attenuation. The theorem supplies the sharp attainable information scale, a universal coefficient, a unique asymptotically optimal time separation, its correction at finite frequency, and a numerical sample-budget comparison. These quantify a specific motivated limitation of initial-state reconstruction, rather than merely rewriting observability. The theorem does not address irregular time design, correlated noise, or joint estimation of dynamics.

## Closest literature, limitations and evidence

- Baran, Szák-Kocsis, Stehlík, arXiv:1704.05719 (2017): stationary complex OU estimation, full-text Secs. 2--3 and Appendix A; adjacent D-optimal context but distinct information matrix.
- Siami, Jadbabaie, arXiv:2005.03143 (2020): joint sensor/actuator Gramian schedule approximation.
- Calle, Bopardikar, arXiv:2303.07903 (2023): random sensor selection, stochastic Kalman covariance guarantees.
- published-finding corpus closest: arithmetic-spectrum D-optimal horizon (research record 64dbf45b5739); different amplitude-and-slope object.
- Fixed-three-time historical novelty beyond searched sources cannot be guaranteed without independent field review.

Self-review: passed. Independent audit: not yet performed.
