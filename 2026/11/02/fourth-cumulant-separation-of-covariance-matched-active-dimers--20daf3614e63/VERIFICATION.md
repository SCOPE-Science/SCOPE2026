---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python verify_cumulants.py` from a directory containing the supplied program. It requires NumPy and SciPy and has no external files, stochastic seeds, or network dependencies. The code constructs polynomial generator moment ODEs for two separate models (95 Gaussian-force moments and 50 telegraph-force moments), initializes the force and relative coordinate independently in their stationary laws, evolves to four finite positive times for each of three parameter settings, and compares with quadrature of independent positive-kernel representations. It also checks exact second-moment agreement, strict fourth-cumulant ordering, explicit limiting-rate formulas and the noise-independent ratio.

Observed output: `PASS 84 independent identities / moment-evolution checks`. The validated parameter tuples \((a,b,g,\sigma)\) were \((1.3,2.1,1.7,0.8)\), \((0.55,3.1,1.2,0.71)\), and \((3.2,0.45,0.93,1.4)\). Observation times: \(0.5\), \(1.7\), \(5.0\), and \(13.0\). The common independent thermal displacement contribution has zero fourth cumulant and can be added with any positive variance rate.

Scientific limitations: finite checks do not establish infinite-time limits or strict positivity at every parameter setting; these are proved analytically in `RESULT.md`. The theorem is an ensemble-displacement result, not a finite-sample classification bound or a claim about correlated fluctuations. Independent validation has not been performed.
