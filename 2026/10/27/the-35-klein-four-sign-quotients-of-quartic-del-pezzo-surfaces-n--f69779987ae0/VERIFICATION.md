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

The exact finite checker is `verify_rank_two_sign_quotients.py`, executable under Python 3 without third-party dependencies. It enumerates the sixteen projective sign vectors and thirty-five rank-two subgroups, verifies the \(10,15,10\) distribution, and prints `VERIFY_OK`.

The checker is not a substitute for the geometrical proof. The fixed-point counts follow from smooth intersections of two diagonal quadrics and the classification of local reflection and sign quotients. The degrees follow from Hurwitz, and the fundamental groups from simply connected covers and inertia quotienting. The weighted-sextic model follows by taking an exact invariant ring.

No independent audit or independent validation has been performed. Source-level novelty comparison is based on the explicitly identified inspected articles and database searches, not on universal uniqueness certification.
