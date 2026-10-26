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

# Reproduction instructions

Install Python 3.10+ with SymPy 1.14. In the directory containing the embedded code and data, run:

```
python -W ignore biquad3.py
python biquad3_independent.py
python biquad3_groupcheck.py
```

The first program exactly enumerates 41 projective orbits spanning all 9841 normalized equations, computes geometric Jacobian-ideal smoothness on four charts, writes `biquad3_results.json`, and obtains 14 smooth orbits/5184 equations and six branch pairs. The second independently loops over every normalized equation, computes both discriminants using modular-integer polynomial arithmetic, factors every squarefree quartic including its point at infinity, and obtains the same six counts and rational-point distribution; it writes `biquad3_independent.json`. The third builds all 1152 group actions by evaluation and interpolation and checks each smooth orbit's exact size and disjointness. Every one of these programs was executed successfully with the reference outputs included in this package. The table `REPRESENTATIVES.csv` provides independent traceable model identifiers and counts. The geometric argument establishes completeness beyond bounded extension-field experiments.

Scope of verification: exact computations and self-review mathematical reconstruction for this finite classification. An independent external audit has not been performed; published priority is not certified.
