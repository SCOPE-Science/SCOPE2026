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

# Verification instructions and boundaries

Run from the directory containing the embedded files:

```sh
python3 enum_orbits.py
python3 independent_enum.py
```

Both scripts require Python 3 and a compatible SymPy package; they were run with SymPy 1.14. No network access, external classification table, or hidden dataset is required. They use different monomial orders and methods for generating the projective group action. The first tests all 279 projective quartic orbits and the second tests every rationally admissible candidate orbit.

Actual runs of the included files gave `smooth_orbits 78`, `smooth_eq 10920`, `tangent_filling_orbits 20`, `tangent_filling_eq 2656`, `candidate rational smooth 2782`, and `singular candidate 126` (the two programs have slightly different output labels). The distribution over \((N,r)\), counts of rational curve points and distinct tangent lines, was \((3,3):364\), \((4,3):84\), \((4,4):1176\), \((5,4):252\), \((5,5):588\), \((6,6):168\), and \((7,7):24\). The direct derivative calculation for the three-point example is included in `RESULT.md`.

`verification_a.txt` and `verification_b.txt` preserve reference output. The programs themselves, not these logs alone, implement the exact finite tests. The unit-ideal calculation of the dehomogenized quartic and its partial derivatives on three affine charts establishes geometric smoothness over the algebraic closure. Exhaustive enumeration covers exactly the \(2^{15}-1\) nonzero coefficient vectors. This verification does not test a theorem for other finite fields and does not constitute an independent external mathematical audit.
