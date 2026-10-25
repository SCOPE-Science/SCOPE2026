---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

A homogeneous ternary quartic has 15 coefficient bits, 32767 nonzero forms. A geometric singular point annihilates the degree-10 Jacobian-ideal map S6⊕(S7)^3→S10; when smooth, three general quartic members of this basepoint-free ideal form a degree-(4,4,4) regular sequence with socle degree 9, proving the rank-66 converse over an algebraic closure and hence F2. For each of seven rational lines the restricted binary quartic is a square precisely when the s^3t and st^3 coefficients vanish. I inspected the complete C++ bit-rank enumerator and independent Python orbit/Groebner source, compiled and ran the 32767-case exact enumerator afresh, reproduced 10920 smooth forms and the entire 8×6 point/bitangent joint table, with bitangent frequencies 3072,5278,2352,105,112,1. Independently checked concurrent bitangent triple and four-line multiplicities from the exact per-subset output; finiteness is the full universe, not a sample.

## originality

PASS

Best-of-knowledge priority assessment distinguishes the actual joint/exact invariant and mathematical implications from stronger but non-covering frameworks; pertinent primary statements were compared and residual risks are explicit. Joint rational-point and rational even-contact-line spectrum of smooth plane quartics over F2

## value

PASS

A simultaneous exact distribution of F2-rational points and F2-rational even-contact lines on all smooth genus-three plane quartic equations is a natural arithmetic incidence invariant, not a random slice. Its empty support at five and six lines, rigid three/four-line incidence, and explicit frequencies are independently usable refinements of a known classification; the finite universe is complete.

The dated certificate retains the supplied scientific assessment, sources and limitations.
