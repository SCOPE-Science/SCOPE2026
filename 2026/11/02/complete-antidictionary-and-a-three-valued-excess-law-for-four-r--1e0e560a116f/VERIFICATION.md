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

For each of 4,096 parameter quadruples with run exponents 1 through 8, `python3 verify.py` reconstructs the word, enumerates its distinct factors, builds candidate minimal absent words independently from one-letter extensions of present factors, and compares those with the proposed exact structural list and the polynomial length histogram. It also evaluates the cardinality law, verifies all nine parameter comparison regions, and tests 120 reproducibly drawn larger quadruples. The executable reported:

`VERIFY_OK exhaustive_quadruples=4096 verified_maws=45328 total_maw_lengths=257664 larger_quadruples=120 comparison_regions=9 offset_values=[1, 2, 4]`

The infinite part of the theorem is established by the run-transition proof in `RESULT.md`, not by finite enumeration. No independent audit or external certification is asserted. Reproduction requires only Python 3 with its standard library.
