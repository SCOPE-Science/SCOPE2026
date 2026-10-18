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

Run the included standard-library checker using `python3 verification/check.py`. It exercises 2,185 independently generated parameter cases with integer lengths from 1 through 23. It checks (i) recovery of all lower-index coefficients from isolated outer lags; (ii) the exact one-collision identity at lag \(n\); (iii) reconstruction of the entire autocorrelation from \(4n+1\) equally spaced intensity samples; (iv) eigenvalues of the independently assembled two-real-coordinate Gram matrix against the claimed exact singular squares; and (v) explicit preservation of every autocorrelation by each balanced conjugate-reflection partner.

Expected terminal line: `PASS 2185 parameter cases; exact edge coefficients, finite Fourier sample inversion, real singular spectrum, and balanced two-fold fibers`.

These finite numerical comparisons are not an exhaustive proof. The proof in `RESULT.md` uses identities valid for all integers \(n\ge1\) and all complex parameters with \(b\ne0\). Standard floating-point error is tolerated only in the checker, not in the theorem. No independent audit or formal certification has been performed.
