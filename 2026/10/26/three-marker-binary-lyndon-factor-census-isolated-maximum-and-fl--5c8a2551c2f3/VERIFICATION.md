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

# Verification instructions

The exact all-length proof is in `RESULT.md`. The independent finite implementation `check.py` uses Python 3.10+ without third-party dependencies. Run:

```text
python3 check.py
```

The script directly compares Lyndon factors to all their nontrivial rotations on 5,985 words (all length-3 through length-20 binary words with exactly three ones), checks 23,751 nonnegative four-gap compositions through total zero mass 25, computes rational generating-series coefficients independently from its numerator and denominator, checks the isolated extremum, and evaluates the moments of the explicitly described ordered simplex by exact rational arithmetic.

Observed checks:

```text
PASS independent brute words: 5985
PASS gap compositions through m=25: 23751
PASS full rational series through m=25, isolation through m=25
PASS conditional continuous first and second moments: 19/24 37/45
```

These are reproducible finite checks. They are not an exhaustive verification of all lengths and do not establish historical priority. The infinite statements follow from the classification of Lyndon rotations, formal generating-series summation, exact case bounds, and simplex integration proved in `RESULT.md`. Independent mathematical audit has not been performed.
