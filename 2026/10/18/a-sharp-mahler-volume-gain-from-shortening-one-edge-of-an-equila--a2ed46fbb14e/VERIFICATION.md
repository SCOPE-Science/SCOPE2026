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

The proof obtains the primal volume from sign-chamber integration and a beta-density identity; it obtains the polar volume from ordering simplices and Dirichlet gap distributions. These are arguments valid for every stated dimension and real parameter, independently of the finite checks.

Running `python check_one_short.py` (dependencies in `requirements.txt`) constructed the primal molecule polytope and the polar constraint polytope on \(3,4,5\) metric sites for four rational edge parameters each. All twelve primal and dual volumes exactly matched the rational closed formulas after exact Fraction arithmetic and determinant accumulation. The convex hull triangulation supplies only face index sets using SciPy's Qhull algorithm; this distinction limits the claim of an entirely independent rational combinatorial certification. The script also performed exact rational comparisons of the claimed maximizing value versus three alternatives for dimensions \(3\) through \(23\); these finite comparisons are not a substitute for the derivative proof.

Recorded terminal completion: `ALL 12 EXACT RATIONAL POLYTOPE-VOLUME TESTS PASSED`.

No independently commissioned or external scientific audit has occurred; an exhaustive bibliographic uniqueness claim is not made.
