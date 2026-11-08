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

Conditional max part distribution for uniform ordered compositions n has counts A_n(r,m)=B_n(r,m)−B_n(r,m−1), B_n(r,m)=[z^{n−r}](1+…+z^{m−1})^r; dividing each row by C(n−1,r−1)>0 does not affect determinant signs. For n≤9 independently reconstructed every row by cut-subset enumeration and exhaustively checked all C(n,k)^2 minors for 1≤k≤3, 15,111 exact minors in total, none negative. For n≥10 the three rows r=2,3,4 and decreasing maximum labels floor(n/2)+2,+1,+0 have count matrices shown in proof by unique-max configurations plus extra two-max odd case; direct determinant expansion gives −6(q²−5q+2)<0 at n=2q and −12(q−4)(q−1)<0 at n=2q+1, q≥5. Symbolic family proof covers ALL n≥10, supplementary exact calculations n=10..79 only test arithmetic.

## originality

PASS

Exact conditional run/maximum distribution and first-order stochastic monotonicity are known. Their statements do not logically imply TN3 sign regularity of point masses. The complete sharp threshold n=9/10 and two persistent parity-dependent 3×3 obstructions are not contained in the inspected underlying distributions or published covariance-coupling result.

## value

PASS

Third-order total nonnegativity is a natural strong shape/dependence property of a conditional longest-run kernel; its exact finite cutoff is a nontrivial complete classification. Finite exhaustive lower-side certificate plus explicit forever-negative parity-dependent minors resolve a precise mathematical structural gap. First-order stochastic monotonicity alone does not settle these third-order signs, so it is not a known-table reprint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
