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

# Reproducibility
Execute `python3 verification/verify.py` with Python 3 and no external packages. The run output stored in `verification/output.txt` checks all possible local triples and exact zero-cost transitions, all \(3^{2n}\) vertex labelings on \(L_n\) for each \(2\le n\le6\), and transfer-versus-composition counts for \(2\le n\le27\). For the infinite statement, the source verifies the finite certificate used in the symbolic proof in RESULT.md; a finite enumeration of graph orders alone would not justify the universal claim. No independent human or external formal audit was performed.
