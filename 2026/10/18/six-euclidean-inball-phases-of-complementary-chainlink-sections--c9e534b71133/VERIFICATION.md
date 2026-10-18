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

# Exact verification

Run `python verify.py` with SymPy installed according to `requirements.txt`. The program reconstructs the six algebraic support triples, verifies all nonnegative dual coefficients and 18 dual-identities, solves all exact center triples, checks every other shifted facet inequality at both interval endpoints, and checks six bound-comparisons at each endpoint. Affinity extends these finite endpoint certificates to the full real intervals. It also enumerates every feasible vertex of the two claimed hexagons using the nine given halfplanes, and symbolically recomputes Euclidean perimeter and area. Results were replayed successfully from these actual files.

No theorem about all chainlink parameters is being inferred from those finite operations. The argument for all continuous height values is the affine interpolation of certified endpoint constraints; the equal-Ehrhart conclusion is an explicitly cited, pre-existing primary theorem, not something tested through point counts. Independent mathematical audit has not been performed.
