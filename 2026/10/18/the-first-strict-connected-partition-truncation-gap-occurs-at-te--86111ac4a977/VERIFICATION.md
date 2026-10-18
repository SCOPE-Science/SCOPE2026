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

# Verification and proof boundary

Running `python3 verify.py` reproduces `verification_output.txt` by exact integer arithmetic using only the Python standard library. The checker uses exhaustive recursively generated rooted-tree isomorphism codes and unrooted center codes, evaluates every subset of the \(k-1\) edges of each tree on \(4\le k\le10\), and cross-checks component profiles by disjoint-set union and independent graph traversal. It asserts the complete class totals \(2,3,6,11,23,47,106\) and computes the rank-prefix collision classes.

At \(k=10\), one unordered pair collides at rank \(5\), none at rank \(6\); its members have diameters \(6\) and \(7\). Their six-edge forest coefficient for \((4,2,2,2)\) is respectively \(1\) and \(0\). The root-multiset recursion and center-isomorphism argument in `RESULT.md` establish why finite enumeration covers every unlabeled tree of these orders; checking selected examples alone would not establish this.

These checks prove the stated finite result only. They do not address larger orders or guarantee novelty against unavailable or unindexed literature. No independent external assessment is claimed.
