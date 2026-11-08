---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For deterministic complete tripartite K_{n,n,k}, n>=16k, uniform among currently feasible edges, exact state (a,b,c)=(m-x,m-y,k-x-y). At AB level m>=4k, a fixed unmatched C vertex meets the first edge with probability (a+b)/(ab+c(a+b))>=1/m; successive-level survival telescopes to <=M/n, hence all C vertices absorbed above M with failure probability <=kM/n. At each rare edge, A/B endpoint conditional probability a/(a+b) differs from 1/2 by <=k/[4(M-k)], coupled across <=k choices, giving <=k^2/[4(M-k)] mismatch. If all rare vertices matched, final dense imbalance exactly |k-2X|. Therefore TV bound kM/n+k^2/[4(M-k)], M=ceil(sqrt(kn)), and convergence for k=o(n^(1/3)); conditional binomial CLT gives folded-normal scaled law. Maximum matching leaves k mod 2 vertices (given n>=k), so p_odd=2^(1-k)binom(k,(k-1)/2), p_even=2^-k binom(k,k/2). Independent exact-rational state DP checked 104 n/k cases and representative TV bounds, not an infinite proof.

## originality

PASS

Best-of-knowledge O PASS for the precise assessed final statement. Reviewed the actual final package and compared statements/implications with primary literature and published SCOPE/Resultary semantic results, using aliases, broader cases, tables and corollary checks. A binomial obstruction to random greedy matching under a rare tripartite perturbation: the cited prior results cover background tools, objects and/or weaker observables; no identified theorem implies the complete evaluated final statement. Negative search is not a novelty proof; primary-source limitations and risks are explicit.

## value

PASS

Determines an entire terminal-defect distribution and a nontrivial rate at which a vanishing third part in a dense deterministic multipartite graph prevents random edge-greedy from finding a maximum matching. The persistent parity/central-binomial obstruction is a motivated natural randomized-algorithm observable, beyond worst-case approximation ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
