# Scientific review: cycle–leaf dependence in uniform connected unicyclic graphs

## Correctness — PASS

For a fixed cycle-root set of size \(c\), the rooted-forest determinant \(\det(nI_{n-c}-J_{n-c})=c n^{n-c-1}\) provides the exact count; deleting specified leaves proves the entire conditional leaf-indicator law through matching empty-box avoidance probabilities. The strictly positive increments of \(m(1-1/n)^{m-1}\) establish the signed covariance for any strictly increasing function of cycle length. The cycle-length law is a left-truncated Poisson distribution, giving a half-normal limit. A bounded-increment martingale central limit theorem for vacant boxes, together with a conditional coupling and its variance bounds, yields asymptotic independence. A uniform quadratic response and uniform integrability prove the nonzero covariance asymptotic. All boundary cases, in particular the pure cycle and \(n=3\), are handled explicitly. Exhaustive enumeration for \(3\le n\le7\) checks the exact joint counts and mixed moments; its scope is finite.

## Originality — PASS, with historical-priority risk

The full accessible text of Ben-Naim–Krapivsky (2004, arXiv:cond-mat/0403453v1) studies evolving random multigraphs and the numbers and size distributions of their unicyclic components; it does not provide the conditional distribution of leaves given the cycle length in one uniform simple connected unicyclic graph. The full accessible text of Zhang–Zhang (2013, arXiv:1311.1987v1) uses precisely the girth/leaf parameters, but its theorems are about extremal Laplacian coefficients, not random enumeration or dependent limits. OEIS A057500 supplies aggregate unicyclic counts, and OEIS A098909 already supplies the exact cycle-length refinement. Neither contains the bivariate leaf/cycle law; marginal cycle-length enumeration is not claimed new. Standard rooted-forest enumeration, the known cycle-length triangle, occupancy identities and marginal normal limits are ingredients, not purported new results. The precise combined law—finite conditional vacancy representation, strict regression for all increasing cycle functions, first-order independence alongside a quantitative nonvanishing second-order covariance—was not located in the comparisons. General conditioned-graph theory could contain an implicit version; independent priority checking remains necessary. The broader random-graph literature may contain an equivalent formulation not identified by available searches.

## Mathematical value — PASS

Cycle length and leaf count are intrinsic, geometrically interpretable statistics of the canonical finite connected unicyclic model. The exact conditional law gives all finite-dimensional leaf-indicator probabilities; the strict conditional-mean theorem answers a natural dependence question for every order and all increasing transforms of cycle length. The joint limit distinguishes leading-order asymptotic independence from a negative mixed covariance of order \(\sqrt n\), making the quadratic finite-size response relevant. This is a coherent structural probability result, not a relabeling or an arbitrary finite slice.

## Closest literature and limitations

- E. Ben-Naim and P. L. Krapivsky, *Unicyclic Components in Random Graphs*, arXiv:cond-mat/0403453v1 (18 March 2004). Population-scale random multigraph process and component sizes.
- J. Zhang and X.-D. Zhang, *Laplacian coefficients of unicyclic graphs with the number of leaves and girth*, arXiv:1311.1987v1 (8 November 2013). Deterministic extremal spectral questions with matching parameters.
- OEIS A057500. Aggregate connected labeled unicyclic counts.
- OEIS A098909. Exact unicyclic counts by unique-cycle length, not by joint leaf count.

The proof does not show full stochastic domination of conditional leaf counts as the cycle grows, nor analogous results for multigraphs or disconnected random graph models. Historical priority is not independently established.

Self-review: passed. Independent audit: not yet performed.
