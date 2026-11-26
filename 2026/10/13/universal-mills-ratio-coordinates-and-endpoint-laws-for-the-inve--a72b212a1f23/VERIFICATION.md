---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Uniqueness is in the reduced variable x=sqrt(lambda/mu), not the pair (mu,lambda); all positive pairs with the optimum ratio are equivalent. In the new variables, the entire objective is G(rho,z)=Phi(rho z)+phi(rho z) M(z) since 2x^2=(1-rho^2)z^2/2. Its z derivative is phi(rho z)(1-rho)((1+rho)zM(z)-1). The Mills integral gives 1-zM(z)=integral u exp(-zu-u^2/2) du over u>0, strictly decreasing from 1 to 0. Thus the root determines the unique interior global minimum. At the root G_rho=z phi(rho z)(1-rho zM(z)), giving the asserted exact derivative. For the singular endpoint, expand exp(-u^2/2) to first order with remainder bounded by u^4/8, and integrate against u exp(-zu); this gives 1-zM(z)=z^-2-3z^-4+O(z^-6). It follows that z=rho^-1/2(1+O(rho)), and both terms in the centered minimum contribute phi(0)sqrt(rho) at leading order. At rho=1 the reduced expression is identically 1, while the smooth branch selected by the distinct equation zM(z)=1/(1+rho) has a finite limit z*. The one-sided derivative at 1 is z*phi(z*)/2 and 1-rho=2/(kappa+1), yielding the stated O(kappa^-2) error and the optimizer estimate. Independent numerical check using the Taylor series for the Gaussian integral and exponential brackets z* between 0.61200318096248076 and 0.61200318096248077 and reproduces z*phi(z*) to the shown digits. Replay: RESULT.md lines 57–127; VERIFY.py lines 13–65 was inspected, not executed, and provides sampled numerical checks only.

## originality

PASS

Credit the reduced minimizer, phase-transition location and equivalent stationary equation to Hu–Lu–Zhou–Zhou. The supported distinct refinement is the exact envelope derivative and the matching sharp optimizer and value expansions at both ends, not the renaming of the prior first-order equation or qualitative monotonicity on its own.

## value

PASS

The singular square-root rise from the sharp threshold and coefficient of the 1/kappa deficit at large thresholds quantify how useful the optimized probability bound is, and the optimizer laws tell how the shape ratio must be tuned to reach it. This is a useful quantitative refinement of an existing optimization problem; the elementary change of coordinates by itself would not warrant a pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
