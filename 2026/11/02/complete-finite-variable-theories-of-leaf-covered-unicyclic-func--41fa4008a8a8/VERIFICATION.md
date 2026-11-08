---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

In arc-only signature the indegree criterion Core(x)=∃y E(y,x) uses two variables. One-pebble logic sees loops only; two-pebble atomic extension types yield 5 phases (loop with 1 or ≥2 leaves, core lengths 2,3,≥4). For k≥3, 3 reusable variables define arbitrary fixed-length core walks; kth child-count threshold uses root variable shadowed after k−1 selected siblings and a third-variable sibling-parent predicate, hence min(b_i,k) is FO^k-definable. Conversely, k-pebble Duplicator uses fixed cyclic core rotation and injective fiber matching, with ≥k fibers always leaving free leaf after at most k−1 occupied. Burnside counts necklace orbits and minimal clipped representatives. Independent exact type-refinement of bounded test structures and independent Burnside necklaces (k=3,4,5, ℓ≤6) agreed; all-length theorem relies on pebble proof, not finite tests.

## originality

PASS

Brown–Hoshino 2007 give rank-bounded undirected paths/cycles EF game classification, not fixed-variable width of directed leaf-covered coronas. Dawar–Holm 2012 establishes general pebble-game semantics, not this explicit FO^k equivalence invariant and necklace count. Nearby published Resultary classification of finite directed paths addresses quantifier rank and a crown-homotopy necklace deals with a different logic. Broad unary-function model theory may imply the result by general types, so that remains residual risk.

## value

PASS

A complete FO^k theory equivalence classification at every depth, with sharp k=1,2 phase changes, k≥3 orientation-sensitive clipped necklaces, exact number of theories and minimal models, is a motivated finite-model-theoretic invariant for a natural family of functional digraphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
