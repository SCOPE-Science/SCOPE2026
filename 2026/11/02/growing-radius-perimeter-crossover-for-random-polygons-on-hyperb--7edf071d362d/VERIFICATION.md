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

# Reproducible checks
Run `python3 verify.py` with Python 3. The program uses only the standard library and an independent seed. It evaluates the finite-dimensional beta integral, directly simulates intrinsic hyperbolic chord lengths from the hyperbolic cosine law, evaluates the critical fluctuation variance functional, and numerically checks endpoint and fixed-radius asymptotics. A successful run terminates with `ALL_CHECKS_PASSED`.

## Proof-level validation and limits
The mathematical argument is in `RESULT.md`: Dirichlet spacing normalization, the exact chord formula, endpoint inequalities, normalized-exponential coupling, triangular-array central limit expansion, and remainder bounds. A finite sample of random polygons cannot certify infinite asymptotics or uniqueness of the mathematical statement in the literature. No independent audit or formal-machine proof was performed. The executable checker is diagnostic evidence only, not an external certification.
