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

# Verification record

Run `python3 verify_joint.py` with Python 3.8 or later. The file requires only the standard library and enumerates every naturally labeled poset of sizes 1 through 6 by transitively closed relations compatible with the fixed linear extension.

For each poset, it constructs all order ideals as bit masks, computes each pseudocomplement directly from principal downsets, and independently counts elements satisfying excluded middle and double-negation elimination. It checks the center/regular formulas, the power-of-two ratio, the universal sharp bound for every positive defect, and the if-and-only-if extremal shape condition. Separately, it verifies explicit connected constructions with 2–5 minimal points and 1–4 points in the upper chain.

Expected counts of tested naturally labeled posets, in increasing size, are `1, 2, 7, 40, 357, 4824`, totaling 5231; each result appears as `NATURAL_POSETS_PASS`. The final marker is `JOINT_HEYTING_ALL_CHECKS_PASS enumerated=5231 equality_counts={1: 35, 2: 21, 3: 7, 4: 1}`.

The program checks the finite boundary and the proof's invariant formulas, but it does not certify infinitely many algebras, historical novelty, or independent scientific validation. The universal statements are established by the mathematical argument in `RESULT.md`.
