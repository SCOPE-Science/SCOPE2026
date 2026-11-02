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

# Verification

Run the following from the directory containing this file and `verify_radau_bipartite.py`:

```sh
python3 verify_radau_bipartite.py
```

Expected successful output: `VERIFY_OK 30768 exact-rational assertions`. No additional dependencies are required beyond Python 3. The checker implements the original rational Runge–Kutta formula by explicit exact matrix inversion for finite complete bipartite graphs, compares all matrix entries to the five projector-derived formulas, and tests polynomial/diagonal identities, the negative-diagonal witnesses, and rational root-isolation brackets for both distinct phase patterns.

All-pair assertions follow from the analytic proof in `RESULT.md`: orthogonal spectral projectors, positive off-diagonal factorizations, the global minimum of the scalar stability function, a negative-quadratic-discriminant witness and Descartes' two-root bound. These computations verify examples and symbolic identities only and are not an independent mathematical certification of the infinite theorem. No intermediate-stage positivity or universal graph-level assertion is tested.
