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
# Exact verification

Run `python3 check.py` in the directory containing the packaged checker. No external dependencies are required. It reproduces the rational numerator from the finite-difference formula, checks the rational generating identity beyond the numerator degree, verifies every coefficient sign, calculates all principal Hurwitz determinants by integer Bareiss elimination, and constructs an independent exact fraction-based Routh table for each integer dimension from \(2\) to \(11\). It also checks the primitive integral Cayley numerator in complex dimension \(11\).

The expected last line is `CHECK_OK: full n=2..11 exact Hurwitz and Routh certificates`.

The determinant and pivot signs certify the exact open-right-half-plane counts under the classical Routh theorem. The analytical step identifying the auxiliary disk with actual off-diagonal kernel fibers is in RESULT.md. The output does not claim to prove statements outside the finite complete range \(2\le n\le11\), independently certify priority, or numerically approximate every root.
