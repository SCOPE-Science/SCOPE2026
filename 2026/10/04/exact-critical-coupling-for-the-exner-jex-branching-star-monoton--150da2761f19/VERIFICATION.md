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

The proof was reconstructed from the negative-energy edge solutions and the central \(\delta\)-matching condition. At \(\kappa=2\), the axial endpoint condition with coupling \(-2\) selects a pure exponential for every axial length, so the critical energy is exactly \(-4\).

`verify_exner_jex_threshold.py` checks the symbolic/numerical critical value, the length-independence of the axial logarithmic derivative at \(\kappa=2\), the analytic formula for its length derivative, including representative sign checks on both sides of the threshold. It prints `VERIFY_OK`.

The numerical replay is supplementary. The all-length regime classification follows from the exact matching equation, strict ground-state monotonicity in the central coupling, and implicit differentiation.

The direct source was inspected in full text, including the theorem, zero-index remark, discussion, and the figure specifying the model parameters. No independent audit has been performed.
