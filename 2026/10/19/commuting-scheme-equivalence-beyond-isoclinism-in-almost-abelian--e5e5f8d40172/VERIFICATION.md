---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For any k, choose complements to ker D and bases of im D. The bracket of inputs (a_i,v_i),(a_h,v_h) has coordinates a_i Dv_h−a_h Dv_i in im D. This identifies defining ideals under a linear input change, with c independent kernel coordinates per input; it is not merely a pointwise match. If a is nonzero, every row of Y is a multiple of a, so the support is the union of a=0 and the rank-at-most-one stacked matrix locus. The irreducible rank-one cone has dimension equal to number of rows plus number of columns minus one, and neither locus contains the other for r,s≥2. This proves the stated dimensions, intersection and unique equidimensional case. For finite fields, counting on a=0 and a≠0 gives N_s and hence the displayed zeta function. On all tuples the joint map is (b,u)↦(a_i u−b y_i)_i: when a=0 it has rank 0 or 1; otherwise the u-block has rank r and the b-column adds one precisely when Y is not of the form ua. This gives the claimed four frequencies, including in characteristic 2. For the nilpotent rank-two example D_{31}²≠0 and D_{22}²=0; γ_{j+1}=D^jV, and the central quotient is abelian exactly when D²=0. For d≤3, rank fixes the nilpotent partition. Independent direct simultaneous-centralizer enumeration used two invertible rank-two matrices over F₂ and one rank-two singular matrix over F₃, checking both the rank frequencies and commuting counts (python3 /workspace/reviews/evidence/reproduce.py 1).

## originality

PASS

The common ideal is exactly a known generalized binomial edge ideal after transpose, and its decomposition and the component formulas are covered. Credit that prior result rather than treating the geometry of this model as new. The distinct contribution is the Lie-theoretic identification of all-arity commuting schemes and joint-adjoint rank distributions for same-dimension, same-rank almost-abelian algebras, including the sharp nonisoclinic class-two/class-three collision. No checked source covers that conclusion or the full joint-adjoint enumerator.

## value

PASS

The value is the sharp failure of Lie reconstruction even if every ordered-tuple commuting scheme and every joint-adjoint rank frequency is supplied. The pair changes nilpotency class and isoclinism at the first possible dimension, so it isolates a real loss of structure. The known determinantal component geometry alone is not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
