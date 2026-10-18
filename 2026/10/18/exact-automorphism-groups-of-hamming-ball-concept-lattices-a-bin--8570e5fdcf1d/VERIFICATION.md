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

# Reproducibility and limits

Run `python3 verify_hamming_lattice.py` in the same directory as this file. The program is self-contained and uses only Python 3's standard library. It reconstructs the radius-one ball sets directly, enumerates finite closed intents and verifies every candidate closure, and compares with predicted singleton, coordinate-line, distance-two-pair and neighborhood families. Small parameters are checked exhaustively, including complete enumeration of all attribute permutations for binary \(d=2,3\) and ternary \(d=2\). It also validates every member of the proposed parity-lift group for binary \(d=2,3,4\).

Recorded finite verification: `VERIFY_OK closed_intents_total=881 exhaustive_ball_perm_counts={(2, 2): 24, (3, 2): 192, (2, 3): 72} binary_parity_generated={2: 24, 3: 192, 4: 1920}`. The all-parameter upper bounds and exact group structures rely on the proof in `RESULT.md`, not on finite enumeration. External independent audit has not been performed.
