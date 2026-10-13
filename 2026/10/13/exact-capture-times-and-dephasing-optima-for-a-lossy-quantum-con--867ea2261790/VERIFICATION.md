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

# Verification

With NumPy and SciPy installed, run `python verify.py` from the same directory. The standalone program constructs the Hamiltonian and each matrix-unit image of the full trace-decreasing Lindblad generator; it does **not** use the five-real-variable equations in the proof. It obtains the survival integral by solving the full complex matrix Liouvillian. The completed reference run returned:

```
VERIFY_OK lindblad_inverse_cases=40 optimization_checks=8 max_abs_error=7.11e-14 max_real_eigenvalue=-0.0297
```

Twenty parameter sets cover leaf counts 2, 3, 4, 5 and 7, each checked at two distinct initial leaf positions. Randomized but deterministically seeded parameters include both signs of hub–leaf hopping, positive/negative interleaf hopping, hub-detuning and positive noise/sink strengths. The program independently checks full-Liouvillian exponential stability for the sampled cases, resonant and detuned noise optima for eight configurations, and the joint-rate optimum for four leaf counts. The exact formula, normalization, positivity argument and infinite-size quantifiers are proved symbolically in `RESULT.md`; **finite experiments do not establish them**. The inaccessible complete text of a closely related star decoherence source remains a priority risk.
