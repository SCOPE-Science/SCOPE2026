---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reproduced the census with standalone Python, without executing check.py. For each potential exposed Petersen edge h, orient the other 14 Petersen edges toward a chosen endpoint in all 2¹⁴ ways and retain assignments with even indegree at each base vertex. Cubicity means occupied buckets contain exactly two edges. The resulting pairs are a near-perfect matching of L(P), and every such matching yields a unique assignment because two incident Petersen edges have exactly one common endpoint. This produced 32 states for each h and 480 in total, attaining the upper bound of seven matching edges on fifteen vertices. Reconfiguration adjacency was constructed by grouping states with a common six-edge core. This captures all one-edge exchanges: the removed and inserted edges have endpoints among the same three uncovered vertices of the core and must share one. All degrees were four, yielding 960 edges. Independent layer traversal from every source reached all 480 states with eccentricity nine; unordered-pair distances 1–9 were 960, 2400, 6120, 13080, 23310, 32730, 26550, 9330, 480, and excess over 7−|M∩N| for values 0–3 was 81120, 32340, 900, 600. Distance-nine edges gave 120 connected four-vertex components, each 2-regular and with constant exposed vertex, proving the C4 assertion. The four adjacent ground-symbol transpositions preserve every neighbor set and generate orbits of sizes 60, 60, 60, 60, 120, 120. Replay of frozen hamcycle.txt (SHA-256 20b24d8b4f5331617d6b72bf75d8673707048076f7e60d23cfd4899c122dcc05) validated its permutation of 0–479 and every link including wraparound, using lexicographic sorting of the reconstructed edge-tuples as in the frozen specification. Replay inputs are the fixed KG(5,2) definition and hamcycle.txt next to RESULT.md; construct cores, traverse each source, and check the cycle against those cores. No approximation or untested source class enters this proof.

## originality

PASS

The matching-graph construction is known. The distinct contribution supported here is the exact instance classification of the single-exchange maximum-matching graph of L(Petersen), particularly its farthest-pair squares with constant exposed vertex and certified Hamiltonicity. Related catalogued graphs and the inspected general reconfiguration statements do not determine these data. The two older matching-graph articles remain material access risks; no claim of exhaustive exclusion is made.

## value

PASS

This is the first object in a canonical construction from the Petersen graph's edge incidence and a standard maximum-matching move, with no tuned cutoff. Its degree follows locally, but the full metrics, uniform eccentricity, and 120 antipodal squares confined to exposed-vertex fibers describe global geometry not visible from that local rule. The certified Hamilton cycle gives an explicit cyclic listing of all optima by minimal edits. Together these are useful benchmark data for one-hole matching reconfiguration, without claiming a general Gray-code theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
