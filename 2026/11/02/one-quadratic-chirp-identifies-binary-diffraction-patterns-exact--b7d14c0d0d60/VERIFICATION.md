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

The analytical proof uses the inverse discrete-Fourier autocorrelation identity, the irreducibility of the prime cyclotomic polynomial, and an algebraic-integer norm bound. Reproducing the standalone arithmetic checks requires Python 3 only:

```sh
python3 check_chirp.py
```

The program evaluates all binary inputs at prime lengths \(3,5,7,11\) for one or two invertible quadratic coefficients and confirms that only different singleton inputs have equal coded intensity signatures. Composite-length examples are checked through exact integer coefficient arrays for every correlation lag at the listed lengths \(4,6,8,9,10,15,21,25\). These calculations are finite consistency tests, not proofs for arbitrary lengths; the mathematical argument supplies the general result.

The separation estimate \(p^{-(p-2)}\) follows analytically from the nonzero cyclotomic norm and is not numerically optimized. No independent audit or validation has been performed.
