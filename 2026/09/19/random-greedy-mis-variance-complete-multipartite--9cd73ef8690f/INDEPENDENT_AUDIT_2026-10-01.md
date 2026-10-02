# Independent audit — Sharp variance of random greedy maximal independent sets on complete multipartite graphs

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The first accepted vertex fixes the output part, so the size-biased law and all moments follow exactly. Conditioning on a largest part and applying the bounded-range variance inequality gives the sharp fixed-largest-part bound; equality forces every other part to be a singleton. The small-largest-part range is strictly dominated, and the exact first difference of the remaining one-variable polynomial has a unique integer maximizer. An independent exact enumeration of all multipartite partitions for orders three through fifteen reproduced that unique maximizer; the repository verifier source was also inspected, but its saved success log was not used as proof.

## Originality

**PASS.** Best-of-knowledge originality passes for the sharp finite-order variance extremum and unique complete-split extremizer. The elementary size-biased law itself is not treated as novel.

### Equivalent formulations

The originality question was compared at the level of the exact maximizing part partition and variance value, not merely by graph-family titles.

Evidence: The semantic search returned this record as the only exact match; no earlier equivalent finite-order extremal theorem was located. The size-biased output law is immediate from the first vertex and is excluded from the novelty claim.

### Broader coverage

Neither broader source implies the claimed all-connected-complete-multipartite extremum.

Evidence: Shaikh's accessible abstract gives the sharp edge-sensitive triangle-free bound with stars as connected equality cases; it does not cover complete multipartite graphs having three or more nonempty parts, which contain triangles. The 2024 paper develops local-limit methods and expectations for several graph families rather than a finite-order variance maximization over complete multipartite graphs.

### Exact database or table

This is a theorem rather than a standard tabulated invariant; the applicable database check is the published theorem archive.

Evidence: No earlier published archive row with the same finite-order maximizer or the \(27/256\) asymptotic variance constant was located.

### Claim versus prior implication

The claimed theorem is not a corollary of either inspected prior statement.

Evidence: Shaikh controls the complete-bipartite subfamily and recovers the star equality case there, but its hypothesis excludes the triangle-containing multipartite cases that determine the full optimization problem. General local-limit expectation theory does not mechanically supply the exact variance objective or its discrete maximizer.

### Source inspections

- **Variance of random greedy independent sets in triangle-free graphs** — RELATED_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2609.14826
  Material read: accessible abstract and bibliographic record; full text could not be retrieved through the lawful routes attempted.
  Evidence: The accessible statement is restricted to triangle-free graphs and identifies stars as connected equality cases.
- **Greedy maximal independent sets via local limits** — RELATED_NOT_COVERING.
  Identifier: https://doi.org/10.1002/rsa.21200
  Material read: accessible full-text introduction and family/result sections.
  Evidence: The paper develops local-limit and expectation results, not the exact finite-order complete-multipartite variance extremum.

### Checked sources

- https://arxiv.org/abs/2609.14826
- https://doi.org/10.1002/rsa.21200
- Resultary published-finding semantic search

### Residual risks

- The full text of the very recent Shaikh preprint was not accessible during this audit; an unadvertised multipartite calculation remains a limited overlap risk.
- Older random-sequential-adsorption terminology may hide related calculations not surfaced by the searches.

## Scientific value

**PASS.** The theorem gives a complete sharp finite-order extremal classification for a natural dense graph family, including uniqueness at every order and a nontrivial asymptotic constant. It is not merely a recomputation of the elementary output law.

## Final assessment

The unchanged final claim passes correctness, originality, and scientific value. No research claim or slogan change is required.

This assessment is not formal verification or expert attestation and does not guarantee that no undiscovered prior art exists.
