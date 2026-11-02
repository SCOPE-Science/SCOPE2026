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

# Verification details

The analytical proof in `RESULT.md` applies to the infinite family. The two included scripts independently provide finite tests, not independent mathematical audit.

The direct pair-spectrum verifier `verify/cycle_rank3.py` was run using Python 3. It checked radii 1 through 15, each stable threshold \(4r+3\), fifty consecutive lengths from each threshold, and the opposite-side boundary. Recorded output is `verify/cycle_rank3.out`, concluding `ALL_CHECKS_PASS`.

The full two-sided three-round game verifier `verify/ef3_independent.py` independently computed complete game states, checked that all 45 pairs among ten class representatives are distinguishable, and checked stable-tail equivalences at several pairs of lengths/radii. Recorded output is `verify/ef3_independent.out`, concluding `INDEPENDENT_EF3_CHECK_PASS`. It invokes neither the other program nor a pair-spectrum reduction.

Both scripts rely only on the Python standard library. Run from the directory containing `RESULT.md`:

```
python3 verify/cycle_rank3.py
python3 verify/ef3_independent.py
```

A finite sample is not a proof of stability for all radii/lengths; that follows from the pair-spectrum theorem, geometric arc analysis, and complete symbolic case table in `RESULT.md`. Historical-priority checking is incomplete. No independent external audit or certification has been performed.
