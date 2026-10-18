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

The independent-audit field above records **not performed**; it is not a certificate of outside validation.

The mathematical results have a complete derivation in `RESULT.md` and a standalone exact checker `verify.py` using Python's integer and rational arithmetic. Run it with `python3 verify.py`; its expected stdout is `VERIFY_OK 737 exact assertions`. Verified checks use exhaustive permutations at lengths four through eight, distinct, tied and nearly constant samples; separate exact degeneracy checks on ternary multisets up to length twelve; and exact support counts plus equal multiplicities using bit-separated integer sample values. The special test numbers make every unordered-edge product occupy a unique binary digit, so numerical support counts are exact and do not depend on floating point tolerances.

These finite checks are not exhaustive for unrestricted sample length. For the unrestricted theorem the proof relies on the complete edge-overlap classification, the deterministic all-pairs identity, and the cyclic-graph automorphism calculation. For sample values without algebraic independence, the generic atom-count claim must not be applied. No proof of an asymptotic joint distribution, independence across lags, or test power under alternatives is provided.
