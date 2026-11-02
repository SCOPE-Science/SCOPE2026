---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

With externally imposed 0/h pump and rates off-to-on a, on-to-off b, Y'=1-(1-g)Y and Z=Y-1 have vector fields F0=-Z and F1=h+(h-1)Z. The average multiplicative exponent [-b+a(h-1)]/(a+b) gives stationarity iff h<1+b/a, including nonexistence at equality via recurrent zero-drift switching cycles. The zero-current stationary transport equations imply rho1=Z rho0/[h+(h-1)Z]; for 1<h<1+b/a with k=h-1 and theta=b/k-a>0, U=kZ/(h+kZ) gives f0=p0 u^(a-1)(1-u)^(theta-1)/B(a,theta), f1=(u/k)f0, p0=b/(a+b). The Pareto tail K_Y=p0(h/k)^(theta+1)/[theta B(a,theta)] follows from the u=1 endpoint. Since Q=sqrt(cY)G for independent normal G, the normal-scale mixture has tail K_Q R^(-2theta), K_Q=K_Y (2c)^theta Gamma(theta+1/2)/sqrt(pi). For 0<h<1 the bounded variance endpoint gives Gaussian rate -(1-h)/(2c); for h=1 the gamma-mixture Laplace variational minimum gives -sqrt(2b/c) times R. Y moments iff m<theta; Gaussian photon n_g scales with Y and Wick factorial second moment scales with Y², yielding distinct strict theta>1 and theta>2 thresholds. Complete statements restricted to stationary intracavity homodyne under the linear Gaussian model.

## originality

PASS

Generic dichotomous-noise transport stationary distributions and prescribed-pump optical quadrature ODEs are old; their conjunction does not automatically state an exact laboratory observable tail constant and strict photon-moment phase diagram in a telegraph-modulated cavity. The exact model-specific transition is not located in the inspected abstracts and Resultary query; these are not full-document priority guarantees.

## value

PASS

A proper trace-class optical mixture with infinite measured energy is physically and mathematically distinctive. Exact Gaussian/exponential/Pareto tail rates, coefficients, and separate first/second factorial photon moment thresholds are natural experimental observables of a precisely specified switching system; they are more than a routine reparametrization of the beta stationary density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
