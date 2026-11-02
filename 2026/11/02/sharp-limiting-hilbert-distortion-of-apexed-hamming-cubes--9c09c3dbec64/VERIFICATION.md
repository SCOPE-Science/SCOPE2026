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
# Reproducibility checks
Run `python3 VERIFY.py` from the directory containing this report. The script uses only Python's standard library and exact fractions. The observed output was:

```
CHECK_OK exact_rational_assertions= 4030 dimensions_tensor=2..40 dimensions_fourier=2..40
```

It checks all Hamming shells in dimensions \(2\) through \(40\), analytic Krawtchouk degree-one/two identities in these dimensions, and exact Walsh two-shell energy identities for 299 rational test profiles. The full proof applies to every integer \(d\ge2\) and to every real Hilbert embedding, including non-symmetric embeddings, by the quantified Hilbert-valued Fourier argument in RESULT.md. These finite checks are a regression test, not an independent audit or an infinite certificate. The exact linear-program characterization is proved from positive-semidefinite Gram averaging and is not solved by the checker.

The upper embedding uses Euclidean tensor products and hence is not claimed dimension-optimal. The bound \(\sqrt{8(d-1)/(3d)}\) is not asserted to equal the exact finite-\(d\) distortion. No independent mathematical audit has been performed.
