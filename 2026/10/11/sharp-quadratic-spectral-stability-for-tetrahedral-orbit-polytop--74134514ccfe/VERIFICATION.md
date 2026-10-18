---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The frozen RESULT.md identifies the symmetric 3×3 cubic block B with entries (a,s,d; s,-a,d; d,d,-a), a=x1, s=x2+x3, d=x2−x3 and a+2s=1. Recomputing det(tI−B) reproduces the displayed cubic. For L²=a²+s²+d², the exact evaluation p(L)=d²(2a−1−L) is nonpositive: it is immediate for a≤1/2 and follows for a≥1/2 from L²−(2a−1)²=((11a−3)(1−a)+4d²)/4≥0. Therefore largest eigenvalue ≥L and square ≥x1²+2x2²+2x3²; the weighted completion-of-squares gives unique 1/5 minimum. Equality requires d=0, and its converse follows from the 2×2 block. Principal-submatrix interlacing gives λ3≤−sqrt(a²+s²)≤−1/sqrt5; equality forces uniform weights. The geometric numerator conditions produce c_g=0, a_g/b_g=golden ratio, the icosahedron. Symbolic polynomial identities were independently recomputed; rational-grid verifier is auxiliary, not infinite proof. The bound does not concern collapsed smaller orbits.

## originality

PASS

The source group-orbit paper reports the icosahedral extremum from Maple and plots; this audit does not count that reported optimum as new. The claimed novelty is the stronger all-weights quadratic spectral stability inequality, exact equality locus x2=x3 and analytic justification, not supplied by the source abstract or the nearby general symmetry-reduction work. The complete primary original could not be retrieved on lawful routes, so this is explicitly best-of-knowledge with a substantial risk if its uninspected appendix already derives the same inequality.

## value

PASS

The weighted squared-distance deficit controls departure from uniform transition weights pointwise and supplies a quantitative stability statement for a natural group-orbit random walk; it is not merely a restatement of the already reported optimizer. The proof isolates the precise algebraic spectral mechanism and equality locus, addressing the source’s computational rather than analytic extremum discussion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
