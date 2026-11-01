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

The all-order proof is the exact discrete Fourier correlation extraction, the invertibility of the three-site cyclic amplitude-sum map when \(3\nmid N\), the parity restriction from the two-step correlations, and the forced single phase ratio from adjacent products. The converse explicitly constructs the only second phase class.

The standalone `CHECK.py` uses only the Python standard library and independently builds complete spectrograms, inverts discrete Fourier samples at three lags, and compares the predicted partner signals. The actual package-local execution returned `CHECK_OK 29120`. These finite tests are supplementary; there is no inference from numerical experiments to arbitrary cyclic orders.

The scope excludes zero coordinates, dimensions divisible by three, other window weights, and stability in noise. Independent mathematical audit: not performed.
