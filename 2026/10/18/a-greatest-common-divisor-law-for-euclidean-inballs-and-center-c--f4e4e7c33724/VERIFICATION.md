---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The source-level argument proves the result for every integer \(p,q\ge2\) using: (1) projected facet normals of norms \(\sqrt{1-1/(pq)}\) and \(2\); (2) the exact nonnegative grid-coupling dual gap identity; (3) the evaluated floor-process covariance; and (4) equality-case propagation giving precisely \(\gcd(p,q)-1\) independent closed-interval parameters. The contact-facet count follows from the number of distinct grid subdivision points.

Run `python3 verify_rectangular_monge.py` with Python 3 and no external packages. The included checker passed 1,806 exact rational parameter profiles across \(2\le p,q\le12\). Other checks during derivation included 169 exact dimension-pair normalization checks across \(2\le p,q\le14\), 5,839 parameter-grid contact checks, and numerical linear-programming spot checks. None is an exhaustive check over all dimensions or an independent mathematical audit. The mixed-difference and dual-certificate proof, not numerical output, supports the unbounded quantifiers. Independent audit: not performed.
