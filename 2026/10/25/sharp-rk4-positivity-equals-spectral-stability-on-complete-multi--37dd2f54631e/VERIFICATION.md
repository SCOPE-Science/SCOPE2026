---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The projector splitting P0+(E-P0)+sum Q_i has Laplacian eigenvalues 0,N,N-n_i. All cross-part entries equal h phi(Nh)/24; same-part offdiagonal entries have positive h^2q/24 times a quadratic with negative discriminant -16(2p^2+5pq+5q^2). R(-x) has a strictly positive sum-of-squares form. phi is strictly decreasing, and N is attained, so both sign and real symmetric 2-norm contractivity have exactly the same sharp cutoff; h=0 and singleton parts handled. Fresh symbolic identities and 492 exact rational entries checked (six graphs, four scaled h). Finite examples do not prove all partitions; projector/inequality proof does.

## originality

PASS

Best-of-knowledge originality is the complete-multipartite endpoint positivity/contractivity equivalence with a universal scale, not the classical rho RK4 stability radius; primary full Horváth 2005 paper concerns general scheme positivity classes and invariant cones, not this exact projector computation.

## value

PASS

A sharp natural all-partition diffusion positivity classification, including unequal community sizes and exact decoupling at the spectral boundary, gives an exact network-integrator benchmark not implied by scalar stability alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
