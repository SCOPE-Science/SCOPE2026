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

# Verification

Reconstruct the unrestricted proof in `RESULT.md` from the height identity \(h_i=(p+q)B_i-qi\), congruence classes modulo \((p+q)/\gcd(p,q)\), balanced-window deletion, exact arithmetic-progression intersections and adjacent-swap continuity. No computational certificate substitutes for these arguments.

Run `python3 checker.py`. The direct enumerator checks all 32,738 nonconstant binary strings of lengths 2 through 14, computing actual indexed rotations and scattered `01` counts rather than reusing the proof's height formula; it checks bounds, equality, pairwise collision conditions, and complete fixed-content attainment sets. It additionally checks 9,801 content pairs using explicit lower and upper witnesses and the length-\(N/d\) cyclic balancing lemma. These finite experiments cannot establish the infinite theorem alone.

The 2004 Chuan paper uses a moment statistic affine-equivalent to the coefficient in this theorem. Its complete text was inaccessible in this scientific comparison; the historical comparison remains qualified. No independent mathematical review was conducted.
