---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For complete multipartite graphs, a nonempty selected set dominates iff it meets two classes or fills one class; its complement has no isolate iff empty or meeting two classes. For p=0 every singleton qualifies when N≥3, and the two blocks in K₂ form a coalition. For p≥2, singleton-class vertices qualify by themselves; vertices in large classes can pair across two large classes, leaving members of both classes outside. This proves the maximum N in both cases. With one large class and u=1, the only restrained dominating set is all vertices, hence the maximum is two. When u≥2 each clique vertex is itself restrained dominating, and splitting the large class into two proper nonempty blocks gives the asserted u+2. Theorem 2.1 of Dobrynin–Glebov–Golmohammadi supplies the upper bound by the ordinary coalition number: every block containing a universal vertex must be its singleton in an ordinary coalition partition, and the large class can contribute at most two blocks, since a pair of its blocks dominates only if it covers that whole class. Independently, if three or more blocks lie entirely within the large class, a union of two such blocks cannot dominate, and a potential partner containing a clique vertex either is already RD (another clique vertex and a large-class vertex remain outside) or contains all clique vertices and its union still leaves an independent outside. This also excludes more than u+2 blocks directly. It gives 4 for K_{3,1,1}. The uploaded checker was inspected, not executed; it visits all 101632 candidate partitions on 58 profiles through order 8, with validity tests pruned by the incumbent order. The proof, not enumeration, covers all orders.

## originality

PASS

The initiating paper states the order-N formula without a part-size restriction, while separately giving the correct star case. The new content is the exact corrected boundary, especially the non-star regime of one class of size at least three and at least two singleton classes. The later bound and the catalogue classifications of other coalition parameters do not supply that correction.

## value

PASS

This corrects the published exact value for a standard graph family, distinguishes where the conclusion remains true, and gives a non-star counterexample and a complete proof rather than only pointing to the visible star inconsistency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
