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
# Reproducibility and limits

The self-contained numerical checker is `artifacts/verify.py`. Run `python artifacts/verify.py` with Python 3, NumPy, and SciPy. It reconstructs each stated finite SSH hopping and positive onsite-loss matrix rather than reading saved eigensystems. It checks the clean spectrum, all dark eigenvectors, the dimension formula \(2g-1\), each localized B-site projector plateau, and absence of extra imaginary-axis eigenvalues of the loss generator for 2,343 combinations with chain half-length \(1\le M\le11\), nonempty loss subsets of cardinality at most three, and several hopping ratios. It also checks selected long-time matrix exponentials. Verified output:

`VERIFY_OK 2343 clean-spectrum, dark-space, survival, and non-Hermitian checks`

Finite floating-point checks do not prove an infinite family. The all-size proof rests on the analytic Jacobi eigenvectors, Bézout divisibility, finite-dimensional dissipative spectral decomposition, and the roots-of-unity sum in `RESULT.md`. Only the one-particle no-jump survival probability is asserted; no independent audit or experimental verification has been carried out.
