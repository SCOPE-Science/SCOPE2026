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

# Reproduction and limits

The formal claim is proved analytically in `RESULT.md`, including the exact quotient-to-probability reduction, closed-form integration, positive-part correction, sharp transition and strict torus comparison. The following are computational cross-checks, not an external certification.

Run `python verify.py` with Python 3 and no third-party packages. The standalone verifier checks exact fractions \(67/180\) and \(59/90\), a Simpson integration of the positive correction against the elementary closed form at seven aspect ratios, and direct enumeration of the relevant deck translates against the closed-form nearest-image minimum at four aspect ratios. It also draws independent pairs of uniformly distributed quotient representatives to check the squared-distance expectation at four aspect ratios.

The verification execution passed with the following observed/expected sample means (each based on 150,000 samples):

| \((a,b)\) | sample mean | theorem | standard error |
|---|---:|---:|---:|
| \((1,1)\) | 0.37167708 | 0.37222222 | 0.0006704 |
| \((1,2)\) | 0.65642051 | 0.65555556 | 0.0010346 |
| \((2,1)\) | 0.95515399 | 0.95236031 | 0.0021379 |
| \((3,1)\) | 1.80645213 | 1.80832072 | 0.0046279 |

The maximum absolute nearest-image discrepancy in the 12,000 tested orbit pairs was \(7.105\times10^{-15}\). The universal equality and regularity statements are not inferred from this finite evidence: those conclusions use the complete exact derivation. The closed-form branch for \(a>b\) can lose relative floating-point accuracy at very large aspect ratios because of cancellation, whereas the integral expression is manifestly nonnegative and better conditioned.
