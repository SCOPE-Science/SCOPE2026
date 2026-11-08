---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For 1<=p<q, gcd(p,q)=1, rational phases generate min(q,n+1) distinct length-n factors in prefix-count chain order. Iterated deletion of first ones and appending them preserves prefix dominance: the one-position vectors obey coordinatewise ordering after every iterate. Each internal phase cut either changes total ones or makes disjoint 01-to-10 moves at positions congruent to the cut. Exactly when the last moved one has rank <=k does T^k identify adjacent factors, equivalent to the final affected index j<=H=floor((kq-1)/p). The residue-class interval gives the deficit B; H is never divisible by q, giving sharp last collision at n=q+H-1. Independently recomputed 15,260 exact counts and 1,204 sharpness/boundary checks using literal cyclic factors and iterated map. Finite tests supplement but do not prove all integers.

## originality

PASS

Campbell–Rampersad 2026 introduce tortoise complexity and analyze paperfolding/Thue–Morse; their full original PDF has no Christoffel formula. Carey–Clampitt 2018 treat Christoffel partitioned factors but not the tortoise operator. A previously known rational one-iterate formula and irrational Sturmian all-iterate statements are acknowledged as prior; neither automatically covers q-periodic modular collisions for all k>=2. PASS qualified by possibility of an unindexed equivalent sorting language result.

## value

PASS

This resolves a naturally posed combinatorics-on-words image-complexity question across every iterate k and length n on rational mechanical periods, identifies the sharp final collision, and explains genuinely periodic deviations from the irrational case. It is not a renamed one-step formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
