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

Reconstructed covariance equality E[X−p|T]=aT, a=σ²/(σ²+v), from orthogonal projection and Cauchy-Schwarz, with mandatory saturation of budget. Bounded conditional Bernoulli expectation forces T and centered noise bounded, hence entire characteristic functions. The identity (1−a)φX′φY=aφXφY′ and a simple complex zero of Bernoulli φX force an integer zero multiplicity m=(1−a)/a=v/σ²; integrating logarithmic derivatives with φX(0)=φY(0)=1 gives φY=φX^m. Conversely exchangeability with m Bernoulli summands yields E[X|S]=S/(m+1), exactly attaining covariance bound. At v=0 constant noise is the only equality. Huang existence of minimizers is essential to promote nonattainment to strict infimum at noninteger v. The 54 finite rational examples test only construction, not the analytic argument.

## originality

PASS

Ernst–Kagan–Rogers establish the integer convolution construction, not the converse exact Bernoulli sharpness spectrum or uniqueness of all equality noises. Huang supplies a general existence theorem, not the integer-only obstruction. Classical conditional-regression characterizations may be aliases; available older abstract/theorem scope requires extra prescribed conditional distribution, and unindexed equivalences remain a risk.

## value

PASS

Provides a mathematically sharp arithmetic boundary for a recognized least-favorable-noise optimization problem, classifying every noise that saturates a universal covariance bound and explaining why integer convolutions cannot interpolate to fractional budget ratios. This nontrivial structural rigidity is independently worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
