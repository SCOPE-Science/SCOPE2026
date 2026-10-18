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

For every 0<s<1, the regression polynomial for E[X2²X3² | X1=x] is v2v3+2r²+(a²v3+b²v2+4abr)x²+a²b²x⁴ with v2=1-a²,v3=1-b²,r=c-ab. Gaussian negative-moment ratios are 1-s and (1-s)(3-s), giving normalized signed difference exactly -s[a²+b²+4abc-(2+s)a²b²]. For q=|ab|, the positive-semidefinite elliptope condition and AM-GM imply F>=-2q+(6-s)q²>=-1/(6-s), with equality iff |a|=|b|=sqrt(1/(6-s)), c=sgn(ab)(2/(6-s)-1), a rank-2 boundary correlation. Equality gives s/(6-s); positive definite matrices approximate but do not attain. Direct symbolic algebra independently rederived the conditional identity and extremum; s=1/2 gives 1/11. No infinite conclusion was inferred from finite grids.

## originality

PASS

Bivariate opposite Gaussian product inequalities and existing multivariate mixed-sign inequalities do not imply this exact ternary comparison with the *joint* X2²X3² positive block, its signed correlation criterion, its global sharp additive excess and singular equality classification. Lan–Ouimet–Sun convex-positive-block upper bounds cannot be substituted because (x2,x3)↦x2²x3² has indefinite Hessian; their marginal-product comparator also differs. No Resultary or targeted literature hit was shown to dominate the final theorem. Bibliographic risk persists, especially an unindexed polynomial-elliptope optimization.

## value

PASS

The first dependent positive quadratic block after an inverse-power Gaussian coordinate has a nontrivial failure region of the natural opposite-product comparison. An exact algebraic sign classification, sharp uniform excess constant, and all singular extremizers give a checkable boundary case relevant to mixed-sign Gaussian product inequalities rather than a mere parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
