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

Execute `python verify.py` with Python 3 and no optional dependencies. Its direct method enumerates every possible distinct co-player subset and evaluates both focal-strategy payoffs with exact fractions. Its separate method computes the hypergeometric generating function and evaluates the two-marked-player second-difference formula. They agree in 796 payoff comparisons and 532 curvature identities for populations of size 4 through 9, all group sizes, and multiplier values 1/4, 1, 3/2, and 3. It also reconstructs the four-player two-switch witness exactly:

\[
\bigl(\Delta(1)/c,\Delta(2)/c,\Delta(3)/c\bigr)
=\bigl(1/9,-7/60,1/10\bigr).
\]

These finite tests are reproducibility checks. The universal statement rests on the explicit one-marked-player and two-marked-player proofs in `RESULT.md`. No computer-assisted infinite exhaustion, formal proof certificate, or independent audit is claimed. The method does not examine arbitrary realized-payoff updates or spatial interactions.
