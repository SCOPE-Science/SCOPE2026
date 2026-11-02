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

The source file `verify_binary_block_sas.py` is self-contained (Python standard library only). Run `python3 verify_binary_block_sas.py` from its containing directory. It enumerates all binary targets shorter than the claimed shortest absent length to verify universality, then directly tests every word at that shortest length against the concrete host. Separately it generates every word predicted by the state-path classification. The asserted exact equality between the two sets is checked for all 216 parameter combinations with \(1\le a,b,m\le6\).

Observed output:

`VERIFY_OK instances=216 literal_targets=139272 classified_shortest_absent=985`

All tested cases passed. The result for unrestricted integer parameters is proved in `RESULT.md`; finite tests alone would be inadequate as an all-parameter certificate.

Self-review passed; independent audit was not performed.
