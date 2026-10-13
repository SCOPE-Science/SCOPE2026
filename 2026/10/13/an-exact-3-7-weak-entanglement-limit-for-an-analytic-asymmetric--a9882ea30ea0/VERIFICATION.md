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

The proof uses the exact outcome-0 projector probabilities for the two-qubit state and the standard asymmetric threshold identity. The critical symbolic checks are:

1. Under the six-parameter scaling, the coefficient of \(\theta^2\) in the ideal Bell value is
\[
-\frac1{16}\left[a^2f^2+8af+6b^2-8b+6d^2+8d+4u^2\right].
\]
Completing squares yields the displayed upper bound \(4/3\).
2. The one-sided no-click penalty is \(M_A=-(1+u^2/4)\theta^2+O(\theta^3)\).
3. For the explicit angles, direct Taylor expansion gives the coefficients \(4/3\), \(-25/9\), and \(-1/9\) for \(Q\), while \(M_A=-\sin^2\theta\).
4. Series division gives the limiting threshold \(3/7\) and first corrections shown in the result.

`verify.py` uses only the Python standard library. It numerically re-evaluates the exact probability formula for several decreasing values of \(\theta\), checks that \(Q>0\), verifies convergence toward \(3/7\), and checks the completed-square coefficient identity exactly on rational inputs. These calculations are replay evidence; the analytic identities, not the finite evaluations, prove the stated limit and scaling-class sharpness.

Unproved limits: the displayed scaling class is not shown to include every possible asymptotic qubit strategy. Therefore no global efficiency lower bound is asserted.
