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

The formula is proved by subgroup classification, a subspace-pair Gaussian intersection count, and an affine-coset alignment count. In the nontrivial complement case the alignment count is exactly \(p^{n-r}\) ordered lifts for kernel intersection dimension \(r\), not a probability estimate or a computational heuristic.

Execute `python3 check_intersection_profile.py` with a standard Python 3 interpreter. It checks every subgroup degree in seven configurations: \((3,1,2)\), \((3,2,2)\), \((3,3,2)\), \((5,1,4)\), \((5,2,4)\), \((7,2,3)\), and \((7,2,6)\); and all ordered subgroup-pair intersection-size strata in five configurations: \((3,2,2)\), \((3,3,2)\), \((5,2,4)\), \((7,2,3)\), and \((7,2,6)\). Observed strata are constructed from actual subgroups and their set intersections, while expected strata use Gaussian coefficients and the independent formulas. The exact output terminates in `ALL_INTERSECTION_PROFILE_CHECKS_PASSED 12`.

The finite checks do not certify formulas for every dimension or field; the algebraic proof establishes those claims. Independently authored formal or human validation has not been performed.
