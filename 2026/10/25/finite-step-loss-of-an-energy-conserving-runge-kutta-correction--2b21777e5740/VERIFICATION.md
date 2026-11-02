---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

On each active planar skew oscillator the modified Heun update is ((1-br_j)I+hω_j J)u_j with b=1/2−ε. Orthogonality yields gain (1-br_j)^2+r_j; conservation is V b²−2U b+U=0, real roots iff μ=V/U<=1, both b>=1/2. Substituting 1−2b=−b²μ gives gain 1+b²r_j(r_j−μ). If r*<=1 then μ<=r* at every state so roots always exist. If r*>1 every feasible step multiplies the maximal active frequency group by at least 1+δ, δ=r*(r*−1)/4>0, contradicting finite conserved total energy after more than floor(log(E_total/E*,0)/log(1+δ)) steps; no branch switching avoids this. For two active modes a<1<c the initial μ<=1 inequality is exactly p<=a(1−a)/[a(1−a)+c(c−1)]. Independent exact rational computation checked the example r=(1/4,9/4), initial E=(27,1), b=2/3, next E=(51/2,5/2), U1=12,V1=57/4, next discriminant=-108.

## originality

PASS

Best-of-knowledge PASS only for the all-step branch-uniform spectral dichotomy, sharp two-mode frontier and bounded failure horizon; original RF-RK method and one-step discriminant fully credited.

## value

PASS

The method can conserve a quadratic invariant exactly on a successful step yet be guaranteed to encounter a finite-step impossibility later. The sharp active-frequency threshold and all-branch failure bound expose a practical mathematical distinction between local feasibility and indefinite integrability. The exact two-mode boundary and rational one-successful-step counterexample are motivated by the real correction mechanism, not by an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
