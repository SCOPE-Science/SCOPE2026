# Scientific review

## Correctness — PASS

The residual average is an independent Gaussian factor because its cross covariance with every residual difference vanishes. Gaussian regression yields a full-rank residual-difference matrix and, after projecting one column away from the other \(m-1\), a nondegenerate isotropic Gaussian remainder of dimension \(d-m+1\). Its inverse-radius moment is finite exactly below that dimension, and independent residual-average noise forces the corresponding Anderson coefficient moment to diverge at and above it. The output separates as \(H\alpha+B\), where \(H\) has full column rank and \(B\) has all moments, precluding cancellation of the heavy tail. Fixed positive ridge regularization bounds the inverse singular-value filter and makes every output polynomial moment finite. The included checker passed 12,310 identities and matrix checks. The infinite-domain arguments are proved analytically; sampling alone would be insufficient.

## Originality — PASS, subject to publication-priority risk

The accessible primary text of Lupo Pasini et al. (arXiv:2110.14813, first version 2021-10-26) treats noisy Anderson acceleration, mixing and smoothing but does not state an exact all-moment output threshold in the materially inspected equations and analysis. De Sterck–He (arXiv:2109.14176) develops deterministic linear Anderson convergence and standard mixing formulas. Shi et al. (arXiv:1909.03245) and Scieur et al. (arXiv:1606.04133) study regularization, without the identified correlated Gaussian moment threshold in the inspected material. Classical small-singular-value / Wishart integrability facts explain the core small-ball mechanism and are explicitly not claimed as novel. The specific application additionally requires the shared-noise independent-average representation, the affine-span noncancellation step, and a sharp all-memory classification. Targeted literature and published-record searches found no directly covering claim. Pollock–Rebholz (arXiv:2211.12953) was not fully accessible; comparison with its filtering work is limited to accessible descriptive text. No absence-of-prior-work claim is certain without independent exhaustive review, especially in Gaussian regression literature.

## Mathematical value — PASS

The memory parameter is a natural user-controlled numerical design choice; the theorem identifies a sharp dimension-dependent loss of finite expected error that generic conditioning warnings do not quantify. The full-memory singular regime has infinite mean even with arbitrarily small nonzero oracle noise, and near-full memory has finite mean but infinite variance. The theorem distinguishes two common remedies: fixed output damping is ineffective at removing the tail while ridge regularization restores all moments. The result is one-shot and does not purport to prove stochastic Anderson iteration convergence. These boundaries are useful for interpreting moment-based solver diagnostics and designing safeguards.

## Closest sources and risks

The closest algorithmic source is *Stable Anderson Acceleration for Deep Learning* (arXiv:2110.14813), particularly its residual least-squares and noisy-oracle sections. *Regularized Anderson Acceleration for Off-Policy Deep Reinforcement Learning* (arXiv:1909.03245) is the closest regularization comparison. *Filtering for Anderson Acceleration* (arXiv:2211.12953) remains a full-text accessibility limitation. Classical random matrix inverse moments could imply parts of the numerical theorem once the correlation structure and exact output decomposition are supplied; specialized prior formulations remain a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
