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

# Reproducible verification and analytic scope

Execute `python3 verify_apple_convexity.py` using the accompanying standalone Python file (Python 3 standard library only). It verifies 120 exact rational Taylor coefficients and their alternating tail signs, the strict positivity of the local radial majorant through \(17/50\), the exact rational root brackets, a high-precision bisection, and 5,000 deterministic Schwarz–Blaschke numerical tests. The main theorem requires the analytic Taylor-sign induction and Schwarz–Pick argument in `RESULT.md`. In particular, the finite sample does not prove an infinite assertion.

The exact claimed radius is the unique zero of \(H\) in \((1/3,17/50)\), not the printed decimal. The scope does not include classical convexity beyond this root, claims concerning unrelated target functions, or independent external validation.
