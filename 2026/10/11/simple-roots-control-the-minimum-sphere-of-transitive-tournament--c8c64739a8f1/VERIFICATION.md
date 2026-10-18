---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For all n≥3 and the standard Euclidean edge-root realization, S=n(n²−1)/6 and c_k=(n+1−2k)/S. Positive weights λ_i=i(n−i)/S sum to 1 and express c as the barycenter of simple roots e_i−e_{i+1}. Then ||c||²=2/S and every vertex e_i−e_j, gap d=j−i, has exact squared distance 2−(4d−2)/S, so only gap-one vertices touch at R²=2−2/S. For arbitrary y, Σ λ_i||α_i−y||²=R²+||y−c||² gives a global strict lower bound outside c and uniqueness. I independently checked rational identities for n=3..100 from the source definitions, corroborating the universal identity proved algebraically.

## originality

PASS

The principal Numata–Takahashi–Tamaki result establishes the directed edge-polytope vertex configuration and facet theory, not the unique Euclidean minimum enclosing sphere. The positive-root chamber paper studies the same roots but combinatorial arrangements. Related semi-balanced sphere formulas require a unit rank increment on all arrows and cannot cover shortcut arcs in a transitive tournament (1→2→3 together with 1→3).

## value

PASS

A natural full type-A positive-root polytope has a surprisingly sparse exact Euclidean contact set, strictly stratified by interval length. The all-n contact classification and minimality witness are geometrically informative, not a routine numerical radius evaluation of a tiny special instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
