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

# Verification and scope

The standalone `verify.py` reconstructs the complete continuous-time joint generator from first principles, solves its stationary linear system numerically for \(2\leq N\leq5\) at both extreme bath-switching rates, and compares every pair covariance with the rigorously proved endpoint limits. It also checks that the stationary means do not depend on the bath's positive switching rate. Separate exact algebra solves the two-site mixed-moment system and verifies the rational covariance and its unique positive zero. Finally, the static open-SSEP harmonic and adjacent-source identities are checked for chain lengths up to eighty.

Run in a directory containing `verify.py` with Python 3, NumPy, and SymPy using `python verify.py`. The expected terminal line is `ALL CHECKS PASSED`.

These calculations do not establish the infinite family on their own: the finite-state limiting-law argument, the moment equations, and the strict numerator inequalities supply the mathematical proof. For more than two sites, the number and locations of any additional covariance zeros remain undetermined.
