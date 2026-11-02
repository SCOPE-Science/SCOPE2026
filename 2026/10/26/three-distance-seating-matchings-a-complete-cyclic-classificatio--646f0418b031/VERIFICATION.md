---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Parity-class conservation gives an equal number of even-even and odd-odd length-two edges, forcing b even. When 3|n the n−1 length-three edges remain within even-sized mod-three classes, while the unique length-one edge leaves two odd residual classes, excluding the stated profile. For b=2t>0, the six explicit disjoint-endpoint tiles A=(1,0,0), B=(1,0,1), C=(0,2,0), D=(0,0,3), E=(0,2,1), F=(0,2,2) concatenate to give all residue classes of c modulo 3 with t≥1. For b=0, r copies of B and q of D plus a−r of A handle a≥r where c=3q+r; remaining a=0 and 3∤n cases admit the step-three Hamiltonian matching because gcd(3,2n)=1. The sole a=1,r=2 remainder is exactly the excluded 3|n case. The n=3 diameter-three boundary is covered. An independent exhaustive matching-mask recurrence checked n=3,...,8 and produced [5,9,12,15,20,25] admissible histograms, not the proof of all n.

## originality

PASS

Earlier even seating-couple work proves two-length and some special multiplicity cases and conjectures parity sufficiency in odd prime orders; the new exact three-shortest-length all-multiplicity theorem covers genuine positive a,b,c cases with b even and finds the exceptional 3-divisible composite profile. Some two-length special cases are prior and acknowledged, but do not imply the general constructive decomposition.

## value

PASS

Solves the first nontrivial full three-distance region of a concrete published seating-couples question, including the odd-prime three-length conjectural case and the sharp new composite-order obstruction. Explicit six-tile concatenations yield an algorithm for every allowable multiplicity triple, not a small isolated numeric instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
