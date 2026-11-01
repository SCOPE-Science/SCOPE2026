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

Every nonzero cubic in four F2 variables is included in a 2^20-1 enumeration. Smoothness over the algebraic closure is equivalent to the four quadratic partials forming a parameter regular sequence, detected by rank 56 among degree-five multiples; each ternary plane section is geometrically smooth iff its three derivatives have zero-dimensional affine common zero, detected by rank 15 among degree-four multiples. Fresh independently written C++ enumerated all 322560 smooth cubics, classified their fifteen planes and found the exact t spectrum 0:1708,4:11340,6:68320,7:10080,8:94500,9:60480,10:64512,11:10080,12:1540. New group-generator orbits of the 1708 t=0 forms have sizes 28 and 1680. Both representatives and stabilizer orders match. All conditions are exact finite linear algebra, not finite-extension sampling.

## originality

PASS

The classical surface taxonomy and Vikulova 2023/2024 already identify the exceptional highly symmetric orbit (28 equations, stabilizer 720). Karaoğlu 2021 full 36-orbit classification covers underlying cubic surfaces, including a stabilizer-12 orbit; we explicitly do not claim new projective cubic surface classes. The assessed novel invariant is the property of having NO geometrically smooth F2 rational hyperplane section and the complete incidence spectrum across all 322560 surfaces; the inspected 36-orbit study does not tabulate this property or the 1708 zero-section census. Strong residual risk is that it could be mechanically extracted from known orbit tables; present full exact relation is recorded.

## value

PASS

A sharp obstruction to small-field finite Bertini is a natural geometry question: zero transverse sections occur not only for the known F2 space-filling 28-surface orbit but for a second 1680 orbit, and all others have at least four. Complete transverse-plane spectrum is a meaningful geometric incidence invariant despite pre-existing overall cubic-surface classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
