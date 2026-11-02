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

# Reproduction and checked limits

Run `python3 verify_hamming.py` beside `TREES.json`. The program checks all complete adaptive witness trees against directly computed Hamming distances, recomputes finite adaptive and static shattering dimensions from the complete incidence matrix, and tests the two-positive-intersection obstruction on representative finite instances. `VERIFY_OUTPUT.txt` records the exact output observed.

The unrestricted depth-four obstruction is proved in `RESULT.md`; no finite grid is used to extrapolate that bound. The general static VC classification is explicitly attributed to Adler–Benediktsson–Macpherson, Theorem 4.7. The finite certificates cover the minimal parameter instances needed for all online lower bounds by induced embedding. No independent audit or formal machine proof of the unrestricted theorem is asserted.
