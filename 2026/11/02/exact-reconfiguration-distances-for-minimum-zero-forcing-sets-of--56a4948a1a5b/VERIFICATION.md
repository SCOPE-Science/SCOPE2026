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

# Reproducible checks

`verify_primary.py` builds each crown graph from its bipartite incidence condition, independently tests ordinary forcing closure for every four-white set, derives single-vertex exchanges, checks all shortest distances against the exact formula, and verifies every distance-histogram coefficient and Wiener sum for integers \(3\le n\le8\).

`verify_alt.cpp` uses independent bit-mask Johnson vertices, constructs legal noncollision moves directly, and checks every pairwise breadth-first distance, histograms, graph diameters and Wiener indices for the same finite values.

Execute `python3 verify_primary.py` and `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. Both finished with `PRIMARY_CROWN_CERTIFICATE_OK` and `ALTERNATIVE_CROWN_CERTIFICATE_OK`. The outputs for \(n=3,4,5,6,7,8\) respectively recorded Wiener indices \(27,912,9750,58860,252105,857472\).

The code does not prove the theorem at arbitrarily large \(n\); that conclusion follows from the explicit geodesic constructions and algebraic counting in `RESULT.md`. No separate external validation or independent scholarly audit was performed.
