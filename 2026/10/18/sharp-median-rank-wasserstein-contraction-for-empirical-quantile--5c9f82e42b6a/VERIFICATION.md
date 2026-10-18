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
# Verification

Reproduce the exact finite computations with `python3 verify_empirical_qc.py` from the embedded package directory. Successful run: `PASS: 282876 exact rational slope/endpoint tests; 272 attained contraction factors; 289 non-uniqueness examples.` The script enumerates all data multisets over the stated finite alphabet and checks every interval cut at pair midpoints and sample positions; it does not enumerate arbitrary real datasets.

The infinite-domain claims are proved in RESULT.md by piecewise-affine slope bounds and completeness of the finite-second-moment Wasserstein space. The uniform-measure stationary law follows from an exact two-branch affine identity, and the total-variation failure follows from atomicity at every finite time. No numerical fitting or finite-horizon extrapolation is required for those conclusions. The uniqueness conclusion refers to measures with finite second moments; no total-variation mixing or optimizer consistency is claimed.
