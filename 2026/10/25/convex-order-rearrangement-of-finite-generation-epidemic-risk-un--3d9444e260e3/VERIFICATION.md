---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For K nonnegative integer with m>0 and finite second moment and independent thinning, a 2-generation adjacent swap p<q yields conditional offspring variables B_p Bin(K,q) and B_q Bin(K,p), same mean pqK. Convexity of Bernstein polynomials gives convex-order monotonicity of their zero-end secant slopes; independent sums and further branching preserve convex order, permitting bubble-sorting any rate multiset. PGF composition implies strict terminal P(Z_h=0) if P(K>=2)>0, and the variance recurrence gives the exact stated c2 swap increment. For K supported in {0,1} thinning pgfs commute. Independent exact rational checks: 432 stop-loss inequalities for K=1,2,3 and 3 rate levels; benchmark P0 2401/4096 versus 1849/4096 and variance gap 3/8.

## originality

PASS

Qualified best-of-knowledge PASS for an exact convex-order rearrangement over all permutations of a FIXED multiset of thinning rates with sharp equality boundary and adjacent-swap variance identity, not for time-varying branching PGF models themselves.

## value

PASS

The result gives a genuine finite-horizon optimization under fixed intervention levels for a natural Galton–Watson thinning model. Convex order simultaneously controls variances, elimination and stop-loss for any offspring distribution with finite second moment; exact swap increment and nonbranching equality cases make the chronology law informative and usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
