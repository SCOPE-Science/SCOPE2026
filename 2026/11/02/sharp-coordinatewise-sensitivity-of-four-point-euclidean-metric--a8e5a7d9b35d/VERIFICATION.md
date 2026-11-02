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

# Reproducibility

Run `python3 verify_metric_cone.py` with Python 3 and no third-party packages. The script uses exact integer and `fractions.Fraction` operations to enumerate every one of the \(2^{12}=4096\) subsets of oriented triangle inequalities for four points and all eight subsets for three points. It verifies the rank-by-rank norm envelope \((1,4/3,3/2,8/5,3/2,10/7,0)\), the number of subsets at each rank, and strictly positive primal and dual certificates for explicit equality witnesses. This is an exhaustive finite certificate for the asserted finite cases, not approximate quadrature or sampling.

The analytic proof separately supplies the polyhedral-cell reduction to these finite projectors, the integration along line segments needed for a global modulus, and the embedding into every greater number of points. The executable is not a machine-checked proof of those abstract steps, and no claim of independent audit is made.
