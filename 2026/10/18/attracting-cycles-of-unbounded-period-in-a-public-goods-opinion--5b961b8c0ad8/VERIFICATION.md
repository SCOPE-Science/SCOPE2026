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

# Verification evidence and limits

The standalone `verify_cycles.py` uses exact `fractions.Fraction` and SymPy rational matrices. Execute `python verify_cycles.py` beside the extracted RESULT.md. It verifies exact source-parameter identities, the cyclic update and formula including the tie convention for sizes from two to eight, divisor assertions for primitive periods, and twelve explicitly solved periodic orbits on positive-off-diagonal directed networks with three to six players. It checks that the actual threshold decisions match the prescribed cyclic itinerary at every phase, and that the exact return state is periodic. This is a finite consistency check; the arbitrary-size and arbitrary-network-near-cycle theorems are proved analytically in RESULT.md.

No asynchronous convergence statement is tested or claimed. The original conditional all-defection theorem applies to another weight regime. No external independent scientific audit was performed.
