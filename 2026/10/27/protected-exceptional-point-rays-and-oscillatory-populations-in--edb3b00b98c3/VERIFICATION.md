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

Run `python verification.py` using Python with NumPy and SciPy. The verification independently assembles the 9-by-9 Lindblad superoperator from the qutrit jump matrices, checks the exact population projection against all nine matrix-unit inputs, checks the analytic propagator against independent matrix exponentials, confirms the root formula, and verifies the rank-two Jordan conditions at both exceptional rays. The script passed 1,820 finite assertions on the recorded run.

The global all-positive-parameter and arbitrary-diagonal-perturbation statements rest on the explicit polynomial/Cayley–Hamilton and quotient proof in RESULT.md, not on finite numerical assertions. The check program does not establish the absence of additional exceptional points elsewhere in the full Liouvillian. Independent external audit is not performed.
