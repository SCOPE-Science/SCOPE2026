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

For every two-stage second-order explicit RK applied to constant L=[[0,−ω],[ω,−γ]], R=I+zA+(zA)²/2, z=γh, v=(ω/γ)². Energy defect B=I−R^T R has B11=vz³[4−(v+1)z]/4 and det B=vz⁴(vz−2)Φ_v(z)/16, Φ_v(z)=z[(vz−1)²+3]−8. Independently recomputed/factored both identities symbolically. Φ'=3(vz)²−4vz+4>0, unique positive root q. Comparing q, z0=4/(v+1) and 2/v via exact endpoint polynomial evaluations gives B positive definite strictly inside, positive semidefinite on, indefinite or negative diagonal beyond H(v)=q if 0<v<1 and 2/v if v>=1. Parameter s=vq yields q=8/[(s−1)²+3], v=s[(s−1)²+3]/8; unique global H max 8/3 at v=3/8. At optimum R=(1/9)[[−3,2sqrt6],[−2sqrt6,5]], eigenvalue mod1/3 but singular values 1,1/9 (checked independently), distinguishing spectral and norm thresholds. At (v,z)=(1,2), R=−I. All v,z>0 and all vectors, not an arbitrary dissipative system theorem.

## originality

PASS

Qualified PASS for this exact all-parameter Euclidean operator-norm frontier and unique optimal coupling of the canonical damped oscillator. Sun–Shu establish lack of general strong stability of explicit order-2 RK for all seminegative matrices; Achleitner et al. develop hypocoercivity criteria. Neither relevant inspected primary theorem directly provides the special exact H(v), H max or singular/spectral boundary contrast.

## value

PASS

Determines a sharp, natural numerical integrator one-step energy-safe timestep across physically standard two-component damped oscillators, with a unique global optimum and a striking eigenvalue/singular-value separation. It is a motivating finite-dimensional exact boundary, not merely a software stability check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
