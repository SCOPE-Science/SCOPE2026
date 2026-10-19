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

# Verification of the scalar-core risk formula

Run `python -m pip install -r requirements.txt` as needed and then `python verify.py` within the same directory. The reproducible checks use SymPy for seven exact symbolic identities, two constant inequalities, Python exact rational arithmetic for three direct-matrix identities, and deterministic angular quadrature for twelve ridge choices, four hard-core cutoffs, and five tail-probability checks. The script's expected output begins `PASS:`; the checks were executed successfully on the packaged source before delivery.

The analytical proof in `RESULT.md` establishes the continuum result. In particular, finite quadrature is **not** evidence that every positive parameter attains the claimed formula, that no further stationary point exists, or that moments diverge: those facts follow from the arcsine integral, factorized derivative, and near-zero density argument. The hard-cutoff integrand is discontinuous at the retained/rejected boundary, and the deterministic midpoint checks accordingly use a modest numerical tolerance; no precision certificate is claimed from them. The exact coefficient optimization is conditional on the stated spectral model. Published priority and implementation accuracy on general matrices remain outside these checks.
