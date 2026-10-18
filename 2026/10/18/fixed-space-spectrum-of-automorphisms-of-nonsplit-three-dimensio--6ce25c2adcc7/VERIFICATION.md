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

# Reproduction

Run `python verify.py` with a Python 3 standard-library interpreter. It constructs quadratic-irreducible companion operators and directly enumerates all automorphisms by checking the defining bracket equation and invertibility. Fixed-space dimensions are obtained from Gaussian elimination rather than the formulas being checked. Field orders tested are \(2,3,4,5,7,11\), including a nonprime field and both available trace types. All ten computed four-bin histograms equal the theorem; the checker prints `VERIFY_OK` on success.

The test scope is finite. The exact result for all prime-power fields is established by the proof in `RESULT.md`, including completeness of the automorphism description and the norm-one classification. No independent audit or external certification has been performed.
