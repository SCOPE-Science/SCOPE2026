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
# Verification procedure

Run `python3 verify_incidence.py` and `python3 verify_distance.py` from the directory containing those scripts. No network connection or external libraries are required. The first program computes distances directly from the seven Fano lines and checks all five-subset incidence types. The second constructs a different incidence labeling by zero binary dot products, computes graph distances by BFS, scans all 16384 subsets, then constructs exchange adjacency via common four-subsets.

Both independently conclude that there are 168 five-vertex metric bases, 420 single-replacement edges, degree five, and distance-layer profile \((1,5,18,49,71,24)\) for every base. The first certifies the triangle–tangent classification and partition into 56 triangles; the second certifies transitivity using 168 invertible coordinate maps and polarity. `incidence_output.txt` and `distance_output.txt` are recorded outputs, but correctness rests on the included source programs and the exhaustive search bounds, not on the logs alone.

All calculations are finite and exact; there are no randomized steps or floating-point tolerances. A failure to execute in a different environment would not by itself be a mathematical counterexample. Independent external audit has not occurred.
