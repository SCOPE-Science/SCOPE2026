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

Partition ordered edge pairs by matching/different directions, each edge of uniform weight 1/(d 2^{d−1}). Different directions: mismatched other fixed bits K~Bin(d−2,1/2), and independent endpoint offsets U,V~Unif(0,1), D=K+U+V. Same direction: mismatched fixed bits K~Bin(d−1,1/2), K=0 gives |S−T| density ℓ; K≥1 gives K+min(S+T,2−S−T) with density h=2t on (0,1). Assemble mixture with kernel g(t)=min(t,2−t) on (0,2). Only h kernels jump at integer endpoints, with exact displayed magnitudes; ℓ and g are continuous there as asserted. Exact mixture integrations reproduce mass, mean and second moment; independent four-endpoint shortest-path evaluations for d3..5 and rational edge coordinates yielded 22,704 matches, with broader 22,829 bounded checks. Coupling to different-direction event with failure 1/d and binomial Berry–Esseen proves the uniform O(d^{-1/2}) CLT. Bounded comparisons do not establish all d.

## originality

PASS

The prior continuous mean-distance papers provide integrals, bounds, and graph examples but the inspected full statements do not give the all-dimensional distance law or binomial jump spectrum on hypercube wireframes. Older 1982 papers on mean distances were unavailable in complete text; authorized institutional retrieval returned vpn_disconnected. Historical priority of a geometric distance-distribution formula is a real residual risk, not a reason to fabricate absence.

## value

PASS

The complete probability law of intrinsic distances between uniformly sampled points on a classical d-cube wireframe is a natural geometric invariant. The nontrivial all-dimensional binomial jump spectrum, exact moments, and normal limit distinguish it from a simple mean calculation; exact formulas can be reused in graph-metric probability and benchmarking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
