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

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. The bundled script verifies the derivative factorization, logarithmic derivative, strict-convexity expression, algebraic resultant factorization, shifted quartic, critical root, representative crossing counts and the near-critical window-opening coefficient. A completed execution returned `PASS` and 85 diagnostic test groups.

The proof in RESULT.md is the infinite-domain argument; numerical sampling does not establish universal quantifiers and has not been presented as an independent check. The approximation is Wien, not full Planck; no observation, laboratory experiment, or independent audit is claimed.
