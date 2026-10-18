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

The mathematical argument is contained in `RESULT.md`. The standalone `check_folded_geometric.py` uses only the Python standard library. Run `python3 check_folded_geometric.py`; the observed successful output is `PASS exact rational checks: 3921`.

The checker verifies exact rational examples for the probability coefficients, the logarithmic derivative recurrence, the folded probability summation with exact geometric residuals, positivity of jump intensities, the adjacent canonical inequalities and log-concavity minors. The infinitely quantified claim and the sharp threshold rest on the analytical monotonicity proof and the cited canonical-sequence characterization. Independently performed mathematical review is not claimed. No additional software or datasets are needed.
