---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every diagonal matching-field vertex occupies k positions within the active k by (n-k+1) band, one per row. All lie on the sphere around the uniform row coordinate c, of squared radius k-k/(n-k+1). Consecutive blocks cover each active coordinate exactly once, so their centroid is c; averaging ||v_s-q||^2=R^2+||q-c||^2 proves both optimality and uniqueness without reliance on affine-dimension details. The source p.5 supplies exact vertices; the source p.7 confirms dimension. Independently enumerated all vertices for (n,k)=(5,2),(7,3),(9,5), obtaining 10,35,126 equal-distance contacts and correct squared radii.

## originality

PASS

This is a Euclidean native-coordinate result, not a consequence of unimodular equivalence to a GT/order polytope. The source theorem provides the vertex realization and dimension; new cosphericity and the short positive-contact certificate are additional statements. Resultary found itself and distinct polytope radius problems, not the same formula.

## value

PASS

The exact minimum sphere in a standard representation-theoretic polytope, all-contact phenomenon, and certificate with only n-k+1 positive vertices give a precise natural metric invariant relevant to comparing embeddings. The certificate establishes minimality rather than mere cosphericity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
