---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Fixed support F of size r has a unique lightest extension, of weight N+r-U(F), because each eligible off-support pair can be zero independently. If F contains disjoint a,b, a pair disjoint from exactly one is an X-to-Y pair (X=a union b), excluding a,b themselves. Unique disjointness for the full support otherwise requires a cross pair between a and b (a pair disjoint from both can never work). A third support pair with 2, 1, or 0 points in X eliminates respectively 2(n-4), 3(n-5), or 4(n-6) of the X-to-Y candidates, offsetting the at most four cross pairs for n>=7. A pairwise intersecting family is a star or a full triangle: the U counts are 2(n-3) for a two-edge star, 3 for a three-edge star (outer leaf pairs), 0 for a larger star, and 3(n-3) for a triangle. All satisfy the bound 4(n-4). Consequently W>=N+2-4(n-4) for r>=2, with equality only for a two-edge matching (strict for two intersecting edges or r>2). Subtract the singleton weight 2n-2 to get (n-5)(n-8)/2; the empty support of weight N is never competitive. Counting singleton or unordered disjoint two-edge supports gives the claimed 105, 238 and binom(n,2) with no other extensions. My independent bitset recursion (branches/independent_kneser_supports.py 7 8 9) exhausts 27896, 1683218 and 40999516 supports at those orders and obtains 11/105, 14/238 and 16/36 (weight/count), with support-size distributions matching the frozen record. These cutoffs are exhaustive for minima at tested orders because the weight is at least 2r. The bundled crosscheck's description overstates its small supplemental loop: the code skips size 3 at n>8. The decisive bounded-support enumeration and infinite proof do not depend on that loop.

## originality

PASS

There is material indexed overlap for the two-edge support branch via complementation, but it does not supply the Kneser optimization across all support sizes. The supported distinct contribution is the full KG(n,2) exact optimum transition and optimizer census. The related ordinary Roman and unique-response findings use different requirements.

## value

PASS

For a standard Kneser family the exactly-one-neighbor constraint at zero vertices changes the optimizer class precisely at two adjacent boundary orders. The exact counts explain the tie at n=8 and the eventual rigidity. The all-support bound makes that structural distinction, beyond the matching branch already visible on the complement, available without solving an optimization at each order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
