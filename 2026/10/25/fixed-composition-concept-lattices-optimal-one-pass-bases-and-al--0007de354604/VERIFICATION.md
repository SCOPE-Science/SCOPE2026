---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The closure trichotomy follows by distributing the residual multiset over remaining positions; with >=2 unfinished colors, no extra literal is forced. Minimal incompatible stems are same-position mismatches and m_a+1 over-quota literals; compatible minimal nonclosed stems saturate all other colors and leave omitted color a unused. Their proper subsets are closed, so every complete implicational basis needs a distinct antecedent for each; these implications are one-pass direct. Count is n*C(q,2)+sum C(n,m_a+1)+q*n!/prod(m_a!). Closed-set enumerator follows by deleting feasible but singly-unfinished partial words. Möbius inversion sum over subsets closing to T gives Boolean incomplete intervals, complete-word coefficient (-1)^r(1-s), top truncated multinomial. The independent closure enumeration checked all 512, 4096, 32768 literal subsets for m=(1,1,1),(2,1,1),(2,2,1) and 399 Möbius intervals in the first two cases. Universal proof is combinatorial, not extrapolated from these tests.

## originality

PASS

General FCA direct-basis and pseudo-intent theorems do not state the fixed-quota classification; the all-one permutation context is a strict specialization of fixed positive quotas, and unrestricted surjective assignments have a different closure relation. No exact multinomial rule-count or interval-Möbius table was found in the relevant primary material. Originality is best of knowledge: older contingency-table or multiset-permutation lattices could encode an equivalent result.

## value

PASS

Fixed-content word contexts arise naturally when every position receives one of several colors with prescribed totals. A simultaneous minimum Horn basis and explicit full Möbius function solve real structural/computational tasks for this natural family; neither follows mechanically from the generic existence of Duquenne–Guigues bases. Sharp basis size and all-interval inversion are useful exact invariants, not a manufactured tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
