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

The analytic proof in `RESULT.md` establishes the formulas for all positive aspect ratios. The executable `check.py` uses high-precision truncated Gaussian series, which do not establish the universal quantifiers.

Executed with Python 3 and `mpmath` at 50 decimal digits. The actual output is embedded as `check_output.txt`.

The checker separately evaluates the exact derivative sums and direct Zak values. For six aspect ratios (0.3, 0.5, approximately 0.70710678, 1.0, 1.4, and 2.0), it verifies positivity, the reciprocal-duality identity, both symmetry zeros, and finite-difference quadratic ratios. For two small and two large aspect ratios it verifies the leading asymptotic curvature ratios. For aspect ratio 0.7 it computes two sublevel areas using 32 angular samples and 48 radial bisection steps, and checks convergence to the analytic ellipse coefficient as the level falls from 0.002 to 0.0004.

All executed tests passed. These finite computations are numerical probes, not an exhaustive proof or independent certification. Bounds on the truncation tails are not computed by the checker; analyticity, positivity, duality and asymptotics are established by the symbolic arguments in the proof.
