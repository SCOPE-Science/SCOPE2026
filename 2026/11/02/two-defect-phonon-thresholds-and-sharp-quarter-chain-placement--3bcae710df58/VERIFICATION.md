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

# Reproducible checks and limits

Run `python3 CHECK.py` using the Python 3 standard library only. The checker builds the free-end finite-chain Laplacian independently from its diagonal and off-diagonal entries, inverts the proposed Green kernel symbolically at rational entries, computes the signs of the exact tridiagonal \(LDL^{\mathsf T}\) pivots for the full mass-perturbed problem, and compares those inertia counts against the explicit two-by-two determinant criterion. It separately checks the Rayleigh formula and exact equality witnesses at chain lengths congruent to two modulo four.

Recorded execution output:

```
PASS: exact Green inverse entries: 2104
PASS: exact geometric Rayleigh checks: 6544
PASS: rank-two vs full-system inertia: 39264
Skipped singular-pivot/equality diagnostics: 0
PASS: sharp quarter-site witnesses: 25
```

These are finite exact arithmetic diagnostics across specified test lengths and contrasts. The analytical rank-two inertia proof and Rayleigh inequality in `RESULT.md` prove the unrestricted assertions; the program alone would not. The code does not independently test every band-edge equality, whose zero/positive inertia convention is established algebraically. No external audit or certification is asserted. No variable-spring, damping, nonlinear or infinite-chain conclusion is verified.
