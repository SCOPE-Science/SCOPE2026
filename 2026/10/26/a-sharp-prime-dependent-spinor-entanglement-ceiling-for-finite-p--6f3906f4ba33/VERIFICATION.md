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

# Reproducibility and verification

Run `python3 verify.py` with Python 3's standard library. The script builds the finite hopping matrices, derives numerical momentum spectra using direct finite Fourier transforms, evolves normalized spinor–position states with a convergent matrix-exponential Taylor series, and computes the binary entropy of the reduced spinor. The obtained output was:

```
VERIFICATION_OK 178 finite checks; arbitrary-depth proof is analytic
```

Checks cover \(p\in\{2,3,5,7\}\) and depths up to four, strictly positive off-diagonal hoppings, Fourier eigenvalue multiplicities, exact saturation for the connected example, the arbitrary-mass ceiling at sampled times, and the massless closed formula on independently chosen radial matrices. The package is standalone; it uses no external downloaded data.

The proof of the full theorem is analytic: radial shell character sums establish high-conductor degeneracy of multiplicity \((p-1)p^{\ell-1}\); the resulting rank-one summand enforces the two-level entropy bound. Equality follows from the exact three-valued symbol for the positive connected kernel. No finite numerical trial is represented as a proof for arbitrary depth or time. The independent audit was not performed.
