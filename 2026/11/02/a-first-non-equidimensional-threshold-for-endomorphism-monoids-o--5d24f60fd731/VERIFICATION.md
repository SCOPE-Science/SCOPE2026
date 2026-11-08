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

Unital endomorphisms send nilpotent generators into the maximal ideal and all cross-product relations split independently by target coordinate branch. For d=2 no constraints; one n^2-dimensional affine component. For d=3 row equations a_i a_j=0 yield n distinct maximal coordinate spaces each dim n+1 and n^n products. For d=4 equations a_i a_j=0 and a_i b_j+b_i a_j=0 force either all a=0 (L0 dim2n) or one nonzero a_s and b_i=0 for i!=s (Ls dim n+2), with all c free. These n+1 affine components are pairwise noncontained for n>=2, in every field/char, giving product component multiplicities binom(n,j)n^j and dimension 2n^2-j(n-2). Disjoint rational-point counts give [q^{2n}+n(q-1)q^{n+1}]^n, and analogous d2,d3 formulae. For n>=3 component dimensions differ; n=2 all nine dim8. Independent direct polynomial multiplication enumerated row cases (n,d,q)=(2,3,2),(3,3,2),(2,4,2),(3,4,2),(2,4,3), producing 12,32,32,112,189 respectively, all formula-matching. Scheme nonreduced structure not claimed.

## originality

PASS

The exact same truncated-cross automorphism family had a published arbitrary-field normal form, inspected in full. Its theorem computes invertible group only, not noninvertible End reduced scheme, all-endomorphism counts or component dimensions. Perepechko realization of other nonassociative monoids and Timofeeva fibre-product presentation do not imply this specific End locus classification; broad monomial-algebra representation varieties remain a priority risk.

## value

PASS

Determining the entire reduced unital endomorphism variety of a basic Artinian fibre-product algebra and its first non-equidimensional threshold is a natural algebraic monoid classification across all n and all characteristics. It detects structural behavior invisible from the already known unit group and yields exact finite-field counts; no claims for d>=5 or nonreduced schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
