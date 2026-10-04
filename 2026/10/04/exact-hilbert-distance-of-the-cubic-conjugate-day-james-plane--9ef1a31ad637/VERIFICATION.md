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

The analytic proof in `RESULT.md` is the verification basis. It reduces arbitrary Euclidean pullbacks to swap-invariant quadratic forms, proves a lower bound for every parameter \(\rho>0\) from exact test directions, and proves matching global extrema for \(\rho=3/2\) by derivative signs on both branches.

`verify.py` is a supplementary numerical replay. It recomputes \(2^{5/3}/3\), the endpoint and critical-point ratios, and samples both one-variable branches densely. A successful run prints `VERIFY_OK`. The grid is not used to establish the infinite-domain claim.

The proof does not claim uniqueness of every optimal linear map. It proves that the displayed swap-invariant pullback is optimal and that no quadratic pullback can have smaller distortion.
