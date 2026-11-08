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

For an involution with f singleton and m paired orbits, equivariance forces exactly f^f(f+2m)^m maps. A constant power must converge to one fixed-point root; rooted Cayley trees on fixed vertices contribute f^(f-1), and a weighted rooted forest on m paired orbits contributes f(f+2m)^(m-1). The Prüfer edge weights f to fixed sink and 2 to each other paired orbit give the latter exactly; product yields f^f N^(m-1), including f=1,m>=1, whereas m=0 gives f^(f-1). The n-ary table to X² swap-commuting transformations is bijective and preserves powers, yielding n^(n²-2). A separate direct enumerator counted all commuting maps for nine (f,m) values f=1..3,m=0..2 and agreed in each case, including 189/1323 for f=3,m=2. Finite tests corroborate, not establish the all-f,m proof.

## originality

PASS

The centralizer/pairmorph correspondence and Cayley trees are known, but the exact all-involution constant-power law and its magma-monoid power enumerator were not found in compared primary source content. Novelty is best-of-knowledge and subject to older centralizer power-class work.

## value

PASS

The probability that a uniformly random permutation-centralizing endomorphism eventually collapses is a natural dynamical statistic. Its surprising independence of the involution orbit type (subject to fixed points) and exact magma-power count are mathematically meaningful closed classifications rather than routine idempotent counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
