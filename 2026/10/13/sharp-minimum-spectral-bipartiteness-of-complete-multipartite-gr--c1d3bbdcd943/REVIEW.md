# Self-review

## Correctness
**PASS.** The claim follows from an explicit symmetric quotient \(B=uu^\top-D\), rank-one interlacing against \(-D\), the one-positive-eigenvalue property of connected complete multipartite graphs, and the trace-zero identity. The equality case is not inferred from numerics: equality forces all middle quotient eigenvalues to be \(-1\), and a direct eigenspace calculation shows that multiplicity \(r-2\) of \(-1\) requires at least \(r-1\) singleton parts. The converse complete-split spectrum follows from a quadratic factor. The boundary \(r=2\) is expressly excluded because all bicliques have value \(0\).

## Originality
**PASS.** The closest inspected primary source on complete multipartite adjacency spectra (Stevanović–Gutman–Rehman, DOI 10.26493/1855-3974.499.103) proves that the complete split graph minimizes spectral radius and energy, but it does not optimize the sum of the largest and least adjacency eigenvalues. The recent source arXiv:2609.00210v1 studies spectral bipartiteness and proves general upper bounds for clique-free graphs, not the present lower extremum. Exact and alias searches for complete multipartite graphs, complete split graphs, spectral bipartiteness, and the sum of extreme adjacency eigenvalues found no implication covering this statement. The main residual risk is an older theorem filed under different terminology for \(\lambda_1+\lambda_N\).

## Value
**PASS.** Spectral bipartiteness is an active measure of distance from bipartiteness. The theorem gives a sharp, unique extremizer on the canonical fixed-order/fixed-part-number multipartite family and shows that its normalized value can be exactly \((r-2)/N\), tending to zero for every fixed \(r\ge3\) despite the persistent \(K_r\). This is a structural extremal fact rather than a finite computation or parameter increment.

## Closest literature and limitations
The 2015 complete-multipartite spectrum paper supplies the closest same-family extremal result, while arXiv:2609.00210v1 supplies the current spectral-bipartiteness context. The new theorem does not extend beyond complete multipartite graphs and does not assert a lower bound for all graphs of clique number \(r\).

Self-review: passed. Independent audit: not yet performed.
