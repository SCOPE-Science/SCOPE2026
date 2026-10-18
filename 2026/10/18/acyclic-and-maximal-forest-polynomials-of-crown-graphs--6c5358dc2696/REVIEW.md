# Scientific review

## Correctness — PASS

The graph is specified by \(a_i b_j\in E\) if and only if \(i\ne j\). A selected bipartite profile has exactly \(ab-t\) induced edges, where \(a\), \(b\) count vertices on the two sides and \(t\) counts shared indices. For \(a,b\ge2\), acyclicity forces \((a-1)(b-1)\le t\le\min(a,b)\), restricting the profile to \((2,2,t\ge1)\) or \((2,3,t=2)\), up to transposition. Each surviving profile is directly confirmed acyclic, and the min-side-at-most-one profiles are forests. Counting these disjoint cases gives the full bivariate polynomial.

Every smaller profile admits an explicit one-vertex extension; exactly the \((2,3,t=2)\) profiles and (for \(n\ge4\)) full-side-with-one-opposite-vertex profiles prohibit every extension. These yield the facet polynomial and its pure/nonpure threshold. Complementation correctly converts facets to inclusion-minimal feedback vertex sets. An independently implemented adjacency and union-find checker verified all bivariate coefficients for \(3\le n\le9\), examining \(349{,}504\) subsets. The general proof does not depend on those finite checks. Scope excludes \(n<3\).

## Originality — PASS, subject to residual priority risks

Barton, Brown, and Pike introduced the acyclic polynomial and derived a join identity (arXiv:2011.01735, Theorem 1.3). It does not directly cover a bipartite graph with a perfect matching deleted. Jafarpour-Golzari's well-\(f\)-covered classification includes complete bipartite graphs (arXiv:2105.14339, Theorem 6.15 and Corollary 6.16), but not the matching-deleted crown family. Gunderson and collaborators study largest induced forests of Kneser and tensor-power graphs (arXiv:2301.05207), including \(K_n\times K_n\), which has \(n^2\) vertices and differs from \(K_2\times K_n\). That result is not a formula for the present graph's entire induced-forest or facet distribution.

Published findings on crown-graph dissociation, domination, and graph-metric invariants do not imply these acyclic-polynomial coefficients: their feasible subgraph classes differ. Search terms included crown, bipartite double cover, induced-forest complex, minimal feedback vertex set, and acyclic polynomial. No covering formula was located in the inspected material, though search incompleteness and alternate terminology create a nonzero bibliographic-priority risk. Independent priority verification has not occurred.

## Value — PASS

The result solves a natural, fully specified counting problem for a connected, regular, distance-transitive bipartite graph family: both all faces and all facets of its induced-forest simplicial complex are enumerated exactly by their two bipartition occupancies. It also yields a sharp transition from well-\(f\)-coveredness to nonpurity at \(n=5\) and an unbounded gap in the sizes of maximal induced forests and minimal feedback vertex sets. Neither a scalar decycling number nor the pre-existing complete-bipartite well-\(f\)-covered classification determines these distributions or gaps. This is a complete infinite-family classification, rather than a finite census or a numerical parameter substitution.

## Limitations and closest literature

The theorem applies only to \(n\ge3\) and deletion of a complete perfect matching. The graph-product comparison is with a nonisomorphic family and does not itself establish novelty. Finite verification is not an infinite proof. Relevant primary sources were inspected in full-text accessible renderings, but not every possible print or unindexed record can be excluded. Scientific priority and correctness have not been independently assessed.

Self-review: passed. Independent audit: not yet performed.
