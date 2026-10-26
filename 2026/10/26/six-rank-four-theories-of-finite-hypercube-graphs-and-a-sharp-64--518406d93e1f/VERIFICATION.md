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

# Verification scope

Execute `python3 verification.py` (Python 3, standard library only). It regenerates the dimension-by-dimension rank-four signatures, checks six distinct classes, tests stabilization through dimension 17, validates the six pair-extension types, and cross-checks every ordered triple and pair in dimensions one through six against direct adjacency calculations on the actual finite hypercube graphs. `verification_output.txt` is the recorded output from that execution and ends with `VERIFY_OK`.

The code enumerates all coordinate-class splits and exact atomic adjacency/equality profiles, rather than sampling formulas. The accompanying proof shows why those profiles are logically complete and why truncation at 16 covers arbitrarily large dimension. Full finite graph enumeration alone would not establish this last step. All scientific statements are conditional on the definitions in RESULT.md; no independently performed audit is claimed.
