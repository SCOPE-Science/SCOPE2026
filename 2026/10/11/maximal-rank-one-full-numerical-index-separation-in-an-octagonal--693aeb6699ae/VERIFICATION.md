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

Read both original author-posted primary papers and checked the unrestricted two-branch n(X_xi) and rank-one four-branch n1(X_xi) for exactly the same normalization. The ratio equals 1 on [0,sqrt(5)-2] and [(sqrt(5)-1)/2,1]. Independently recomputed both derivatives in SymPy as rational positive denominators times A_- and A_+, and symbolically verified the displayed sextic polynomials, P_-(a)=16(263sqrt(5)-588)>0, P_+(b)=416-296sqrt(2)<0, P_+(c)=32-15sqrt(5)<0, and positive second derivative of P_+ on [b,c]. This proves strict rise and fall, unique b=sqrt(2)-1, and numerical 1.5068785848642205 matching the radical. Algebraic comparisons, not sampling, establish interval-wide signs.

## originality

PASS

The 2007 and 2015 primary sources already determine the individual full and rank-one index functions for every xi, including the regular-octagon point. This is close pointwise prior coverage; it must not be represented as new index formulas. The final claim is the separate global optimization of their nontrivial quotient and unique maximizer, neither of which is stated in the inspected source Theorem 2, Corollary 3 or older index theorem. Symbolic derivative sign analysis supplies the additional uniform inequality. Targeted searches found no published standalone ratio-optimization theorem, but the fact that both source profiles determine R implicitly is a significant originality limitation.

## value

PASS

The ratio measures the intrinsic multiplicative loss of restricting the operator-infimum to rank-one maps, a motivated quantity in numerical-index theory. Determining its unique worst-case octagonal parameter and sharp radical value distinguishes the regular octagon within a standard one-parameter family; the proof requires two nontrivial global radical monotonicity certificates, not a pointwise substitution alone. The value is bounded to this family and does not claim all Banach planes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
