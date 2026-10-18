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

# Verification and limitations

The standalone `verify.py` implements a finite exhaustive search over four distinct vertices of pairwise Hamming distance at most two. For each omitted vertex it computes the intersection of radius-one neighborhoods of the remaining three, removes neighbors of the omitted vertex, and checks the witnesses. For each dimension two through eight, it verifies every qualifying object set, witness uniqueness, square/parity classification, and the exact two summands of the scale count.

Recorded number of contranominal four-scales at dimensions two through eight: 1, 8, 40, 160, 560, 1792, 5376. The program uses Python's standard library, deterministic iteration, and assertion failures on discrepancies. Execute `python3 verify.py` in a directory containing this file. The finite tests check small cases only; the general theorem relies on the proof in `RESULT.md`. No independent review or external certification has been performed.
