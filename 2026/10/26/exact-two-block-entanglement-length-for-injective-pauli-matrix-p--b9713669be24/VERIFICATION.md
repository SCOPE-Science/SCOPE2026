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

# Verification record

The analytic proof reconstructs the density operator for any two nonempty finite contiguous blocks as a product of injective local tensor maps and a two-qubit output-first Choi operator with separable virtual spectators. Because each local map has an explicit left inverse, this is an equivalence for separability and positive partial transpose, not just a one-direction witness. The primitive transfer property is checked from the Pauli eigenvalues, and the necessary/sufficient channel criterion is the established Ruskai unital-qubit theorem.

Run `python verify.py` with Python 3 and NumPy. The computation reported `PASS 57 direct density/partial-transpose tests, including 2-site blocks`. It compares direct MPS contractions against inverse-filter-recovered Choi operators for six strictly positive probability vectors, eight separator lengths with one-site blocks, and nine additional two-site/one-site combinations. It checks trace-one positivity and consistency between the strict sign of \(\sum_j|\lambda_j|^L-1\) and physical partial-transpose eigenvalues. This script does **not** prove the infinite quantifiers, does **not** test all equality cases, and does **not** establish global priority.

The scope excludes parameter endpoints with a zero tensor weight, disconnected unions of several intervals, and finite-boundary corrections. The isotropic product-state limit does not entail a uniform spectral gap at the endpoint. No external independent audit or certification was performed.
