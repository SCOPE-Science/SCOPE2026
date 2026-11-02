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

Place `verify_random.py` and `verify_second.py` in the same directory and execute:

```
python verify_random.py
python verify_second.py
```

Both scripts use only the Python standard library. The first checks a uniform all-size formula for the pairwise mean, the exact first-moment Bellman equations, and independent rational linear solutions. The second checks the explicit finite-sum second-moment potential, the exact second-moment Bellman equations, the all-size average second moment, and independent rational Gaussian elimination.

Observed outputs in the tested environment:

```
VERIFY_OK n=2..80 Bellman_states=85320 linear_states=220
VERIFY_SECOND_OK n=2..80 Bellman_states=85320 independent_states=220
```

Finite verification covers 85,320 statewise equations in each moment calculation and 220 statewise independent exact linear-system checks per moment for lengths 2 through 11. The all-integer proof uses the explicitly displayed Bellman solution and polynomial summation identities in `RESULT.md`; finite computations alone do not prove the infinite theorem. No independent external mathematical audit has been performed.
