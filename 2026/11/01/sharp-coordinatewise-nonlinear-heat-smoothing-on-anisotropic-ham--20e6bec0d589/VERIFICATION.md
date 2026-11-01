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

## Verification procedure

Execute `python verify_hamming_pheat.py` from the same directory as the standalone checker. It requires only the Python standard library.

The exact-arithmetic part rebuilds each tested Hamming product, computes the nonlinear vector field on independently enumerated vertices and checks the optimal directional active-edge inequality for rational data with exponents 2, 3 and 4; it also checks exact extremizer equalities for each coordinate. Further tests evaluate scalar extinction profiles for noninteger exponents and integrate sampled nonlinear flows by fourth-order Runge–Kutta.

Observed output:

```text
EXACT_DIRECTIONAL_DINI_INEQUALITIES_OK 2265
EXACT_SIMULTANEOUS_EXTREMIZERS_OK 54
SCALAR_FLOW_AND_EXTINCTION_DIAGNOSTICS_OK
NONLINEAR_FLOW_ENVELOPES_OK 80
ALL_HAMMING_PHEAT_TESTS_OK
```

The exact tests are finite, while the numerical tests have finite precision. Neither is an infinite proof. The general conclusion is justified by the scalar power inequality, the pairing of neighbors across coordinate fibers, the Dini-derivative comparison, and the explicit separable equality flow proved in `RESULT.md`. No independent audit has been performed.
