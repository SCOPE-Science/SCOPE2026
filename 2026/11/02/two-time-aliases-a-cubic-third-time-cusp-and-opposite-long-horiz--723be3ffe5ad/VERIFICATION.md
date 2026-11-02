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

The formulas in RESULT.md are proved for all real \(h>0\), all finite real symmetric \(L\preceq0\), and all data satisfying the stated positivity conditions. For the actual signed unbounded limit, additionally assume \(\ker L\ne\{0\}\). The proof contains the feasibility converse, both explicit parameter branches, all-time formulas, exact cubic discrimination and all-time sign classification. Run `python verify.py` to reproduce 22,426 arithmetic evaluations: these tests do not certify the infinite statements, which follow analytically from the proof. The code depends only on Python's standard library. No independent audit was conducted. Semigroup trajectories and higher-order ETDRK4 are outside scope.
