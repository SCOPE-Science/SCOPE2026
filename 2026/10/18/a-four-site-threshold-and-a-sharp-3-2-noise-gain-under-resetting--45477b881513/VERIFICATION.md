---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The last-reset resolvent gives stationary p_n(r)=r/n sum_{k=0}^{n-1}(r+lambda_k)^-1=tanh(t)coth(nt), lambda_k=4sin²(pi k/n), t=0.5 arcosh(1+r/2). Integrating stationary covariance by Green–Kubo and differentiating that renewal resolvent yields exact V_n=2 p_n p_n′=(p_n²)′=2p_n/n sum_{k>=1} lambda_k/(r+lambda_k)². Exact reciprocal spectral identities S_1=(n²-1)/12, S_2=(n^4+10n²-11)/720 give V_n(0)=(n²-1)/(6n²), V_n′(0+)=(n²-1)(n²-9)/(120n²). In n=3 V=4(r+1)/(r+3)^3 strictly decreases; n>=4 starts increasing and vanishes at infinity, so has an interior maximizer (uniqueness not claimed). Hyperbolic comparison shows (r/(r+4))′-V_n>0 by n sinh(2t)>2 tanh(nt), establishing strict envelope. At mesoscopic r=1/n, nt→∞ and V_n→1/4; no-reset variance→1/6, yielding factor 3/2. Independently solved exact stationary/Poisson finite-chain equations and compared with reset-free resolvent at five rational (n,r) pairs; verified mesoscopic values through n=4000. Finite data does not prove global envelope.

## originality

PASS

Evans–Majumdar established Poisson stochastic resetting; Méndez–Flaquer-Galmés 2025 treat general reset functionals and obtain general characteristic/moment formulas (read accessible complete arXiv HTML §§II–VI), with detailed application to Brownian/subdiffusive half-line occupation. Their techniques provide general tools, not the evaluated finite discrete-cycle threshold/envelope and 3/2 maximum. Grange studies Brownian ring winding numbers and Zatloukal no-reset graph local times; neither is the same observable. Historical equivalent specializations remain possible.

## value

PASS

Time-integrated origin occupation is a fundamental dynamical fluctuation observable, distinct from monotone stationary occupancy or hitting-time performance. The exact minimum cycle length four for positive initial noise response, size-independent sharp upper bound and attainable 50-percent large-cycle gain provide an interpretable complete structural threshold and optimal benchmark, rather than an arbitrary finite simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
