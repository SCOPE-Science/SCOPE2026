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

# Verification notes

Run `python3 check.py` with Python 3 and no external dependencies. The checker constructs the two families of \(351\) explicit lines, verifies that all line-spanning pairs have distinct row-reduced spans, and checks the restricted gradient cubics coefficient-by-coefficient on every line. It also enumerates all \(9841\) projective points of \(\mathbb P^8(\mathbb F_3)\) and finds exactly \(522\) singular points, matching the predicted line union. The eight two-value combinatorial derivative cases are separately recomputed. An optional second standalone checker, `gf9_stress.py`, verifies all 14,112 assignments of three distinct values and positive multiplicities totalling nine over the extension field \(\mathbb F_9\); it finds 336 satisfying the gradient equations and agrees with the two asserted multiplicity patterns. Run `python3 gf9_stress.py` for the additional finite-extension stress test.

The exact proof of the theorem over an algebraic closure is in RESULT.md: the degree-three common-root equation, multiplicity congruences, exhaustive two-value table, and the geometric consequences. Finite point enumeration is corroboration, not an argument that no additional points exist over extensions of \(\mathbb F_3\). No claim about the nonreduced Jacobian scheme or complete intersection lattice is verified.
