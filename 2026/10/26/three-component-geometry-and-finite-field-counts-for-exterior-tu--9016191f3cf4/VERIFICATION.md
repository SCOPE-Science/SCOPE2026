---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The square and mixed coefficients are separately imposed; in any characteristic, a nonzero b_h forces all a_i=c_i=0, and for b=0 the coefficients are exactly those of det(sum t_i H_i). For a nonzero rank-one uv^T in the span, every other nonzero member shares its image or row line; members with opposite strict alternatives would sum to a rank-two matrix. This proves the union in all characteristics. The common-line loci are closed by projective incidence (also by stacked-matrix minors). On a chart with a selected nonzero column/row, recovering the common line or kernel by that column/row is rational, so the incidence map is birational, not merely generically injective in positive characteristic. The two rulings are incomparable for r>=2 (take two independent matrices in one ruling); neither lies in L, and L has points with b nonzero. Their dimensions are 3r+1 against 4r for L. The intersections reduce respectively to 2r free entries, rank-at-most-one 2-by-r arrays, and tuples in Hom(k^2/K,I) for a pair of lines; including f gives 3r, 2r+1, 2r+2, with the stated triple intersection. Over F_q, span ranks 0, 1 and 2 have respectively 1, (q+1)^2(q^r-1), and 2(q+1)(q^r-1)(q^r-q) ordered tuples before the q^r factor; L adds q^(4r)-q^(3r). In particular the rank-two term vanishes at r=1. The proof does not address scheme structure.

## originality

PASS

The demonstrated overlap is the pair case within a related commuting family, not the uniform anticommuting square-zero tuple theorem. Credit the classical Segre rulings and the overlapping pair results; the supported contribution is the arbitrary-r fixed-flag component, intersection and counting result together, not new rank-one matrix-space theory.

## value

PASS

This is a complete reduced component classification for a natural fixed-flag exterior representation space, not just a rank-one lemma or a few checked field counts. It explains non-equidimensionality and which branches can meet and gives uniform, characteristic-two-inclusive point counts useful as tests of more general fixed-flag analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
