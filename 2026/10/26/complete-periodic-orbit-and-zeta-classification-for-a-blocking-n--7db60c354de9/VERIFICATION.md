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

# Verification
The complete theorem has a combinatorial proof: isolated-zero swaps lead to the exact recurrent-state split; two finite transfer matrices count admissible rings for every length; Möbius inversion gives primitive cycles. The calculations below supplement the proof and are finite.

Run `python3 verify.py` beside these documents. The checker implements the eight positive truth-table neighborhoods separately from the polynomial formula and checks 24,676 exact-integer predicates on rings of size 1 through 12: update identities, conservation, stationary-word recognition, cyclic shift, capture by time N, linear recurrences and all-iterate counts for tested time horizons.

A successful execution reports: `PASS 24676 exact-integer checks over ring sizes 1 through 12`. This does not establish correctness for all N or historical novelty. Neither independent audit nor independent validation has been performed.
