---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For P1,P2,P3 in P4 over F5, chart X4=1 centered at [1:...:1] eliminates P1 and yields Q=a²+b²+c²+ab+ac+bc and cubic -3(a+b)(a+c)(b+c). The conic is nonsingular (determinant 4 mod 5) and intersects the three lines transversely in the six explicit F5 projective directions; Bézout gives exact reduced degree six, and the global (1,2,3) complete-intersection degree excludes hidden components. The six rational lines meet only at P. Their tangent graded ring has Hilbert function 1,3,5,6,... versus six branches, giving delta 5+3+1=9. S5 orbit stabilizer of a direction is affine normalizer AGL1(F5) of size 20, hence six components; over F5^m point count 6(q+1)-5=6q+1. Independent modular direction computation recovered exactly six directions (script attached to execution report); finite check alone is not the geometric proof. Inspected actual RESULT.md at frozen Git commit and verify.py blob; the latter tests directions/Hilbert/S5 but cannot replace Bézout and normalization.

## originality

PASS

Best-of-knowledge: claim-specific mathematical comparisons of exactly defined source objects against established primary results; no matching stronger implication identified in actual searched and materially read sources. The characteristic-zero symmetric Bring theorem and smooth p≥7 generalization cannot imply the p=5 reducible fiber by base change, because smoothness fails and the earlier positive-characteristic hypotheses exclude it.

## value

PASS

The precise fiber at the exceptional bad characteristic of a canonical genus-four symmetric model is a natural deformation/boundary problem, and delta, S5 action, and point counts are mathematically useful invariants, beyond a routine degree computation; no stable reduction is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
