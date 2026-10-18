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

# Computational verification

The complete, reproducible experiment uses Python 3 standard-library integer and set arithmetic. Run `python3 verify_incidence.py` and `python3 verify_coefficients.py`; compare the standard output byte-for-byte with `incidence_output.json` and `coefficients_output.json`, respectively.

`verify_incidence.py` enumerates every \(4\)-arc among the thirteen rational points, every unordered pair, and every line; it calculates all blocking unions, minimality, complement behavior, and conic decompositions. Its four explicit generator matrices yield exactly the full group order 5,616 and its pair-orbit propagation finds precisely five orbits. Its independent sweep of all six-subsets checks completeness of the extremal point sets.

`verify_coefficients.py` enumerates all normalized quadratic coefficient vectors, rejects geometrically singular quadrics via the exact polar Hessian determinant, evaluates their rational point sets on three disjoint charts, and recomputes all aggregate pair classifications. This is an algebraically independent parametrization of the same finite objects.

Both programs were executed successfully; their assertion suites passed. These finite exhaustions prove the specifically enumerated finite assertions because their search spaces are complete. Independent external audit has not been performed. They make no claim about other field orders, unseen literature, or arbitrary higher-degree curves.
