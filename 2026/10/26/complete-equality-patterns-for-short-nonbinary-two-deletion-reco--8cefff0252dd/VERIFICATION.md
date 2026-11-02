---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every ordered pair of length-n centers corresponds uniquely to an RGS partition on 2n positions; every q-symbol realization is an injection of s equality labels, giving (q)_s, and center-swap is fixed-point-free under disjoint one-deletion shadows. Inspected full C++ recursion over Bell(6),Bell(8),Bell(10),Bell(12) partitions and exact deduplicated deletion subsequences. Independently wrote/compiled a separate C++ RGS enumerator: counts 203, 4140, 115975, 4213597 total patterns; eligible 133,3690,113073,4194600; maxima 3,4,6,6; extremal support multiplicities {3:1},{2:1,3:4,4:1},{3:1},{2:2,3:8,4:2}. Thus all q>=3 labeled unordered-pair polynomials follow, with quaternary totals 12,66,12,132; orbit-replay logic for swap/reversal inspected. Exhaustive only at n=3..6; no arbitrary-n assertion.

## originality

PASS

Recent known global six-overlap bound and large-length reconstruction maxima are credited, not presented as novel. The assessed statement is the complete short n=3..6 equality-template and falling-factorial population census for all q>=3, plus 1/4/1/5 symmetry class counts. Relevant published Resultary findings use different alphabet/number of deletions, and inspected primary quantified theorems do not imply the finite equality populations.

## value

PASS

Equality-case classes of the natural two-deletion reconstruction ambiguity under one-deletion separation are mathematically meaningful, even when the maximum alone is known. The exact support-profile and all-alphabet labeled-population polynomials resolve the exceptional short-length boundary not characterized by large-length bounds. Finite exhaustion is valid and valuable because these are the entire finite parameter range claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
