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

# Verification details

Run `python3 rectangular_schur_verify.py` in the directory containing the packaged source. The standalone code uses only the Python 3 standard library and directly enumerates all set partitions on \(2m\) cells for \(\(m=1,2,3,4\)\), tests products of every pair of block sums in the rational semigroup ring using integer coefficients, verifies the two-form classification and compares the explicit generator orbits with the proposed blocks.

Observed separated/balanced counts respectively: \((1,1),(2,3),(5,8),(15,33)\). All sums match the claimed \(2,5,13,48\). The formula gives \(184\) at \(m=5\), but that case is not exhaustively checked. Execution produced `VERIFY_OK`. This finite experiment does not certify the unrestricted theorem or originality; the infinite quantifiers are supported by the mathematical proof.
