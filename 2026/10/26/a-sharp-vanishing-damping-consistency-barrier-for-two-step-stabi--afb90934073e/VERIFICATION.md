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

# Reproducibility and scope of verification

Run `python3 verify.py` with a standard Python 3 interpreter. The script tests exact rational identities (including the quadratic order equation and both forcing moment conditions); numerically reconstructs the two internal stages from the published formulas instead of presuming the collapsed update; checks the defect identity at several abscissae and step sizes; evaluates the closed-form finite-horizon error against direct recurrence; and tests numerical instances of all three asymptotic regimes.

The proof in `RESULT.md` establishes the infinite limiting assertions. Finite numerical checks do not prove convergence of every sequence, do not establish uniqueness against unpublished prior work, and do not validate any other damped solver or an implementation in finite precision.
