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

# Reproducibility and verification

The companion `verify.py` exhaustively enumerates all uniform permutations for each order \(2\le n\le8\). Without invoking the analytic conditional law to calculate its left-hand side, the program evaluates the empirical exact rational quantities \(\mathbb E[R_kX_{ij}]\), \(\mathbb E[R_k]\), and \(\mathbb E[X_{ij}]\). It then checks each entry of the piecewise cross-covariance formula, sums entries for every inversion pair to test endpoint flatness, and independently tests a nonconstant polynomial weight array.

Run with a standard Python installation: `python verify.py`. The executed run returned per-order assertion totals \(5,14,32,62,107,170,254\), respectively, giving **644 exact assertions passed** in total. No external packages or data are required.

**Limits:** Exhaustive testing of a finite sequence of orders does not certify the identities for all positive integers; that conclusion comes from the independent conditional-symmetry proof in RESULT.md. Previous aggregate joint-count theorems are not claimed original. No independent audit has been performed.
