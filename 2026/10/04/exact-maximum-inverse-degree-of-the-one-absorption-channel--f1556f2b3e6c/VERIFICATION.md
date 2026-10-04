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

The universal proof is the insertion-plus-genuine-split count in `RESULT.md`. The finite verifier is corroboration only.

`verify.py` uses two separate constructions of the parent relation: (1) enumerate each source word and run every allowed one-absorption operation forward; (2) start from a received word and enumerate all inverse adjacent-pair expansions plus terminal parents. It compares those parent sets, checks the decomposition into insertion supersequences and genuine splits, evaluates every received word over a bounded multi-parameter range, and verifies the saturated witness and the closed-form maximum.

The verification does not enumerate unbounded alphabets or lengths and therefore is not a certificate for the universal quantifiers without the written proof. It also does not assess multiple absorptions, forward-ball sizes, or optimal code cardinalities.
