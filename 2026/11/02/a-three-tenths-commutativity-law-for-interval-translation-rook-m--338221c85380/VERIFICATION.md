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

For nonzero maps (a,c,length) between contiguous intervals, exact disjointness of domain of x with image of y and image of x with domain of y separates into two independent placement counts. For length l,k with l+k<=n, there are 2*binom(n-l-k+2,2) disjoint ordered interval placements in each pair of coordinates, giving 4*binom(n-l-k+2,2)^2. Summing over lengths yields Z_n=sum_{r=1}^{n-1}(n-r)r^2(r+1)^2=n(n-1)(n+1)(n+2)(n^2+n-1)/30. Independently evaluated this identity symbolically as zero difference and directly counted pairs at n=2,3,4,5: 4,44,228,812. For xy=yx nonzero, equality of first nonempty domain points forces a=u or c=a or w=u or c=w, bounding such pairs by 4n^5. Total monoid size is 1+n(n+1)(2n+1)/6, so normalized commuting probability tends to 3/10 and nonzero-product commuting share is O(1/n). The argument handles zero-element pairs separately; finite enumeration is only a cross-check.

## originality

PASS

Best-of-knowledge qualification: actual Resultary searches and directly compared primary mathematical results show no decisive prior implication of this exact final claim; component methods, previously known examples, accessible full-text scope and named inaccessible-source risks are explicitly distinguished.

## value

PASS

A finite inverse monoid of contiguous partial translations is an intrinsic and nontrivial object in rook semigroup theory. Its exact mutual-annihilation polynomial and limiting commuting density expose a structural phenomenon—almost every commuting pair annihilates each other—rather than a renamed generic semigroup identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
