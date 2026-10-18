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

Half-orbit solutions of the two opposite rotations yield alternating semicircles of exact physical duration π; from incoming height −r the reset produces F(r)=4r(1−r), so half-return is F and published full section return is F². The invariant arcsine measure µ(dr)=dr/[π√(r(1−r))] follows from r=sin²(πu) and doubling u; the parity-flip constant-roof suspension with uniform age a∈[0,π) and parity is invariant/ergodic. Angular pushforward is uniform, giving spatial density [2π²r√(r(1−r))]^(−1). With H_m(r)=cos(2π m u), Fourier orthogonality yields E H_m(R0)H_n(F^k(R0))=δ_{m,2^k n}/2; random reset count floor((a+t)/π) gives exact convex combination at q=floor(t/π), α=t/π−q. Radius covariance is 1/8·max(1−t/π,0). For X=−R sinφ and φ(t)=φ(0)+t, E[R0 Rt] is 3/8 when no reset and 1/4 otherwise; direct integration over ages with N=0 yields correction [((π−t)cos t+sin t)]/(16π) for t≤π, beyond which only cos t/8 remains. Independent endpoint checks give Var(X)=3/16, Cov(X0,Xπ)=−1/8, Var(R)=1/8. Nondecay shows not mixing. Infinite-index proof is exact Fourier orthogonality, not finite quadrature.

## originality

PASS

Published Llibre–Santana model provides identical geometric return F² and chaotic dynamics, while discrete Chebyshev correlation and constant-roof nonmixing are classical. The new scoped result is the physical-plane density and exact continuum-time Cartesian correction plus full Chebyshev time-index law, not a claim to have invented logistic conjugacy or suspension nonmixing.

## value

PASS

Quantifies a real question left open by a chaotic planar hybrid example: natural stationary Cartesian observables are phase-locked and non-mixing even though a physically meaningful centered radius loses correlation after exactly one half flight. Exact invariant spatial density and an all-degree radial correlation hierarchy reveal the mechanism; neither a generic statement that logistic maps are chaotic nor a routine finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
