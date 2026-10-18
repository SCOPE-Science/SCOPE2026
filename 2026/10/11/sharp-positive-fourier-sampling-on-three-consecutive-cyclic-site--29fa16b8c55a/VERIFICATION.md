---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The Parseval Gram condition on three consecutive spatial sites is exactly ∑w=1, ∑wz=0 and ∑wz²=0. Three positive frequencies must form a 3×3 unitary Vandermonde matrix, hence equal 1/3 weights on a coset of the cubic subgroup, existing only if 3|N. If four distinct frequencies existed for gcd(N,6)=1, a missing quadratic coefficient in the vanishing polynomial for the generalized 4×4 Vandermonde rows would force ∑_{i<j} z_i z_j=0, a length-six vanishing sum of N-th roots. Read the original Lam–Leung Theorem 5.2 in full, verifying allowed lengths are additive semigroup of prime divisors, so 6 is excluded when gcd(N,6)=1. For even 3∤N, the explicit 4-node construction k=⌊N/4⌋ and positive symmetric weights satisfies first and second moments exactly. For gcd(N,6)=1, Carathéodory applied to origin in convex hull of 4-real-dimensional two-moment embedding yields ≤5 nodes; the lower bound forces 5. Vandermonde/Lagrange coefficient extraction gives unique real weights on each fixed 5-node support and an exact strict-positivity test. Independently checked constructed even rules and small cases, but finite numerical examples are not the all-N proof.

## originality

PASS

Best-of-knowledge new full cardinality trichotomy and exact five-node positivity criterion for consecutive cyclic triple. Vanishing-sum semigroup, Carathéodory, and frame theory are acknowledged inputs, but no inspected source derives this precise combined sharp statement. An equivalent classical Szegő/circle quadrature theorem could be indexed under other terminology.

## value

PASS

Exactly determining the minimum positive weighted Fourier sampling cardinality on a natural consecutive triple of cyclic sites is a useful discrete harmonic-analysis/finite tight-frame invariant. The arithmetic trichotomy is not a generic dimension count (gcd-dependent 3/4/5), and the positive interpolation formula classifies feasible supports by an exact test. It contrasts with the larger unweighted prime-order sample requirement and supplies constructive sparse quadrature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
