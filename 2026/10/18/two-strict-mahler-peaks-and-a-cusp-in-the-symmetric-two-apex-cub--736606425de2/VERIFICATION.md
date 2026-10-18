---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational and analytical verification

Execute `python verify_two_apex.py` with Python 3, SymPy, NumPy and SciPy. The checker derives candidate outward triangulations at one representative parameter in each of the two combinatorial regimes. This floating-point step **only proposes** finite face incidence data; it is not evidence of global validity by itself.

The checker then evaluates **exactly** every supporting-plane inequality against all twelve primal input points and, independently, for the dual. For the complete open chamber \(0<t<2\), the substitution \(t=2u/(1+u)\) maps \(u>0\) onto that chamber. For \(t>2\), the substitution \(t=2+u\) does likewise. Each symbolic numerator and denominator in all support inequalities has a certified constant coefficient sign across all nonzero coefficients. The script verifies closed oriented boundary triangulations, duality from each primal facet, recovery of primal vertices from polar facets, and symbolic volume determinants. Exact symbolic algebra verifies the two rational product expressions, positivity of the Mahler gap, the two critical-point formulas, their order, and endpoint continuity.

A successful execution reports sixteen outward primal face triangles and twenty outward polar triangles in each chamber, correct symbolic primal and polar volumes, and success for all product and critical-point tests. This is a reproducible exact-arithmetic certificate for a continuum of \(t\)-values, not a claim of exhaustive floating-point sampling. The degenerate transition at \(t=2\) and initial point \(t=0\) are determined by continuity and direct cube geometry. The certificate does not examine bodies outside the stated one-parameter family; independent verification is not part of this package.
