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

Normal form q1=gamma e1+sqrt(1−gamma²)e_{s+1}, q2=e2, q3 normal to plane. Center/scale B=(A−cI)/d, symmetric contraction; then H=cI+d[[a−t nu,b−t v],[b,k]], t=sqrt(1−gamma²)/gamma. For conjugate nonreal eigenvalues, (Im λ/d)²=t b v−b²−(a−k−t nu)²/4<=t b v−b². Bq2 contraction implies b²+v²<=1. Largest eigenvalue of [[−1,t/2],[t/2,0]] equals (sqrt(1+t²)−1)/2=(gamma^{-1}−1)/2. Orthogonal rank-two B=q2 h^T+h q2^T with h=b*q1+v*q3, b=sqrt((1−gamma)/2),v=sqrt((1+gamma)/2) attains bound with eigenvalues ±1. At gamma=1 ordinary orthogonal compression symmetric. Exact rational witness A [[6,−1,0],[−1,6,2],[0,2,6]], gamma=3/5 gives H [[6,−5/3],[1,6]] and sharp Im=sqrt(5/3). Independently verified rational discriminant and extremal numerical checks.

## originality

PASS

The phenomenon that symmetric input can produce complex sketched Ritz values is explicitly prior (Nakatsukasa–Tropp 2024 §6.8, Liu–Liu 2026). Earlier E-optimal three-state construction attains the same profile only as a lower-bound example, not a universal upper bound. Reviewed claim is sharp maximum over all bounded SPD operators/trial planes; no inspected prior covers it. Original 2026 Liu–Liu full text unavailable, Oxford VPN disconnected; residual overlap risk.

## value

PASS

A real symmetric eigenproblem can yield nonreal outputs under sketching; the exact worst-case imaginary height in terms of two observable parameters (spectral diameter and missing-coordinate principal angle) is a sharp diagnostic/design limit, with attained examples for every nonzero angle. It resolves a real stability question beyond the known qualitative observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
