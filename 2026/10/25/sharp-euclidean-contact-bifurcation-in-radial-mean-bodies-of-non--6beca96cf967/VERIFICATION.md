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

# Verification of the rectangular radial mean-body contact theorem

Run `python3 verify.py` with Python 3.10 or later. It requires only the standard library and should print `RADIAL_RECTANGLE_CHECKS_OK`.

The program performs independent midpoint integration of the exact *exit-distance density* for a set of unit directions and exponents \(p=-0.8,-0.2,0,0.4,1,2,2.1,3,4,8,20\), using a power substitution to regularize the negative-moment origin. For all sampled eccentricities it compares these independently integrated radial values against the closed profile. Dense angle sweeps check the proposed inradius and circumradius across the short and long branches, including eccentricities on either side of computed thresholds. It also checks the \(p=4\) radical identity at 60-digit decimal precision.

The exact analytic proof in RESULT.md is needed for the universal, uncountable parameter range, uniqueness of extrema, and the exact transition. No finite experiment establishes those statements, and no independent external audit has been performed.
