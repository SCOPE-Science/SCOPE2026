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

# Reproducibility and limits

Run `python3 verify.py` from a directory containing both `verify.py` and `certificate.json`. No network access or external packages are required. The program prints a single UTF-8 JSON line. Its exact bytes, including the terminating newline, should equal `certificate.json`.

The program enumerates finite stationary state pairs and triples at integer time lags for one two-patch and one three-patch example, and verifies 12 pairs of exact covariance/third-cumulant identities. It reconstructs rational relaxation factors and stationary occupancy probabilities using exact fractions, and checks the two-patch alias with distinct signed lag-one third cumulants \(5/384\) and \(-5/384\).

The finite examples validate definitions, orientation and normalization. For arbitrary positive real rates, the proof in `RESULT.md` establishes the claimed inverse uniquely by a positive definite covariance Hankel matrix and two invertible Vandermonde systems; finite examples cannot replace that proof. Numerical conditioning and independent scientific audit were not evaluated.
