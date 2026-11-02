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

The self-contained program `verify_linear_extensions_vc.py` was run against its accompanying `verification_output.txt`; it enumerated all labeled strict posets through five elements and all unordered-pair support sets. For each, it compared literal permutation-based shattering to the contracted-comparability digraph criterion, checked the exact dimension, and checked the Cayley-weighted enumeration of all maximum supports. The output is supplied verbatim. This finite computation does not certify the unrestricted theorem, for which the proof in `RESULT.md` is the evidence. There has been no independent scientific audit.
