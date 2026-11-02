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
# Verification and reproducibility

Run `python3 verify.py` with Python 3.8 or later. The script checks all unordered pairs of unequal-weight binary messages at each length \(k=2,\dots,11\), using independently calculated cyclic pair distances. The complete count is 2,318,009. It also checks all suffix bit assignments at redundancies at most two in the last-message-bit lower-bound configuration for lengths \(k=1,\dots,39\), and checks the constant-block witness for the one-bit exception. The success marker is `PAIR_WEIGHT_FCC_VERIFY_OK`. Mathematical validity for unlimited message lengths follows from the run-count proof, not these finite tests. Formal machine verification of that proof and independent mathematical auditing were not performed.
