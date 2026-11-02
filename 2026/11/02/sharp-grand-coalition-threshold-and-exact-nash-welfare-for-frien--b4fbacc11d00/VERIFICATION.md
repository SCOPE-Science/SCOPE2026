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

# Reproducibility

Run `python3 verify_cycle.py` from the extracted package. The program implements unrestricted coalition subset dynamic programming, computes every agent's utilities directly from the cycle graph, and separately evaluates the cyclic arc contribution recurrence. It compares the two exact integer optima through 12 agents, checks balanced two-arc improvements for cycle sizes 12 through 200 and checks the displayed asymptotic formula at four increasing sizes.

Observed result: `VERIFY_OK exact_all_partition_n=4..12 balanced_breakup_n=12..200 asymptotic_n=100,400,1600,6400`.

The program is a finite regression check, not a proof for arbitrarily large cycles. That proof is supplied in the analytic derivation in RESULT.md.
