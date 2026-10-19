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

# Exact certificate verification

Place `three_deletion_capacity_cert.json` and `verify_three_deletion_profile.py` in the same folder. Invoke `python3 verify_three_deletion_profile.py three_deletion_capacity_cert.json` under Python 3. The verifier uses only standard-library `itertools`, `json`, `sys`, and `fractions`.

It checks the full \(32\times256\) exact-deletion incidence matrix, confirms each received five-bit word has exactly \(93\) compatible eight-bit supersequences, validates six rational feasible duals and their exact objective coefficients, checks one explicit optimal code for each integer list size \(1\le L\le93\), and confirms the zero and saturation endpoints. The outcome is a completely finite, reproducible proof by explicit witnesses and rational inequalities, not an infinite mathematical claim inferred from experiments.

Expected output:

`VERIFY_OK n=8 deletions=3 dual_lines=6 explicit_witnesses=93; exact capacity for every integer list size L>=0`

Limits: the checker proves only the declared finite-block theorem and does not evaluate originality or other lengths/alphabet sizes. Independent scientific audit has not been performed.
