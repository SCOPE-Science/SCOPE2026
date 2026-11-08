---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The hat-function Gram matrix is G=(2dI+A)/6 with d=m(r-1). Direct multiplication proves its exact inverse has diagonal X/T, same-part off-diagonal 1/T, across-part -2/T, T=m^2(r-1)(2r-3), X=3m(2r-3)+1. Its kernel edge types are incident (X,-2), same-part-adjacent (1,-2), and external (-2,-2); their exact absolute integrals give the stated R. Since every projected function is affine on each edge, an L-infinity norming evaluation is a vertex. Kernel-sign inputs attain R. Algebra verifies R-2 sign regimes, monotonic m-increment, both limits, and negative kernel mass (R-1)/2. Independent direct SymPy Gram inversions and exact integrals at (m,r)=(1,2),(2,2),(3,2),(3,3),(2,4) agree; universal statement follows from matrix proof, not sample sizes.

## originality

PASS

Bounded best-of-knowledge originality after comparing equivalent mathematical statements, stronger-coverage implications and relevant primary material. No inspected source is shown to imply the target exact statement; incomplete historical coverage is retained as a risk.

## value

PASS

Optimal max-norm amplification of an L2 projector is a standard stability invariant in spline/FEM analysis. The natural balanced branched graph family gives a complete two-parameter formula, exact sign extremizers, the sharp m=4 transition above 2, and an unattained universal 7/3 benchmark without pendant vertices. These are substantive approximation-instability boundaries, not mere routine plug-in numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
