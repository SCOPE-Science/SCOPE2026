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

# Verification of the two-Hermite half-line concentration law

The `verify.py` program requires Python 3 and no third-party dependencies. Run it from the extracted package directory using `python verify.py`.

The program evaluates Gaussian half-line Gram entries independently by composite Simpson quadrature and checks them against the Gaussian-tail formulas on 41 thresholds. It also checks positivity and distinctness of both eigenvalues; direct-versus-closed spectral defect calculations; reflection symmetry; an isolated positive root of the derivative equation; and derivative signs before and after that root on finite grids. The observed output was:

```
VERIFY_OK checks=527 tstar=0.748111391996229 Vmax=0.257120277198686
```

The analytic proof of uniqueness does not depend on the root-finder or grid resolution. It uses the strictly increasing integral ratio \(\int_0^1 e^{t^2(1-u^2)}du\) and strictly decreasing rational function \(2(1+t^2)/(1+2t^2)\). The finite checks are consistency diagnostics and do not certify the decimal last digits, historical originality, or unproved extensions. Independent mathematical audit has not been performed.
