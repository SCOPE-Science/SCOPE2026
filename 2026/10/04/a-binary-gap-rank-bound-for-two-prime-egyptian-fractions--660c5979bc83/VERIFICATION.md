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

The mathematical proof is self-contained in `RESULT.md`. The accompanying script `verify_rank_bound.py` uses only Python's standard library and exact arithmetic. It performs four finite checks: exhaustive small dyadic-gap cases, the discrete optimization inequality over many odd integers, comparison with the full published Table 4 data, and exact replay of the Fermat-support identity for the five known Fermat primes.

These finite checks are diagnostic. They do not establish the universal theorem; the universal statement rests on the binary-popcount lemma and the subsequent integer inequalities in `RESULT.md`. No independent audit has been performed.
