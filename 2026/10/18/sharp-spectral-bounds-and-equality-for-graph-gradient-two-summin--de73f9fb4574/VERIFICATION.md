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

# Computational verification
The included standalone `verify.py` numerically constructs incidence matrices, the Laplacian pseudoinverse half-power, explicit norming frames, and the two sharp bounds. It checks cycles, complete graphs, complete-bipartite graphs, hypercubes, and a 28-vertex Chang graph (constructed by a specified Seidel switch). The boundary case is a four-vertex path with unequal edge half-resistances, for which the spectral trace baseline is strictly smaller than the explicit test-family lower bound.

Execute `python3 verify.py` with NumPy available. A passing run reports the number of checked parameter instances. These are finite floating-point corroborations only; the general validity is established analytically in RESULT.md. Independent validation has not been performed.
