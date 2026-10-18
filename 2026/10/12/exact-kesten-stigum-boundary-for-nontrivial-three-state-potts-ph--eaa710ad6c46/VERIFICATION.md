---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read actual Git RESULT.md blob 4f0df2764d9f56f6a059f7f64d8cfa1230839af0 and verification/verify.py. Reversible positive t=z^1/4 parametrization away from t=1 yields θ(t)=(t⁴+t³+t²+t+2)/(t(t²+t+1)); the three-state Markov transition matrix splits into antisymmetric spin-2/3 mode and a lumped 2-state mode. Independent Sympy characteristic polynomial and exact integer identities confirm λa=1/((t+1)(t²+1)) and λb=t³(t+2)/((t+1)(t²+1)(t⁴+2)); their ordering changes at t=1. For t>1, 2λb<1 follows from a polynomial in s=t−1 with positive coefficients (6,14,36,59,54,28,8,1); for 0<t<1, 2λa>1 iff cubic t³+t²+t−1<0. θ′(t)<0 on 0<t<1 and at unique root ρ, θ=2(1+ρ). Hence KS sufficient non-extremality criterion 4λ*²>1 holds exactly when t<ρ; no converse/reconstruction conclusion is drawn.

## originality

PASS

Best-of-knowledge PASS: the q=3, k=4 rational t=z^(1/4) parameterization and exact branch-specific second-eigenvalue inequality give a complete algebraic threshold not present in inspected foundational k=2 theorem, later k=3 paper or 2021 survey. The result deliberately restricts itself to what KS certifies, not the true extremality threshold.

## value

PASS

Provides exact complete all-branch Kesten–Stigum certification on q=3, order-four tree, the first order past explicitly studied three-state k=3; resolves a concrete algebraic threshold using a natural boundary-law parametrization. Separating sufficient non-extremality from true extremality is scientifically necessary, and the exact threshold can guide subsequent reconstruction analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
