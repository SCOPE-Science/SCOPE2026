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

# Reproduction of the analytic checks

From a working directory containing the packaged `standalone_check.py`, with Python 3.10+, NumPy, and SciPy installed, run:

```sh
python standalone_check.py
```

Expected output begins with `PASS: 36 parameter sets`, reporting 72 generator-versus-beta-moment comparisons, 144 tail/bias comparisons, and 1044 zero-flux checks. The script computes beta densities independently using the special-function implementation, integrates their first two raw variance moments, compares them to stationary-generator recurrences for the second and fourth position moments, and checks the balance of the two environment-conditioned fluxes, and numerically approaches the closed beta-tail coefficient and universal extreme-state ratio. The zero-flux check is an independent numerical check only; the transport derivation in `RESULT.md` gives the analytic identity. The finite tests do not prove the heavy-tail coefficient, conditional Gaussianity, uniqueness, or any infinite-parametric statement; these follow from the displayed proof and elementary beta/Gaussian asymptotics. Verify the latter by redoing the beta-endpoint integral and the Gaussian power moment in Steps 4–5.

The test covers a subset satisfying \(\theta>2\) so that the fourth moment is finite. The theorem covers all \(\theta>0\), including infinite-variance cases. There is no external certificate or independent audit.
