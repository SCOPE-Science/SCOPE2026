---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Reconstructed all graph distances for s∈[1,3] and the zero-sum p-distance form. Splitting the distinguished endpoints, equal-part means and fluctuations produces the claimed 3x3 matrix M with m+n−4 positive orthogonal directions; independent symbolic determinant expansion verified det M=−F/((m−1)(n−1)). For 0<p≤1, 0≤h=s^p−1≤a=2^p and the lower 2x2 block is strictly positive; Schur complement makes negative type equivalent to F≤0. Combined with Li–Weston strict exponent inheritance, the endpoint F at p=1 and initial strict negativity imply the unique critical exponent; m=n=2 is checked separately via (2^p−1)^2=s^p and path equality. At intact p0, direct substitution gives F=h(−2a0²+2(m²−m+n²−n)h/T), yielding exact threshold H. Independent symbolic checks verified these identities and sampled (m,n,s)=(2,3,3),(2,8,3),(3,3,2),(5,5,3),(4,10,1.3). The implicit asymptotic and Euclidean rank arguments apply only in their stated regimes.

## originality

PASS

Li–Weston supply the strict negative-type interval, and Sánchez already computes the unperturbed complete-bipartite exponent. The perturbed singled-out edge metric is no longer uniformly edge-transitive, and neither inspected theorem provides the exact F and positive/negative response trichotomy, including the K2,8 reversal versus all balanced stretch improvements and inverse-cubic balance limit. Distance energy under edge deletion is a different matrix functional, not negative-type exponent. General distance-matrix methods are credited and could lead to equivalent reductions, so literature priority remains qualified.

## value

PASS

Supremal negative type/generalized roundness is a natural metric-embedding invariant. An intuitively local edge stretch has opposite qualitative impacts depending on graph balance, with exact cutoff and dimensions; the uniform biclique benchmark and balanced asymptotic give a structural sensitivity law, not a tiny arbitrary improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
