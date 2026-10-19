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

Run `python verify.py` with any recent Python 3 interpreter and no third-party dependencies. The program exhaustively enumerates all bridges with at most eight positive steps and eight negative steps (sixteen steps total), independently builds excursion-count distributions by a Catalan dynamic program, checks algebraic and rational identities through size 120, verifies strictness and boundary conditions, and compares large finite sizes with the asymptotic limit. The executed program reported **25,711 passing checks**.

The exact analytic proof appears in `RESULT.md`. Enumeration only checks finite ranges. The square-root limit additionally requires uniform Catalan tail control and Stirling asymptotics, supplied in that proof. The result is not a complete conditional distribution theorem and does not address nonnearest-neighbor paths or different occupation conventions. Potential implicit historical coverage by broad generating-function identities is unresolved. Self-review passed; no independent audit or independent scientific validation has been performed.
