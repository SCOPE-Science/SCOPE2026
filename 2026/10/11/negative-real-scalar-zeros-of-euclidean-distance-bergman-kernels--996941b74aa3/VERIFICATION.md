---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For complex ball B^d, d≥2 and integer t≥0 with exactly weight (1−||z||)^t dV, unit-sphere monomial integral and radial beta B(2k+2d,t+1) give normalized coefficients (d+(t+1)/2)_k(d+(t+2)/2)_k/[(d+1/2)_k k!]. Euler transforms 2F1 into (1−s)^(−d−t−1)Q(s), Q=2F1(−m,−floor(t/2)−1/2;d+1/2;s), m=ceil(t/2). Pfaff and Jacobi produce (1−s)^m P_m^(d−1/2,(-1)^t/2)((1+s)/(1−s)) m!/(d+1/2)_m. Both Jacobi parameters >−1 ensure exactly m simple real x∈(−1,1), mapping to simple negative scalar s. For F(u)=Q(u−1), all roots are real; Descartes sign changes of its Taylor coefficients at u=0 equal the exact number positive roots, correctly excluding a boundary root s=−1. |s|<1 is exactly the attainable ball inner-product disk. Independent rational symbolic check reconstructed Q_{2,3}, Q_{3,3}, Q_{3,4} and Jacobi identity for six (d,t) pairs, including t=0 and t=8; finite checks supplement all-integer proof.

## originality

PASS

The exact several-variable Euclidean-distance weight numerator, complete negative-simple-root geometry, and exact boundary-aware count were not implied by surveyed primary work. The 2026 Marinescu–Xing manuscript uses the same δ^t weight but abstract/theorems accessible here concern parameter regularity, not scalar zero geometry; full text inaccessible is a specific residual risk, not independent novelty proof.

## value

PASS

The Lu Qi-Keng zero problem is a natural invariant for Euclidean boundary-distance weighted Bergman kernels. The exact all-d≥2, all-integer-exponent scalar root geometry and finite rational-arithmetic count resolve an actual parametric classification, including non-monotone dimension-dependent zero-free examples (d,t)=(2,3),(3,3),(3,4). Neither isolated trial examples nor a known disk table supplies the classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
