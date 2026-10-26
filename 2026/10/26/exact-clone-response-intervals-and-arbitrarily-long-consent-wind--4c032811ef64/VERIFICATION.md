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

# Verification of the clone-response interval theorem

The finite AWVC criterion is evaluated directly from its strict blocking inequality with every nonempty coalition of voters disapproving the target. The independent analytical evaluator instead computes the affine clone inequality before adding copies. For the explicit five-voter family, both evaluators are compared against the proposed exact interval \(1\le t\le 3h-2\), for \(2\le h\le36\) and \(0\le t\le3h+3\).

A second check samples 100 strict-ranking profiles with top-prefix approvals for every pair \(3\le n\le8\), \(3\le m\le9\), then checks five distinct clone counts per profile. The deterministic seed and complete implementation are in `check.py`. All 25,270 exact-integer comparisons passed when executed with Python 3.

These computations check finite cases only. The universal affine identity follows by counting new alternatives ranked unanimously above the target, and the unbounded five-voter family follows by evaluating the three possible disapproving coalitions; both are proved without extrapolating the finite tests. No independent audit or external certification was performed.
