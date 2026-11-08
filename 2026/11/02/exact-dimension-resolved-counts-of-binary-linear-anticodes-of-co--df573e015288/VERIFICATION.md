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

For a binary (n−r)-space ker H, diameter ≤n−2 iff its full-rank parity-check columns satisfy s=Σh_i≠0 and h_i≠s for each i (exclude all-ones and all-one-except-i words). For fixed nonzero s, finite-character orthogonality yields F_j(n)=((2^j−1)^n−ε_{j,n})/2^j on a j-space containing s, ε=1 for n even, 2^j−1 for n odd. Möbius inversion over subspaces containing s with Gaussian coefficients and division by free GL(r,2) action proves the claimed exact B_{n,r} for all n≥2,2≤r≤n. r=3 simplifies to (7^n−6·3^n+5)/192 for even n, +11 for odd; fixed-r rarity follows from the largest exponential base and Gaussian asymptotics. Independently enumerated all distinct binary RREF generator row spaces for n=2..7 and tested their actual maximum codeword weights for every r. The zero subspace when r=n is included; n<r and exact-diameter counts are outside scope.

## originality

PASS

Best-of-knowledge statement-level comparison of actual published records and inspected accessible primary mathematics supports a distinct contribution. Evidence and residual priority risks follow; absence from search results is not proof of historical novelty. The forbidden maximum-weight words are exactly 1 and 1+e_i; this reformulates the anticode condition as a full-rank parity-check column constrained-sum problem. Previously classified optimal binary Hamming anticodes correspond to r=2, explicitly excluded as an independently novel slice. The r≥3 matrix-class count is not simply the maximum-dimension classification.

## value

PASS

Counts every dimension of a natural, near-full-diameter binary linear anticode class, rather than just optimal-dimension spaces or total asymptotic order. Exact codimension-three parity formula and sharp fixed-codimension probability supply usable finite parameters to coding theorists. Character orthogonality and Möbius inversion are standard, but their exact specialization answers a motivated previously non-tabulated classification question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
