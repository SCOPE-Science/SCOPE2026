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

The fiber relations can be made monic with leading terms x²,z² in graded lexicographic order with z>x: they are x²−uz+v and z²+uxz+2u²z−vx−uv−w. Their relatively prime leading monomials give a free degree-four quotient with basis 1,x,z,xz. For u!=0, simple substitution into the quartic identifies geometric multiplicities with root multiplicities. Writing A=u² and C=2(v+u³), the derivative is x(4x²+3Ax+2C); the discriminant of the quadratic in parentheses is S. A nonzero triple root requires S=0 and p(−3A/8)=0, the latter equivalent to T=0 on S=0. The source's phrase 'cubic derivative factor' is imprecise: it is the quadratic after factoring x, and S=0 alone does not make a triple root. Two nonzero double roots would force their sum zero by the missing linear term, incompatible with A!=0; on B=0 the remaining polynomial is x² times a quadratic and gives the two stated intersection cases. The independent exact resultant and restriction check confirmed Q and the factors with orders 3 and 1. The triangular target changes give the two irreducible surfaces and singular lines. On u=0, the equations x²=−v and z²=w−x³ give two doubled points at v=0,w!=0, a double and two simple points on w²=−v³ with v!=0, and the single length-four algebra C[x,z]/(x²,z²) at the origin. These arguments cover the branch divisor on and off u=0 and exhaust the partitions.

## originality

PASS

The exact map, degree four, reduced branch equations, Whitney umbrella, and generic simple branch fiber are prior. The distinct claim is the explicit polynomial cusp-cylinder model and singular line, together with the two-curve incidence with unequal contact orders and complete exceptional fiber-length classification for this map. The closest earlier record normalizes the second surface but does not classify these singularities and strata.

## value

PASS

For a motivated published test map, the exact two branch models, two contact orders and exhaustive scheme-length partitions distinguish genuine local degeneracies left open by knowing the branch support and monodromy. These data locate all exceptional fibers and can be used directly in further local branch calculations. The value lies in that complete incidence and collision classification, not in routine verification of the degree or re-expansion of its discriminant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
