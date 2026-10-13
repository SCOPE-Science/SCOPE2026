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

Run `python verify_c6.py` with Python 3, SymPy, NumPy and SciPy. The included checker independently validates exact distance-polynomial normalization, the four radical identities giving \(1/6\), the exhaustive single-time obstruction, and numerical matrix exponentials for all 36 transition entries. It also checks periodicity numerically. Scientific exactness follows from the symbolic identities and the proof; finite numerical error tolerance does not establish an infinite-family or robustness claim. The minimum-support assertion is a logical consequence of the explicit exact two-time upper bound and the algebraic one-time exclusion.
