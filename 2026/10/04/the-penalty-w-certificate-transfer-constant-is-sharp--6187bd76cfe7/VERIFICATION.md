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

The proof reduces the certificate definition to two affine minimizations on \( [0,2\iota] \). At the base penalty, the model slope is \(\rho/2\), giving normalized residual \(\rho/2\); the feasibility inequality is attained with equality. At the larger penalty, the model slope is \(\widetilde\rho-\rho/2\), so any transferred tolerance must be at least that value. This exceeds the feasibility lower bound \(\widetilde\rho/2\) whenever \(\widetilde\rho>\rho\). Substitution into Proposition 4.3 gives exactly the same value.

`verify.py` repeats these calculations with exact rational arithmetic for several positive parameter choices and checks equality with the proposition's transfer formula. The verification is finite algebraic replay of the displayed proof; it is not an independent audit and does not establish literature uniqueness.
