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

The mathematical identities and critical witness in `RESULT.md` were independently reconstructed from the specified matrices and checked in exact symbolic arithmetic with the accompanying `verify.py`. The checker evaluates the three possible two-row coordinate selections, DEIM/Q-DEIM pivot inequalities, the projected characteristic polynomial, the sharp optimization identity, and a rational SPD example with eigenvalues \(2,3,4\). It also performs 100 seeded exact-rational phase checks. Its current run completed successfully.

Reproduce with `python verify.py` using Python and SymPy. The proof is analytic; the sampled tests alone are not an exhaustive verification of the real-parameter continuum. The only reviewed method is two-row unmodified dsRR in exact arithmetic, not floating point or randomized oversampling. No independent audit is asserted.
