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

Total cover time equals the sum, over every deleted prefix, of the number of edges remaining uncovered. With remaining part counts \(r_i\) and fixed total \(R\), the remaining edge count is \((R^2-\sum_i r_i^2)/2\), so each prefix is optimized by maximizing the convex squared sum subject to the part capacities. Moving remaining mass from a smaller-capacity part toward a larger-capacity part never decreases that squared sum, proving that larger parts should remain full first. One smallest-part-first block ordering attains these prefix minima simultaneously. Summing the positions of the vertices in each exhausted block gives the displayed formula. The exhaustive verifier through order eight is a stress test only.

## originality

PASS

The 2006 source gives the exact complete-bipartite value, and the recent general MSVC paper gives broader algorithms, but neither inspected source states the arbitrary complete-multipartite closed form or its simultaneous prefix-majorization proof. Targeted searches including the cograph alias did not find a stronger theorem. The result is therefore a genuine natural-family extension rather than a recomputation of the two-part case.

## value

PASS

Complete multipartite graphs are the natural many-part extension of the previously solved complete-bipartite family. The theorem gives a transparent optimal structure and exact closed form for every number of parts, providing a useful dense-family benchmark for current MSVC work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
