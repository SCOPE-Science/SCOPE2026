---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For lexicographically ordered binary RM(2,m), N=2^m, m≥3, Q=N/4 and K=1+m+m(m−1)/2. Quadratic polar forms have even rank 2r. The character-sum decomposition makes any nonzero word below weight 3N/8 a weight-Q rank-two quadratic, equivalently the indicator of an affine codimension-two flat. A cyclic window with b>5N/8 zeros confines support to an interval shorter than 3Q/2. Projecting such a flat to the two most significant bits rules out all but four aligned quarter blocks and four neighboring boundary half-quarter blocks, exactly eight length-Q runs with starts multiples of Q/2. Each has a zero gap of length 3Q and hence b-symbol weight b+Q−1 for b≤3Q; all others have full weight. Above b=3Q all nonzero words have full weight, and the strict lower cutoff has extra flats. Dimension K yields coefficients 2^K−9 and 2^K−1. Independently exhaustive Boolean polynomial enumerations for m=3,4,5 at every admissible integer width reproduced complete coefficient tables; the rank/flat argument supplies the all-m proof.

## originality

PASS

Pan–Ling–Liu Theorem4.6 gives the exact first nonzero b-symbol distance for the same RM(2,m) code but not multiplicity eight or the complete high-window enumerator. Zhu–Li–Shi–Xia–Solé bound cardinality of distinct weights, which does not count words per weight. Irreducible cyclic-code enumerators address different code families, and the published first-order RM case is a proper smaller subcode. This is a coefficientwise infinite-family refinement.

## value

PASS

This exact all-dimensional two-coefficient tail enumerator for classical quadratic Reed–Muller codes determines not just minimum distance but the full rare-event multiplicity, a natural coding-theoretic invariant for sliding-window/b-symbol channels. The constant eight and sharp 5/8 threshold arise from rigid affine-flat support geometry. It is a meaningful structural classification over an infinite family rather than arbitrary finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
