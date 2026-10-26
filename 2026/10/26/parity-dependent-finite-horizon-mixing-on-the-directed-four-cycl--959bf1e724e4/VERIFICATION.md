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

# Verification

Running `python verify.py` with Python 3 performs 1,830 exact rational comparisons of direct cyclic transition distributions with the Fourier-inverted formula for horizons 1 through 30 and parameters \(p=j/60\), \(0\le j\le60\). Additional assertions check exact even-horizon center values, sample odd-horizon local improvement and the phase-aligned witness for odd \(h<100\). Expected ending: `PASSED 1830 exact rational Fourier/convolution comparisons, parity bounds, odd improvement and asymptotic witness checks`.

The all-horizon and asymptotic arguments are analytic, not computer-assisted. No independent audit or external validation has been performed. Exact odd-horizon global minimizing parameters remain open within the statement.
