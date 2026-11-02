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

`python verify.py` (SymPy) was executed against the standalone source in the package. Its checks reconstruct all six configurations and transitions directly, derive every matrix-tree cofactor and the signed-hop observable, and verify two exact multivariate polynomial identities by zero remainder. There are also 32 independent exact-rational stationary solves, an exact exceptional landscape check, and the elimination identity entering the reflection criterion. The proof of the reflection iff uses the positive-rate arithmetic-geometric-mean inequality and is not inferred from a finite parameter grid. The proof and checker make no inference about larger rings, random samples or independent validation.
