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

# Verification scope

The character transform uses normalized Haar measure and the standard spin-indexed \(SO(3)\) characters. The quadratic coefficient proof is analytic and exact. All higher exponents follow from a positive beta mixture; all lower positive exponents are excluded by an endpoint cosine-transform asymptotic with a strictly nonvanishing prefactor. Rational and irrational support radii are handled separately, including the endpoint \(R=\pi\).

The companion `checker.py` independently checks character quadrature against the incomplete-gamma expression, the exact quadratic formula, sampled positive differences, and subcritical negative indices, with 374 finite checks passing in the recorded run. Finite diagnostic tests cannot prove the all-index statements; those are justified in `RESULT.md`.

Prior comparisons cover known sufficient thresholds for projective spaces and spherical Pólya criteria. In particular, the sufficient exponent range is acknowledged as prior work, not as an independently new result. The completeness of the originality search and independent mathematical validation remain unverified.
