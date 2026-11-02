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

The analytical argument is given in `RESULT.md`. Run `python verify.py`; it builds the finite killed continuous-time generator directly, solves resolvent and mean equations, and compares them with a separately coded characteristic-root expression. It also tests strict monotonicity in the wall-conversion rate and numerical convergence of the quadratic-time and first-order cap-difference limits. The replay outcome is reported here.

The local replay returned **PASS 3960 checks**. These are finite reproducibility tests: they neither prove limits over all lengths and rates nor establish originality, publication priority, or independent validation. The proof is the algebraic recurrence and its asymptotic analysis. Unavailable full text for the 1997 microtubule reference creates an originality limitation, not a correctness certificate.

No independent audit was performed.
