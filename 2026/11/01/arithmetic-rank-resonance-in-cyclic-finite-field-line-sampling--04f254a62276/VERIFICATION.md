---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

The origin row and its subtraction produce rank(M)=1+rank(T). Multiplicative-character decomposition of functions on nonzero field coordinates block-diagonalizes T up to permutation of character channels. Each nontrivial channel is a nonzero Gauss-sum scalar times a weighted cycle adjacency C_chi; the trivial channel is -q C_1. For odd d the two Hamiltonian cycle terms give determinant 2 product_i chi(w_i)^(-1), nonzero over complex numbers even when char(F_q)=2. For d=2m the parity-ordered cyclic bidiagonal block has exactly two perfect matching terms; singularity is chi(r)=(-1)^m, with rank exactly m-1 by its nonzero triangular (m-1)-minor. Evaluation at r of multiplicative order h assumes each h-th root exactly (q-1)/h times, giving the claimed complex nullity. Independent direct construction of 25 matrices for p in {2,3,5}, d=3..7 and nonzero edge assignments confirmed the formula; this finite check is not the all-q proof. Ambient B need not be invertible; theorem is about the restricted M, not full Fourier inversion.

## originality

PASS

Best-of-knowledge comparison of exact statements and implications: Checked graph-circulant and finite Fourier aliases through the actual decomposition: a generic determinant or Gauss sum alone does not specify the multiplicative-order resonance or nullity; no identical statement located in searched SCOPE or Resultary results. A general norm/extension estimate cannot by itself imply exact complex nullity for a finite union of lines and weighted cycle; no dominating theorem with equivalent premises was found. Standard Gauss estimates and weighted-cycle matching determinants are prerequisites; together with character evaluation they support the proof but the cited finite-field restriction theorems do not state or logically imply this rank classification.

## value

PASS

This is a natural reconstruction/invertibility threshold for sampling on a full union of coordinate axes, with a nontrivial obstruction depending on multiplicative order of an edge-product ratio rather than solely rank of the ambient form. It provides all q and all weighted cycles, distinguishes odd/even/4-divisible lengths, and can guide exact interpolation tests; it is not merely an arbitrary finite determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
