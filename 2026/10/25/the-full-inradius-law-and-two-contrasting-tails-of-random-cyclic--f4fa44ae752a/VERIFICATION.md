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

# Verification of exact random cyclic-triangle inradius law

## Analytic checks

The normalized half-angle simplex density is \(8/\pi^2\), the simplex coordinate area is \(\pi^2/8\), and the half-angle inradius product is \(4\sin X\sin Y\sin Z\). The Jacobian-one angle-difference transformation yields the displayed survival integral. Near three simplex corners the log-singular hyperbolic sublevel area gives \(6/\pi^2\). Near the unique equilateral maximum the Hessian ellipse gives \(8/(\pi\sqrt3)\). No finite experiment is substituted for those arguments.

## Reproduction

Run `python inradius_law_check.py` under Python 3 with `numpy`, `scipy`, and `mpmath` available. The checker was executed using the embedded source, not an earlier unrelated program. The following are actual success tokens from that execution:

```text
DIRECT_CARTESIAN_AND_DIRICHLET_ANGLE_IDENTITY_OK 360000
FIVE_INDEPENDENT_CDF_CHECKS_OK
KNOWN_INRADIUS_MOMENTS_REPRODUCED_OK
CDF_INTEGRATED_MOMENTS_OK
SHARP_EQUILATERAL_ENDPOINT_COEFFICIENT_OK
LOGARITHMIC_THIN_ENDPOINT_COEFFICIENT_TREND_OK
ALL_CYCLIC_INRADIUS_LAW_CHECKS_OK
```

At thresholds \(0.05,0.1,0.2,0.3,0.4\), analytical CDF values were \(0.164930053728\), \(0.289469233743\), \(0.500063271454\), \(0.682648234206\), and \(0.847672428678\), each agreeing with independent Cartesian sampling within the stated error tolerance. Numerically integrating the full survival function reproduces the **previously published** mean \(12/\pi^2-1\) and second moment \(5/2-24/\pi^2\).

## Limits

The CDF numerical evaluation and the endpoint coefficient trend tests are finite independent consistency checks. They do not prove the full distribution or the two asymptotic equivalents. Those claims rest on the analytic geometry and integration in `RESULT.md`. No independent mathematical audit was performed.
