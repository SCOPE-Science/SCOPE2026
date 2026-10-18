---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the predator-extinction orbit with tau_l=0 and psi(0)=0, the prey solves xdot=rx(1-x/K). Hence d(log(K-x))/dt=-rx/K and exp(integral -rx/K)=(K-x_T)/(K-x_0)=B/A. This cancels the A/B factor in the exact printed source multiplier, leaving rho=(1-p2 E_l)e^{-mu T}, strictly in (0,1) for finite T and 0<p2 E_l<1. Witness r=2,K=100,mu=1,eta=3/5,h=30,p1=3/10,E=2,p2=1/10 gives A=48, B=30, T=log2, p2<3/16 and nevertheless rho=2/5. Independent Fraction computation confirmed the cancellation and exact counterexample. The assertion is local orbital stability under the same state-dependent impulse criterion as the source, not a classification of positive cycles.

## originality

PASS

The exact 2026 Xu–Zou primary PDF prints the unsimplified ratio and then the erroneous converse implication p2<pbar => instability. The logistic integral evaluation removes the proposed threshold. Earlier weighted-harvesting models do not visibly establish this cancellation for the same general predator Allee condition. This is a substantive primary-result correction, with earlier inaccessible source risk noted.

## value

PASS

Corrects the proposed harvesting stability threshold in an identifiable published nonlinear impulsive model: stability is uniform over the stated admissible predator-harvest parameter range, changing the interpretation of management regimes and undercutting a downstream instability premise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
