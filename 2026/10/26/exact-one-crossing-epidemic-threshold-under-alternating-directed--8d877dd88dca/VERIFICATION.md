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

# Reproducibility and verified boundaries

Run the included file `verify.py` beside this document with `python3 verify.py`. It uses only the standard Python library and a fixed pseudorandom seed. The executed program returned:

```text
VERIFICATION_OK matrix_tests=1300 monotonic_cases=260
example_critical_half_period=0.8441526499425871
example_rho_tau_0.2=1.0902442189024490
example_rho_tau_1.0=0.9353925203135697
```

The 1,300 matrix tests independently compare the exact product of two \(2\times2\) exponentials with the trace, determinant and principal-multiplier formulas. The 260 monotonicity tests use unequal off-diagonal rates and a recovery rate in the strict crossing regime, bisect the unique sign change, and test the sign on both sides. Additional checks cover the two asymptotic regimes and the stated exact example. A separate high-precision evaluation of the sample threshold produced \(0.8441526499425879627717372195092473\ldots\).

The finite tests do not prove any assertion for all real parameters. The exact matrix identity, the strict concavity computation, the endpoint limits and the asymptotic inversions in `RESULT.md` supply those proofs. The assertion concerns linearized deterministic growth; stochastic outbreaks, unequal phase durations and nonlinear equality-case dynamics were not validated or claimed. Independent mathematical audit has not been performed.
