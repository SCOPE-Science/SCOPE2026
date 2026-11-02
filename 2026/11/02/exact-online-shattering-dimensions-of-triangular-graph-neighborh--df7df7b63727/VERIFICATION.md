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

`verify.py` uses independently computed pair intersection to check every branch of both complete adaptive trees in `lower_certificates.json`: 8 leaves at depth three for \(J(5,2)\), and 16 leaves at depth four for \(J(7,2)\). It also evaluates the exact recursive online dimension of each finite concept system \(J(n,2)\) for \(2\le n\le9\), producing the results recorded in `verification_output.txt`.

The unbounded result requires the algebraic classification of positive fibers and its low-branch obstruction in `RESULT.md`; finite recurrence checks alone are not infinite proofs. Only the rank-two Johnson neighborhood family is treated. Literature searches do not prove historical uniqueness. No independent scientific audit has been performed.
