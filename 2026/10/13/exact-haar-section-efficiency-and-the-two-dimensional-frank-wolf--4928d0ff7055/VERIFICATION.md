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

# Reproduction and evidence

Run `python3 verify.py` with an ordinary Python 3 standard-library installation. The script checks the exact rational arithmetic equality for every \(2\le n\le200\) and \(1\le d\le n\), then samples Haar orthonormal frames by Gaussian Gram--Schmidt with seed `271828`. It compares the first-projection squared mass, tangential derivative moment, and small-angle squared-norm difference on four dimension pairs. The observed samples fell within the script's explicitly stated stochastic tolerances and concluded with `VERIFY_OK`.

The all-dimension theorem is certified by the **written analytic proof**, not by bounded numerical tests. Its critical steps are the exact norm-difference identity, full periodic Fourier coefficient inequality, the projection-idempotence moment calculation and dominated convergence for coalescing directions. None of these steps uses an external computational oracle or an extrapolation from finite data. Reproduction of the source-derived expected-rate corollary additionally requires the original strong-set-convexity, uniform rolling-ball, smooth convex objective, fresh Haar sections and exact section-LMO assumptions; the proof invokes the inspected Proposition 3/Theorem 1 of the cited preprint.

No separate audit or independent scientific validation has been performed. This file does not certify any unproved stronger theorem about high-probability rates or non-Haar sampling.
