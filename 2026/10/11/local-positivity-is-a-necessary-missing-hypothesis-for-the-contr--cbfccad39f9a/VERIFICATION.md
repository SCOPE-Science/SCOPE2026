---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Let C=[[2,1],[1,1]], C′=[[1,−1],[−1,2]], W_i=span(e_i), v_i=1 in R². Both controllers are positive definite, inverses with C*C′=I. Since P1+P2=I, the total quadratic controlled-form sum is exactly ||f||² for every f; this satisfies the displayed Definition 3.1 with A=B=1. Yet C*P1C′=[[2,−2],[1,−1]] is not selfadjoint and <A1e2,e2>=−1, so no positive square root exists and its squared-norm identity would demand a negative norm square. Conversely local positivity allows bounded positive roots and the coefficient norm equality. Exact rational 2×2 matrix arithmetic independently reproduced; no extrapolation.

## originality

PASS

The 2012 Khosravi–Musazadeh precursor and 2022 target explicitly introduce positivity as the condition for taking local positive square roots, so this condition itself is prior, not novel. The surviving contribution is a concrete positive-controller Parseval example proving the global Definition 3.1 fails to imply the condition and showing the later unqualified operator construction cannot cover the full defined class. No matched correction appeared in the bounded source/Resultary search, but the target’s conditional sentence substantially narrows any accusation of oversight.

## value

PASS

The issue affects whether the target’s central coefficientwise analysis/synthesis operator and associated boundedness statements are defined at all for every frame in its own global class. The obstruction is exact in dimension 2 with positive-definite controllers and Parseval bounds, not a contrived invalid type or numerical blemish; it identifies the precise additional hypothesis required for that operator model. No claim is made that the global definition or all conditional later results are false.

The dated certificate retains the supplied scientific assessment, sources and limitations.
