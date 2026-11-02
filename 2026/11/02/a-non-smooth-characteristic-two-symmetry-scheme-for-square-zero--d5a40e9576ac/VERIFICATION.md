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

# Reproducible verification

Execute `python3 verify.py` with a standard Python 3 interpreter. The program implements squarefree-monomial multiplication and its own field operations for prime fields and for \(\mathbb F_4\) via an explicit irreducible quadratic. It enumerates all square-zero generator images, checks every possible cotangent-linear matrix by Gaussian elimination, weights each permitted linear tuple by the actual number of generator-image lifts, and compares the totals to the formulas for six specified small configurations. A second calculation independently forms the linear equations of derivations and computes the dimensions by elimination. These are finite checks, not proofs of the arbitrary-field scheme theorem.

Expected final line: `SQUARE_ZERO_COMPLETE_INTERSECTION_AUT_OK`.

Expected automorphism totals: \(24\), \(72\), \(2880\), \(800\), \(688128\), \(944784\) for \((d,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3)\), respectively. Their tangent dimensions are \(8\), \(4\), \(8\), \(4\), \(24\), \(12\).

The general proof relies on the explicit universal-map coordinate equations and on nilpotent-ideal invertibility; it does not follow from these small enumerations. The characteristic-zero part is strongly related to existing monomial-algebra automorphism theory. An independent audit has not been performed.
