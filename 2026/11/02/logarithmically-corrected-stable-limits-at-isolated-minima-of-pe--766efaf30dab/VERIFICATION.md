---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

With uniform exponential mixing of the torus/regime projection, continuous positive invariant density at finitely many positive-definite Morse minima, symmetric variable-order kernel and fixed initial state, the predictable rescaled jump intensity n b_n^{-alpha(z,i)} gamma(z,i) is bounded above by (log n)^{d/2}. Laplace stationary averaging at quadratic minima contributes (2 pi alpha0)^{d/2} sum rho gamma/sqrt(det H); mixing L² error is O((log n)^d/n). The drift is zero by pointwise kernel symmetry; jump compensator and modified second characteristic yield the deterministic stable Lévy characteristics and standard J1 semimartingale convergence. Sharpness at larger/smaller scales follows from tightness and nonatomic fixed-time stable laws. Independent Bessel/cosine Laplace normalization arithmetic and source SciPy verifier reviewed, not misused as stochastic proof. Additional density assumption is explicitly independent of cited mixing theorem.

## originality

PASS

Sandrić (2026) Theorem 3.1 proves conventional n^{1/alpha0} scaling and zero limit when minimum set has measure zero; final paragraph explicitly leaves finding a nontrivial alternative normalization open. Franke (2006) abstract covers the conventional scaling but full paper is inaccessible. Kuhwald–Pavlyukevich (2016) has time-periodic independent-increment exit asymptotics with related log Laplace factors; it does not entail a spatial-index Markov-modulated full-process J1 limit. Thus qualified best-of-knowledge originality survives, with a real uninspected Franke risk.

## value

PASS

Answers the specific zero-measure minimizing-index open normalization question for a natural nondegenerate Morse class, identifying sharp log correction, Hessian/invariant-density coefficient and functional limit. Not a renaming of conventional scaling or a simulation artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
