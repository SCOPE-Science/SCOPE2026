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

# Verification and reproducibility

The exact standalone script `verify.py` uses only the standard Python library and was executed from its packaged source file. It returned:

`EXACT_OK instances=1360 edges=18925 contacts=12880 two_path_invariances=252`

For every tested graph, it checks the potential gaps, nonnegative contact weights, weighted incidence identity, sum of weights, squared norm, explicit radius, and the complete list of contacting roots, all with `fractions.Fraction`. The second sweep tests the unchanged normalization and old center coordinates after adding a new two-edge path. Additional numerical constrained optimizations on seven mixed-length graph families agreed with the formula within numerical tolerance.

These finite checks do not establish a universal theorem. The infinite-family certificate is the explicit nonnegative edge weighting that reconstructs the proposed center, together with the weighted squared-distance identity proving optimality among every Euclidean center. The mathematical proof and quantifiers are stated in `RESULT.md`.

No independent audit has been performed.
