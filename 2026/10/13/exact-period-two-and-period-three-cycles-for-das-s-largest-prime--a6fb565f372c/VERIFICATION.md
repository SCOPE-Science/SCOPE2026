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

The symbolic proof was checked case by case against the definition of the map. Exact periods two and three exhaust only the patterns described in RESULT.md; no finite search is used to promote a bounded observation to an infinite theorem.

A standalone regression checker enumerates all parameters \(1\le k\le500\) and starting values \(2\le n\le5000\). It canonicalizes cycles of lengths two and three and compares the observed cycles to the two closed-form criteria. The packaged run returns:

`VERIFY_OK k_max=500 n_max=5000 period2_period3_mismatches=0`

The computation does not test or claim anything about cycles of length at least four. Its finite range is a consistency check only; the unbounded result rests on the proof.
