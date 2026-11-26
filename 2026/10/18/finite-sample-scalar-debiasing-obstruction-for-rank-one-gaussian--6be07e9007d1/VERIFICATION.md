---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In a basis containing v, the signal sketch column g and perpendicular columns are independent Gaussians with covariance I/m. Conditional trace and reflection give the two eigenmeans a=E[X/(tau+hX)] and tau b=1-ha/m, X=chi-square_m/m. Simultaneous target matching therefore forces tau_m. Integrating (tau+hX)^(-1) against the scaled gamma density by parts gives (tau+h)a+(2h tau/m)E[X/(tau+hX)^2]=1. Weighted strict Cauchy–Schwarz bounds the second expectation below by a². At a*=1/(h+lambda), the corresponding increasing quadratic has value 1+h(2tau_m-lambda)/[m(h+lambda)^2]>1 even at m=2 because tau_m>lambda/2. Hence the signal deficit is positive; perpendicular excess equals h times this deficit divided by m tau_m. The difference-of-quadratics formula also gives the stated strict lower bound using the slope at a*. The scaled chi-square means converge a.s. to one under the Gaussian sequence coupling, and X/(tau_m+hX)^2 is bounded by 1/(4h tau_m). Taking limits in the exact integration-by-parts equation gives h lambda/(h+lambda)^3 and then h²/(h+lambda)^3 at the two different scales. The calculation is dimension-independent once the perpendicular eigenspace exists. Independently applied the chi-square Laplace transform and quadrature (python /workspace/replay.py 3, mpmath 1.3.0), not the frozen gamma-density script: both signs and the exact relation held in all five probes; at m=8192, h=3, lambda=2, the scaled biases were 0.0479971867174 and 0.0720010535908, consistent with 0.048 and 0.072. Finite quadrature is corroboration only. No conclusion for adaptive ridge, extra scaling, or general spectra.

## originality

PASS

The estimator and effective-dimension ridge are prior, as are asymptotic resolvent equivalence and the gamma identities. Best of knowledge, the additional exact obstruction for every m≥2 and the opposite sharp directional residuals are not covered by the strongest inspected comparisons. In particular the same asymptotic resolvent equivalence in the rank-deficient model only gives vanishing discrepancy, with no finite sign or matching obstruction.

## value

PASS

Rank one is the first nontrivial split between signal and nullspace, and separates the finite mean bias left by a standard ridge correction from variance removed by averaging. The no-scalar obstruction and two distinct sharp rates answer a motivated design question at its simplest natural spectrum, without claiming failure of adaptive algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
