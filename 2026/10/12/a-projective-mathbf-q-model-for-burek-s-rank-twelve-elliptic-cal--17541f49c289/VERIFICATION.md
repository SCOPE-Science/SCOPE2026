---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The complete reproduction files are `verification/verify.py` and `verification/certificate.json`. Install SymPy 1.13 or later and execute `python verification/verify.py` with the certificate in the same directory. The executable recomputes the elliptic section identities, the discriminant factorization, all 96 section-node incidences, the tangent-plane ruling tests, and the local Weil classes using exact arithmetic over \(\mathbf Q(i)\), then compares its results with the bundled certificate. The final success token is `VERIFY_OK`.

The enumeration is exhaustive because Burek's Proposition 7.1 identifies precisely the 24 roots of the discriminant polynomial and four nodes over each root; the checker verifies the distinctness and defining equations. The passage from nonzero local class to a projective small resolution is mathematical, using the completed conifold class group and Veronese relative Proj, not inferred from a finite test alone. The public certificate does not independently audit that geometric argument or claim the arithmetic Mordell–Weil rank.
