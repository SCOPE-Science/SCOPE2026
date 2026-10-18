---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

With four exact uniform pairwise-independent p-values, the five bin probabilities are α/4 for each of the first four bins and 1−α for the fifth. Simes rejection is exactly N1≥1 or N1+N2≥2 or N1+N2+N3≥3 or N5=0. The explicit quadratic polynomial B(N) in RESULT.md majorizes this indicator on all 70 weak five-part compositions of four. Pairwise moments E[Nj(Nj−1)]=12pj² and E[NjNk]=12pjpk yield E[B]=α+13α²/16. All 13 support-state weights of the explicit exchangeable extremizer are nonnegative for 0≤α≤2/5, sum to 1, and match all five first moments and all fifteen same/different bin factorial moments. On each support state B=indicator; independent exact symbolic reimplementation verified every inequality, polynomial moment, normalization, and objective, including 333/6400 at α=1/20. Uniform conditional sampling inside bins makes all P_i exactly continuous Uniform[0,1] and every coordinate pair independent. It does not establish behavior for α>2/5.

## originality

PASS

The previously published three-variable pairwise-independent Simes envelope has leading α+4α²/9, but its 20-state moment problem does not imply the four-variable 70-state extremum. The original pairwise-independent probability-bound literature treats union and sum-tail events, not this nested 1-of-4/2-of-4/3-of-4/4-of-4 Simes region. Hommel 1983 full eight-page primary text, retrieved through authorized access after unsuccessful OA/preprint search, concerns sharp arbitrary-dependence bounds for adjusted overall tests; it does not impose pairwise independent uniform marginals or yield coefficient 13/16. No stronger prior coverage found.

## value

PASS

The exact four-test global-null calibration loss at small α is a natural finite-dimensional probability invariant with direct interpretation for Simes/BH under pairwise (but not joint) independence. Unlike a mere negative warning, it gives an attained sharp parameter interval, rational upper certificate, constructive continuous extremizer, and the exact practical 5% discrepancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
