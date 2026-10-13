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

# Verification of the ternary deletion-covering equality

Execute `python3 verify.py` from the directory containing the standalone verifier. The expected final marker is `VERIFY_OK`.

The verifier defines the deletion shadow as a **set**, thereby deduplicating identical subsequences obtained by deleting different positions. It expands all six symbol permutations and coordinate reversal; confirms the ten listed four-word orbits are disjoint and cover 81 targets; checks orbit sizes, integer weights and total numerator 468; computes the full shadow-weight sum of all 243 five-word centers, finding a maximum of 23 with the exact score histogram `{10: 3, 15: 12, 18: 12, 19: 36, 20: 18, 21: 12, 22: 24, 23: 126}`; checks that the five-word action has 25 orbits; and expands the seven prototype words by cyclic alphabet translation to 21 distinct centers whose shadows cover all 81 targets **exactly once**, with target multiplicity checked directly. It checks the integer inequality `ceil(468/23)=21`.

This is a finite, exhaustive exact calculation embedded with its mathematical proof. There is no dependence on optimization software, internet resources or unpublished state. It establishes no infinite-family bound, and it is not an independent scientific audit.
