# Self-review

## Correctness — PASS

The weighted Laplacian is defined explicitly and has a simple real spectrum for pairwise distinct positive leaf conductances. Its Gramian diagonalization yields an exact finite-horizon determinant factorization. An exact characteristic-polynomial evaluation eliminates the unknown eigenvalues, while polynomial identities for all Krylov determinants handle every repeated-weight boundary. Direct inequalities eliminate the hub and smallest-weight leaf, and the explicit near-collision construction realizes every remaining weight rank as a unique optimum. The standalone exact-rational verification program tests the identities and constructive rankings; it does not replace the proof for all real parameters. No claims are made about directed stars or other sensor criteria.

## Originality — PASS (bounded literature check)

The closest powerful antecedent is Fitch and Leonard (ECC 2016), Theorem 2, which already gives the general Laplacian-eigenvector product for Gramian log-volume ranking. That general spectral factorization is not claimed as new. The added claim is the spectral-free closed conductance formula for weighted stars, complete coincident-conductance observability classification, and attainability of exactly all nonminimum leaf ranks as unique optima. Parlangeli and Notarstefano (2011) treat unweighted paths/cycles; Xiang and collaborators (2013) treat qualitative weighted/directed leader control, including a star-symmetry criterion; Summers and Lygeros (2013) focus on modularity of a trace metric; Dilip (2019) studies packet-loss observability. Inspected material does not cover the explicit full statement. A 2025 tree-graph survey could not be read beyond its abstract, and older specialized weighted-star results may exist: this is a real residual risk, not asserted evidence of independence.

## Value — PASS

The theorem gives an exact, horizon-independent D-optimal node-placement rule at every star size and conductance tuple, determines whether any single node is fully observable at repeated weights, and shows exactly which conductance-rank positions can be made uniquely best. All these are motivated by single-sensor design for Laplacian diffusion rather than by an arbitrary fixed size or parameter selection.

## Scope and verification limits

The full-state finite-horizon determinant differs from pseudodeterminants in unobservable cases. Only undirected stars with positive time-independent weights, one coordinate sensor and strictly positive finite horizons are treated. The finite exact-arithmetic tests are supportive diagnostics, and no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
