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

# Verification of eleven rank-three cycle-power theories

Run `python3 verify.py` alongside `RESULT.md`. The program requires only the standard Python library. Its actual recorded output is provided in `verification_output.txt`.

## Verification checks

The calculator reconstructs the eleven exact signatures from the closed-neighborhood overlap expression, verifies their proposed regimes across 34,268 parameter choices, and independently constructs 132 adjacency matrices to reproduce third-vertex extension patterns. A second implementation, based on atomic diagrams of ordered triples and a full three-round type recurrence rather than interval arithmetic, identifies eleven distinct representative theories, distinguishes all 55 pairs of representatives, and checks additional representatives in each class. The smallest representative in each class is determined from the exact arithmetic parameter constraints, making order eleven sharp within this family.

These checks supplement a proof whose scope is all integers \(k\ge1\), \(n\ge2k+1\). Finite arithmetic trials do not establish the infinitely many remaining parameters, and an absence of matches in literature searches is not proof of independent novelty. The infinite assertion follows from the uniform interval-overlap formula and the sign inequalities given in `RESULT.md`. No independent external scientific audit or formal proof-assistant certification has been performed.
