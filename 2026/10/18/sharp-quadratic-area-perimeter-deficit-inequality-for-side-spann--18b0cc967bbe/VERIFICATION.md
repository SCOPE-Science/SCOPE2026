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

The standard-library script `check.py` builds independent Euclidean convex hulls of explicitly marked boundary points on a triangle, a quadrilateral, and a pentagon. It compares geometric perimeter and area deficits with the corner formulas, evaluates both terms of the exact stability identity, and verifies the inequality on 1,800 randomized feasible configurations. For each outer polygon the script also constructs a strictly side-spanning equality case using the sharpness parameterization. Its completed output was:

`OK: 1800 random hulls; 3 attained equality configurations; exact stability identity verified.`

The numerical comparisons use finite floating-point tolerances; they cannot certify the universal theorem. The actual proof is the corner decomposition, the monotonic normalized chord ratio, positive-weight Cauchy–Schwarz, and the explicit feasible equality construction in `RESULT.md`. No external or independent audit was performed.
