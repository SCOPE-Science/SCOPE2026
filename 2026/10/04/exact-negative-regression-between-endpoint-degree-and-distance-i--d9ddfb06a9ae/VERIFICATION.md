---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a fixed ordered path of length \(k\) between the two marked vertices, Moon's forest-extension formula gives exactly \((k+1)n^{n-k-2}\) labeled trees containing that path; multiplying by the \((n-2)_{k-1}\) ordered intermediate lists yields the claimed distance law. Conditional on the path, requiring any fixed \(r\)-set of outside vertices to be additional neighbors of the endpoint enlarges the path component from \(k+1\) to \(k+1+r\), so the inclusion probability is \((k+1+r)/(k+1)n^{-r}\). Subset expansion of the degree probability generating function then factors exactly into a \(\operatorname{Bin}(n-k-2,1/n)\) term and an independent \(\operatorname{Bernoulli}(1/(k+1))\) term. Coupling deletes one Bernoulli trial and lowers the extra Bernoulli parameter as \(k\) increases, proving strict stochastic regression, including the terminal path case. Averaging the conditional mean against the Prüfer-code degree law gives \(E[1/(D+1)]=E[D]/n\), from which the covariance identity follows algebraically. The product representation of the distance law gives the Rayleigh scaling and uniform integrability of the first two scaled moments, yielding covariance limit \(-1\) and the stated correlation asymptotic. The verifier exhaustively enumerates Prüfer codes through \(n=8\) and checks stochastic tails through \(n=80\); these checks are supplementary to the exact counting proof.

## originality

PASS

Pitman records Moon's classical extension formula: an unrooted forest with component sizes \(n_1,\ldots,n_k\) lies in exactly \((\prod_i n_i)n^{k-2}\) labeled trees. That is the counting engine, but it does not state the endpoint-degree law conditional on marked distance. Aldous and later random-tree work treat degree marginals, distances and distance profiles broadly; targeted searches did not locate the factorized conditional distribution, strict stochastic regression, or covariance identity. Current Resultary search for uniform Cayley-tree degree conditional on distance returned no same-object result among its leading findings. The audited theorem is therefore an exact bivariate refinement derived from a classical tool, not a claim of originality for the forest formula itself.

## value

PASS

Degree and marked-vertex distance are two of the most basic statistics of a uniform Cayley tree. The exact conditional distribution is stronger than a covariance calculation: it gives strict stochastic regression for every finite \(n\), all monotone covariance inequalities, and transparent asymptotics. This is a natural structural joint law derived from a classical forest formula and is likely useful whenever local branching is conditioned on geodesic separation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
