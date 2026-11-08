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

For E_n with e_i^2=e_{i+1}, substitution proves exactly r_i^2=(2r_i+lambda)r_{i+1}, every n>=3 over every field. At lambda!=0, zero is isolated by invertible cyclic Jacobian; on the open all-r_i-nonzero locus t_i=1+lambda/r_i obeys t_{i+1}=t_i^2, so after removing t=1 the coordinate ring splits into t=0 and t^(2^n-1)=1 components. In positive characteristic p, the p-adic multiplicity of M=2^n-1 yields M0+1 geometric points, length M-p^a+2, and exactly M0-1 nonreduced geometric points when p^a>1; field-rational lambda=0 solutions follow by cyclic multiplication. All automorphisms of this perfect evolution algebra are monomial rotations and cyclotomic diagonal factors; only rotations act on diagonal R and Burnside gives g+1 operators and 1+(1/n)*sum_s gcd(g,2^s-1) orbits over Fq. Independent prime-field direct basis equations reproduce (p,n)=(3,4),(5,3),(7,3),(7,6), weight 1, plus rotation counts. The finite counts do not prove scheme local-length statements; their ring derivation does.

## originality

PASS

Best-of-knowledge original specific final mathematical result after explicitly excluding known foundational subclaims. All four equivalence/coverage/table/implication comparisons use stated primary reading, semantic search and uncertainty; no failure-of-search-as-proof assertion. The original claim is accepted without publication or unearned provenance.

## value

PASS

A scheme-theoretic, every-characteristic classification distinguishes reduced and modular nonreduced strata and counts rational conjugacy classes for a natural perfect cyclic evolution algebra family. The first nonreduced example n=4,p=3 is a real boundary; these are motivated infinitesimal invariants rather than mere periodic-point enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
