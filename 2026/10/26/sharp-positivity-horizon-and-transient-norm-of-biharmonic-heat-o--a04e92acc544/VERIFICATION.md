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
# Computational verification and reproducibility

The provided `check.py` builds the triangular graph from unordered pairs, constructs the three spectral projectors using exact rational arithmetic, and tests projector identities, spectral decomposition, absolute row sums, signs, and the closed formulas. For small dimensions it compares independent numerical matrix exponentials with the projector formula. The completed run returned `CHECK_OK exact_and_numeric_assertions=65720` for dimensions 4–11 and several asymptotic-scale checks.

Execute `python check.py` with NumPy and SciPy available. The script is a reproducible finite verification, not an exhaustive or infinite proof. The proof in `RESULT.md` derives the universal claims and their asymptotics. No independent mathematical audit or separate external certification has been performed.
