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

# Verification

The accompanying standalone `verify.py` can be run with `python3 verify.py` in a directory containing that file, SymPy, NumPy, and SciPy. The checker tests exact-rational sample evaluations, independent convex-hull volumes of primal and polar bodies, optimization of support functions by linear programming, and symbolic derivative and cubic-root identities. The proof of the all-dimensional volume formula and the strict three-dimensional extremum classification is analytical and appears in `RESULT.md`.

Finite rational samples, numerical hulls, and numerical root approximations cannot certify a statement for all dimensions or all real parameters. The source comparison does not eliminate all possible historical overlap, particularly when full text was unavailable. Independent audit has not been performed.
