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

Run `python3 verify.py` with Python 3; only the standard library is needed. In a completed run, the script printed:

```
VERIFY_OK Fourier_eigenmodes=621 phase_witness_n8=(1189, 0.0003302767617501288) phase_witness_n16=(5304, 0.09556053091147157) power_two_cyclotomic_supports=8
```

The calculations test the wheel's Fourier/exceptional eigenvectors for all even rim orders from \(4\) to \(48\), account for the parity obstruction families, and check the monomial-support separation underlying cyclotomic rational independence at \(2^r\) for \(3\leq r\leq10\). The reported positive integers \(1189\) and \(5304\) are numerical examples at times \(2\pi j\), with the numbers after them being spectral-formula state-vector distances to the exact antipodal targets.

All floating-point checks use explicit tolerances, and the polynomial support check concerns finitely many orders only. Neither the returned log nor the finite searches imply approximation at every accuracy or all orders. The proof in `RESULT.md` establishes those statements via rational independence and Kronecker's theorem, and separately proves all nonexistence cases. The sole real quadratic subfield fact is an elementary Galois-theoretic property of cyclotomic fields; it is not supplied by numeric checks.
