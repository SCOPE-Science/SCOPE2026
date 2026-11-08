---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For m≥1 and the scattered subsequence order, the leftmost embedding of a word u into (01)^m uses exactly c(u)=|u|−(# adjacent 01 transitions) blocks. Internal deletion changes this block cost by zero precisely for neighborhoods 010 or 101; endpoint deletion leaves cost unchanged precisely at initial/terminal 01. Thus minimal absence equals c=m+1 with those local configurations excluded. Four-state transfer on 00,01,10,11 and matrix (I−T)^−1 yields the stated rational F(x,z), and its positive-binomial expansion gives H_m(m+1+j)=binom(m+2−j,2j+1) on 0≤j≤floor((m+1)/3). I independently generated every candidate binary word for m=1..7 and checked absence and all one-deletions: histograms m1 {2:3}, m2 {3:4,4:1}, m3 {4:5,5:4}, m4 {5:6,6:10}, m5 {6:7,7:20}, m6 {7:8,8:35,9:6}, m7 {8:9,9:56,10:21}. The formal transfer and coefficient algebra, not these finite cases, cover all positive m. Replacing z=1 gives the stated total recurrence and dominant λ.

## originality

PASS

Best-of-knowledge PASS with substantive source-access uncertainty: earlier general absent-subsequence papers give automata and enumeration methods but not, in read material, a closed binomial length profile for the complete alternating family. Troníček 2023 explicitly gives an algorithm for counting minimal absent subsequences; a matching specialization could be hidden in its inaccessible full text, but no displayed abstract theorem establishes coverage. Thus priority is qualified and explicitly not certified.

## value

PASS

PASS. The infinite canonical alternating family makes the exact length distribution, extreme absent lengths and exponential enumeration output size natural intrinsic invariants of a fundamental string family. Its binomial spectrum and shortest-layer versus total-growth contrast can inform precise enumeration complexity; it is more than a generic implementation of an existing algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
