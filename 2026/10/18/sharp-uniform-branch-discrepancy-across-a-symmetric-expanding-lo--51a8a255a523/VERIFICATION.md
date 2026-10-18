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

The analytic certificate has five states indexed by parity, discrepancy, and a closed position interval. Each possible branch transition is explicitly included in `RESULT.md`. It relies only on \(0<\beta(\beta-1)/2<1/2\), \(\beta(d-1/2)\ge L\) and \(L+\beta s\le R\), all verified symbolically from \(1<\beta\le\sqrt2\). Hence it establishes the bound for **every** length and real allowed parameter.

`CHECK.py` checks the parameter inequalities using exact fractions for four representative slopes and replays 33 initial rational points for 401 steps each using exact rational arithmetic. These finite checks are secondary confirmation and do not prove the universal assertion. The period-parity and invariant-measure results derive from integrating the proved finite-window bound.

Historical comparison is limited to the literature explicitly listed; original full-text inspection was completed for Section 4 of the 2023 paper and the specific renormalization statements in the 2009 paper. No independent mathematical audit has been performed.
