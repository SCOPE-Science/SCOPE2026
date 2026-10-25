---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Universal proof reconstructed: for normalized unconditional Schauder E not equal to coordinate ell1, finite-support density yields positive a with ||a||=1<sum a_i. Hahn--Banach gives f0 norming a; lattice modulus f=|f0| is positive with ||f||=f(a)=1, and some a_i>0 has f(e_i)<1. The sign isometry fixing i and negating all other basis coordinates gives x=(Sa,0), F=(S*f,1), ||x||=||F||=F(x)=1. The positive parts satisfy x+=(a_i e_i,0), F+=(f_i e_i*,1), ||F+||=1 and F+(x+)=a_i f_i<a_i=||F+||||x+||. Coordinate functionals determine the E* lattice parts because finite spans are dense. Conversely, if every finite-support norm is ell1 additive, completion E=ell1, X=ell1 on the enlarged index set; equality in Holder forces each F_j=sign x_j on occupied coordinates, so HNAp holds for both Jordan parts, including zero parts and all normalized/scaled pairs.

## originality

PASS

The closest sound original source, arXiv:2106.05935v1, proves two-dimensional HNAp and exhibits one three-dimensional failure, not an iff classification over all normalized 1-unconditional Schauder Banach sequence lattices. Its L1 sufficiency is known and explicitly credited. Independent result-index searches return the assigned published record as a self-match but no separate valid universal extension result. An apparently encompassing 2026 Proposition 4.1 is mathematically false: its asserted universal Jordan upper bound is contradicted by the original 2021 octagonal example (sum 5/4>1), so it cannot supply a valid prior proof of this classification. AHSp and operator BPBp sums treat a distinct property. Best-of-knowledge originality PASS, not proof of historical priority.

## value

PASS

The exact one-scalar-summand HNAp permanence question is natural because the introducing paper proves every 2D absolute norm has HNAp but constructs one failing 3D scalar-l1 extension. The new iff identifies the precise geometric obstruction: norm nonadditivity on disjoint positive coordinates. It classifies every finite/countable normalized unconditional Schauder sequence lattice, including Euclidean and supremum planes, and explains failure by a uniform norming pair. A structural all-space boundary is a meaningful independent mathematical fact; it is neither an arbitrary slice nor a table recomputation. Significance is restricted to HNAp and this normed/direct-sum class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
