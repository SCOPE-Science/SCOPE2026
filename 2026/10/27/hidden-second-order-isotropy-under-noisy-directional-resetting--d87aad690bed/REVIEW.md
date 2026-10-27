# Scientific assessment: hidden second-order isotropy under noisy directional resetting

## Correctness — PASS
The stationary angle generator fixes the first two Fourier coefficients. Its first-mode semigroup yields the exact all-time Green–Kubo covariance. Decomposition of the traceless heading covariance proves the complex condition \(a_2=a_1^2\); monotonicity of the two-angle polynomial gives its unique threshold and boundary. The additional positive transverse term from random mixture follows from the law of total covariance. The independently executed standard-library checker passed 2646 assertions, supporting but not replacing the analytic proof.

## Originality — PASS, subject to independent scholarly priority assessment
Kumar, Sadekar and Basu (2020, arXiv:2008.03294) already imply the fixed-heading endpoint at \(q=1/2\); that case is credited. Baouche et al. (2024, arXiv:2405.06769v1) introduce a general angular reset-law framework but work out displacement moments for a point-mass reset direction. The new statement is the all-time complex-harmonic cancellation criterion together with a strictly interior two-angle isotropy curve, complete sharp anisotropy classification, and random-angle transverse mixing correction. Chaki et al. (2024, arXiv:2406.17550) study a passive shape-anisotropic object; Ghosh et al. (2025, arXiv:2501.05149) consider related active anisotropic transport but do not identify this classification in inspected sections. A broader uninspected theoretical result could imply it; scholarly priority is not independently certified.

## Scientific value — PASS
Angular refresh jitter is a natural perturbation of fixed-orientation resetting. The exact family shows that positive mean propulsion can coexist with completely isotropic centered displacement covariance at all positive times; the sign diagram identifies transport-anisotropy inversion, and the positive rank-one mixing term prevents an invalid averaging shortcut. These are interpretable, testable second-order structural statements, not merely recomputations of fixed-heading tables.

## Scope and remaining risks
Requires stationary angle process, fixed rates \(r,D_R,v>0\), independent Poisson angular redraws, and stationary additive thermal Brownian motion. The claim is centered covariance isotropy, not isotropy of the complete displacement distribution or a stationary spatial position law. The two-angle classification assumes equal-probability symmetric headings. No finite-sample inference guarantee is proved. Independent literature priority review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
