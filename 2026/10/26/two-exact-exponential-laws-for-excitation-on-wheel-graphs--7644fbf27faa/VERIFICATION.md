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

# Reproducibility and limits

Run `python3 verify_gh_wheel.py` using Python 3 and no external libraries. The checker constructs the exact nine-state periodic-point transfer matrix \(M\), the three-state extinction-basin matrix \(B\), and their characteristic polynomials with exact rational arithmetic. It separately builds the full \(3^{n+1}\)-state deterministic transition graph for every \(n=3,\ldots,10\), decomposes cycles and basins, and compares each result with the closed forms. The `CHECKS.txt` file records the actual execution output. The infinite-family proof depends on the cited finite-graph synchronization theorem and combinatorial transfer matrices, not on finite case checking.

The finite tests verify examples, not arbitrary \(n\). No independent audit or third-party verification has been conducted.
