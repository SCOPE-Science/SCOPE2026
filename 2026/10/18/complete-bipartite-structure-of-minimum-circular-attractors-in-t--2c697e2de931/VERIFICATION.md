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

# Finite verification

`checker.py` builds Fibonacci words from the literal binary seeds and checks each index from one through twelve. It creates every distinct circular factor for every length from one to the entire word length and all unordered position pairs, and exactly characterizes intersections through per-position bit masks. Every pair that survives all factor lengths is a minimum circular string attractor because both binary symbols occur in every word. It then computes the entire resulting graph, colors connected components and verifies it equals the complete bipartite graph between the two non-isolated color classes. It verifies the total edge count and the exact critical lengths, recording a short digest for each edge list. The full observed stdout appears in `checker-output.txt`.

Run `python3 checker.py` using Python 3.9 or later; no network and no packages are needed. The final line must be `ALL FINITE ENUMERATIONS PASS`. The experiment is exhaustive for exactly the twelve finite words; it neither investigates larger indices nor claims a proof of an infinite recurrence. The executable algorithm is fully available for independent code inspection but such an independent audit has not occurred.
