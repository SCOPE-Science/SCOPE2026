---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

At 1/3<alpha<1/2 the bounded-mass extreme points on a fixed finite support have exactly two weights alpha and one beta=1-2alpha; separate affinity of convolution allows three such laws. For three 3-element supports the count at a sum is <=7; the corresponding counts for 2x3x3, 2x2x3 and 2x2x2 are <=5,<=4,<=3. A sharp 7 requires all three supports be 3-term arithmetic progressions with the same spacing, and the three pairwise heavy-set counts cannot all be 4 because their adjacent 2-subsets would require binary e_i+e_j=1 for all three pairs. Writing delta=3alpha-1, weighted expansion loses at least min(beta^3,beta delta^2) from W=7beta^3+15beta^2delta+12beta delta^2+3delta^3. Independent exact polynomial simplification gives W-beta delta²=alpha(7alpha²-6alpha+2) and W-beta³=3alpha²(1-alpha). Explicit U,U,V at sum3 and U,U,U at sum4 attain both branches; at alpha=2/5 both are 36/125. Truncation with displaced tail mass gives total-variation approximation for arbitrary countable support; endpoints alpha=1/3,1/2 follow directly or continuously. The independent source program was inspected for its 197568 exact finite pair checks, which corroborate but do not prove the unrestricted argument.

## originality

PASS

Kurauskas arXiv:2603.11043 Conjecture 1.3 explicitly posits the finite exact signed extremizer theorem; its Theorem 1.1 is conditional on sufficiently large variance and has (1+delta) slack. The primary article states exact cases alpha^{-1} integer or [1,2], leaving the interior alpha^{-1} in (2,3) unaddressed. Juškevičius–Kurauskas 2020/2021 Theorem 1 treats an even number of summands, and Theorem 2.27 cited by Kurauskas applies to #log-concave laws, not arbitrary weight arrangements with a light mass between heavy sites. The new three-summand incompatibility supplies the missing finite interior case.

## value

PASS

An explicit nontrivial sharp phase transition in a natural open three-summand Littlewood–Offord extremal problem, including all admissible integer laws and exact optimizing orientations. The weighted incompatibility step goes beyond a routine parameter substitution or table count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
