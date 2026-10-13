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

# Reproduction and limitations
Run `python check.py` with Python 3, SciPy and mpmath. The program checks finite quadratures (bump and cutoff), evaluates the proved positive-margin bound, tests column-balancing at selected coordinates, tests selected row masses and evaluates small-parameter Clayton deficits at high precision. It is not a sampling-based proof: the all-direction tail bound, all-positive-Clayton-parameter reversal, normalization for every coordinate, smoothness and finite mutual information are established in `RESULT.md` from explicit formulas. Results depend on the mathematical proof and have not undergone independent audit.
