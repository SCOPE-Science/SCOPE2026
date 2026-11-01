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

Classify all nonempty contiguous factors of 0^a1^b0^c1^d by run count: one-run complementary pairs contribute 2Σ_{k≤m}z^k, two-run pairs are indexed by the union Q of rectangles [1,p]×[1,q] and [1,q]×[1,r], and three-run pairs exist iff b=c, contributing 2Σ_{i≤p,j≤r}z^{b+i+j}. Four-run factors cannot have complements, as opposite orientation absent. At z=1, inclusion-exclusion gives C=2(m+pq+qr-h+1_{b=c}pr). For b=c=t, exact reduction C/2=max(t,min(a,d))+t(min(a,t)+min(d,t)) implies upper t(n-2t+1) with equality a,d≤t. Concave quadratic optimizes at t=ceil(n/4), and b≠c case proves C≤n²/4, strictly below target n≥6. n=4,5 direct cases. Independent brute force checked 1296 compositions up to individual run length 6 and all maxima/equality n=4..40. Infinite proof is symbolic run classification and inequalities, not extrapolation.

## originality

PASS

Best-of-knowledge PASS for full length spectrum and sharp all-n extremum for exactly four-run words. Currie and coauthors study complement-avoidance thresholds and count complementary factors in *infinite* morphic words; this prior invariant is the same but their quantifiers and extremal family differ. No inspected theorem implies the four-run polynomial/equality classification.

## value

PASS

The exact length spectrum and sharp fixed-size extremizers answer a natural finite combinatorics question for a simple nontrivial class of binary words. The structural b=c resonance produces an additive linear improvement over the best unequal-interior-run bound; the complete equality classification is useful beyond a mere scalar maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
