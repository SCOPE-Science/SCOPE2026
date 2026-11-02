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

# Reproduction and limits

From the extracted artifact directory run `python3 checks/verify.py` with any recent Python 3 interpreter. The verifier uses only standard-library integer operations and enumerates original octahedron/icosahedron edges, triangular faces, rectified vertices and crossed edges.

The exact checks cover every original edge's axial balance relation (12 octahedral and 30 icosahedral identities), the four-valent rectification property, and exact base-normal section counts of 8 and 12. It additionally evaluates 720 and 960 distinct generic small-integer normal triples, respectively. The final expected output is `EXACT CHECKS PASSED`. Rational-direction enumeration is a stress test, not a proof about infinitely many directions; the neighbor-pairing argument in `RESULT.md` establishes the global theorem.

No independent external validation, priority certification, or formal mechanical verification was undertaken. Exceptional central cuts through vertices are excluded, and historical-priority uncertainty remains.
