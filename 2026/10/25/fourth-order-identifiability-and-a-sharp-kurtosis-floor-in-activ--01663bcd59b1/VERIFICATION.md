---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For independent centered stationary OU factors U,V (rates a,b>0), multiplication of Gaussian pairings gives R=e^{-(a+b)t} and F=e^{-2at}+e^{-2bt}+R². The quadratic z²-(F-R²)z+R² recovers unordered rates from t>0. The entire product path has zero odd moments; same (a+b,c²u²v²,D0) gives identical second-order displacement statistics. Conditional Gaussian mixture establishes kappa4(X_T)=3Var(S_T)>0. Independently derived fourfold covariance trace integral by Fourier methods and checked sharp asymptotic eta²*6(a²+3ab+b²)/(ab(a+b))>=30eta²/(a+b), equality iff a=b. Exact population inference only: no finite sample/noisy direct-force recovery promise.

## originality

PASS

Best-of-knowledge originality for the precisely restricted final claim: The original dimer reduction plus standard Isserlis identities permit derivation of formulas but provide neither the fourth-order measurement sufficiency statement nor the sharp constrained long-time kurtosis minimum. Novelty is the substantive model-specific assembled inverse theorem, not Gaussian pairing identities. Sources were compared for logical implication, not merely title and number overlap. Residual risks retained rather than treating unsuccessful searches as novelty proof.

## value

PASS

For an explicitly motivated active dimer with two latent relaxation rates masked by the stationary product, this gives the first informative cumulant order, a one-lag exact inverse reconstruction up to exchange, and a sharp integrated-displacement kurtosis floor. These resolve a natural observability limitation not mechanically supplied by the known MSD.

The dated certificate retains the supplied scientific assessment, sources and limitations.
