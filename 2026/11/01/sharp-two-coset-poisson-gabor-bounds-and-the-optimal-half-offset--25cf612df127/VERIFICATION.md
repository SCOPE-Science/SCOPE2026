---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Unitary Zak transform diagonalizes each critical-density modulation row and the second modulated row becomes a shift s->s-delta. Direct Poisson geometric expansion yields |Zg|²=(pi/w)²(a_s²+b_s²+2a_sb_sc)/(1+q²-2qc)² with a_s,b_s>=0, c=cos(2pi x). Its c derivative is nonnegative and strictly positive except isolated zeros; hence global extrema occur x=1/2 and x=0. The minimum fiber is 4q sinh²(L(s-1/2))/(1+q)²; minimizing on each wrap interval yields cosh(Ld)-1. The maximum fiber is strictly convex on each wrap chamber, so maxima occur at endpoints. Essential extrema equal optimal frame bounds by Zak-image concentration. Taylor yields A~8*pi^4*q/(1+q)^2 d²; strict convexity/symmetry yields unique half-offset. Checked actual RESULT.md Steps 1-6 and source verify_bounds.py, independently compared nine Zak spatial sums and 5,289 multiplier samples plus extremal fibers. Finite numerical checks are corroborative, not universal proof. Endpoints delta=0,1 are excluded; w>0 essential.

## originality

PASS

The original candidate is the exact sharp nonrectangular two-coset frame-bound profile and unique offset optimum, not the qualitative frame property or Zak diagonalization. The close October 2026 Poisson theorem qualitatively covers frame existence, but no accessible statement asserts the two-coset exact constants. Best-of-knowledge originality passes with explicit inaccessible-source and implicit-formula risks.

## value

PASS

Sharp lower and upper operator norms, exact optimal nonrectangular frequency offset, and quadratic conditioning collapse are mathematically motivated quantitative invariants in Gabor analysis, not merely a numerical example or restatement of the already-known qualitative frame criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
