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

The affine singular equations y^7=1, z=y^5, w^4+w^2=y give exactly fourteen geometric nodes. Artin–Schreier splitting over F8 establishes the Frobenius orbit partition (2,3,3,6). The finite-field formula X(F_{2^m})=q²+q+1+S_m is exact; independently enumerated S_m with a separate binary-field routine for m=1..8, and independently compiled a separate C11 enumerator for m=9..12, matching ALL twelve source sequence values. Exceptional P¹ corrections yield traces on K3 H²; Newton identities from twelve sums, rank22 and reciprocal functional equation uniquely recover the cyclotomic polynomial. Finite counts plus this global cohomological bridge, not extrapolation, establish every extension. Independent checks support the exact arithmetic and the proof uses standard K3 facts for the unrestricted cohomological conclusion.

## originality

PASS

Catanese and Schütt already construct the fourteen-node characteristic-two quartic and supersingular K3 resolution. The new claim is the explicit F2-model Frobenius descent and complete arithmetic zeta factorization, not the geometric node bound. Relevant primary sections were read; no exact same arithmetic result was found there, with usual unindexed-computation risk.

## value

PASS

A complete Hasse–Weil zeta function and geometric Frobenius orbit decomposition are natural arithmetic invariants of a highly singular small-characteristic quartic; the result distinguishes the singular surface from its smooth K3 resolution and determines every extension-field point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
