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

# Reproducibility and scope

The included `CHECKER.py` passed 26 assertions requiring Python 3 and SymPy. The checks include two separate derivations of the exact two-site variance and fourth cumulant (direct exponential convolution and the stationary polynomial-generator system), four rational switching rates, exact large- and small-rate limits, and a positive fourth cumulant for a sign-changing response. It also tests the known one-coordinate trapped-telegraph fourth cumulant. These finite symbolic tests are supportive; they do not certify the whole finite-dimensional statement. The all-network proof uses the exact four-time telegraph cumulant, the positive matrix semigroup, and dominated convergence.

No independent audit was performed. The complete text of Pawula's 1987 general output-moment work was not available; its abstract indicates possible implicit priority overlap. Stationarity requires a Hurwitz drift; the sign conclusion requires nonnegative probe and input responses. No thermodynamic-limit or arbitrary signed-probe extension is claimed.
