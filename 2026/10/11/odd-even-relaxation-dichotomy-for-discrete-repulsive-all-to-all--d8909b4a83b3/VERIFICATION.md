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

# Verification procedures and limits

The standalone Python 3 standard-library script `verify.py` performs seeded reproducible checks of the full \(N\)-oscillator update, exact even-family invariance, formula for its order parameter, strict scalar decrease, tested odd-size one-step order-parameter contraction and the coordinate increment bound. It compares the asymptotic residuals at two large finite cutoffs to check the predicted logarithmic correction. When run as packaged, it reports `VERIFY_OK; deterministic assertions: 2864`.

The script is deliberately only a finite diagnostic. The all-odd-size uniform estimate rests on the exact Gram inequality, matrix spectral bound and complex-exponential Taylor remainder in RESULT.md. The even-size infinite-time asymptotic rests on a proved invariant family, a controlled local expansion and summability of renormalized inverse-square increments. No finite numerical comparison is treated as an infinite limit proof. The novelty comparison with one publisher article remains limited by inaccessible full text; it has not been declared decisively absent from that article.
