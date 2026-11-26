---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Reproducibility of the nonbinary two-monitor theorem

The accompanying `verify_two_monitor.py` can be run with Python, NumPy and SciPy. It builds explicit Hamming adjacency matrices, constructs spectral projectors from their distinct eigenvalues and compares the diagonal of the bright-space projection with the Krawtchouk formula. The original finite run reports 23 detector-distance cases and 394 site comparisons across nine graph families; that count includes binary benchmark cases. The separate unequal-rate propagation example in \(H(2,3)\) at \(t=900\) reports survival \(0.4444444444443397\), compared with the theoretical infinite-time survival \(4/9\).

These are finite numerical checks; they do not establish the exact rank for arbitrary size or asymptotic decay for all permitted rates. The proof in `RESULT.md` establishes the two-projected-vector rank on each eigenspace by the strict nonbinary Krawtchouk inequality and gives the exact infinite-time projection law.
