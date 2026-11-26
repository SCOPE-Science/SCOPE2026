---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Equation (11) of the source scheme gives the multiplier 1+z/(1−zT), hence the stated R_s for z=−s. Independently, put x=1+sT, B=1+s and m=1+s/2. For f(x)=(1−s/x)^2, the endpoint chord error is s(x−1)(x−B)(s/x+s+s/B−2)/(xB). The last bracket decreases in x and at x=1 has sign 2s²+s−2, proving strict support in the interior up to c. The error from the tangent at y is s(x−y)²[s(2x+y)−2xy]/(x²y³). The tangent through B has y=2sB/(s+2), and y−1 and y−m change sign precisely at c and d. Its affine error bracket is positive below B and vanishes at B. For s>=d the tangent at m has nonnegative bracket throughout the interval, checked at x=1 and B; at s=d the additional contact B cannot carry mass at mean m. Equality in the integrated supports forces exactly the proposed contact laws and their unique masses, including at both thresholds. Exact symbolic evaluation in x gives the three stated optimal values. IID products give the stated squared iterate expectation, including s=2 and deterministic zero initial data.

## originality

PASS

The multiplier and general affine-support method are known, as is the uniform-stage analysis. What is distinct in the inspected literature is the global fixed-stiffness optimizer over all mean-half laws, its exact two transitions, unique support and masses, and sharp optimized value. The closest indexed records optimize different quantities or restrict the admissible laws.

## value

PASS

The full law optimization under one prescribed moment is a natural design question for the existing randomized stage. The exact asymmetric two-point regime shows a strict advantage over midpoint damping at s=1 (7/64 versus 1/9), while the upper threshold certifies when any nontrivial randomization strictly loses. The sharp classification and unique equality cases are useful even within the scalar model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
