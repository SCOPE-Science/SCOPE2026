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

The result was checked with exact finite calculations and a complete symbolic argument.

Run `python3 verify.py` using Python 3 and the standard library. The program independently enumerates every proper coloring for each \(3\le q\le5\) and \(3\le n\le7\), obtains exact rational means and covariances, and checks them against the formula in RESULT.md. It also multiplies exact rational covariance and precision matrices, and checks every claimed off-diagonal sign for \(3\le q\le7\) and \(3\le n\le12\). Expected output: `VERIFIED_EXACT_ASSERTIONS 6605`.

Analytically checked steps: transfer-matrix eigenvalues and marked-color moments; the finite circulant Green-kernel inverse identity; the rank-one update; positivity and the exceptional triangle; strict adjacent and nonadjacent precision signs; and the large-cycle coefficient. Exhaustive checks at finite sizes do not certify unrestricted quantifiers by themselves. No third-party independent mathematical review has been performed.
