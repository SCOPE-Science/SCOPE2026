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

Run `python3 verify.py` in a directory containing that script. Expected terminal output begins `VERIFY_OK`.

**Actual checks.** The checker constructs the finite Fermi-plus-flip kernel directly for the specified four-agent, two-triad witness. It enumerates all 16 states, checks stochastic row sums and the exact normalized-payoff bound, compares rows in total variation and relative entropy at five finite exponent values, checks a common four-update entrywise lower bound, and tests that the witness row discrepancy divided by \((2/3)^\gamma\) tends to a positive coefficient. The complete checks executed successfully.

**Proof scope and limits.** The universal payoff inequality, coupling estimate, Doeblin minorization and exact witness asymptotic are proved symbolically in `RESULT.md`; finite tests are not substituted for any universal quantifier. Uniqueness of the stationary law uses \(\mu>0\). The convergence bounds do not establish an infinite-population phase-transition result or any behavior under other update mechanisms. Independent audit has not been performed.
