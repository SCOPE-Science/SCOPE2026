# Review of Leaf-label complements give an exact biclique lower bound for Krajíček search-tree error

## Correctness
PASS. The claim is reconstructed directly from the published definitions. For an admissible restriction, \(|D^\rho|=2d+1\) and \(|R^\rho|=2d\). If the leaf-label set misses that rectangle, every possible output is an error independently of the chosen design. For fixed complements \((D,R)\), exactly \((n-2d)!\) bijections produce the corresponding partial injection, so the two complements are independent uniform subsets. The biclique-density identity, union bound, leaf-count bound, and Zarankiewicz consequence then follow with the stated quantifiers. No infinite conclusion is inferred from a finite experiment.

Risk: the paper's notation alternates between the pair \((\rho,L)\) representation and the induced map \(\omega\). Section 5 explicitly averages uniformly over restrictions and then designs, which is the distribution used in the theorem here.

## Originality
PASS. The 2026 primary source was inspected in the sections defining \(\Omega(n,d)\), the residual output condition, the tree-error functional, and the final reduction. Targeted searches for “biclique”, “Zarankiewicz”, “leaf labels”, and “range” found no statement of this support-only theorem. The 2024 predecessor was inspected around Definition 4.2, Lemma 4.3, and Problem 4.4; it supplies the restriction construction but not the biclique-density or support-size conclusion. Published-finding searches using the source identifier and aliases for residual rectangles, leaf-label support, biclique density, Zarankiewicz numbers, and output-range union bounds returned no implication covering the claim.

Residual risk: an equivalent finite set-system fact may be known abstractly as a rectangular hitting-set observation. The checked literature did not locate its application to this search-tree reduction, and the result is stated as that application rather than as a new extremal-graph theorem.

## Value
PASS. The 2026 reduction turns a long-standing proof-complexity lower-bound problem into an error question for a newly introduced search-tree formulation. The theorem extracts the exact portion of that error forced solely by the output support and identifies its governing invariant as complete-bipartite density in the complement. This gives both quantitative finite-error thresholds and a sharp zero-error obstruction via a standard extremal parameter. The limitation is mathematically informative: once the output support is dense enough, any stronger lower-bound argument must use the algebraic/path information omitted by the support-only invariant.

The value is structural and diagnostic rather than a downstream proof-complexity lower bound; the limitations state this explicitly.

Self-review: passed. Independent audit: not yet performed.
