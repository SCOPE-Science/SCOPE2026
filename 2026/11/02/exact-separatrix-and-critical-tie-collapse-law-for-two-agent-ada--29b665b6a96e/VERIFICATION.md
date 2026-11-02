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

# Reproducibility and limits

Extract `verification.py` to a directory and run `python verification.py` with Python 3, NumPy and SciPy installed. It numerically integrates the reduced two-person ODE using adaptive DOP853, checks conservation at independently sampled times, tests consensus and separation on both sides of the derived threshold, and checks the critical \(t^{-1}\)/\(t^{-2}\) limits on three different kernels or parameter choices. The expected terminal message is `rational kernel, three regimes PASS`, after the exponential-kernel test messages.

The packaged checker was executed from the embedded-file directory and completed successfully. Its 80 general phase/invariant test cases, two exponential critical tests, and one rational-interaction three-regime test use floating-point arithmetic. Its tolerances and time horizons are visible in the code; they are not exhaustive, certified enclosures or substitutes for the analytic proof. The proof's nonstandard steps are the exact conserved quantity, the scalar separation argument and the double-zero expansion at the threshold. Independent external validation has not been performed.
