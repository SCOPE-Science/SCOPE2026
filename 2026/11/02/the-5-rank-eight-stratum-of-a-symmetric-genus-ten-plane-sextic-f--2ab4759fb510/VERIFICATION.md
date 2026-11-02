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

Running `python3 verify_hasse_sextic.py` using the Python standard library yields:

```
SYMMETRIC_SEXTIC_CHAR5_HASSE_AND_STABLE_RANK_ALL_F25_SMOOTH_PARAMETERS_PASS
symbolic matrix: six A entries, three B entries, three D entries
A=-t(t-2)^2(t+2), B=2t(t+2), D=2t(t-2)^3
22 smooth F_25 parameters: 1 zero Hasse matrix and 21 stable rank-8 matrices
```

The verifier expands the fourth power of the six-term homogeneous sextic via the multinomial theorem in \(\mathbf F_5[t]\), constructs all one hundred Hasse-coefficient entries, and asserts the complete twelve-entry symbolic matrix. It then checks over every smooth member parametrized by \(\mathbf F_{25}\) that the one-step rank and five successive twisted-product ranks are zero at the Fermat parameter and eight elsewhere. The polynomial identities prove the symbolic matrix over an algebraic closure; the explicit invariant-block argument in RESULT.md proves the stable rank over all algebraically closed characteristic-five fields. Finite-field tests do not prove the infinite-field statement by themselves. Smoothness is proven separately by differentiation and homogeneous Euler identity, not by testing only small fields.

No independent audit, independent validation, formal-system certification, or external replication is claimed.
