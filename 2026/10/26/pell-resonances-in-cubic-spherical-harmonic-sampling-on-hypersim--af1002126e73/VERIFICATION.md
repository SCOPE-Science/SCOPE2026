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

`checker.py` and `checker_output.txt` are supplied as standalone files. Run `python checker.py` with NumPy and SymPy. The exact symbolic rational-function check is independent of the numerical eigenvalue comparisons. The numerical comparisons cover nine moderate configurations; four larger Pell pairs are checked using exact integer identities and rational spectral levels.

# Scope of checks

The primary mathematical proof is the normalized degree-three Gegenbauer addition identity, the inclusion-matrix spectral formula, finite-difference algebra, and the classification of positive Pell solutions. The checker verifies identities and finite examples but does not serve as an independent proof of Johnson incidence diagonalization or establish publication priority. No external audit is represented.
