---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The Stirling-permutation insertion representation has 2t-1 equiprobable gaps at birth t. If earlier labels S remain adjacent, precisely |S intersect [1,t-1]| gaps are forbidden; once split an adjacent equal pair cannot reform. Multiplication proves every finite-subset joint survival identity. For i<j, the ratio of two survival probabilities is product_{k=j}^{n-1}(1-1/(4k^2)), giving strictly negative pair covariance for j<n. Log-product asymptotics yield n Cov(I_i,I_j)->-(1-y)sqrt(x/y)/4 for 0<x<y<1. Bounds p_{n,i}<=sqrt(i/n) and n|Cov|<=1/2 control the origin; diagonal and off-diagonal Riemann sums integrate to K(s,t)=s^{3/2}(6-3sqrt(t)+t^{3/2})/9-s²/3 for s<=t. Independently enumerated all insertion words for n<=6 and all subset survival probabilities exactly; the infinite kernel is analytic, not inferred from finite enumerations.

## originality

PASS

Janson provides the plane-recursive-tree/Stirling-permutation correspondence and aggregate leaf variance, Haglund–Visontai stable-polynomial theory already yields qualitative negative dependence, and Zhang studies fixed-vertex degrees. The exact pair survival multiplier and continuous birth-age covariance kernel are quantitative refinements, not new generic negative association claims. Priority is qualified particularly by a 1993 tree-branch study whose full text was not inspected.

## value

PASS

The exact age-resolved covariance and arbitrary Riemann-integrable weighted kernel quantify collective fluctuation not captured by the known total-leaf variance. Such a covariance kernel is a natural input to weighted statistics and potential process limit results without claiming a functional CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
