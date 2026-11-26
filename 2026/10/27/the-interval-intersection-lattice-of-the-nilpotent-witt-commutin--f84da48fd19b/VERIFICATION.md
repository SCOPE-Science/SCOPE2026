---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For positive label i write r=i+1. In fg'-gf' a first nonzero term of g of exponent s<=p-r must satisfy s=r, since otherwise (s-r)f_r g_s is nonzero below degree p. After subtracting a multiple of f, all exponents are >=p-r+1, giving exactly the claimed centralizer. The locus in g_i^2 of rank <=1 on the interval of coefficient columns i+1 through p-1-i is the product of an affine space and an irreducible rank-one cone. The leading-nonzero stratum is dense in it and agrees with the cited positive-label stratum, so these are global reduced equations. For label zero the unit centralizer is one-dimensional (differentiate g/f); the unit locus is dense in the irreducible nilpotent cone, and scaling in either coordinate yields all dependent pairs of nilpotents. Intersecting with g_b^2 cuts off low columns, and projection of the surviving rank condition to any intermediate label preserves rank <=1. This gives the stated geometry, dimensions and path. The count of nonzero rank-one matrices follows by choosing their column line in F_q^2 and then a nonzero d-vector of coefficients; 'row-space' in the frozen proof is a terminology slip only. At label zero, when f(0)=0, triangularity shows p-nilpotency iff the linear coefficient vanishes. For f(0) nonzero, D^p is a scalar times D; the top coefficient enters that scalar with coefficient (p-1)! f(0)^(p-2), as only the top derivative term followed by p-1 constant derivative terms contributes a top-coefficient summand to D^p(x)(0). The resulting nilpotent count is q^(p-1), and scaling the nonzero dependent pairs gives the same point-count expression at (0,0). These arguments use equations and constructions over the prime field and count all extension-field points, not just prime-field checks.

## originality

PASS

Existing component and centralizer theorems are ingredients. The supported contribution is the simultaneous reduced intersection classification, including the interval rule, determinantal models, dimensions and extension-field counts. The related low-characteristic census does not give that classification, and the strongly relevant accessible passages stop at the component/stratum level.

## value

PASS

A reducible commuting variety is not understood solely by listing its components. The uniform global rank conditions give a usable model of how these components glue, produce a codimension-one path rather than just a component count, and provide exact simultaneous-intersection counts useful even when several strata contribute. These are natural structural invariants of the family, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
