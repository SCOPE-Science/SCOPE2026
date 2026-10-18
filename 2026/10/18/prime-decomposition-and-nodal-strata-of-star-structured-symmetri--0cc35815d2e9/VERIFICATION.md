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

Run `python3 verify_arrowhead.py` with Python 3.8 or later. The exact-arithmetic checker enumerates normalized projective points for \(m=3\) over fields of orders \(3\) and \(5\), and \(m=4\) over order \(3\). It computes each determinant by modular elimination, independently calculates all gradient coordinates, classifies component membership, and checks corank by direct row reduction. It prints `VERIFY_OK` after every assertion passes.

The proof of the all-size statement is mathematical: determinant expansion, Schur complements, published radicality of the ideal of submaximal minors, and nondegenerate transverse quadratic forms. The code checks finite cases only.
