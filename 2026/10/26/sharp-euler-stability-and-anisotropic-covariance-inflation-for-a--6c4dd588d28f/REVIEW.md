# Scientific review

## Correctness — PASS

The exact Itô update is matched to Equation (17) of Louis, Pavliotis and Vilmart [1]. Direct multiplication yields the full symmetric second-moment matrix and its Perron-dominating two-dimensional block. The positivity of \(I-K_h\) is equivalent to the explicitly stated quadratic inequality. A unique crossing and its boundary multiplicity are proved rather than inferred from finite tests. The stationary covariance and strictly positive normalized anisotropy follow by exact solution of two linear moment equations. The finite-invariant-moment impossibility past the frontier follows from a positive left Perron eigenvector. Independent full-operator numerical checks and exact-rational algebraic checks support the analytic proof. Risk: the theorem is confined to second moments and the specified update.

## Originality — PASS, subject to independent priority verification

Closest inspected source: G. Louis, G. A. Pavliotis and G. Vilmart, arXiv:2610.03191 [1], particularly continuous-time Theorem 2, Equation (23), the Euler experiment in Section 6.1, and the discrete-analysis question in Section 7. The foundational predecessor [2] handles the continuous process. Lang, Petersson and Thalhammer [3] provide abstract tensor-product numerical mean-square stability criteria but do not state the exact spectral root or normalized covariance bias for this particular multiplicative-noise sampler. Other published harmonic UBU and randomized integrator claims involve different recursions. An equivalent derivation in broader noncommuting linear-SDE literature could still exist; no uniqueness or priority certification is claimed.

## Mathematical value — PASS

The sharp frontier quantifies a real time-stepping limitation of the source’s accelerated sampler and rules out trusting contraction of first moments alone. The exact overdispersion and anisotropic difference expose finite-step distortion of quadratic observables and give a usable step-selection warning. The \(\lambda\downarrow0\) uniform positive limiting threshold is informative in the singularly anisotropic regime. No higher-moment, full-law, or alternative-integrator theorem is asserted.

## Source and verification limits

Primary material inspected: complete accessible original arXiv article [1], full six-page 2019 source PDF [2], and the definitions and operator-criterion sections of the open-access 2017 stability paper [3]. Reproducibility: `verify.py`, `verification-output.txt`. Finite tests check selected parameters; the universal claim rests on the written exact proof. Independent priority and correctness assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
