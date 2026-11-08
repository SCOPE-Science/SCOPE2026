---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Given the shared Riccati x-flow and polynomial-affine y-flow (L>=1,N>=L+2), x_i-x_j satisfies (B+C(x_i+x_j))(x_i-x_j); barycentric weights over |S|=L+2 obey dlogw_i/dt=-(L+1)B-C(Lx_i+sum_S x). Because the (L+1)-st divided difference of every polynomial of degree <=L vanishes, dΔ_S/dt=(D-(L+1)B-C sum_S x)Δ_S. The difference law cancels in all K_i, and the Δ ratio multiplier cancels in the normalized J_i. Conversely matching 3 x coordinates determines a pole-free positive-denominator Möbius transform, matching x order and all K forces all x; sign(Δ0) fixes positive lambda, and interpolating Q at L+1 nodes with Δ constraints reconstructs all y. The rational coordinate inverse proves independence of N-3 plus N-L-2 integrals = 2N-L-5. I independently checked exact rational Möbius/divided-difference covariance and differential-identity examples without relying on saved verifier logs. This covers finite regular flow portions only, not singular strata.

## originality

PASS

Tokunaga 2026 already supplies the I20^(L) normal form and finite group action; general Lie–Scheffers existence of invariants is also prior. This theorem supplies explicit barycentric normalized invariants and actual real orbit separation on the stated generic region; novelty does not include discovery of the Lie family.

## value

PASS

An explicit complete set of first integrals and real orbit reconstruction for an entire natural imprimitive Lie-system network family is mathematically useful. Higher divided differences supply precisely the N-L-2 missing fiber invariants that classical Riccati cross-ratios cannot detect, permitting full generic dimension reduction without solving the residual L+5 group equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
