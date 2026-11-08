---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The normalized symmetric Gaussian ambiguity is positive and decreases strictly with radius. Threefold angular minimization reduces to e^{-y}+2e^{y/2}; the cosh/sinh comparison for k>=1 establishes the minimizer for every y>0, not just sampled angles. Differentiating the resulting W_R gives h(y)-y/sqrt(T^2+y^2). The scalar T(y)=y sqrt(1-h(y)^2)/h(y) rises strictly from 2 to infinity via P''(t)=e^t-t e^{-t}>0, giving global uniqueness and a->sqrt(3). My independent finite angular comparisons: 9696 inequalities, plus sampled global squeeze bounds and asymptotic a(20)=1.7320507555. The finite grid does not prove the quantified inequalities.

## originality

PASS

Best-of-knowledge positive originality for the full final claim after identifying all presently established subclaims; actual source-material inspections and possible dominating alternatives are recorded. Literature gaps are residual risks, not proof of novelty.

## value

PASS

The sum of positive ambiguity windows appears as the inversion divisor in the main multiwindow STFT reconstruction formula. The sharp crossover explains when symmetric windows maximize the worst denominator over a disk and when squeezing gains stability, with a unique design parameter for every radius. This is a full natural parameter continuum, not a merely reparameterized Gaussian integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
