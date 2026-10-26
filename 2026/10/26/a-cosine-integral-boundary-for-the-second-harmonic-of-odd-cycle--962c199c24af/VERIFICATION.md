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

## Checks performed

The portable `checker.py` recomputes character sums and the exact \(s=0,1,2\) Fourier identities for ten distinct odd cycle orders. It brackets the unique frequency-two root and checks a finite positive eigenvalue witness above the root. Scientific assertions for every odd order are supported by the sign-variation and Riemann-sum arguments in `RESULT.md`, not by these samples.

The cosine-integral limiting constant was independently evaluated to high precision and checked against the scaled root estimates; finite data cannot certify a limit. No formal or independent mathematical audit has been performed.
