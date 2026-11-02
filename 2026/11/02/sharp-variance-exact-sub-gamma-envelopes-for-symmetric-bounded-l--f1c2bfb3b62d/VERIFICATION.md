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

# Verification record

The bundled `check.py` was executed using Python 3 standard-library exact rational arithmetic. The actual `check_output.txt` reports 1,625 passing assertions. The test checks the hyperbolic coefficient formula and positivity at finite indices, finite rational instances of the two-level variance envelope, and rigorously bounds the sign of the scalar-optimum derivative at \(3.82237\) and \(3.82238\) using rational Taylor remainder enclosures.

The infinite-dimensional proof is in `RESULT.md`: the Lévy–Khintchine representation; optimal-scale equivalence; strict measure-profile comparison and constructible equality cases; all-index proof of power-series coefficient-ratio monotonicity; and asymptotic two-region bounds. Finite tests do not certify a universal inequality in isolation. The full text of the closely related directional-scales manuscript was unavailable, so historical priority is provisional. No independent mathematical audit or certification has occurred.
