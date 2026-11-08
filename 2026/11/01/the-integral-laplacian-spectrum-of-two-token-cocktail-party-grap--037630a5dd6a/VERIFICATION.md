---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For every m≥2, T_m=F_2(K_(2,...,2)) has N=m(2m−1) unordered two-token states. Let q=binom(m,2). Its unnormalized Laplacian polynomial is t(t−2m)^(m−1)(t−(2m−2))^m(t−(4m−4))^(m(m−2))(t−(4m−6))^q(t−(4m−2))^q, combining coincident roots (notably m=2). The identity L(T_m)=L(J(2m,2))−L(F_2(mK_2)) is valid edgewise. In the matching-token complement each cross-pair block is C4, with sign-character eigenspaces E0,E2,E4 of dimensions m+q, 2q, q. Using the unsigned configuration incidence matrix X, L(J)=(4m−2)I−X^T X and XX^T=(2m−2)I+11^T; X ranks m,m,0 on these invariant eigenspaces, yielding every eigenvalue/multiplicity and a simple zero. Matrix tree theorem then yields τ(T_m)=product positive eigenvalues / N; degrees give edge count 4m(m−1)^2. Independently built actual Laplacian matrices m=2..7 and recovered exact eigenvalue histograms, plus exact spanning-tree determinants m=2,3,4; all-m proof is linear-algebraic.

## originality

PASS

Token/symmetric-square graphs and the complement-Laplacian identity are established; algebraic connectivity for two-token complete multipartite graphs is also known. The assessment concerns the entire six-branch spectrum with exact multiplicities and its spanning-tree product, not the known gap or complement relation. Comparison of the full Dalfó complement theorem and related primary abstracts did not locate this exact matching-complement joint decomposition. An unstated specialization of general association-scheme or SRG symmetric-square theory remains a meaningful priority risk.

## value

PASS

The full integer spectrum of nonregular collision-free two-token configurations on a canonical matching-deleted complete graph is a natural spectral invariant. The explicit joint eigenspace pairing and exact spanning-tree complexity refine the previously known complement identity and scalar spectral gap, permitting study of dynamics and combinatorial complexity for every m; a meaningful full family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
