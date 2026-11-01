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

Analytic evidence: two exact sums-of-squared-Hilbert-norm identities establish three independent lower bounds on squared distortion. Explicit regular-simplex realizations attain the maximum bound in each regime. Saturation in the identities forces every optimum to have the claimed Gram geometry, with an affine-rank jump at the lower phase transition.

Reproducibility: run `python3 verify_matching_stretch_distortion.py`. Its exact rational tests cover 161 parameter instances across all phase boundaries and both graph endpoints, as well as 120 independent arbitrary rational-vector verifications of the exact Hilbert identities. These finite tests corroborate; they do not replace the proof for every real parameter and arbitrary integer size.

Independent audit: not performed.
