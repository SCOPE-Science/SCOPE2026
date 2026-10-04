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

Claim checked: at the singular alternating weight \(x=-1\), the cubic three-term recurrence has the explicit finite endpoint identity stated in `RESULT.md`, with auxiliary finite difference \(s_{n+1}-s_n=2P(n)\).

The universal proof was reconstructed directly from the recurrence. Its critical algebraic checks are:

1. Expanding the displayed polynomial gives \(s_{n+1}-s_n=2P(n)\) identically.
2. After substituting the three-term recurrence into \(H_{n+1}-H_n\), the mixed coefficient is \(cn^r(-2P(n)+s_{n+1}-s_n)\), hence zero.
3. The remaining coefficient is exactly \(W_n\), including the signs from the denominator \((-c)^n\).
4. The initial increment is checked separately using \(u_1=P(0)u_0\), so no undefined \(u_{-1}\) enters when \(r\ge1\).

`verify.py` uses only exact rational arithmetic. It checks six independent coefficient choices, both signs of \(c\), exponents \(r=1,2,3,4\), and every \(N\) from \(1\) through \(12\). The replay result is stored verbatim in `verification_output.txt`.

The finite replay is corroborative only. It does not certify the infinite family; the displayed telescoping derivation supplies the proof for all allowed parameters and all \(N\ge1\).
