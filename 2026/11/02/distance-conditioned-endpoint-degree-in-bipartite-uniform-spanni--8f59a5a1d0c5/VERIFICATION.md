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

The proof uses a restricted graph-Laplacian determinant, exact factorial moments of the additional endpoint degree, and elementary likelihood-ratio inequalities for Bernoulli convolutions. The attached standalone `verify_exact.py` enumerates small bipartite spanning trees and executes exact rational checks. Run with `python verify_exact.py`; the recorded output is `PASS 47930 exact assertions`.

An additional standalone exact-rational sweep checked 1,566,873 monotone-likelihood-ratio cross-products for both part sizes from 2 through 34. Finite tests cannot certify the statements for all sizes: the all-size conclusions come from the determinant identity and log-concavity proof. No independent audit or external formal proof certificate has been performed.
