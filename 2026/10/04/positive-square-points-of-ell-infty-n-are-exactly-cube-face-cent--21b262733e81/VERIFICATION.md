---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

In finite dimensions the approximate definition is equivalent by compactness to the existence, for each admissible functional, of a norming vector \(y\) with both \(f(y)=1\) and \(\|x+y\|_\infty=2\). For \(f=(a_i)\in S_{\ell_1^n}\), every nonzero coefficient forces a norming vector coordinate \(y_i=\operatorname{sgn}(a_i)\). If \(x\in\{-1,0,1\}^n\setminus\{0\}\), either a saturated coordinate has zero functional coefficient and can be chosen freely, or \(f(x)\ge0\) forces some saturated coordinate whose sign agrees with its coefficient, yielding norm two. Conversely, if \(0<|x_j|<1\), placing small total opposite-sign mass on all saturated coordinates and the remaining mass with the sign of \(x_j\) gives \(f(x)>0\) while every norming vector cancels every saturated coordinate, so \(\|x+y\|_\infty<2\). This proves exactly the nonzero ternary coordinate locus and the cube-face-center count \(3^n-1\).

## originality

PASS

Langemets's new paper introduces the square-point notions and publicly indexed descriptions confirm pointwise comparisons with Daugavet, Delta, and nabla points; the motivating material includes the positive-square example in \(\ell_\infty^2\). Current Resultary search returned the assigned all-dimensional cube-face classification as the exact hit and no prior classification of the entire positive-square locus of \(\ell_\infty^n\). The exact primary body was not available through the inspected web route, so no whole-document noncoverage claim is made; the assessment remains best-of-knowledge with that access risk explicitly retained.

## value

PASS

The theorem completely resolves the canonical finite-dimensional cube for a newly introduced pointwise Banach-space property, turning an isolated two-dimensional example into an exact geometric locus of all face centers. That is a natural model-space classification with a clean obstruction mechanism, not an arbitrary coordinate exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
