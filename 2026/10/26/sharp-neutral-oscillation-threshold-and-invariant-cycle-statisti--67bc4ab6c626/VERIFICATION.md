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

Run `python checker.py` with SymPy, NumPy, and SciPy. The code expands the specialized replicator/environment vector field, verifies by exact symbolic simplification that the conserved quantity has zero derivative at \(r=2\), and checks that the Dulac divergence is the stated signed rational function for every positive symbolic parameter. Three exact total-derivative identities for the time averages and mixed moment are also checked symbolically.

For corroboration, the code numerically integrates three distinct positive-parameter cases on one periodic level and uses event-detected return times and Gaussian quadrature to estimate both coordinate averages, the mixed moment, and energy drift. The printed values are computed, not hard-coded target traces. Numerical integration neither proves existence of cycles for every parameter nor excludes cycles in an infinite continuum; those assertions rely on the level-set and Bendixson–Dulac proofs in `RESULT.md`.

The public artifact contains only a deterministic checker and a fully explicit analytical argument. No independent audit or formal proof certification is asserted.
