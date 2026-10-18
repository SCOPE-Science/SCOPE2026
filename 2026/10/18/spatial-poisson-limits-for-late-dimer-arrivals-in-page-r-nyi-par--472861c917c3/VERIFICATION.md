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

# Verification and reproducibility

Run `python3 check.py` using Python 3 and only its standard library. The program checks exact rational values for finite endpoint-vacancy probabilities, exact marginal edge-acceptance probabilities for every path size \(2\le n\le9\), and the decreasing-causal-chain condition needed for finite-window approximation at radii one and two. Expected completion message begins `VERIFY_OK`.

The infinite assertions do not follow from finite enumeration. Their proof instead uses: the endpoint-vacancy integral recurrence; the alternating exponential Taylor bound; the no-long-decreasing-priority-chain coupling; a local-dependence Poisson bound; and mixed factorial moments for marked windows. The quantitative count bound applies to a fixed compact range of centered times and does not quantify total variation of a continuous spatial process. The scalar Gumbel jamming law predates this result.
