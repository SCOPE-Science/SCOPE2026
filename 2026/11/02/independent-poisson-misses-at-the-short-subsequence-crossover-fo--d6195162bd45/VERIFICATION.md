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

For fixed r≥1 and independent uniform binary length-n strings with d_n a_nr→lambda, greedy matching makes a single fixed r-pattern absence probability a_nr=2^-n sum_{j=0}^{r-1} binom(n,j). For distinct patterns u,v, the joint greedy automaton has at most r-1 loop-capable states on live paths (otherwise they agree at every coordinate), hence O_r(n^(r-2)) jointly avoiding binary words and pair absence o(a_nr), including r=1 exactly zero. Single-row probability generating functions have rare-event expansion 1+a_nr sum_u(t_u-1)+o(a_nr); raising to d_n yields 2^r independent Poisson(lambda) coordinate misses. Coordinate zeros give Binomial(2^r,e^-lambda) common r-patterns; a_(r-1)/a_r→0 and a_(r+1)/a_r→∞ sandwich maximum LCS into {r-1,r} (empty subsequence for r=1). Independent exact enumeration and greedy DP checked one-pattern and paired-avoidance cases r≤4. Finite checks are not the asymptotic proof.

## originality

PASS

Best-of-knowledge original joint rare-pattern independent Poisson law and two-point common-subsequence length crossover for exponentially many input words at fixed r. Fixed-d normalized LCS asymptotics and one-word universality-index laws cover different observables and regimes.

## value

PASS

The exact many-input crossover resolves a natural transition for the existence of short common scattered patterns, providing all joint limiting counts and a sharp two-point LCS distribution rather than just an expectation or a heuristic independence statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
