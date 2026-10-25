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

# Verification of the attractor criterion

Execute `python3 verify.py` using Python 3 standard library only. The executable constructs factor-occurrence unions from raw strings, tests all supplied position sets directly, checks the four uniqueness certificates, and independently finds the smallest cardinality by enumerating all subsets through size four when \(1\le b,c,e\le6\).

Observed output:

`VERIFY_OK exact_minima=216 complete_factor_witnesses=1728 random_large=160 fixed_length_counts=5..100`

The full factor-cover test covers 1,728 parameter triples with run lengths at most 12, plus 160 deterministic samples with parameters at most 60. Length-class coefficients are checked by direct positive-composition counting for every integer \(5\le n\le100\). The proof in RESULT.md handles all positive parameters without relying on finite observations. The checker does not establish worldwide novelty or constitute an independent audit.
