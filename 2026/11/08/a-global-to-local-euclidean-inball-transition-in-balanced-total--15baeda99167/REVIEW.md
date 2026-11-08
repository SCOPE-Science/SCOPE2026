# Self-review

## Correctness — PASS

The statement uses the full-dimensional standard Euclidean incidence embedding, with explicit quantification over all integers \(n\ge2\). Faenza--Ferrarini [2, Theorem 2] supplies the complete facet list. The proof checks all five facet families, including the weighted nonbalanced lifted inequalities in [2, equation (7)]. Inward-shifting the coordinate facets yields the universal lower bound on every inball-center coordinate. This gives an upper bound from each remaining positive normal, while the uniformly shifted center attains the minimum of those obstructions. The algebraic identity \((u+2)B-S=\tau b(u-a)\), and the positive-coefficient expansion of \((u+2)B^2-H\), show that all nonbalanced facets lie strictly outside the candidate ball. The strict comparisons at \(n=2,3,4\) and monotonicity beyond establish the claimed sharp phase change. Tight positive-coefficient inequalities prove uniqueness and exclude all other facets from the contact set. A separately run SciPy checker reconstructed the complete facet system for \(n=2,3,4\), verified radius/contacts/center coordinate extrema, and tested all lifted-facet parameter orbits through \(n=30\); these checks corroborate but do not replace the proof.

## Originality — PASS, with stated residual risks

Ferrarini [1] describes balanced and nonbalanced lifted biclique facets; Faenza--Ferrarini [2] provides an irredundant full facet description and a compact extended formulation. Neither inspected full text computes intrinsic Euclidean inradii, uniqueness, or the global-to-local tangent-facet transition. Direct comparisons also covered the stable-set reinterpretation and the closest recorded formulas for perfect-graph stable-set inballs and ordinary matching-polytope inballs. The former is not applicable because the total graph of \(K_{2,2}\) has an induced five-cycle; the latter changes the coordinate polytope. Originality is assessed against checked accessible materials and mathematical implication, not claimed as absolute priority. Residual risk remains from alternative Chebyshev-center terminology or unindexed theses.

## Mathematical value — PASS

The cited complete facet lists are exponential in size, with highly nontrivial lifted normals. It is not automatic from the facet catalog which inequalities control Euclidean inballs; the proof yields a uniform all-dimensional screening lemma and a surprising sharp transition between one *global* biclique contact and \(2n\) *local* degree contacts. The exact radius and complete tangent-facet census constitute natural metric and structural invariants of a graph-polytope family used in total coloring and combinatorial optimization. This is not merely a numerical sample, a restatement of a facet inequality, or a routine special case of the perfect-graph stable-set result.

## Sources and limitations

[1] Ferrarini, arXiv:2111.15528 (2021), sections on biclique inequalities and complete bipartite graphs.

[2] Faenza--Ferrarini, arXiv:2303.00328 (2023), sections 2--4, especially Theorem 2 and equation (7).

The result is limited to the canonical unweighted balanced embedding, with no assertion for unbalanced graphs or alternate metrics. Independent priority and independent mathematical verification have not been established. Finite LP and orbit checks are reproducibility evidence, not an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
