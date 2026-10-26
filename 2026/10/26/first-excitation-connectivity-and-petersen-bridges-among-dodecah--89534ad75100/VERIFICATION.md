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
# Reproducibility and scope

Run `python3 verify.py` in a directory containing that file. It needs Python 3.9+ and no third-party library, external database or network connection. All graph edges arise from the modular definition of \(GP(10,2)\), with integer vertex labels 0 through 19. Every unlabeled bisection is counted once by requiring vertex 0 to lie in the selected side.

The program performs two independently organized exact enumerations, using crossing-edge counts and induced-degree counts respectively; their complete histograms must match. It constructs the 340 admissible states by the threshold test, calculates swap edges by explicit vertex exchanges and then independently checks all pairwise symmetric differences. It checks the ten distance-two balls, all distances and eccentricities, all two-step bridge multiplicities, and a concrete bijection to the disjointness graph on two-subsets of five points.

Passing the assertions proves only the stated finite graph assertions with the supplied exact routines; it neither establishes an infinite-family theorem nor constitutes independent external review. Published prior results already cover the scalar isoperimetric number and the antipodal quotient, as explained in RESULT.md and REVIEW.md.
