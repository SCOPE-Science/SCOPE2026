---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For X,Y with standard uniform marginals and Z=X+Y on {1/4,3/4,5/4,7/4}, write A=4X, B=4(1−Y); A−B belongs to {−3,−1,1,3}, so A and B share a fractional part. Conditional row and column probabilities each equal 1/4 because both variables are uniform on [0,4]. The unique cells for extreme differences immediately give p0,p3≤1/4 and the sum mean1. Conversely the explicit 4×4 nonnegative matrix in RESULT.md, with a=p0,d=p3 in [0,1/4], has all row/column sums 1/4 and diagonal totals (a,1/2−2a+d,1/2+a−2d,d); inverse transformation constructs the required joint coupling. Independent exact Fraction checks at 25 rational parameter pairs including edges and corners validate each identity. Symbolic construction, not finite grid, proves every real pair and degenerate boundary mass.

## originality

PASS

Mao–Wang–Wang characterize target laws of sums of uniforms only for biatomic and equidistant triatomic distributions in their cited theorems and note the general n=2 set is not fully determined. Joint mixability with all components uniform is not equivalent to coupling two uniforms to an arbitrary discrete third distribution. Makarov bounds are pointwise rather than joint attainability of an entire CDF. No corresponding four-atom quarter-grid rectangle appeared in Resultary semantic search; older transportation/shuffle equivalences remain a real residual risk.

## value

PASS

The centered four-point quarter-grid is a minimal natural next support beyond the two- and three-atom cases studied in the primary paper. The exact rectangle and explicit coupling settle all admissible target laws on this lattice including boundary and vanishing-atom cases, a useful nontrivial small-support feasibility classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
