---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every q≥2 the deletion shadow of length-three subsequences of a length-five word carries universal weight h(aaa)=1, h(aba)=0 if a≠b, h(abc)=1/5 if a≠c. If some symbol repeats ≥3, constant triple already gives unit weight. Otherwise the equality multiplicity partition is (2,2,1),(2,1,1,1) or (1,1,1,1,1); the elementary finite pattern argument establishes at least five *distinct* nonpalindromic triples for each class. Hence ∑_(v∈D2(w))h(v)≥1 and for disjoint deletion shadows |C| ≤ ∑_(v∈Σ_q³)h(v)=q+(q³-q²)/5. At q=3 floor bound is 6, attained by the six words 00000,11111,22222,00112,10221,21100, whose explicit length-three shadow sets are disjoint. Independently verified every equality pattern (Bell(5)=52) and all ternary/5-ary literal strings, and checked witness shadows. The finite equality-partition exhaustion is logically exhaustive across arbitrary alphabets, independently of numerical sampling.

## originality

PASS

Qualified PASS: classical deletion hypergraph fractional transversal bound of Kulkarni–Kiyavash supplies methodology, not this specific q-ary five-letter weight or sharp exact ternary A_3(5,2)=6. Other exact length-five t=1 published findings and ternary edit-distance tables use different metrics. Ternary code size 6 could coincide with Hamming-code tables, but a Hamming minimum distance assertion does not prove all two-deletion upper bounds. A possible specialized older deletion-capacity table remains a source-risk.

## value

PASS

Natural exact finite blocklength optimal code with an all-alphabet symbolic upper bound and six-word construction, plus a simple sharp nonuniform fractional shadow dual; resolves a bona fide two-deletion benchmark, not an arbitrary handpicked code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
