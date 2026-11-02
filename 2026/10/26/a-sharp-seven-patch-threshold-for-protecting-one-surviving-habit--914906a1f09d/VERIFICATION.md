---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For protected vertex v, failure means all neighbors of v fail and the remaining survivors form an independent set. Therefore 1-R_v=q^(n-1)I(T-N[v];p/q); the factor q^(n-1) is common. Independent fresh exhaustive Prüfer enumeration of every labeled tree of size 2..7, with direct independent-set subset counts, gave per-size (total, nondominance) (1,0),(3,0),(16,0),(125,0),(1296,0),(16807,840). Every one of the 840 nondominance cases has precisely the equally subdivided 3-star structure (automorphism group size 6). Its center residual polynomial is (1+t)^3 and arm-neighbor residual polynomial is (1+2t)^2, with leaf residual polynomial 1+5t+6t²+t³. Center-minus-arm success is p(1-p)^3(1-p-p²), giving the unique golden threshold. All n<=7 are exhausted, not sampled; no assertion above n=7.

## originality

PASS

Best-of-knowledge originality of the exact final statement, rather than its standard background ingredients: An intervention that protects one fixed vertex to retain at least one viable habitat link is a motivated binary network-reliability objective. The exact smallest size without a single universal optimum, unique 7-vertex topology and probability crossover locate a concrete structural threshold; ecology is used as motivation, not a claim about field resilience. The searched and materially inspected primary results do not directly cover the full exact statement; plausible uninspected generalizations remain residual risks.

## value

PASS

An intervention that protects one fixed vertex to retain at least one viable habitat link is a motivated binary network-reliability objective. The exact smallest size without a single universal optimum, unique 7-vertex topology and probability crossover locate a concrete structural threshold; ecology is used as motivation, not a claim about field resilience.

The dated certificate retains the supplied scientific assessment, sources and limitations.
