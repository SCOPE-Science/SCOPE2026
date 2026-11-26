---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Integrating the radial weight gives squared monomial norm Γ(p)n!/Γ(p+n); the analytic and anti-analytic series share only the constant, so their sum minus 1 gives the stated kernel. For r<=ρ_p, strict Bernoulli gives pr<1. The argument ψ(δ)=arg(1+r exp(iδ)) is strictly concave for 0<δ<π and has tangent slope r/(1+r) at zero. Consequently θ+(p+1)ψ(π-θ) lies strictly between 0 and π and the real part decreases strictly along the upper half of each circle to its unique minimum (1+r)^(-p) at -r. This proves the inradius including uniqueness. In u=(1-t)^(-1) the analytic derivative of u^p does not vanish, giving regular real levels. On Re u=1/2, the derivative of cos(pφ)/cos^p(φ) alternates at jπ/(p-1). Odd-index minima are negative and even-index maxima cross the target exactly as in A_p and D_p, with strict boundary cutoffs at φ=π/2. The endpoint divergence sign is cos(pπ/2), or sin(pπ/2) at odd integer p; the start value is sublevel and a final increasing interval contributes one crossing exactly for positive divergence. Reflection and u=1/2 handle the lower side and -1. At contact u=exp(iπ/3), for B=Re u^p-1/2 the derivatives are B_x=p, B_y=0, B_yy=-p(p-1)/2 and B_p=-π√3/6. These give quadratic contact and the stated coefficient and direction of splitting. All checks are in the scalar product disk. The frozen numerical check and recorded output were inspected but not executed.

## originality

PASS

The kernel family and power/Möbius formulation are not new. A later-dated indexed result matches the exact radius and antipodal zero. The complete all-real-p unit-boundary staircase and exponent-driven tangency law are distinct from that later record's fixed-exponent radial nodal opening and were not established by the inspected earlier work.

## value

PASS

A first-zero radius answers when kernel zeros become possible; the boundary classification answers a different question about how many zeros reach the unit circle as the weight varies. It gives an exact count including endpoint and double-contact exceptions, and quantifies how crossings disappear. These are natural invariants of a standard weighted harmonic kernel, not numerical scans or a claim of full nodal topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
