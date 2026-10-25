---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For positive two-periodic full-line mesh lengths a,b, hat-function Gram has diagonal (a+b)/3 and neighboring off-diagonals h_j/6, uniformly strictly diagonally dominant. Its inverse row obeys alternating-sign geometric recurrence with Q(r)=ab r²+(a²+b²-4(a+b)²)r+ab, smaller root 0<r<1 and factors u=(a+br)/(2(a+b)), v=(b+ar)/(2(a+b)) satisfying uv=r. Direct substitution verifies recurrence and invertibility. The kernel row is linear interpolation of inverse coefficients; exact absolute area on one cell is h(c²+d²)/(2(c+d)); summing four tails and reducing algebraically modulo Q gives the ratio (5a²+22ab+5b²)/(3a²+10ab+3b²). Independently verified a symbolic polynomial remainder exactly zero and assembled/inverted 128x128 cyclic Gram matrices at (a,b)=(1,1),(1,2),(1,10),(4,7), obtaining matching L∞ norms 2, 1.971428571429, 1.799007444169, 1.981052631579. Reflection/translation of the mesh makes nodal Lebesgue constants identical, and convex combinations bound all non-nodal x; the kernel sign attains at a knot as an L∞ function. The full-line operator norm is thus 2-(a-b)²/(3a²+10ab+3b²), uniquely 2 at a=b, strictly lower for alternating grids, inf5/3 approached at degenerate ratio. Cyclic finite tests corroborate, not prove, the bi-infinite inverse formula.

## originality

PASS

Best-of-knowledge original exact full-line alternating two-periodic linear-spline projection L∞ norm and opposite global-distortion behavior; broad Shadrin/Passenbrunner bounds are prior. Historical formulas by Jia or Oswald remain material priority risks because full texts could not be accessed.

## value

PASS

The natural alternating class gives a complete exact two-parameter projection-stability law on the whole line, exhibiting strict *improvement* relative to the uniform grid rather than worsening with distortion. Explicit inverse Gram kernel and optimal sign input provide useful sharp operator estimates and a counterpoint to single-cell perturbations, a motivated structural phenomenon rather than arbitrary finite experimentation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
