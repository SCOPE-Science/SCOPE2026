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
# Verification and scope

The standalone executable diagnostic `checks/circle_tongue_check.py` requires Python 3 and SymPy. Run `python checks/circle_tongue_check.py`. Execution checked four exact symbolic identities and 90 numerical orbit/multiplier identities, including 2-sided angular perturbations for five forcing strengths and the half-turn case. The mathematical proof is in RESULT.md, notably the necessity-and-sufficiency reduction to the quadratic `Q`, sign-changing evaluations at `q=s²`, `q=2s`, `q=1`, and the monotone interval dynamics of an orientation-preserving circle homeomorphism.

The code checks finitely many inputs and does not establish the universal theorem. The analytic argument supplies completeness, including both critical endpoints and `theta=pi`. No third-party proof certification or independent scientific audit is claimed.
