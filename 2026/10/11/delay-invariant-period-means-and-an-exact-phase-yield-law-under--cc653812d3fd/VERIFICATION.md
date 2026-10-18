---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Log-v period integration fixes ubar=u* and lag invariance fixes E[uτ]=u*. Log-u average minus equilibrium gives predator mean deficit; expansion 1/(1+mx)=1/(1+mu*)−m(x−u*)/(1+mu*)²+m²(x−u*)²/[(1+mu*)²(1+mx)] gives the positive Q. Subtract u* times log-u average from undivided prey average to obtain αCov(u,v)+(r/K)Cov(u,uτ)=am Q/(1+mu*). Zero Q forces constant u and then v. Independently verified exact rational source specialization u*=5, v*=469/102, r/K=2/75, am/(1+mu*)=15/68, α(1+mu*)/m=17/15. Finite tests only corroborate algebra; proof covers all classical positive periodic orbits.

## originality

PASS

The exact primary 2022 paper has a nondelayed periodic-integral relation; it is expressly treated as partial prior coverage, not ignored. The new delayed model identities add strict rational Jensen deficit and weighted *lagged* phase covariance, with all-period amplitude validity. Different later model modifications are not stronger coverage of this specific balance.

## value

PASS

The delay is scientifically relevant because coexistence cycles have lagged phase correlations. An exact finite-amplitude mean-yield loss tied to both predator–prey and prey autocovariance provides a useful structural diagnostic beyond the nondelayed mean-balance motif and near-Hopf spectral calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
