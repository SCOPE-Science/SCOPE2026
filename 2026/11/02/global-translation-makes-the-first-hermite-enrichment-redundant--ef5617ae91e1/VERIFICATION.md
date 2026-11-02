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

# Verification methods and limits

The analytical proof in RESULT.md establishes the claims for every finite nonzero positive Borel mixture; the numerical script does not approximate an infinite quantifier.

Run `python3 verify.py` with Python 3 and no third-party dependencies. The script was executed from this research package's source directory and reported:

```
VERIFY_OK: 15 overlap quadratures, 63 energy derivative checks, 4 multi-peak optimizer comparisons, 5 sharp doublet regimes, signed boundary
```

Exact analytic checkpoints: the Gaussian translation overlaps have coefficients \(c_0,c_1,c_2\) in RESULT.md, satisfy \(c_0'=c_1/\sqrt2\) and \(c_1'=c_2-c_0/\sqrt2\), and yield \(Q_1'=2c_1c_2\). The positivity of the mixture makes \(c_2\ge0\) with equality only at a point-mass center. The two-Gaussian stationarity function has one positive root if and only if \(a>\sqrt2\), by monotonicity of \(\tanh(z)/z\).

The source literature was compared for equivalent implications, general coverage and aliases; closest prior work primarily treats adaptive movement/scaling of Hermite bases or Gaussian mode-finding, rather than the combined globally optimized projection identity. Missing or inaccessible specialized literature remains a priority risk. No independent audit or certification has been completed.
