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

# Verification record

The analytic proof of `RESULT.md` is the basis for correctness. In particular, equation (5) is the multivariate beta integral; the inverse is the standard root/elementary-symmetric correspondence together with simple-real-root persistence; and equation (8) is the exact first-contact cap decomposition. These steps cover arbitrary dimensions and all positive side lengths and do not depend on numerical experiments.

Running `python3 verify.py` in an environment with packages from `requirements.txt` checks the following independently reproducible finite instances: reconstruction of distinct side lengths in dimensions three through five; a direct one-coordinate slicing integral of the three-dimensional box with lengths \((1,2,3)\) below its first contact radius; and the approach to the predicted \(\pi/9\) breakpoint constant from the right. The script prints `ALL_CHECKS_PASSED` on success.

The tests use floating-point arithmetic, and their tolerances do not prove exact symbolic equalities. They do not enumerate all dimensions or all side-length vectors, do not establish historical priority, and do not constitute an independent mathematical audit. At repeated reciprocal roots numerical polynomial-root extraction can be poorly conditioned, although the exact algebraic reconstruction remains unique.
