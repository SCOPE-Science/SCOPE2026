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

Analytic verification covers every positive real width, every finite cardinality, arbitrary real endpoints, and any competing finite positive-length interval union. Four critical steps are proved explicitly in RESULT.md: torus pushforward zero and finite integer endpoint deconvolution; mean-square Fourier averaging and integer coefficient rigidity; local autocorrelation slope fixing component count; and oriented difference measure equivalence.

The exact arithmetic checker is included as `verify.py`; execute `python verify.py` with Python 3 standard library. The recorded execution returned:

`VERIFY_OK finite exact comparisons: 588 ; candidate interval unions: 351 ; three-window targets: 300 ; six-window homometric witness: verified`

For the finite integer-endpoint enumeration, targets have three unit-width disjoint intervals, and competitors include all positive integer-length strictly separated interval unions of total length three in the enumerated window. The checker uses signed endpoint autocorrelation coefficients, not floating FFTs, and checks the six-point literature example. It is finite corroboration, not a universal proof or an independent audit. Exact noiseless Fourier magnitudes and the indicator hypothesis are necessary; there is no numerical stability result.
