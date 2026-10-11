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

# Verification and scope
The proof checks the uniqueness of the norming functional in \(\ell_p^3\), reduction of the complex absolute value to the positive-magnitude quotient, strict improvement from every boundary face, all three interior stationary equations, uniqueness of their positive root, and phase equality. No continuum maximum is inferred from finite sampling.

The attached standalone `CHECK.py` uses Python's standard library and fixed-seed direct sampling. It was executed on the packaged source and completed 60,000 independent direct quotient samples, three \(p=2\) formulas, and 15 Hölder-duality comparisons without assertion failure. Those samples are diagnostic and cannot certify an infinite parameter range; the elementary compactness and calculus argument supplies the proof for every \(p>1\) and positive pair of weights.

The example \(p=4\), unit weights, was also evaluated with high-precision scalar bisection to 30 decimal places. A root of equation (1) is the defining exact answer, not an interval derived from numerical optimization. Neither infinite-dimensional shifts nor endpoint exponents are certified by these checks. Relevant primary texts were inspected for the rank-one Banach and Hilbert weighted-shift comparisons; bibliographic coverage remains non-exhaustive.
