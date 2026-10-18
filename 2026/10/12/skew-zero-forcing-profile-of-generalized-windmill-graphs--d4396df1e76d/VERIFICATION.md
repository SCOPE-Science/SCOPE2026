---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

A peripheral white vertex has epsilon+w_i-1 white neighbors, a blue peripheral vertex epsilon+w_i, and the central vertex sum_i w_i. If any blade has at least three whites, no permissible skew force can reduce that blade below three even after all other blades clear. With blue center and w_i<=2, pairs of whites force each other then a blue blade vertex forces the remaining single white (m>=3). With white center, the profile w_i=2 for all blades is stalled, whereas any w_j=0 or 1 permits forcing the center first and then clearing. Counting admissible blue sets gives (1+x)F_m(x)^k-C(m,2)^k x^{k(m-2)} with F_m=x^m+mx^{m-1}+C(m,2)x^{m-2}. Exact coefficient analysis gives Z_-=k(m-2)+1, minimum-set count C(m,2)^(k-1)[C(m,2)+km] and failed forcing number km-2. Independently exhaustively enumerated all 2^N sets of W_(2,3), W_(2,4), W_(3,3), matching criterion, polynomial and extrema; infinite quantifiers rely on occupancy proof.

## originality

PASS

The claimed incremental conclusion was compared by statement and implication against the most relevant primary work and indexed mathematical results. Known component statements are explicitly credited and are not themselves asserted as new. This is a best-of-knowledge priority judgment with the listed full-text and alias risks.

## value

PASS

The complete all-initial-set skew forcing profile and exact size enumerator for an infinite natural graph family substantially strengthen knowledge of an extremal forcing number. Explicit local occupancy constraints and the unique global dead profile are natural combinatorial structural facts; the two-edge friendship boundary is expressly separated as prior knowledge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
