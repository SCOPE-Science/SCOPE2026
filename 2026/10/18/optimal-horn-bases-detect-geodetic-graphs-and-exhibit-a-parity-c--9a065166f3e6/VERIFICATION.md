---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Direct bounded checks

Run `python3 verify.py` with the Python 3 standard library. The checker computes distances by Floyd–Warshall and identifies convex sets by the all-shortest-path interval condition, independently of the candidate rule sets. For cycles through seven vertices, it tests every candidate optimum basis against every subset; for cycles on eight through ten vertices, it tests twelve constructed bases each. For cycles on three through five vertices it also solves an exact weighted set-cover problem over all sound nontrivial rules, including larger premises, to check both the minimum cost and its multiplicity.

The verified candidate cost profile on cycles of lengths 3–10 is `0, 8, 15, 30, 42, 64, 81, 110`; counts from the rule-choice product are `1, 1, 1, 64, 128, 1679616, 10077696, 63403380965376`. The checker verifies the proper four-vertex hull obstruction on the four-per-shore crown, and compares every subset on each of the five-, six-, and seven-per-shore crowns against the respective tight unit-head basis of cost 75, 108 and 147. In particular the ten-vertex crown is a directly replayable counterexample to the converse. Infinite families and equality forms are established by the mathematical proof in `RESULT.md`, not by extending the bounded checks.
