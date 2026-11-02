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

# Reproducible verification

Run the included standard-library-only `verify.py` with `python3 verify.py`. It uses no input files, packages, network data, floating-point approximations, or precomputed determinants. It constructs the original shift-and-append graph on ordered distinct triples; computes independent integer Laplacian cofactors via exact Bareiss elimination for alphabet sizes \(5,6,7,8\); and compares these integers with the closed product formula. It additionally computes direct integer determinants of \(xI-A\) at seven values of \(x\), for each of \(n=5,6,7\), against the stated characteristic polynomial. The known shorthand count at size five and the explicit size-six prime-power expression are asserted independently.

The observed output was:

```
n=5 vertices=60 arborescence_digits=16 cycle_digits=16
n=6 vertices=120 arborescence_digits=55 cycle_digits=92
n=7 vertices=210 arborescence_digits=124 cycle_digits=288
n=8 vertices=336 arborescence_digits=233 cycle_digits=696
VERIFY_OK
```

The code checks only finitely many alphabet sizes and polynomial evaluation points; these calculations are **not** an infinite proof or a claim of independent external certification. The all-\(n\) assertion rests on the full symbolic operator, invariant-space determinant, matrix-tree, and BEST proof in `RESULT.md`. This verification assumes only ordinary exact integer arithmetic.
