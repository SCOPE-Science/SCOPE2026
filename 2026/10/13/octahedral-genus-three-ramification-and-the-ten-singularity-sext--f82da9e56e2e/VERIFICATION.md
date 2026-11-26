---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The ordered-root map to Sym^4(P¹)=P⁴ restricts scheme-theoretically to the pullback of the plane of quartics aT⁴+bT³U+cTU³−aU⁴. Exactness of S₄-invariants over C identifies the quotient with this plane; finiteness, generic degree 24, and flatness follow from the ordered-root map or finite Cohen–Macaulay flatness. An independent exact Sylvester determinant calculation gives all six displayed discriminant coefficients. The linear repeated-root equations have rank two for every projective root: their finite-root cross product is (−2t³,3t⁴+1,−t⁶−3t²), and the homogenization gives [0:0:1] at infinity. Generically the quartic has just one double root, so this degree-six parametrization without base points is its normalization. In the finite chart F'' at the chosen root is 6t(1−t⁴); the roots t=0 and t⁴=1 are triple but not quadruple, and infinity gives the sixth triple-root point by swapping homogeneous coordinates. Their distinct images are nonimmersive and each costs at least one delta. For a≠0 a two-double-root quartic must be the square of T²−pT+q with q²=−1 and p²=−2q, giving four distinct polynomials with nonzero quadratic discriminant. At a=0 with bc≠0 the four roots are simple, and bc=0 gives just the two endpoint triple-root cases. The four two-branch delta contributions and six singular branches use up the arithmetic genus 10, giving precisely nodes and cusps. On each transposition diagonal the residual pair roots give y=2t³(u−v), with y²=t⁸+14t⁴+1; its eight simple zeros give a connected genus-three double cover. The repeated-root projection of the diagonal is finite (unique coefficient point and only finitely many orderings of the residual two roots); no extra isolated components are possible because the diagonal is cut by two equations in a three-dimensional ambient diagonal. Smoothness follows from the fixed-locus theorem, and this identifies the entire projective model. Apart from transpositions a nontrivial permutation forces a triple root, two double roots, or a quadruple root, so fixes no divisor. The generic inertia on each diagonal is exactly its transposition and the reduced ramification statement follows.

## originality

PASS

Pass the specific realized ramification identification and accompanying explicit special branch model, not the generic S₄-cover construction, the generic cusp/node count, or the abstract octahedral curve. The closest general cover result works with a generic 2-plane and does not classify the ramification curves of this special plane. The exact K3 source determines the equations and commuting actions, but the specific fixed-curve geometry required the residual quadratic, connected compactification, and analysis of this plane's multiple-root strata. No inspected prior statement supplies this identification or a stronger equational classification that reads it off.

## value

PASS

This identifies a distinguished classical genus-three curve in an intrinsic geometric role for a named symmetric K3: every reduced ramification component for the ordered-root quotient is that curve. The explicit special branch model and confirmed ordinary singularities describe how this particular surface fits the generic cover construction and make it possible to use the quotient without assuming genericity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
