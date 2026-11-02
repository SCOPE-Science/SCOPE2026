# Review of sharp adjacency–Dirac distances on cross-polytope graphs

## Correctness
PASS. The potential symmetrization is valid because graph automorphisms act by unitary permutations and the norm is convex; an involution plus sign reversal preserves the prescribed difference. The antipodal matrix has one rank-two skew block of norm \(\sqrt{r-1}\). The adjacent matrix compresses exactly to the displayed \(3\times2\) rectangular block, whose Gram eigenvalue gives the global minimum. The block's derivative has full column rank and hence induces strong convexity; differentiation establishes the unique optimizer in \((-1/2,0)\). The lower Gram diagonal forces strict separation. The uniform large-\(r\) eigenvalue expansion and derivative justify the leading, correction, and gap coefficients. `verify.py` passed 219 supplementary finite comparisons; these do not prove the infinite family.

## Originality
PASS within the recorded search, not independently confirmed. The closest 2024 motivating paper (arXiv:2409.04146) gives graph-general formulations and a complete result for paths, not for the nonbipartite complete multipartite family \(K_{2,\ldots,2}\). Besnard's 2021 paper (arXiv:2105.09056) supplies general bounds and pruning, not the two sharp distance classes and asymptotic gap. Prior exact work for complete bipartite graphs addresses the excluded four-cycle case and does not imply the result for \(r\ge3\). The comparison included alternative descriptions as cocktail-party graphs, cross-polytope one-skeleta, complete multipartite graphs, and octahedral graphs. An earlier equivalent spectral norm optimization in another language remains possible.

## Mathematical value
PASS. The \(r\)-dimensional cross-polytope is a canonical graph family with only two pair orbits; its adjacency-based spectral metric is an exact and mathematically natural invariant. Determining both orbits for every \(r\ge3\), the unique extremal parameter, and the quantitative collapse of the edge-versus-antipode metric distinction supplies more than a numerical example or a generic norm inequality. The order \(r^{-3/2}\) and leading constant \(1/8\) express a structural comparison between graph distance and spectral distance.

## Closest literature and limitations
Clare et al. (2024), arXiv:2409.04146, is the primary motivating source, first publicly available 2024-09-06. Besnard (2021), arXiv:2105.09056, provides bounds and reductions. Novelty is assessed from the accessible primary material and semantic/terminology checks, not certified against all literature. The theorem excludes \(r=2\), arbitrary weights and alternate Dirac choices. The adjacent distance is an exact attained algebraic minimization, not a uniform closed form in elementary radicals. Independent scientific validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
