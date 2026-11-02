---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The graph consists of K5 on {u,v,a,b,c} plus x,y adjacent to both u,v; it has 7 vertices,14 edges and beta1=8. The ordered deleted-product CW model for F(G,2) was independently built with 42 zero-,140 one-,82 two-cells; exact rational boundary ranks 41 and77, and d1*d2=0 in every column. Thus H1 dimension=140-41-77=22. For finite connected G not homeomorphic to a circle, Barnett–Farber Proposition 1.3/2.3 gives surjectivity of inclusion-induced H1 into H1(GxG) of rank 2 beta1=16, hence kernel dimension 6. Removing uv and deleting endpoints leaves components K3, {x}, {y}; Farber–Hanbury Theorem14 yields a lower bound of 2*3-2=4 for the same kernel, so 6 is strictly greater. Computation is exact over Q (no modular inference) and has a complete cell list; no claim about Z torsion.

## originality

PASS

Best-of-knowledge comparison on actual final mathematical statement for Six-dimensional inclusion H1 kernel for a natural nonplanar two-vertex-cut graph. Four distinct implications were checked, including known covering numeric/special-case portions that are explicitly excluded from the originality claim. Sources and access limits are detailed below.

## value

PASS

A canonical nonplanar 2-cut stress test (a K5 block with two twin length-two attachments at the same pair) demonstrates that the standard two-cut lower bound of 4 need not be exact: the actual kernel dimension is 6. This supplies a reproducible, integral-chain-defined rational test case for refining intersection-form rank estimates, not an arbitrary floating-point number or rebranding of the published lower bound. It is deliberately a narrow but nontrivial structural benchmark, not a general classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
