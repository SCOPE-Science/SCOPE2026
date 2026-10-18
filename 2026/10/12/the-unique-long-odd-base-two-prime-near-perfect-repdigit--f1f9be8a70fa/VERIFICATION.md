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

The Ren–Chen theorem gives only three specified two-distinct-prime families plus 40. For e=v2(N), all satisfy N<2^(3e+2); for odd g, LTE gives v2(U_l(g))=0 for odd l and v2(g+1)+v2(l)−1 for even l. Since a<g≤9, e≤5+log2(l), whence 3^(l−1)≤N<2^17·l³ and monotonicity bounds 3≤l≤19 and 1≤e≤9. This converts infinite families into 31 explicitly enumerated prime-admissible candidates. An independently written exact arithmetic sieve of all 31 candidates against g=3,5,7,9 and l=3..19 produced only 40 as 1111 base3; sigma(40)=90=80+10, with proper d=10 and omega=2.

## originality

PASS

Ren–Chen 2013 classifies all 2-prime near-perfect numbers parametrically, but does not present the repdigit intersection. Hasanalizade 2022/2023 asserts a two-digit upper bound and base-three absence for 2-prime near-perfect repdigits, which 40=(1111)_3 directly contradicts. Published even-base classification (Resultary listed) has disjoint hypotheses. The new all-four-odd-base exhaustive bound and exception are not established by the original statements without further work.

## value

PASS

An exact correction to a published false exclusion coupled with a proven universal finite reduction and complete natural four-base classification; not merely pointing out 40, because the sieve closes all other parameter cases in this range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
