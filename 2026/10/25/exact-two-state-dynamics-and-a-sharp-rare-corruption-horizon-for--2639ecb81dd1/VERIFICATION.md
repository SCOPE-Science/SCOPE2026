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

A=(1,...,1)^T and exact normalized scalar Kaczmarz projects immediately to selected b_i in {0,delta}. At x=0, a corrupt selection occurs iff H>=s-k+1; at x=delta, a clean selection iff H<=k-1. H is hypergeometric for uniform without-replacement sampling, giving P=[[1-p,p],[q,1-q]] and, when p+q>0, unique stationary law pi=p/(p+q), eigenvalue ell=1-p-q and covariance delta^2 pi(1-pi)ell^j. For odd s=2r+1<=c the support H=0,...,s is positive and disjoint/partition/overlap of tails yields strictly positive/zero/negative ell by k relative to r+1. At median two tails partition for any admissible s, giving iid Bernoulli outputs, geometric first-hit time for p>0, almost-sure repeated errors and exact p=0 iff s>=2c+1. Under beta fixed <1/2, c_s/m_s=beta+o(1/s), s^2/m_s->0, the log finite-population/binomial mass ratio is o(1) uniformly, and the upper half-binomial tail is first mass times (1-beta)/(1-2beta), yielding C_beta=sqrt(2beta(1-beta))/(sqrt(pi)(1-2beta)) and kappa_beta=-0.5log(4beta(1-beta)). Independent exact subset enumeration for m=3..9 checked 29,564 assertions; a 50,000/1,000/11 benchmark and asymptotic ratios checked separately. No finite check is used to establish infinite-time or asymptotic claims.

## originality

PASS

Same equality-row algorithm and qualitative small-sample rare spikes are known from Haddock–Ma–Rebrova (2023), but its full accessible Section V-D gives heuristics rather than the displayed exact hypergeometric two-state Markov law, rank-dependent stationary correlation phase, iid median process, finite-population safe cutoff, and sharp square-root-prefactor horizon. Later general sample-size and error-horizon theorems apply to different row-selection mechanisms, and published-record semantic searches returned no matching theorem. This is a limited, best-of-knowledge special-case originality decision, not novelty certification; the potentially relevant Swartworth dissertation could not be fully read.

## value

PASS

The sampled equality-quantile algorithm is a natural specific small-sample variant explicitly highlighted as lacking complete theory by Haddock–Ma–Rebrova 2023 V-D. The rank-sensitive sign reversal distinguishes persistence/independence/anticorrelation; median iid behavior makes long-run rare corruption exact, and s>=2c+1 supplies an absolute finite-population no-error cutoff. The sharp s^-1/2 exp(-kappa s) constant distinguishes a reliable-looking finite experiment from almost-sure recurrence and quantifies observation windows. The conclusion is only a motivated exact scalar benchmark, not an assertion of broad practical matrix convergence. Elementary hypergeometric and Stirling tools alone do not establish value; the model-specific dynamical interpretation and complete parameter/boundary classification do.

The dated certificate retains the supplied scientific assessment, sources and limitations.
