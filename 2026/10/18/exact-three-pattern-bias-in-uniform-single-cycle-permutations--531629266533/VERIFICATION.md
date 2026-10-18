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

The proof uses an explicit bijection from acyclic three-edge partial injections to cyclic permutations of contracted path components, followed by complete inclusion-exclusion on loops, two-cycles and three-cycles.

Run `python verify_cycles.py` (Python 3 standard library only). On the packaged code the checks passed: 36 exact cycle-mean cases for \(4\le n\le9\) and 540 exact acyclic-image-count cases for \(4\le n\le15\). The test enumerates permutations and image injections directly, independently of the inclusion-exclusion derivation. Optionally install `requirements.txt` and run `python derive_table.py` to reproduce all six inclusion-exclusion polynomial identities by symbolic simplification; this check also passed. The finite checks do not prove the unbounded-size theorem; the counting argument does.

The result is limited to first moments of non-wrapping consecutive triple patterns. No independent audit has been performed.
