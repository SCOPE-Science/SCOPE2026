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

Under t=((-ln y)/lambda)^k, the transformed integrand is t^a exp((p-1)lambda*t^(1/k)-p*t/2)(1-exp(-t))^(-p/2), a=(p-1)(k-1)/k. At zero it behaves like t^(a-p/2), requiring k>2-2/p. At infinity for p<1 all exponential terms decay, for p>1 the sign is governed by whether t^(1/k) is sublinear (k>1), superlinear (k<1), or linear (k=1, requiring lambda<p/[2(p-1)]). Combining with p<2 when k=1 gives exactly three branches; equality at either endpoint fails. Direct boundary p=2,k=1 gives square-density ~(pi^2 lambda)^(-1)(1-y)^(-1). All p ranges are analytically exhausted without a finite-to-infinite extrapolation.

## originality

PASS

The final claim was independently compared at statement/implication level against the identified closest original publications and targeted semantic finding searches. Specific prior components are credited and the remaining claimed addition is identified. Residual priority/access risks remain and this is best-of-knowledge, not universal certification. Exact Rényi-integrability phase diagram for the unit arcsine–Weibull law.

## value

PASS

The result determines exactly when a central entropy functional in a newly published bounded lifetime model exists. It materially changes interpretation of the source paper: its own fitted shape k=.9952 makes every order p>1 Renyi expression nonintegrable despite a formal series. Complete all-parameter endpoint existence is a motivated correction, not an arbitrary type or normalization check; it does not challenge ordinary moments/fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
