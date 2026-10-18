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

The trace representation over F25 with gamma^2+gamma+2=0 (order 24) gives an explicit four-dimensional F5 code whose ordinary enumerator is exactly 1+108 z^16+288 z^19+24 z^20+192 z^21+12 z^24. Deleting coordinate 0 gives the published [23,4,15] enumerator; the coordinate-0 kernel has dimension 3 and gives the published [23,3,16] enumerator. Full rank of both generators identifies all r-subcodes bijectively with RREF rowspaces of F5^4 and F5^3. Each support is exactly the union of nonzero positions in any rowspace basis. Independent arithmetic reconstructed field multiplication and trace, independently enumerated all 1119 punctured and 63 shortened nonzero subspaces, and exactly reproduced each support histogram, hierarchy (15,19,22,23)/(16,20,23), and minimizer count (18,5,23,1)/(9,1,1). Exhaustive finite claim requires no extrapolation.

## originality

PASS

The originating Hernández–Vega primary paper gives the ordinary weight enumerators for exactly these two derived codes, not their higher-dimensional subcode support distributions. Pan–Chen–Liu–Liu primary preprint develops exact SSWD for constructions based on modified Solomon–Stiffler and simplex-complement families, and does not report these exact 23-coordinate q=5 trace-code instances. The entire 2-,3-,4-dimensional support censuses and minimizer counts are not implied by ordinary codeword enumerators alone.

## value

PASS

These are the two specific quinary punctured/shortened companion codes singled out in the source construction, with natural generalized Hamming weights for leakage/secret sharing. Complete higher-dimensional support statistics and extremal multiplicities are not contained in ordinary weight enumerators; exhaustive exact finite censuses are mathematically meaningful self-contained refinements, even without an all-q family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
