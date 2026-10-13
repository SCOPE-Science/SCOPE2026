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

# Reproducibility and mathematical limits

Run `python3 verify.py` in the directory containing that standalone script. The exact captured stdout is provided in `verification_output.txt`.

The verifier constructs graph edge sets from cyclic distances, separately counts triangles by exhaustive three-vertex enumeration, tests both derived triangle formulae and their difference, and directly checks the positive-case multiplication isomorphisms. It covers 48 degree-compatible parameter profiles and another 3,800 triples at small orders, including complete-cycle boundary cases. These tests do not exhaust the unbounded integers; the complete proof is the cyclic-gap argument and final modular multiplier in `RESULT.md`.

The universal classification is established mathematically under the stated assumptions. The literature comparison is bounded by obtainable primary texts. An independent external audit has not been performed, and no outside reviewer or publication certification is asserted.
