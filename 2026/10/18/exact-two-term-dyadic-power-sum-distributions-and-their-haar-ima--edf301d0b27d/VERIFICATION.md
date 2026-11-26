---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python3 verify.py` using a standard Python 3 interpreter. It independently enumerates residues of each \(d\)-th power modulo \(2^n\), convolves their frequency histogram, and compares each target with the closed recursion for 44 complete residue distributions. Expected line: `VERIFIED 44 complete residue distributions`.

The exact proof for all stated parameters uses the classical finite unit-group decomposition, explicit parity counts, and the lift factor in the even/even reduction modulo \(2^{n-d}\). The verifier checks only a bounded range; its additional printed support-measure values do not test the multiplicity law.
