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

The included `verify.py` was executed against its own packaged source content, using SymPy rational polynomial expansions. Observed output:

`CHECK_OK: quartic covariance, Laplacian, finite-n zero-mass coefficients, fixed-point decorrelation`

It verifies the exact quartic coefficient of the limiting diagonal covariance, the Laplacian \(\Delta\log K=16|w|^2/45+O(|w|^4)\), the finite-degree Gaussian moments in the local even Taylor expansion, and alternating covariance estimates for finite parameter choices. The theorem's compact-open Gaussian convergence, independence, absence of unit-circle roots and zero-process convergence are justified by the written analytic proof, **not** by finite code tests. The script requires Python 3 and SymPy; run it using `python verify.py`.

The comparison is restricted to the explicitly named research literature. General Gaussian zero calculus is known, and possible older implicit-equivalence coverage has not been excluded. Independent mathematical audit: not performed.
