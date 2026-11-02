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

Run `python checker.py` using Python 3 with SymPy and mpmath installed. The code checks four symbolic polynomial identities, independently integrates the complete prefix/block/tail intensity profiles for 16 expected-spectrum comparisons, checks three duration-root brackets, and certifies one exact rational phase witness. It was executed successfully on the saved source. The proof, not the finite test suite, supplies the infinite-parameter result.

No external independent mathematical audit or empirical genetic-data validation was performed. The direct coalescent calculation requires the specified neutral three-copy model and finite expected branch lengths.
