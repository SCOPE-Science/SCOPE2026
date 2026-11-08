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

Conditioning on the common symmetric two-state trap trajectory makes X_i,X_j conditionally independent centered Gaussian for i!=j; hence covariance of their squares at separated times equals Cov(Y_0,Y_h) of the common conditional variance Y. For kappa>delta>0, Y obeys dot Y=2D-2(kappa+delta*sigma)Y. The two-state generator closes the relevant moments to C_second+(4kappa+2r)C_prime+4BC=F e^{-2rh}, C(0)=V,C_prime(0)=0, with positive F and V. Factorization yields rates a_+/-=2kappa+r +/- sqrt(r^2+4delta^2) and trap pole 2r. Since C_prime(0)=0 and C_second(0)=-(4BV-F)<0, the positive Green kernel gives C_prime(h)<0 for all h>0 and C(h)>0 by decay to zero. Unique slow crossing a_-=2r iff r=(kappa^2-delta^2)/kappa; at this point the forced Laplace pole is genuinely double with positive coefficient F/(a_+-2r), yielding h exp(-2rh), not canceled. Independent numerical 2-state moment matrix propagation and scalar forced ODE agree for r below, at and above 0.84 when kappa=1,delta=.4. All limits apply to finite N>=2, distinct labels, strict positive stiffnesses.

## originality

PASS

Biroli et al arXiv:2312.02570 is identical model and provides the stationary equal-time squared-position covariance, which fixes V but cannot by itself specify lag relaxation. Behme arXiv:2407.05866 gives general Markov-switching OU covariance machinery, not the explicit two-particle squared-covariance harmonic-mean resonance and strict all-lag sign in this parameterization. Frydel arXiv:2407.12213 treats on/off trap with zero off stiffness, not strict interior positive two-stiffness regime. The present result is a nontrivial explicit specialization of general moment propagation, rather than asserting novelty of moment semigroups.

## value

PASS

The time persistence of fluctuation-generated interparticle correlations is a natural physical observable absent from zero-lag stationary statistics. The strictly positive monotonically decaying function with two competing relaxation sources and an exact harmonic-mean crossover, including the resonant t factor, is a complete useful spectral classification in the stated model, not an artificial algebraic exercise or a true thermodynamic phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
