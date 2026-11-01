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

# Verification of the sharp radial Fock lower-edge gap

The analytic argument establishes the exact two heat filters, Fredholm spectral lower edge, Berezin lower edge, and sharp universal discrepancy in all finite complex dimensions. It proves the \(L^1\) upper bound by evaluating the two Gaussian kernels and their crossing radius, constructs smooth periodic near-extremizers, and uses Bohr compactness and duality equality conditions for strict nonattainment. These are infinite-dimensional analytic arguments rather than inferences from the finite checker.

Run `python check.py` with NumPy and SciPy. The script recomputes the normalized Gaussian crossing, compares the error-function constant with independent quadrature, checks increasing-period negative-bump heat masses and the rigorous mass bounds on a spatial mesh, tests dimensional gamma-to-heat and coherent Gaussian-to-heat limits numerically, and checks a two-frequency profile. The extracted checker ran successfully with the diagnostic result `CHECK_OK 399 deterministic validations`. The numerical validations are finite diagnostics only, not certificates of asymptotic convergence, global extrema, mathematical priority, or independent validation.

The normalization is \(\|p\|_\infty\le1\), and the computed gap is an additive difference between two lower edges, not a spectral distance or multiplicative ratio. No claim is made for arbitrary bounded measurable radial symbols or non-Gaussian Fock weights. Independent mathematical audit and publication-priority certification are not performed.
