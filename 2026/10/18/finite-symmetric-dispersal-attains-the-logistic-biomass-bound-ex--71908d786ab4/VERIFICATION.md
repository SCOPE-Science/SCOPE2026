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

# Verification

The finite certificates in `verify.py` are self-contained, run under ordinary Python 3 and require no network or nonstandard package. They exactly verify both three-patch parameter calculations, the positive witness's three stationary equations, the ellipsoid deficit identity at the zero-migration equilibrium, and a strictly positive necessary-cut violation at the unique minimum target of the impossible witness. The script also compares an independent exact-rational Edmonds–Karp max-flow implementation with exhaustive closed-cut enumeration for 600 seeded finite graphs (including ties and disconnected cases).

Run `python3 verify.py` and check its PASS line. The general necessity/sufficiency is proved in RESULT.md and is **not** inferred from the finitely many computational cases. Independent audit has not been performed. No upper-bound rate constraints, dispersal losses, or asymmetric flows are verified by this result.
