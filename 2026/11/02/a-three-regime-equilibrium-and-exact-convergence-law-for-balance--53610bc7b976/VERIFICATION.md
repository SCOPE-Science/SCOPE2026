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

The general proof is contained in RESULT.md. The finite checker is `verify.py`, run using Python 3 with only the standard library:

```bash
python verify.py
```

It enumerates all balanced two-color assignments on each \(K_{n,n}\) for \(2\le n\le7\), evaluates the same-color fraction over each player's closed neighborhood using exact rational arithmetic, tests every opposite-color pair swap, verifies every profitable move decreases the claimed length by one, and compares all equilibrium counts. Seven rational peak values on both sides of and at one half are used. The result is 32,928 state-peak cases and 215,664 profitable pair swaps, with all assertions passing.

The independent rational calculation of \(D_n\) for \(2\le n\le12\) is derived via the binomial telescoping identity proved in RESULT.md and does not establish the asymptotic without the accompanying Stirling argument. All numerical verification is finite; the all-parameter claim rests on the symbolic proof.
