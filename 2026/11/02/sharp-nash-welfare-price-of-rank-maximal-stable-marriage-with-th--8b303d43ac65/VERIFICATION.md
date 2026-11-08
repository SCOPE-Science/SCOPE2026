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

Exactly (3!)^6=46,656 complete strict 3-by-3 preference profiles and all six bijections per profile were independently enumerated with explicit two-sided blocking-pair checks. Calculated lex-max profile (p1,p2,p3), Nash product 3^p1 2^p2, and ratio P*/PR using exact fractions; obtained exactly seven cells 1:42756, 4/3:2484, 16/9:432, 64/27:12, 8/3:828, 32/9:72, 16/3:72. The stable-match count distribution was 34080 one, 11484 two, 1092 three; optimal sets coincide for 42756 and are disjoint for 3900, none partially overlap. The simple n=2 identity P=2^p1 gives universal ratio 1. Since this is the entire finite domain, the exact enumeration is an exhaustive certificate rather than a partial experiment.

## originality

PASS

Prior rank-maximal stable-marriage profile optimization and rank-induced Nash welfare algorithms concern other objectives or broader algorithm design. A published three-pair Resultary classification ranks maximal versus egalitarian stable marriage and shares some frequency counts, but the *additive* egalitarian objective does not imply the exact multiplicative seven-atom ratio law. No explicit stronger implication was identified; the recent Nash paper was not fully accessible, so the priority judgment remains qualified.

## value

PASS

The first nontrivial market size admits an exact worst welfare loss of 16/3 and complete frequency/argmax-set dichotomy, quantifying the concrete fairness cost of lexicographic rank maximality. It is a natural finite classification of distinct optimization criteria, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
