---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

A smooth (2,3) divisor on P1 x P1 has genus (2-1)(3-1)=2 and a finite degree-two ruling; in characteristic three its equation U^2 A(S,T)+UV B(S,T)+V^2 C(S,T) is geometrically smooth exactly when the homogeneous binary sextic B^2-4AC is squarefree, including at infinity. Twelve ternary coefficients modulo projective scaling give (3^12-1)/2=265720 normalized sections. The source provides an exhaustive test, an independent rational-fiber interpolation method, and the 576 transformations of PGL2(F3) x PGL2(F3). Independently programmed polynomial gcds and rational-fiber counts over all 265720 normalizations gave 139392 smooth sections and 6096 smooth sections with N1=8. An independently built 576-matrix coefficient representation classified the 6096 maximal models into 15 orbits, with orbit sizes eight of 576, four of 288, two of 144 and one of 48. Independent F9 point counting and sextic factorization on representatives gave nine orbits with type (6), N2=12, four with (4,2), N2=10, and two with (2,2,2), N2=14. In turn a2=(N2+6)/2 gives zeta coefficients 9,8,10. The all-model original generated 139392-line CSV was only hash-identified, not completely retrieved due transport size; the independent full coefficient census and two source algorithms support counts. No abstract isomorphism classification is claimed.

## originality

PASS

Best-of-knowledge priority after direct comparison of the precise final mathematical statement, known stronger results, equivalent formulations, special cases and searched databases. Prior common premises/corollaries are explicitly excluded from the asserted original contribution; literature completeness is not claimed.

## value

PASS

The specified bidegree gives genus-two curves with two distinguished morphisms of degrees two and three, so ruling-preserving orbit classes encode nontrivial embedded moduli data. The complete 15-class and 6096-section inventory refines the already known eight-point bound by exact Frobenius ramification partitions and three zeta numerators, notably excluding the possible (3,3) type. This natural complete small-field classification cannot be read off from the scalar maximum point theorem, and its value does not require broader-field generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
