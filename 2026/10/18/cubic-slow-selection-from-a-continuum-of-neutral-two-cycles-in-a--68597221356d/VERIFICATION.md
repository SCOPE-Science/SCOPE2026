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
# Reproducibility and verified limits

The accompanying `verify.py` is standalone Python 3 standard-library code. Execute `python3 verify.py` in the directory containing it. The actual run printed `VERIFY_OK` after exact-rational checks of the actual two-step rational derivatives, the drift algebra, and the Jacobian trace/determinant, and numerical first-crossing tests for \(\varepsilon=0.002,0.0005,0.0001\).

For \(u_0=3/4\) and \(u_1=4/5\), the closed-form rescaled clock is \(11/48+(1/8)\log(6/5)=0.251956861265911\ldots\). The absolute errors in \(\varepsilon J_\varepsilon\) for the three test steps were respectively \(0.02604314,0.00654314,0.00134314\). They decreased but these finite observations are not an asymptotic proof. A matching left-branch test from \(u_0=1/4\) to \(u_1=1/5\) gave absolute crossing-time errors \(0.00195686,0.00045686,0.00015686\), respectively.

The actual mathematical support for all fixed-interior \(u_0\) and thresholds is the two-step Taylor expansion, the normal contraction estimate, the summable transverse residual, and the Grönwall/Euler convergence argument in `RESULT.md`. The claim excludes both simultaneous near-midpoint scaling and post-endpoint boundary layers. No third-party review or independent audit has been performed.
