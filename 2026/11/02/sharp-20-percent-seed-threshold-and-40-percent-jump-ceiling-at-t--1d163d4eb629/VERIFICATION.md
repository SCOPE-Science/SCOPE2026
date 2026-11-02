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

The algebraic proof in RESULT.md is the source of the all-parameter assertions. The included standalone `verify.py` runs in Python 3 without third-party packages. It checks the exact witness with `fractions.Fraction`, the strict prevalence-peak inequalities across three pairs of rational transmission perturbations, 840 rational positivity-and-bound cases, and a sequence approaching the sharp bound. The test suite's finite grid is not interpreted as an exhaustive argument.

The crucial inequalities are \(\beta I_1=u(1+u^2r)<1\), \(r<(1-u)/u^3\), and the positivity factor \((2u-1)(u^2-2u+3)>0\). Their algebra and the global peak position (via falling susceptible stock) are explicitly proved in RESULT.md rather than inferred from numerical integration.

At the tie \(I_1=I_2\), only the one-sided limits of cumulative attack are claimed, so results do not depend on how a software implementation breaks an equal-peak tie. The limit \(J\to2/5\) approaches a boundary with \(\gamma\to1\) and \(\beta I_1\to1\); this boundary is expressly excluded from the strictly positive theorem.

Independent audit and external validation are not performed.
