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

The standard-library checker `checker.py` enumerates the seven line-complement tetrahedra, all simplices, and the free translation orbits. It confirms the explicit quotient attaching words, signed integer cellular matrices, chain identity, determinantal divisors \(1,1,7\), and the free face used in the equivariant collapse. It is run with `python3 checker.py`.

The homotopy equivalence is proved by the explicit cellular cancellation of two generator–relator pairs in `RESULT.md`. Matrix ranks alone do not certify an attaching-map homotopy type; the cell argument supplies that step. The integral covering module is derived from the universal-cover chain complex, not inferred from a rational trace.

Independent audit has not been performed.
