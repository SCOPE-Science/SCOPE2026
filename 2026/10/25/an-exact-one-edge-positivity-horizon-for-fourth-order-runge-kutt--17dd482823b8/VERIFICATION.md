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

# Reproduction and limits

Run `python verify_rk4_star.py` with SymPy installed. The checks form every polynomial exactly over the rationals, compare each one-hop and two-leaf entry with its independent matrix-power expansion, test weighted inequalities, and inspect the exact three-state counterexample and eigenvalues. An observed PASS for 387 combinations is a finite regression check, **not** a universal proof. The full result follows from the explicit matrix identities and the strict derivative-discriminant bound in RESULT.md. No independent audit has been performed.
