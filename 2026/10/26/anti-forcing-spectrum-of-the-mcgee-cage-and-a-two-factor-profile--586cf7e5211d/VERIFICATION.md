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

# Reproducibility

`verify_exact.py` is a pure-Python complete enumeration, not random sampling. It constructs all 36 McGee edges, obtains all 60 matchings by branching on each free neighbor of the smallest uncovered vertex, and for each matching enumerates all potential deletion sets of increasing cardinality until the first successful size. Each deleted set is successful exactly when it hits every one of the other 59 perfect matchings. That criterion is equivalent to unique survivability.

`verify_independent.py` uses a separate hardcoded edge list, a differently organized matching recursion, SciPy mixed-integer linear programming for 60 set-cover problems, and direct tests of each stored optimal deletion witness. It additionally uses NetworkX to enumerate all graph automorphisms and their induced matching orbits. Thus the integer-programming solver confirms the same optimum, while the complete exhaustive lower-bound check remains supplied by `verify_exact.py`.

Run these commands in a directory containing `certificate.json` and both scripts:

```sh
python verify_exact.py certificate.json
python verify_independent.py certificate.json
```

Requirements: Python 3.10+ for both; additionally `networkx`, `numpy`, `scipy` for the independent check. Executed standard outputs are preserved in `verify_exact.out` and `verify_independent.out`; their only evidentiary role is to record completed runs. The programs and certificate are the reproducible source.

Scope: finite exact graph specified in the result, not a universal anti-forcing bound. Indexed-literature overlap checks leave an explicit publication-priority risk. The independent-audit channel is unperformed.
