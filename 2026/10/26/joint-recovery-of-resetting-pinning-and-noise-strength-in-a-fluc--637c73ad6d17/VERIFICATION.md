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

PASS: A single Poisson reset clock for the WHOLE profile yields a common stationary age A~Exp(r); conditional on A=a the field is a centered Gaussian stochastic convolution, not a product of independent local reset ages. Its zero-lag variance is D/[2 sqrt(nu mu)] erf(sqrt(2mu a)), and the spatial heat kernel gives C_ell = D exp[-ell sqrt((r+2mu)/(2nu))]/sqrt[2nu(r+2mu)] after exponential-age integration. Hence V=D/sqrt[2nu(r+2mu)] and R=exp[-ell sqrt((r+2mu)/(2nu))]. Gaussian fourth moments and the integral identity for the square of erf give K=(12/pi)y atan(1/y)-3, y=sqrt[1+r/(2mu)]>1. The derivative atan(1/y)-y/(1+y²)>0 follows from integrating a positive rational derivative, giving a bijection from y>1 to 0<K<12/pi-3. The inverse uses s=2nu(log R/ell)^2, y uniquely from K, then mu=s/(2y²), r=s(1-1/y²), D=V sqrt(2nu s); positivity and the stated image are exact. Independently computed forward/inverse parameter triples (mu,r,D,nu,ell)=(.5,.7,2,1,.8),(1.6,.08,.31,.37,2.2),(.11,12,.65,3,.2) with relative reconstruction errors <1e-7. This is an exact infinite-line argument, not a noisy-data estimator.

## originality

PASS

PASS qualified: the 2014 full original Gupta–Majumdar–Schehr paper establishes exponential-age renewal and non-Gaussian fluctuations of massless (unpinned) reset Edwards–Wilkinson interfaces, but its formulas do not treat positive harmonic mass together with a global exact inverse for r,mu,D. The 2013 Gupta–Rosso–Texier paper analyzes pinned Rouse motion without whole-profile resets; Olsen (2023) treats reset harmonic single particles and their moment recursions. These supply valuable pieces but not the spatial covariance and exact three-parameter observable image in the same model. A specialized general Gaussian-field inverse theorem may cover it and remains a residual priority risk.

## value

PASS

PASS: Spatial covariance identifies only the combined damping r+2mu, so two physically different mechanisms are unidentifiable from second moments. A single fourth-order kurtosis observable resolves this genuine degeneracy and determines the minimal compatible region for positive parameters along with noise amplitude. This natural global inverse classification for a widely studied continuum interface is not a trivial three-equation numerical fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
