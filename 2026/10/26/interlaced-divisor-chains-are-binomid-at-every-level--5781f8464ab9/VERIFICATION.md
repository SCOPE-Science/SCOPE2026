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

Run `python verify_binomid.py` with Python 3, using no third-party packages. It checks prime-exponent conditions on randomly generated interlaced monotone chains, the semigroup indicator subclass, and the explicit three-step failure. Finite tests support but cannot replace the symbolic proof. The proof's necessary boundary is the comparison of the unmatched final even-indexed term with the first term of the initial interval.

Scientific scope: all positive integer sequences satisfying the two divisibility conditions; no independent mathematical audit performed.
