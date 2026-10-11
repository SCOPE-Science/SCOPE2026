---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The codimension-one and codimension-two Jacobian formulas show that an invertible linear map multiplies every facet mass and every ridge conductance by the common factor \(|\det A|\), so the generalized Rayleigh quotient is affine invariant. Every origin-symmetric parallelotope therefore reduces to a box. On a box, each signed facet has mass \(M=2^{n-1}V\), each ridge joining distinct coordinate directions has conductance \(C=2^{n-2}V\), and an even function is determined by \(n\) values \(x_i\). Thus the numerator is \(4C\sum_{i<j}(x_i-x_j)^2\), the variance is \(2M\sum_i(x_i-\bar x)^2\), and \(4C=2M\). The complete-graph identity supplies the factor \(n\). Fresh exact replay confirmed the algebra in dimensions 2 through 8.

## originality

PASS

The initiating paper defines the weighted facet graph and its primary abstract states a lower-bound theorem for local minimizers. Accessible same-paper rendering reports the multiplicity refinement and the one-way statement that a suitable global minimizer with maximal multiplicity must be a parallelotope. No inspected source states the converse exact spectrum for every parallelotope. Resultary returned the assigned finding as the exact match and no independent prior. The full primary body remained inaccessible, so the assessment retains that explicit bibliographic risk rather than asserting whole-document noncoverage.

## value

PASS

Parallelotopes are explicitly singled out in the new facet-spectrum theory's extremal multiplicity discussion, so they are the canonical calibration family rather than an arbitrary example. Determining the entire even spectrum and its maximal nonconstant multiplicity supplies a natural exact benchmark for the new operator and future extremal/stability questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
