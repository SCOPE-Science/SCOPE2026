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

## Reproducibility

Run `python3 verify.py` from the directory containing the standalone checker. It uses only the Python 3 standard library. The checker has been executed successfully with the output terminator:

`VERIFY_OK odd-order orbit determinants and two complete finite-field quandle-algebra censuses`

It compares exact integer determinants of Fourier-orbit exponent matrices to the closed arithmetic factors for eleven odd moduli. Separately, it enumerates all coefficient vectors of the two small quandle algebras over finite fields and directly squares each vector using basis multiplication. For \(R_2\) over \(\mathbb F_5\), the component-fiber counts are one fiber of size one and one of size five (six idempotents). For \(R_6\) over \(\mathbb F_7\), the observed fiber histogram is one of size one, four of size seven, and three of size 49 (176 idempotents).

These tests verify finite instances of the formula and do not replace the general proof. The infinite-family correctness argument relies on Fourier inversion, a nonsingular integer torus isogeny, a paired odd-frequency linear system, and the algebraic decomposition over a finite reduced base. The geometric claim is over \(\mathbb C\); the finite-field census is only a compatible check where the necessary Fourier roots split.
