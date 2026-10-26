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

# Reproducibility and scope

Execute `python3 VERIFY_LADDER.py` with Python 3 and its standard library. The provided `VERIFY_OUTPUT.txt` records the actual output: total states and exact extinction counts at rung lengths 2–5, followed by `LADDER_GH_EXACT_VERIFY_OK`. The program constructs graph adjacency from rung and rail edges, simulates state changes, detects loops and independently evaluates every square circulation. It additionally checks all nine transfer rows. All tested configurations are enumerated for each listed size; this is not exhaustive over arbitrary size.

The infinite claim is proved in `RESULT.md` using conservation and lifting of nearest-residue phase differences plus a two-type transfer. The previously established general zero-winding convergence criterion is explicitly acknowledged, not claimed as new. One external source was inspected in its substantive full-text sections. Neither a formal assistant-independent proof review nor independent mathematical validation is asserted.
