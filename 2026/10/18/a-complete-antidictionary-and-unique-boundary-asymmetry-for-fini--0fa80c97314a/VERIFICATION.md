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

# Computational verification
Run `python3 verification.py` using Python 3.9 or later, with no external dependencies. The program independently rebuilds Fibonacci words, contiguous factor sets, minimal absent words, all indicated critical occurrence positions, the trapezoidal factor-count curve, central bispecial positions, and the derived counting identity for each \(k=5,\ldots,11\). Its observed final line is `FIBONACCI_FINITE_ANTIDICTIONARY_PASS cases 7`.

The finite checks reach source length \(233\) and do not prove the universally quantified theorem. The proof instead uses the stated published occurrence and Sturmian/central-word lemmas, along with the algebraic counting identity. No independent mathematical audit or external certification was performed.
