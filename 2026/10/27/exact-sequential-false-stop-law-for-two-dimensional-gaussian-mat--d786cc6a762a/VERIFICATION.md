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
# Reproduction and verification

`verify.py` uses only the Python 3 standard library. Run `python verify.py` from the folder containing this file and the script; seeded Gaussian simulation will evaluate direct matrix formulas and compare them against independent one-dimensional Simpson quadrature. The executed output was:

```
case a=1, b=1, tau=0.5: theory [0.11750309741539608, 0.3379300580710263, 0.5445668445135776]; observed [0.11677, 0.33684, 0.54639]
case a=4, b=1, tau=0.5: theory [0.03024350182003487, 0.25978949520339095, 0.7099670029765741]; observed [0.03089, 0.25908, 0.71003]
case a=100, b=1, tau=0.5: theory [0.001212123269814386, 0.24717657747280655, 0.7516112992573791]; observed [0.00119, 0.24999, 0.74882]
case a=7, b=2, tau=1.4: theory [0.06562761183105556, 0.3502563461096229, 0.5841160420593214]; observed [0.06652, 0.34907, 0.58441]
high-conditioning false-stop limit J(0.5)=0.247126056147587; at kappa=100000: 0.247129436449459
PASS numerical suite: 500029 trial/analytic checks (400000 sequential direct trials; 100000 residual-CDF trials)
```

In each direct matrix trial, the residual is explicitly projected after the first sample and the second sample is separately drawn. The direct squared residual is also compared with \(a^2b^2/d(U)\). A separate distribution experiment compares four empirical CDF levels to the analytic transformed-arcsine CDF. Exact isotropic formulas and near-anisotropic-limit quadrature are additionally checked. Monte Carlo comparisons permit sampling error up to \(0.008\) or \(0.009\), so these finite checks are not proofs of exact universal identities. The mathematical proof in `RESULT.md` establishes the statements without extrapolating from the tests.

No external audit or other-person verification was performed. The first-pass empty-state convention and possible earlier published equivalents remain explicit limitations.
