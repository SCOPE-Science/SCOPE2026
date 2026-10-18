---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

From the precise Jevtić–Živaljević definition, a generator is k successive cyclic partial sums for one length 2 and k−1 lengths 1, total circumference n=k+1. Each proper prefix sum is strictly increasing in an integer lift and less than n, so each facet has exactly k of the n vertices; hence it is a simplex-boundary facet. Choosing the 2 last gives {x,x+1,...,x+k−1}, missing x−1, and varying x achieves every missing vertex: exact equality of complexes with ∂Δ^k and homeomorphism to S^(k−1) for every k≥4. Independent enumeration of all k placements of 2 and all n starting vertices for k=4..8 gave exactly k+1 facets; symbolic argument covers every k.

## originality

PASS

Best-of-knowledge new higher-dimensional family, not the older k=3 special case. Jevtić–Živaljević arXiv:2002.09184 defines the general complex and proves a torus under genericity; repeated unit lengths violate its genericity hypothesis. Catanzaro arXiv:1612.03519 Theorem 24 identifies the triadic C(1,1,2) tetrahedral boundary, but its triadic classification does not give k≥4 in this different arbitrary-k construction. A published all-distinct nongeneric four-length Tonnetz has wedge homotopy, not this simplex boundary. No literal prior all-k family was found in named parameter, equivalent simplex-boundary, repeated-length, and sphere searches.

## value

PASS

A canonical reduced yet nongeneric length vector gives the complete facet-level structure of a sphere in every dimension, sharply contrasting with the generic-torus theorem and extending the known tetrahedral k=3 degeneration. This all-dimensional structural family is naturally defined by the object rather than a hand-picked numerical slice; it offers a simple exact boundary case for studying nongeneric Tonnetz topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
