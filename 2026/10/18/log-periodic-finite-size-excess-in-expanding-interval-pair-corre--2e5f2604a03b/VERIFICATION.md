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

The finite-parameter checker `verify_pair_correlation.py` was executed using standard Python. It checked equality of the affine branch-intersection integral, clipped-branch sum, and fractional-part probability for 156 exact-rational cases. It checked the phase endpoint values and a nontrivial interior value for three expanding bases. Exact finite-sample normalized means at \(N=50,100,200,400\) and \(b=2,s=3\) showed respective errors of approximately \(0.358190110568\), \(0.240117333116\), \(0.155383191665\), and \(0.097794918018\) from the stated phase-corrected formula.

The infinite assertion rests instead on affine partition integration, stationarity, a uniform geometric-tail estimate, and a direct derivative calculation for the phase. Finite samples cannot establish the asymptotic remainder or originality. Independent audit has not been performed.
