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

# Verification record

The proof is in `RESULT.md`, and the independent executable diagnostic is `verify.py` (Python 3 standard library only). Run `python verify.py` from the directory containing both files. All checks were executed from the version included in this record.

Observed program output:

```
Exact-rational pair identities: 12600 passed
Independent RK4 limiting-state checks: 67 passed
Exact Jacobian and seeded-winner probability checks: 4424 passed
```

The exact rational checks independently verify the key rank-invariance and logarithmic-ratio derivative formulas and the rank-one Jacobian structure. The winning-probability tests verify the three-strain exact fraction vector and symmetry in the all-equal case. The fourth-order Runge--Kutta checks range over 2 to 6 strains and include strict winner and tied-maximizer trajectories. These calculations are finite diagnostics: the arbitrary finite number of strains and all forward times are proved analytically using comparison, invariant ordering, asymptotic autonomous trapping, and an exponential-order-statistics computation. A separate human or independent scientific audit has not been performed.
