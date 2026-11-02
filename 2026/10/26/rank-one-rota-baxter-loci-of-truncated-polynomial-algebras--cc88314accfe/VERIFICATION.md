---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For nonzero rank-one P=a⊗phi, inserting into the weight-zero identity shows phi(xa)=c phi(x); then a²=2ca and applying phi to a²x two ways yields c²=2c² and c=0 in any characteristic. Therefore a²=0 and phi(aA_n)=0. In k[t]/t^n, v(a)=i>=ceil(n/2), with image subspace W_i=t^iA_n and allowable phi in U_i=W_i^perp. Each C_i is a rank-one determinantal/Segre cone of dimension n-1; incomparable components, pairwise intersections W_j⊗U_i of dimension n-1-(j-i), and adjacent intersections are precisely the singular locus of the reduced union. Segre degrees sum; valuation stratum over F_q has q^(n-i-1)(q^i-1) maps, yielding 1+h q^(n-1)-sum_{j<h}q^j. An independent check directly tested the original basis identity and valuation criterion for q,n=(2,4),(2,5),(2,6),(3,4), including 8355 nonzero candidate maps; no infinite proof rests on enumeration.

## originality

PASS

General rank-one tensor reduction is elementary and standard Segre geometry is credited; untruncated polynomial RB classifications and Farooq 2026 square-zero truncations are different algebraic objects. The new specific reduced rank-one locus for arbitrary n>=4 and all fields, intersection/singularity structure, projective degree, and q-point strata are not implied by those studied special truncations.

## value

PASS

The rank-one solution space is a natural geometric stratum of an operator variety, and the filtration-indexed reducible equidimensional component decomposition with exact singular geometry and arithmetic point counts is a substantive complete classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
