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
The arbitrary-dimensional theorem is proved analytically in `RESULT.md`. The finite checker is corroboration only.

`verify.py` replays three one-dimensional acyclic flow polytopes with exact rational graph-Laplacian calculations. For each example it computes edge effective resistances, enumerates lower ideals, applies the stated cut-ratio formula using the specified facet-edge set, and compares the result with the direct Euclidean half-length of the segment.

One example is the transitive triangle with netflow \((1,1,-2)\). The edge from the middle vertex to the sink is non-bridging in the underlying triangle but never vanishes on the polytope, so it is not a facet edge. It is correctly omitted from the facet-edge set; the exact radius remains \(\sqrt3/2\). This checks that the replay distinguishes graph edges from actual coordinate facets.

The replay does not mechanize the general Farkas-duality argument or prove uniqueness of the pseudoinverse formula in arbitrary dimension; those steps are given symbolically in `RESULT.md`.
