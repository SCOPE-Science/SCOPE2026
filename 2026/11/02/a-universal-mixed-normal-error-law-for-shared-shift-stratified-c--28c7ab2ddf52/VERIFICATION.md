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

The two interpolation points a=Xi/2,b=(1+Xi)/2 are separated by 1/2, permitting a uniform C2 interpolation remainder R_i(u)=[f''(i/m)/(2m²)](u-a)(u-b)+o(m^-2). Direct uniform moments give V(t)=Var((U-t/2)(U-(1+t)/2))=1/180+(t-1/2)^2/12, E V=1/80, E V²=101/518400. Given Xi, 2m independent centered residual evaluations each have small O(m^-3) contribution; scaled terms vanish individually, total conditional variance tends J_f V(Xi)/8, so a conditional triangular-array CLT gives the normal scale mixture and joint convergence with Xi. Fourth-moment convergence follows bounded summands; standardized moment 3 E[V²]/E[V]^2=101/27 proves it is non-Gaussian. Cell conditional means zero under any shift, so common versus independent shifts have identical finite-m means/variances. Independent shifts yield ordinary Lindeberg CLT. The paired residual difference has expectation 2 Var(R_i|Xi), giving exactly conditionally unbiased estimator; uniform Taylor expansion plus bounded LLN proves m^5 consistency and conditional Slutsky pivot. Independent symbolic polynomial integration confirmed V moments and 101/27, the exact variance identity and quadratic benchmark. Finite checks are not used as proof of all C² limits.

## originality

PASS

Kunsch (arXiv:2309.09059) introduced SCV and explicitly allows a single common interpolation shift across cells in Section 2 Eq.19 and randomized interpolation for smooth functions in Remark 2.8. Those algorithms and their error-rate/confidence bounds are not new. In the materially read primary text, no exact conditional variance mixing law, kurtosis 101/27, equal-variance independent-cell contrast or paired-residual pivot is stated. Chopin-Gerber cubic stratification and Nakayama-Tuffin randomized-QMC normality use different estimators. Classical Gaussian scale-mixture/conditional CLT theory is acknowledged. Best-knowledge PASS for this algorithm-specific sharp asymptotic calibration, with risk of an unlocated general random-environment CLT specialization.

## value

PASS

A single global randomization variable is a genuine algorithmic feature of Kunsch SCV, and two methods can have the same exact variance yet distinct confidence-limit distributions. The universal 101/27 excess-kurtosis calibration and a no-extra-function-evaluation studentization formula directly matter to an investigator using nominal Gaussian confidence intervals. This is a motivated algorithmic boundary, not an arbitrary numerical test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
