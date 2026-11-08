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

Read actual RESULT.md and verify.py. At positive levels the countable Markov depth chain holds with probability 1-q and descends with q; level zero regenerates geometric depth 2^{-j-1}. Direct stationary balance gives pi_0=q/(1+q) and pi_k=2^{-k}/(1+q). The signed-row identities wP=sw+dv* and v*P=rv*, including level-zero boundaries, rigorously give C_n=2(1-q/2)^n+2q(1-q)/(1+q)^2*((1-q)/2)^n. Summing lags yields exact finite variance and Green-Kubo coefficient. A polynomial Poisson solution and martingale CLT establish fixed-q CLT; a uniform-grid/Riemann-sum argument establishes the triangular Nq_N->t crossover. Independently recomputed finite-state transition covariance at q=2/5 for lags 0,1,2,3,5,10 with numerical errors under 1e-9; this is corroboration, not proof of infinite chain or CLT.

## originality

PASS

The known model and stationary density are credited; the exact all-lag unbounded-depth covariance and critical Nq scaling are not given by the inspected model thesis and are not implied by two-cell density or qualitative general mixing/CLT theorems.

## value

PASS

The exact covariance and CLT variance quantify the memory of an unbounded natural state observable in a known critical random interval map. The Nq_N crossover is a mathematically meaningful degeneration of ergodicity, with explicit interpolation between ballistic N² and diffusive N/q fluctuations; neither follows from merely knowing the stationary two-cell density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
