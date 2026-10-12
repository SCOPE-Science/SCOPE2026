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

# Verification of the joint collision–cover law

Execute `python3 verify.py` from the same directory as `RESULT.md`. Only standard-library Python 3.9 or newer is needed. The script enumerates 873,611 length-\(n\) prefixes for \(n=2,3,4,5,6,7\) and uses exact rational arithmetic to compare first-collision probabilities, conditional expected cover times, and the three joint moments that imply the covariance. There are 60 independent exact comparisons. The script separately evaluates the covariance sum at selected larger sizes and tests its approach to the proved Rayleigh constant. The completion marker is `VERIFY_OK`.

The proof of stochastic monotonicity is the common-geometric-waits coupling, while the proof of the infinite limit uses a Gaussian survival bound and Rayleigh moment convergence. Finite enumeration and numerical convergence provide corroboration only, not exhaustive proof over all \(n\). The boundary \(B_n=n+1\), for which \(T_n=n\), is explicitly included. Independent audit: not yet performed.
