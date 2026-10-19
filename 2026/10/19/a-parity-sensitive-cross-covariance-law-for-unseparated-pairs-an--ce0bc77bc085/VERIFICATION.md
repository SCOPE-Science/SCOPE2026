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

# Verification evidence and limits

The theorem is proved analytically in the result document using conditional counting and an explicit rank-nullity argument. A standalone Python 3 script checks finite instances without relying on the symbolic proof: it enumerates every permutation of size \(n=2\) through \(n=8\), obtains empirical joint-event counts exactly, verifies all displayed indexed covariance entries, and verifies the aggregate covariance and matrix rank. Its second check constructs each scaled covariance matrix for \(n=3\) through \(n=40\) and uses rational row reduction to confirm the predicted parity dependence.

Run \(\texttt{python3 verify.py}\) from the extracted package. The finite checks are corroboration, not a proof for arbitrarily large \(n\). There is no external or independent validation claimed.
