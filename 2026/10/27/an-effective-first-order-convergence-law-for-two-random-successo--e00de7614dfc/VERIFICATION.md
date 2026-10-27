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

# Verification record

The standard-library checker `check_successor_local_law.py` enumerates every ordered pair of labelled linear orders of size 2 through 6 (533416 cases total), and verifies 20 exact first-moment identities for four explicit coloured-cycle patterns at each of five sizes. Expected terminal signal: `SUCCESSOR_LOCAL_EXACT_OK 533416 20`. The exact formulas use directed path contraction and distinct colour relations. These checks independently test small-instance counting, not the full factorial-moment convergence, bounded-degree locality or asymptotic limit. The general statements rest on the mathematical proof in RESULT.md. All algorithm inputs are fixed inside the supplied standalone script; Python 3 standard library suffices. No external independent review is asserted.
