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

The proof uses an exact three-type Markov transition, a marked rare-vertex survival product, and an explicit fair-coin coupling. The finite exact checks reproduce only bounded instances; the all-size assertion is analytic.

Run with a standard Python 3 interpreter in the directory containing `checker.py`:

```sh
python checker.py
```

Observed result: `PASS 165 independent enumeration, exact DP, parity, mean, coupling-bound checks`. The implementation independently enumerates all edge permutations for four small labeled graphs and cross-checks a separate rational state-space recursion, then checks parity, distribution normalization, exact absolute-binomial moments and finite quantitative coupling inequalities. No simulation is used as a proof of a limit.

The independent audit has not been performed. Historical-priority risk remains for incomplete access to older full texts.
