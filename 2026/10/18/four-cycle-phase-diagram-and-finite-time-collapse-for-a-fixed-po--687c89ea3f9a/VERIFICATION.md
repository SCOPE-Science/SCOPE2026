---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The branch ranges lie strictly on opposite sides of p, including F(p)=1, so every periodic orbit has even least period. On the left, the normalized two-step map is H(t)=dT(cT(t)) by tent symmetry. For K<1, H(t)≤Kt forces even-phase convergence to 0 and continuity of the left-branch formula gives the other phase 1. For K=1, H is the identity on [0,u] and its image lies in that interval (bounded by 1/2 if c≤1/2 and by d=1/(4c) otherwise); hence one return suffices and any right starting state needs at most one preliminary step. For K>1 and c≤1/2, H consists of Kt and K(1−t). If c>1/2, write r=1/(4c). The signs of H(t)−t at t=0,r,1/2,1−r,1 are respectively zero, positive, the sign of d−A, the sign of d−B, and negative. Affine interpolation gives exactly the stated roots and makes the two endpoint identifications explicit. In particular A−B=(2c−1)^2/(4c(1−c))>0. The return map expands distance to each isolated fixed point by K in a sufficiently small neighborhood, also across an adjacent turning point, and the right-hand representative is interior to its branch domain. Both exact parameter examples satisfy the strict assumptions and reproduce the stated roots or fixed interval.

## originality

PASS

The underlying fixed-point-free map is prior and explicitly credited. The distinct finding supported by the accessible comparisons is the full tent-seed two-cycle and critical-collapse classification in the strict alternating region. The original 2024 full text could not be inspected; the decision does not assert that it omits the classification.

## value

PASS

The strict alternating box is structurally singled out by branch ranges, not an arbitrary parameter slice. The classification identifies global attraction, a critical retraction onto a continuum in uniformly bounded time, and a region of four simultaneous repelling two-cycles in a published chaotic-map family. It distinguishes parameter regimes that no fixed-point calculation for F alone can see and gives explicit testable boundary values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
