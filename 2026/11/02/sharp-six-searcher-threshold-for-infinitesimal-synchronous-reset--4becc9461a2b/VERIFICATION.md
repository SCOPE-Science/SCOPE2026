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

Run `python3 check_restart.py` in Python 3. The package code uses only exact integers and `fractions.Fraction`. It establishes outward enclosures for the infinite series by processing the first 10,000 terms at precision \(10^{32}\) with floor/ceiling arithmetic and adding analytically justified rational tail bounds. It verifies positive \(D_N\) for \(N=5,6\), negative \(D_N\) for \(N=7,8\), and \(h_9<2\), which extends the negative sign to all \(N\ge9\). The reflective survival identity, renewal identity and divergence regimes are proven in the result and are not inferred from code. Independent mathematical audit: not performed.
