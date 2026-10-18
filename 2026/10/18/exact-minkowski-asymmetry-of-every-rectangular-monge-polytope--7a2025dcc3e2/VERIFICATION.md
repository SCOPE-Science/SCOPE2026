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

The exact-arithmetic verifier `verify_monge_asymmetry.py` was executed from this package's source file using `python3 verify_monge_asymmetry.py`. It passed on 60 parameter pairs with \(2\le p\le9\) and \(p\le q\le12\), independently enumerating 4,452 normalized vertices and 4,392 coordinate/adjacent-Monge facet inequalities. Every tested dimension had exact primal facet dominance, dual nonnegativity, exact equality of primal and dual objectives, and coefficient identities tested on every coordinate basis vector.

The infinite-family conclusion is not inferred from exhaustive testing. Its mathematical certificate comprises the explicit convex combination of normalized corner rectangles; the coordinate-maxima tie bound; the identity expressing matrix mass as nonnegative weighted facet slacks; and the inequality \(s+1\ge q+(p-1)(q-1)\). The source's full facet description is an external mathematical premise, and independent external publication-priority auditing has not occurred.
