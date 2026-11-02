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

# Reproducible verification

The source \(\texttt{checker.py}\) runs under Python 3 with only the standard library. Execute \(\texttt{python3 checker.py}\) from the directory containing the script. The completed check produced:

```
PASS exact-rational checks: 46765
n=16, a=1/32, b=1/10: threshold=41/448, modes={0,5}
The continuum and large-n asymptotic parts are proved analytically, not by this finite test.
```

Checks include the exact detailed-balance identity, the stationary-ratio identity, modal-component count, the exact finite minimizer criterion, the parameterized strict-mode rule, and the rational witness. The chain is finite and irreducible because every susceptible has positive spontaneous infection and each infected has positive recovery rate. No finite computational sample can prove the infinitely parameterized theorem; that justification is the analytical argument in RESULT.md. Numerical decimal approximations are not used as mathematical certificates. The absence of an independent audit is an explicit verification limit.
