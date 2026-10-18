---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Use universal f(x)=r x(1-x)<=r/4: any sufficiently negative innovation moves all states below -L with fixed probability p>0. From x<=-L, quadratic negative drift thresholds a_(j+1)=r a_j^2/2 yield uniformly positive probability >=1/2 of infinite descent by the union bound and finite second-moment Chebyshev tail Σ4v/(r²a_j⁴)<=1/2. Markov property and Doob bounded martingale convergence applied to tail event A=X_n→-infinity upgrade uniform P_x(A)>=p/2 to P_x(A)=1. Invariant probability contradicts stationary fixed-B tails. For 1<r<3 interval J about u=1-1/r contracts Lipschitz by q<1, with ±a invariance and W1 contraction. At r2, ±1/16 versus (1-Exp(1))/16 match mean0 variance1/256, while only first preserves positive J. Independently checked exact interval bounds, quartic signs and trap failure bound 1/3840; no finite experiment purports to prove almost-sure result.

## originality

PASS

Published Bassols-Cornudella--Lamb already describes Gaussian-noise almost-sure negative divergence and small bounded-noise attractors; neither the general one-sided unbounded-negative-support finite-second-moment criterion nor the explicit equal-variance non-Gaussian counterpoint is included in the material inspected. Yang--Han studies FORMAL Gaussian moment-closure equilibria, not the existence of invariant probabilities for every innovation law. No originality claimed for Gaussian escape alone or for the closure quartic.

## value

PASS

Stochastic logistic moment-closure formulas can share identical mean/variance for radically different actual Markov-chain stationary behavior. The one-sided tail criterion and explicit equal-variance non-Gaussian pair isolate a mathematically motivated support effect and a precise limitation of noise-variance-only persistence reasoning. Not just a Gaussian repetition: the proof covers every iid law with unbounded negative support and finite second moment for every r>0.

The dated certificate retains the supplied scientific assessment, sources and limitations.
