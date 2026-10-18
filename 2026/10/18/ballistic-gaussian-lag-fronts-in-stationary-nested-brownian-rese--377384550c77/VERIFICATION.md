---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Run the enclosed `check.py` using Python 3.9 or newer with no third-party dependencies. The checker is standalone and does not require external files or downloads.

Observed output: `PASS: 1546 deterministic assertions; no external packages` followed by representative peak positions. Tests verify exact Fraction-valued sums for the two directed integrated covariances, finite-difference checks of the triangular generator relation, strictly increasing/decreasing behavior on either side of the unique peak, known exact small-index root values, and representative large-distance Gaussian-front values. Direct inspection of the full algebraic proof covers all positive \(D,r\), all finite \(N\), and the growing-chain limit; finite numerical checks do not establish the stated uniform convergence or uniqueness for arbitrary index by themselves.

The earlier equal-time static covariance and first public source date were checked in the original 2025 primary work. The original 2025 main text, including its explicit discussion of static rather than dynamic correlators, was read. A related 2026 follow-up on one-time approach to steady state was compared from its accessible abstract and synopsis, but complete full-text inspection was unavailable. Thus independent audit and comprehensive novelty certification remain unperformed.
