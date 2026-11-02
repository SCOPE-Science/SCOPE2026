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

# Reproducibility notes

Run `python3 verify.py` with the Python 3 standard library. The code constructs maximal elements directly from all consecutive-\(321\)-avoiding permutations through length seven, and separately enumerates all admissible endpoint/interior block compositions. It also computes coefficients using the displayed binomial formulas and the weighted recurrence; those three descriptions match through length 27. The direct permutation-poset calculation matches through length seven. The unimodality predicate and the explicitly proved strict-valley coefficients were checked by finite arithmetic through length 160 (odd valley identities also through length 161).

Expected summary:

```
BRUTE_PERMUTATION_OK n=2..7
THREE_METHOD_COEFFICIENTS_OK n=2..27
UNIMODALITY_WINDOW_OK n=2..160
ANALYTIC_VALLEY_IDENTITIES_OK odd_n=11..161 even_n=14..160
VERIFY_OK
```

These are bounded verification checks, not exhaustive independent verification of all integers. The infinite statement is obtained from the published block characterization and explicit coefficient inequalities in the proof. Independent mathematical audit is not yet performed.
