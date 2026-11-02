---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification and limits

The checker `verify_desargues_metric.cpp` uses a fixed twenty-vertex cubic graph. It enumerates all seven- and eight-subsets by Gosper bit iteration, checks the complete ordinary forcing closure, constructs the exchange graph by exact two-bit changes, and performs breadth-first search from each one of its 13,520 vertices. Assertions cover all 91,388,440 distinct unordered pairs. It uses exact integer operations only, no random choices or timeouts.

Reproduce using `g++ -std=c++17 -O3 verify_desargues_metric.cpp -o verify_desargues_metric && ./verify_desargues_metric`. Expected terminal signature: `DESARGUES_METRIC_EXHAUSTIVE_PASS`; auxiliary lines give 13,520 minimum configurations, 178,560 edges, radius seven, diameter eight, and 47,380 distance-excess-one unordered pairs. The metric histogram includes zero excess greater than one.

The second checker `verify_desargues_alternate.py` independently constructs the bipartite-Kneser realization with twenty vertices, uses sequential single-forcing updates, and checks the minimum-set and edge/degree census. It also runs nine complete breadth-first searches from selected sources. Expected signature: `ALTERNATE_KNESER_PASS`. Its coverage is deliberately smaller for pairwise distances; it does not reproduce the C++ all-pairs histogram.

`certificate.json` contains the claimed exhaustive count arrays and an explicit obstruction path, not a freestanding mathematical proof. Exact proof requires reading and running the included code. No independent external audit has been performed.
