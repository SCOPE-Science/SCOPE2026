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

For every prime p, m=p+1 satisfies r_p(m)=2 (p<m<p²). Every admissible row N=(p+1)q with 2≤q<p fails attainment: the particular selected k=p+1 adds to its complement (q−1)(p+1) without base-p carries in either occupied column, so v_p G=0. At q=p, selected k=d(p+1), d=1,...,p−1, has base-p digits (d,d), while its complement has (p−d,p−d), hence exactly two carries for every selected binomial. Kummer gives v_p G=2, proving first attaining row N=p(p+1); p=2 recovers the established 6. Independently recomputed Kummer and Legendre valuations at 1035 pretarget rows, symbolic proof independent of finite p cutoff.

## originality

PASS

Fairfax-Ball October 2026 proves the least-row law T_p(p^a+1)=p^(3a)+1 ONLY for a≥2 and expressly excludes a=1 (Remark 8.3), mentioning prior T_2(3)=6. The September predecessor covers the target-row valuation for p=m−1, but the fact that p(p+1) is the least attaining row for EVERY odd prime requires excluding all smaller multipliers; this is the new all-prime boundary. Kummer itself supplies carries, not the first-row classification without special argument.

## value

PASS

The exact omitted a=1 case is singled out in the motivating theorem, not an arbitrary parameter slice: its minimal row law p(p+1) is qualitatively different from the a≥2 formula p^(3a)+1. One clean universal Kummer carry dichotomy completes the boundary of a natural sharp-extremal family and can be quoted independently. The narrow result is motivated by explicit outstanding scope in the primary article.

The dated certificate retains the supplied scientific assessment, sources and limitations.
