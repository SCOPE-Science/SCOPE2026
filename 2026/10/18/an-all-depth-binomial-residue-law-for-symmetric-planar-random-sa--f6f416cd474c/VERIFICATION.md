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

Run `python verification.py` with standard Python 3. No dependencies are required. The script exhaustively enumerates all 2^n sign sequences for every sample size 2 through 14 and thresholds 1 through floor(n/2)+1, testing each result against the exact binomial residue formula. Separate finite checks recover the first-depth Wendel law and the two-depth closed form. The checks are finite evidence only; all-n correctness follows from the conditional-sign reduction and two-barrier reflection proof in RESULT.md. No randomized samples, publisher data, external certificates, or independent validation are used.
