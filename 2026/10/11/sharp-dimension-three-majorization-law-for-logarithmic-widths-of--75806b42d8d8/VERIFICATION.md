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

Execute `python3 verify.py` in this directory with Python 3.8 or later; only the Python standard library is required. It independently integrates the half-normal maximum-density formula at three- and four-coordinate profiles, compares finite differences with the closed-form three-dimensional solid-angle gradient, checks majorization, and tests a strict analytic counterexample margin.

Critical infinite claims are proved in RESULT.md: (i) uniform-sphere/Gaussian radial independence fixes normalization; (ii) double integration establishes the rectangular-cone solid angle; (iii) monotonicity of the arctangent ratio and coordinate averaging yields strict Schur concavity; (iv) small-ball cubic behavior bounds the fourth-axis contribution; (v) dominated convergence transfers inequalities to boundary and full-dimensional perturbations.

These numerical checks are neither an exhaustive enumeration nor a proof. A successful script does not imply that the result is absent from all historical publications. Independent audit was not performed.
