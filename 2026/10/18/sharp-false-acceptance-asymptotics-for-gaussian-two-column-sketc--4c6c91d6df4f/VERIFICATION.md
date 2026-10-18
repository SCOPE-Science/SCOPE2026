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

# Verification evidence and limits

The included standalone `verify_condition.py` runs exact beta-integral quadratures at three unequal condition-threshold pairs, checks the strict positivity and constants of the unique Wishart saddlepoint, and verifies the equivalent exact tilted-normalization expression for the sharp multiplier. Direct Gaussian Bartlett simulations compare the finite-probability integral with approximately 180,000 Gaussian draws per parameter set. Independent tilted Gaussian importance samples, approximately 180,000 draws per setting at sample size 300, compare the predicted sharp leading constant. The random-number seeds are fixed in the code.

For \(\kappa=3\), \(\tau=2\), the computed exact value for \(s=100\) is \(2.52080258035\times10^{-5}\), while the leading asymptotic yields \(2.70467510988\times10^{-5}\). The sharp rate is \(0.080042707674\), and the multiplier is \(0.809702966340\). Other tested pairs are \((2,1.5)\) and \((4,2)\). The actual extracted-program run reported **PASS: 36 deterministic, quadrature, Gaussian-sampling and importance checks**.

These finite tests cannot certify the \(s\to\infty\) statement or global originality. Universal mathematical steps are derived in RESULT.md using exact Bartlett identities, constrained Wishart rate minimization, an exponential likelihood tilt, and the local Wishart density. The result is limited to fixed, real, two-column bases independent of the sketch. No external independent audit was performed.
