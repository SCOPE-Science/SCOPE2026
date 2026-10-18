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

# Reproducibility of the Taft Hopf-square spectral formula

Run `python verify.py` using Python 3 with NumPy installed. The successful execution prints exactly:

```
VERIFY_OK: n=2,3,4,5,6,7,8,9,10,11,12; all degrees; direct coproduct through n=8
```

The test first independently implements Taft multiplication \(x^rg^b x^tg^u=\zeta^{bt}x^{r+t}g^{b+u}\) when \(r+t<n\), and zero otherwise. It then expands \(\Delta(x^rg^b)\) by repeated multiplication of the two noncommuting summands of \(\Delta(x)\) in the tensor-product algebra, independently of the quantum-binomial formula. For every \(2\leq n\leq8\), all coefficients of the complete map are matched against the claimed block formula. For every \(2\leq n\leq12\), all homogeneous blocks are checked against the exact Fourier–Hankel factorization and the proposed singular spectrum computed by numerical SVD. The first-layer odd/even predictions are separately tested; in even cases its Gram matrix is checked against exactly twice the identity to floating-point tolerance.

Arithmetic involving roots of unity is numerical in this program. Its comparisons use tolerances specified in the source. The finite computations are reproducibility evidence and are not a substitute for the algebraic proof for every \(n\ge2\). No independent audit has been conducted.
