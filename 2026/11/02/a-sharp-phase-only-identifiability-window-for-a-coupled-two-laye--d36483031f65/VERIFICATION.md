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

# Verification of the exact phase-fold theorem

## Analytic proof obligations

The model parameters \(C,D,\lambda,\omega,\kappa\) and the forcing amplitude are strictly positive. For the unique forced sinusoidal state, \(H^{-1}=\lambda+i\omega C+i\omega D\kappa/(\kappa+i\omega D)\). Rationalization yields real and imaginary parts with strictly positive denominators and establishes the open right semicircle. Differentiation of \(\phi=\arg(H^{-1})\) gives an exactly factored numerator whose sign is the sign of \((C+D)\kappa^2+2\lambda D\kappa-\omega^2CD^2\). This polynomial is negative at zero, strictly increasing and unbounded above, so has one and only one positive root. The endpoint phase values, phase-preimage counts, strict bounded-interval frequency window, and gain resolution follow from this structure. The complete algebra and boundary quantifiers appear in RESULT.md.

## Executed reproducibility check

Run `python verify.py` using Python 3 and its standard library only. The replayed output is:

```
VERIFY_OK assertions=149742
phase twins tangent 8/11; k*=0.927050983125
climate two-boundary period window: (82.1910947, 141.8322641) years
```

Exact fractions check 19,000 sampled parameter tuples for the semicircle equation, strict real/imaginary bounds, inverse response and derivative-factorization signs. A second exact-rational sweep over 18,000 parameter tuples checks the strictly bounded frequency-window equivalence, plus the analytical phase-twin certificate. The numerical examples are checked with independent complex-arithmetic evaluation. Numerical tests are not a proof of statements covering all positive reals.

## Reproducible algebraic anchor

For \(C=\lambda=\omega=1\) and \(D=3\), the distinct exchange coefficients \(\kappa=1/2\) and \(\kappa=3/2\) give \(Z=(55+40i)/37\) and \(Z=(11+8i)/5\), hence both yield \(\tan\phi=8/11\) while inverse-transfer squared magnitudes differ as \(125/37\) and \(37/5\). These are exact identities, not fitted observations.

## Scope and unfinished validation

Only the linear, positive, known-parameter, two-layer deterministic case is proved. Stochastic parameter estimation, empirical climate data, broader-network historical priority and unknown auxiliary climate coefficients are not covered. Independent mathematical validation has not been performed.
