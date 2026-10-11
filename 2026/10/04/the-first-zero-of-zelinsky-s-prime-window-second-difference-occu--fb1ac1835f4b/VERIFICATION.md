---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For fixed \(n\), the defining product is strictly increasing with window length, so exact integer numerator/denominator comparison certifies the minimal crossing without floating point. Independent recomputation found \(a(42)=3900\), \(a(43)=4112\), \(a(44)=4324\), terminal primes \(37199,39461,41761\), and \(f(43)=0\); scanning every required \(a(1),\ldots,a(44)\) found no earlier zero and reproduced the published check \(f(31)=-5\).

## originality

PASS

Zelinsky's 2023 paper explicitly asks whether \(f(n)\) is ever zero and gives \(f(31)=-5\) as an example, while the earlier paper introduces the second-difference behavior. Exact-value searches for \(f(43)\) and the triple \((3900,4112,4324)\), plus Resultary search, found no prior answer. The audited computation therefore resolves a stated open finite question and additionally proves minimality.

## value

PASS

The result gives an exact affirmative answer and sharp first occurrence for a question explicitly posed in the prime-factor literature. Although finite, the cutoff is mathematically motivated by the source's second-difference problem and is fully reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
