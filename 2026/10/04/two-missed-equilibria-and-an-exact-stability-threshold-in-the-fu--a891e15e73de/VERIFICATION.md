---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Solving the equilibrium equations directly gives the origin and the two displayed off-origin branches, with no others. Fresh symbolic reconstruction gives the origin characteristic polynomial lambda(lambda-12)(lambda+3)(lambda+35), so the origin cannot be stable. The two quartic characteristic polynomials and Routh first columns in the package were independently reconstructed. Numerical root counts at representative points on each side of the exact threshold agree with the symbolic Routh sign classification, and the threshold factorization isolates one simple imaginary pair.

## originality

PASS

The primary article explicitly states that the origin is the only equilibrium and later interprets a high-d regime as stable at that origin, despite its own displayed origin eigenvalue 12. It does not state the two missed equilibria or the exact off-origin stability threshold. Exact DOI/title/equation searches and Resultary searching found no same-system correction.

## value

PASS

The correction changes the local phase portrait of a published system: an off-origin equilibrium has an open stable basin below a sharp threshold, while the origin is never attracting. This directly affects interpretation of numerical attractors and control claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
