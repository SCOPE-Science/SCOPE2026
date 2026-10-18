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

Reconstructed the 13 matchings of disjoint adjacent swaps in six positions and regenerated every member of the canonical multiset classes. Independent exhaustive exact-rational verification of certificates.json at the assigned Git snapshot: for (2,2,2), (3,1,1,1), (2,2,1,1), universe sizes 90,120,180; explicit distinct upper-cover center sets have 9,15,17 centers and cover every word; nonnegative fractional weights sum to 9,15,17 and have total weight at most 1 in every ball centered at ANY class word (90+120+180 inequalities). This supplies the lower bounds by weak LP duality and relabeling transports each complete certificate to every concrete class. No implicit optimization result, numerical LP, or script exit code is used as proof.

## originality

PASS

The motivating Table 3 gives the same numbers as attainable covers but explicitly disclaims optimality. Exact dual packing inequalities prove minimality, not implied by the original upper bounds. Resultary semantic search found the submitted result and neighboring code/packing records, not an earlier proof of these three minima. Best-of-knowledge claim confined to three multiset types.

## value

PASS

Closes a precise finite optimality gap singled out by an explicit published construction using short rational certificates. Knowing the minimum classwise cover sizes, not merely feasible center lists, provides exact benchmarks for the length-six limited-permutation channel and validates optimality of three improvements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
