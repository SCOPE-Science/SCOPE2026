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

The central infinite-set theorem is established by the constructive proof in `RESULT.md`. No finite experiment certifies arbitrary subsets of the natural numbers. The supplied `checker.py` enumerates every bit sequence of length from one to eight interpreted as a finite initial segment followed by a constant infinite tail, computes its complete Boolean-modal closure, and tests the claimed size and number of atoms.

To reproduce, run `python3 checker.py`; the expected printout is `OMEGA_MODAL_ONEGEN_VERIFY_OK 510`. The core independent computations use the Boolean truth table and the exact prefix-preimage operation on a finite prefix plus a stable tail, rather than simply evaluating formulas on a finite truncated order.

Limits: No attempt was made to exhaust infinite-switching characteristic sequences by code. Possible older-priority overlap is separately disclosed; external independent validation has not been performed.
