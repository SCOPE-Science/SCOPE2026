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

Run `python3 verify_period2.py` with standard Python 3. No third-party dependencies or downloaded datasets are required.

The checker builds the exact \(16\)-state overlap graph from the five-bit condition defining \(H^2(X)=X\), verifies its characteristic polynomial with exact integer Newton identities, and separately checks all \(87{,}380\) Boolean valuations for cycle sizes \(2,4,6,8,10,12,14,16\). It checks the semantic equivalence to simultaneous knowing-whether, the cardinality of the period-dividing-two set, and the unique fixed event.

Expected output begins with `VERIFY_OK`. The finite checks do not establish the infinite family on their own; that follows from the cyclic-window bijection and characteristic polynomial identity. No independent validation or external formal certification has been performed.
