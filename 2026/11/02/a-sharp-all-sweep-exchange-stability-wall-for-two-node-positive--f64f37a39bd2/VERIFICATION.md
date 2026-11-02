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

# Reproducibility and boundaries

The included `verify.py` is a standalone Python 3 standard-library script. Run it with `python3 verify.py`; it prints a successful check count and exits with an error if any asserted identity or independent nonlinear finite-difference comparison fails. The tested script passes 9,766 checks: exact rational recurrence/formula comparisons, exact rational contraction/parity boundaries, positivity of directly computed nonlinear steps, and centered finite-difference derivatives for unequal and equal positive rates.

The universal mathematical claims are proved analytically in `RESULT.md`. The finite tests are not an infinite certificate. Only a local implicit collocation branch near positive equilibria is asserted; no global implicit-solver convergence or full nonlinear step stability is certified. The independent audit status is unperformed.
