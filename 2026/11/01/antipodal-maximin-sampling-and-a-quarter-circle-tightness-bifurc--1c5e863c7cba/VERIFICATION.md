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

The proof uses exact integration and elementary matrix identities for all allowed arc widths and separations. Reproduction: run `python checker.py` with NumPy installed; one execution passed 17,656 numerical assertions. The numerical tests compare direct-integral Gram values, explicit eigenvalues, global optimization inequalities on a grid, exact frame-potential formulas and asymptotic behavior. Finite assertions do not prove global inequalities: those follow independently from the exact strict algebraic comparison and quadratic convexity in RESULT.md.

No independent audit or external certification has been performed.
