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

For each row N the Markov chain has renewal return tail (k+1)^(-beta_N), beta_N=1+c/log N>0. The last-renewal identity P(A_N=k)=u_(N,N-k)(k+1)^(-beta_N) follows exactly. Stochastic monotonicity of the transition makes renewal mass u_(N,m) nonincreasing. The B_N(e^(-t/N))/log N -> h(c) logarithmic Riemann sum, Laplace-transform continuity of locally finite tilted renewal measures, and monotonicity give h(c)log N*u_(N,floor Nx)->1 uniformly on compact x>0. Ages k=N^s, s in (0,1), then yield tilted-log density e^(-cs)/h(c), with endpoint tightness. Exact future survival ((k+1)/(k+r+1))^beta_N yields independent Pareto-II residual ratio conditional on ages diverging. Independently recomputed exact renewal convolutions for N=1500, c=-1,0,1 and normalization exactly 1; finite-size log-age CDFs approach predicted values slowly, not an infinite proof.

## originality

PASS

Targeted Resultary semantic searches and primary literature comparisons, with specific mathematical implication checks and residual priority risks, support qualified best-of-knowledge originality of the final scoped claim.

## value

PASS

The varying-exponent 1/log N critical window yields a natural complete crossover law, interpolating between sides of the infinite-mean renewal phase transition. Its independent residual ratio identifies a genuine two-scale aging phenomenon useful beyond the fixed-beta renewal result, not a restatement of classical c=0 uniform log-age alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
