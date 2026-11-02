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

# Verification and reproducibility

To check the exact bounded census, run `python3 verify.py triples.csv`. To regenerate it from the substitution, run `python3 census.py reproduced.csv`; the regenerated CSV should be bytewise identical to `triples.csv`.

The primary computation checks all first-shift/second-shift pairs and computes precisely the intersection of allowed third shifts over all length-1706 factors. A separate checker constructs the length-1706 language in two ways: adjacent level-14 substitution supertiles and a direct level-18 prefix. Those sets agree and have 3413 members. The checker independently recomputes and sorts all valid triples from the direct prefix, compares the result to the complete 145217-row table, verifies the CSV SHA-256, and checks the ten length cutoffs. The observed return string was `VERIFY_OK; factor_set=3413; pseudoperiod_triples=145217; two_independent_factor_enumerations; independent mismatch_census; CSV_hash_OK`.

The finite-to-infinite implication is supplied by the adjacent-supertile factor lemma in `RESULT.md`, not by an assumption that a sufficiently long prefix is automatically complete. The proof covers only positive strictly increasing triples whose largest shift is at most 1705. Independent audit is not performed.
