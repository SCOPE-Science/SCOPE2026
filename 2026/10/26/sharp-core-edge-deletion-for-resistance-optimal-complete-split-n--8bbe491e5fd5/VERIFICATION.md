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
# Verification of the split-network conductance classification

This package contains an analytic proof in `RESULT.md` and a finite-instance executable `verify_split.py`. The executable is not an independent mathematical audit or a proof for all integers.

Execute from the package directory with Python 3 and the NumPy and SymPy libraries:

```text
python verify_split.py
```

The recorded output is in `verification_output.txt`. It reports `PASS` for 176 graph spectrum/budget configurations, 1,760 symmetric alternative allocations, 1,056 asymmetric sampled allocations, six exact characteristic-polynomial factorizations, and five exact rational matrix-inverse-trace identities. The random generator has a fixed seed, as written in the code. Numerical comparisons have finite tolerance; symbolic/rational checks are exact for the listed examples. Neither the numerical cases nor the finite symbolic cases establish the all-size inequality or uniqueness. Those are proved by the strict-convexity and Cauchy–Schwarz arguments in `RESULT.md`.

The available literature comparison distinguishes general convex resistance optimization from the graph-specific formula, and distinguishes fixed unit-weight Kirchhoff-index results from budgeted conductance minimization. Specialist coverage outside inspected sources cannot be excluded. Independent mathematical validation has not been performed.
