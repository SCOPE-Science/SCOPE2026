---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An independent length calculation over D=K[[y]] checks the all-k result without relying on a monomial order on the completed ring. Modulo x^2+2y^13 the algebra is free over D on 1,x. The remaining generators have coordinates g=(2k y^(k-1),y^12) and h=(y^k,-y^13); multiplication by x sends (a,b) to (-2y^13 b,a). If k is not 2 mod 5, h+yg gives y^k, and yg then gives xy^13. Subtracting the second coordinate of xg, divisible by y^13, gives y^25. For r=min(k,25), the D-span of g and (y^r,0) contains h and is closed under multiplication by x: xg reduces after subtracting 2k y^(k-13)g to a scalar divisible by y^r, since 2k-14>=k, and x(y^r,0) reduces after subtracting y^(r-12)g to a scalar divisible by y^r. This is exactly the submodule and its determinant has valuation r+12. If k is 2 mod 5, h=-yg and the ideal is the D-span of g and xg, with determinant y^(2k-2)+2y^37. The exponents differ, so the length by the elementary divisors over D is min(2k-2,37). The exceptional class starts at 17 and then 22, so on this class the length also equals min(k+15,37). This verifies the plateau starting at 25, the earlier equality at 22, and the values 28,32,30 at 16,17,18. The exceptional calculation relies on the completed local ring, where the nonzero constant factor after removing the smallest power of y is a unit.

## originality

PASS

The family and the k=17 jump are already in Ma–Ying–Zuo v1. The lower range 14<=k<=19 is recoverable from its extended-algebra bases, and stabilization from k>=26 follows from its binomial contact reduction and the binomial Tjurina calculation. The supported distinct contribution is the exact intervening characteristic-five profile 20<=k<=25, in particular the value 37 already at the resonance k=22, the drop back to 35 and 36 at 23 and 24, and the exact start of permanent stabilization at 25. The inspected normal-form and filtered tangent calculations do not give that middle-range ordinary Tjurina length profile.

## value

PASS

This is a published diagnostic family for positive-characteristic jumps, not an arbitrary slice. An ordinary Tjurina-length calculation through the change of Newton-diagram regime determines whether the early residue-class phenomenon persists and where the binomial length first becomes permanent. The resonance at 22 attains the final length early but does not yet stabilize it; this is exact invariant information beyond the motivating three samples and the eventual contact reduction. A researcher comparing jumps across that transition could use the precise lengths without any modality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
