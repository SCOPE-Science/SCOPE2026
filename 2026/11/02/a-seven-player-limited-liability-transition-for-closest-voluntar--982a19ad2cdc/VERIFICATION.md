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

# Exact reproducibility and limitations

Run `python check.py` from a directory containing this file and the included standalone `check.py`; it needs only Python 3 and no external dependencies. The checker recomputes the normalized statewise consent inequalities and weighted norm from the pair-synergy game. It tests the exact rational KKT table for all six sizes \(2\leq n\leq7\), the nonnegative-constrained seven-player solution at five rational values of the parameter \(L\), and the complete statewise Bellman inequalities for several cases. It explicitly enumerates all \(7!\) entry permutations in three seven-player scenarios and confirms their induced mean terminal allocations.

Observed execution output:

`VERIFY_OK cases=14 exact_inequalities=111 enumerated_paths=15120 direct_consent_states=1623`

Correctness for the continuum of \(a\) and \(b\) values follows from the explicitly displayed affine certificate, interval sign checks, and strict convexity in `RESULT.md`, not from finitely many checker runs. The result is bounded to \(n\leq7\). Scientific originality remains subject to publication-priority risk; no independent audit has been performed.
