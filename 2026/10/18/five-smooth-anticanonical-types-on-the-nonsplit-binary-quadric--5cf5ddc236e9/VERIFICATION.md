---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The fixed Q has five rational points, dim H0(Q,O(2))=9 and hence 511 nonzero binary sections. An independent non-repository Sympy implementation independently tested all 511 candidates using exact four-affine-chart Groebner Jacobian ideals over F2, finding precisely 240 smooth divisors and point histogram {1:60,2:90,3:60,4:30}. The source enumerates full 120-element automorphism group via the five-point projective frame, with 17 total orbits and five smooth orbits sizes 60,30,60,30,60. The five-point incidence argument gives rank-five evaluation (15 nonzero sections through all five points), all reducible products of two secant plane sections, hence none smooth. Adjunction proves genus one; Hasse bounds rational point counts between one and five. The independently reproduced smoothness census is exhaustive, not mere F2 point sampling.

## originality

PASS

Earlier finite-field smooth-pencil constructions prove existence; characteristic-zero pencil/classical genus-one classification results do not explicitly entail the fixed nonsplit Q anticanonical orbit and rational-incidence census. An unindexed genus-one model table could nevertheless imply the counts, and the abstract isomorphism classification is not claimed.

## value

PASS

The anticanonical system on the unique nonsplit binary quadric is an intrinsic finite-geometric family. Its complete smooth-divisor orbit census and five-rational-point exclusion answer natural embedding and arithmetic incidence questions more informatively than existence of an individual elliptic curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
