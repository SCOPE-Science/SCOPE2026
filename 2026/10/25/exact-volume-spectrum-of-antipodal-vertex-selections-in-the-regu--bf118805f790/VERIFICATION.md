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

## Checks

- The standalone verifier uses only the Python standard library.
- It enumerates all \(64\) sign selections and uses exact arithmetic in \(\mathbb Z[\varphi]\).
- Supporting planes are found by testing all vertex triples against the remaining points with exact algebraic sign tests; coplanar vertices are grouped into facets.
- Each facet boundary is recovered from shared edges, oriented outward, and triangulated. Exact determinant sums yield \(6\operatorname{Vol}(P)\) as one of \(8+4\varphi\), \(8+12\varphi\), \(8+16\varphi\), or \(12+16\varphi\), with the stated multiplicities.
- A separate floating-point hull calculation over all \(64\) cases agreed within \(1.8\times10^{-15}\); this is a consistency check only, not the proof.

## Limits

The claim is confined to the regular icosahedron in the stated coordinates. The computation does not settle the general higher-dimensional extremal-volume problem. Independent audit has not been performed.
