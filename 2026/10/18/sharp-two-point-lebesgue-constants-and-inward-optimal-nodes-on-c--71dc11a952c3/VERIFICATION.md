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

# Reproducibility and proof boundaries

The mathematical argument is presented in RESULT.md. Its essential checks are: (i) interpolate from two distinct complex nodes and compute the **exact** operator norm by independently selectable unimodular input phases; (ii) obtain the midpoint and exterior-point lower bounds; (iii) show symmetric nodes attain the lower envelope; (iv) minimize the maximum of one strictly increasing and one strictly decreasing function; and (v) exclude asymmetric nodes through a strict exterior test.

The executable `arc_two_node_checker.py` uses only the Python 3 standard library, a fixed pseudorandom seed, six real arc parameters, and direct complex chord lengths. It passed 4,539 finite diagnostic assertions on the stored package. Run with `python3 arc_two_node_checker.py`. Its finite grids and finite pair samples are **not** proofs of an all-angle optimization. The proof does not depend on floating-point output, computer algebra, exhaustive finite enumeration, or an unavailable external certificate.

The result is limited to closed proper circular arcs, two distinct complex sampling nodes, and the subspace of affine analytic polynomials in the sup norm. No independent audit was performed.
