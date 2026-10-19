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

# Reproducibility

Run `python verify.py` in a directory containing the supplied standalone Python file, using installed `numpy`, `scipy`, and `sympy`. The script checks the Chebyshev determinant identity by independently forming full matrices for six dimensions, locates strong-nonreciprocity lobe thresholds and compares all eigenvalues on either side for 24 size/coupling configurations, checks the explicit four- and five-site prefactors, and numerically examines the first asymptotic correction for three sizes in the congruence class three.

Observed output:

```
Exact characteristic identities: six dimensions, N=3,...,8: PASS
Crossings from complex to real: 24 parameter configurations: PASS
Exact central-lobe prefactors and residue check: PASS
Residue-three strong-asymmetry correction: PASS
```

These computations do not certify all real parameters or the absence of related published theorems. The theorem itself is proved by exact trigonometric and spectral arguments in RESULT.md. No independent audit has been performed.
