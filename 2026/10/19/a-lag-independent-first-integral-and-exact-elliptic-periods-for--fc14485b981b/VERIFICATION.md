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

Execute `python3 verify.py` with Python 3 standard library. The checker recomputes the source phase velocity, half-pair coordinate transformation and derivative of the invariant on randomized nonsingular configurations. It computes the predicted period using the arithmetic-geometric mean and integrates 24 exact four-oscillator initial-value problems with fourth-order Runge–Kutta over 4000 steps each.

Observed program output:

```
PASS: 548 first-integral derivative tests, 400 reduction tests, 24 full-phase period tests; maximum return error 3.88e-11.
PASS: strict sampled period monotonicity and both endpoint asymptotics.
```

The sample tests assess algebraic implementation and finite numerical agreement; they do not prove a first integral for every real parameter or periodicity of unexamined orbits. Those claims are proved in `RESULT.md` using exact differential identities, compact regular level sets, and elliptic quadrature. No independent audit has yet been performed.
