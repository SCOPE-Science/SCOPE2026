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

# Reproducible checks

Run `python3 verify.py` with Python 3 and no nonstandard packages. The program enumerates all \(5!=120\) vertex total orders; for each it constructs the unique-earlier-neighbor matching and every simplicial subface. It verifies 12 vertices, 28 edges, eight triangles, 18 inclusion-maximal matchings among 37 distinct generated ones, and the complete sequence of eight free-edge/triangle cancellations displayed in `RESULT.md`. It confirms a connected 12-vertex/20-edge residual graph, first Betti number nine, equivariance of all faces under roof reflection, and the zero signed chain traces yielding degree-one trace one. The script has been executed successfully from this package.

The checks are exhaustive for the **specified** five-vertex house graph. The calculation supplies no inference about all houses of arbitrary size, other matching-complex definitions, or integral eigenspace splitting. The self-contained algorithm itself is an independently replayable finite mathematical certificate; external independent review has not occurred.
