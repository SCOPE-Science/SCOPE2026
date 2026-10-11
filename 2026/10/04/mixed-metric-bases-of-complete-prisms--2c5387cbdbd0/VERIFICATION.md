---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For each matching index \(j\), comparing a clique vertex \(a_i\) with the clique edge \(a_i a_j\) for \(i\ne j\) shows that only \(a_j\) or \(b_j\) can distinguish them, forcing every mixed generator to meet each matching pair and hence have size at least \(n\). Equality is therefore a matching transversal. A transversal with fewer than two selected vertices in either clique layer creates an explicit vertex-edge or edge-edge collision. When both layers contribute at least two selections, the exact zero-distance and distance-two index sets determine every vertex and edge; the only possible cross-layer clique-edge ambiguity would require exactly two selections in each layer, hence \(n=4\), which is excluded. A fresh direct mixed-distance enumeration for \(n=5\) found exactly 20 bases, agreeing with \(2^5-10-2\), and the frozen verifier exhausts \(5\le n\le9\).

## originality

PASS

The foundational mixed-metric paper defines the invariant, studies several graph families and poses broader structural questions, but its inspected full text does not treat \(K_n\square K_2\). The later prism-related paper studies a different planar prism-allied family rather than complete prisms. Targeted searches for complete/clique prisms and the Cartesian product \(K_n\square K_2\) found no equivalent mixed-dimension formula or basis classification.

## value

PASS

\(K_n\square K_2\) is a basic Cartesian-product family. The theorem supplies not only the exact mixed metric dimension but every optimum basis and its count, with a sharp explanation of the exceptional \(n=4\) boundary. This is a natural reusable product-graph benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
