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

# Verification and reproducibility

The analytic argument in RESULT.md is the complete proof: its pivotal steps are the two-side perimeter integral, derivative identity (3), strictly increasing angular function (4), strict exponent comparison (5), root uniqueness, gamma-integral estimate at exponent zero, and implicit derivative at exponent one. Each step specifies its domain. The limiting segment has multiplicity two and is integrable exactly for the stated exponent range.

Run the standalone `verify.py` under Python with `mpmath` (see `requirements.txt`):

```sh
python -m pip install -r requirements.txt
python verify.py
```

The source in this package was executed, with output:

```
RECTANGLE_POWER_PERIMETER_FINITE_CHECKS_OK 194
a=0.5 critical aspect 0.31015211479469559503
upper-endpoint slope 1.2464504802804610268
```

The script checks direct arclength integration against a separate positive-quadrant formula; signs and finite differences for the analytically derived derivative; sampled strict-minimum inequalities; numerical uniqueness/bisection; scaling; monotonicity with respect to both parameters; the closed exponent-one normalization; and asymptotic ratios near both singularity endpoints. All checks are finite and do not establish universal validity, historical originality, or independent certification.
