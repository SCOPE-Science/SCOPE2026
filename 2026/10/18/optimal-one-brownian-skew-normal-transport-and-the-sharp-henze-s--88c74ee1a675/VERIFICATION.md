---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two marginals coincide by conditioning the Gaussian pair ((Z+aE)/sqrt(1+a^2), E) on E>0 and by probability integral transformation. Both have second moment one by reflection of the density. Strict quadratic uncrossing gives the unique increasing optimal joint law; the auxiliary coupling differs for every nonzero a by its positive conditional variance given Z. Differentiating under the integral gives -2 phi(y) phi(ay)/(1+a^2), so division by the positive density gives the claimed sensitivity. For r=phi/Phi, the mean of the upper-truncated normal is -r(t)<t and its variance is 1-r(t)(t+r(t))>0; hence |r'|<1 globally. The L2 sensitivity remainder is at most |a|+sqrt(2/pi)*a^2 since ||Q_a||_2=1. Integrating along the signed parameter interval gives the claimed constant and cubic remainder for either sign. The auxiliary cost follows from covariance (1+a^2)^(-1/2), and squaring the leading quantile displacement gives 2/pi and thus pi/2. The calibrated scalar-step comparison multiplies by sigma^2 h and is only against the unshifted driver; the zero-drift case is exact.

## originality

PASS

The supported distinct contribution is the quantified comparison of two couplings of the actual skew-SDE step to its Brownian driver, not the skew-normal sampler, optimal transport theorem, or CDF differentiation taken separately. No materially equivalent combination was identified in the sources checked.

## value

PASS

The scalar skew-SDE discretization gives a specific reason to preserve a transition kernel while minimizing its displacement from a given Brownian driver. The exact leading ratio separates a choice of coupling from a choice of marginal at the drift-scale cost, and the all-parameter L2 bound makes this a controlled comparison rather than just substituting into transport optimality. This is not a claim of increased strong order or numerical speed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
