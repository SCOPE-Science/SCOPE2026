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

# Verification notes

Run `python verify.py` with Python 3 and SymPy. The program checks the transformed cubic and Gauss equations as **polynomial identities**, the seven rational Fano-plane base points, independent evaluation constraints of rank seven, two-dimensional base-point tangent ranks, a vanishing Jacobian wedge, and both the integral Steiner equation on squared coordinates and its exact characteristic-two specialization. The algebraic-closure exhaustion of the base locus, the complete anticanonical system and its degree, and the inseparable field-extension argument are additionally proved in `RESULT.md`.

The classical dual quartic's fourth-power reduction is distinct from the reduced dual variety. No numerical experiment is treated as an infinite-field proof. The mathematical review is self-review only; no independent audit has occurred.
