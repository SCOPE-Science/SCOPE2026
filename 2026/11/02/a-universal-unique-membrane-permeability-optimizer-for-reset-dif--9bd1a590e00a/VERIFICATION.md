---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The Neumann stationary resolvent with arbitrary interior Borel reset μ has endpoint densities a,b; homogeneous zero-integral flux correction yields J=κ(b−a)/(1+2κg). For h=|a−b|/(a+b)∈(0,1), I=(s h/g)(1−u)atanh(hu) with u=(1+2κg)^−1. Its derivative F_h(u)=h(1−u)/(1−h²u²)−atanh(hu) decreases strictly from positive to negative; therefore unique global optimizer. Implicit differentiation gives strict monotone u_h(h); h→0,1 give sharp scaled band (0.385933275998...,0.5). If h=0, I≡0, no unique maximizer. Independent root/derivative and extreme-asymmetry tests passed.

## originality

PASS

Bressloff 2024 derives boundary stationary entropy and plots nonmonotonicity for selected reset sources, but inspected Sec IV and Fig 8 do not establish the unique global optimizer for every Borel source, strict asymmetry order or sharp universal dimensionless band. The Neumann resolvent is inherited. Broader scalar conductance optimization may implicitly cover the derivative argument.

## value

PASS

A complete sharp optimizer and source-independent band for physically defined membrane interfacial dissipation over every reset source law is a meaningful natural exact control invariant, beyond prior plotted nonmonotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
