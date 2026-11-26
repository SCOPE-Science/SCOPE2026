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

For distinct a,b, ba is absent precisely when last(a)<first(b); missing aa identifies letters occurring once. This recovers exactly the pair (P,S) from the signature. Singleton positions are disjoint; every neighboring interval of a singleton contains its point, so marked vertices are independent and simplicial. Conversely enlarge intervals by less than half the minimum comparable gap (if there are no comparisons, any sufficiently small positive enlargement works). This makes all incomparabilities strict overlaps while retaining every comparison; a further small perturbation removes endpoint ties. For a simplicial marked vertex its closed neighborhood is a pairwise strictly intersecting finite interval family, so max of left endpoints is strictly below min of right endpoints. Choose an interior point avoiding all endpoints and contract the marked interval there. Independence means the contracted intervals were disjoint, so the contractions do not interfere. The endpoint word realizes the original pair (P,S), uses one occurrence per marked letter and two per unmarked letter, and meets the unavoidable lower bound. Adjacent simplicial vertices have identical closed neighborhoods: each neighbor of one must be adjacent to the other or equal to it. Hence the induced components are cliques and each contributes the choice of zero or one marked letter. This yields the stated labeled polynomial, including isolated vertices and q=1, when it is z+z^2.

## originality

PASS

The supported distinct contribution is the exact full-support realization criterion and resulting minimum-length polynomial. Total Simon indices, first/last representations and general results about reduced words are not claimed as new.

## value

PASS

It answers a natural inverse question: which distinct-letter ordering patterns can coexist with specified singleton letters? The exact marking criterion makes this decision from the incomparability graph and gives an all-alphabet length enumerator, qualitatively more than reproducing an index table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
