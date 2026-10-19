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

Run `python verify.py` using Python 3. The script implements arithmetic over prime fields and binary extension fields via irreducible polynomials, enumerates all order-two matrices, and enumerates all square-zero perturbations. Each determinant fiber is checked against the formula involving the number of rational invariant lines. Each number of diagonalizable perturbed matrices is separately checked against the characteristic-dependent formula.

Observed output:
```
PASS q=2 | A=16 | N=4
PASS q=3 | A=81 | N=9
PASS q=4 | A=256 | N=16
PASS q=5 | A=625 | N=25
PASS q=7 | A=2401 | N=49
PASS q=8 | A=4096 | N=64
```
The tested Cartesian products comprise 400,307 matrix/perturbation combinations. These finite tests do not establish the universal statement; the proof is in `RESULT.md`. Independent review has not been performed.
