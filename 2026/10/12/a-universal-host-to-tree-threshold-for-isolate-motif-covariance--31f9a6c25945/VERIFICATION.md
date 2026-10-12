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

The enclosed \(\texttt{verify.py}\) enumerates all simple host graphs in ten motif/host-size cases, compares exact rational covariance in every edge-count stratum against the theorem, and tests six asymptotic sign examples. Its last run reported 113 finite-stratum equalities and six sign checks. The proof does not depend on this enumeration. Only non-induced copies are counted; injection multiplicities multiply the copy count by a constant and preserve the covariance identity. The threshold location is obtained from the analytic limiting expression. No independent audit or validation has been performed.
