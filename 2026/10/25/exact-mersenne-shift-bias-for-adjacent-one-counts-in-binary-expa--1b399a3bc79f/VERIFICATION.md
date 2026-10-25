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

The included `VERIFY.py` checks exactly the conditional increment formulas, the 13 smallest Mersenne shifts using rational residue sums, the 20 bulk-weight cases and 16 boundary/geometric identities. An independent brute-force calculation of integer adjacent-one counts checks the first six shifts on finite intervals.

The proof of the infinite statement is in `RESULT.md` and is based on explicit residue conditioning, binary carry classification and finite geometric sums. The finite verifier does not certify all infinitely many shifts. Some earlier publication may imply the explicit uniform formula without stating it; independent publication-priority verification has not been performed.
