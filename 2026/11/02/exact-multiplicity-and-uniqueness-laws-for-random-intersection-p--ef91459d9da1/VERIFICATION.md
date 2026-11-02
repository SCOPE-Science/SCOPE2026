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

# Reproducibility and verification

The analytical proof and all quantifiers are in `RESULT.md`. Two standalone scripts require Python 3 without third-party packages:

```
python3 verify_counts.py
python3 verify_local.py
```

`verify_counts.py` checks every perfect allocation of every priority profile for \((n,t)=(2,2),(3,2),(2,3)\), cross-checking each number of stable assignments against a separately structured recursive maximal-choice algorithm. For three students and two independent priority lists at each school, it processes exactly \(46{,}656\) profiles and obtains multiplicities \(7776,14256,11664,9072,2592,1296\) for stable-assignment counts one through six. It verifies the mean \(11/4\), unique-outcome probability \(1/6\), and variance \(227/144\) with exact fractions. `verify_local.py` independently enumerates random partial-order maxima for sizes up to four and one to three intersected criteria where within the workload cap. It checks the local closed-form mean and unique-maximum probability in exact rational arithmetic.

Computations use finite exhaustive spaces for the stated finite tests only. They do not enumerate all larger markets or certify the universal theorem independently. The universal claims follow from the written two-way sequential criterion, probabilistic factorization, exact integral, and asymptotic calculation. No independent scientific audit is claimed.
