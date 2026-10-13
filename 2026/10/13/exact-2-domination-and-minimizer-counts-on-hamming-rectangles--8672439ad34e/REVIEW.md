# Self-review

## Correctness
PASS. For an unchosen cell \((i,j)\), direct adjacency in \(K_m\mathbin{\Box}K_n\) gives exactly \(r_i+c_j\) chosen neighbors. The lower bound is an exhaustive dichotomy: either every column is nonempty, giving at least \(n\) chosen cells, or some column is empty, forcing every row count to be at least two and hence at least \(2m\) chosen cells. Both bounds have explicit constructions. Equality in each branch gives the stated minimizer classification, and the counting formulas follow from surjections, independent row-pair choices, and inclusion-exclusion at the boundary. The verifier independently exhausts all subsets for small rectangles and agrees with both the value and count formulas.

## Originality
PASS, with residual risk stated below. The recent full-text source arXiv:2501.03788 identifies triangular Young domination at latency one with ordinary \(a\)-domination, but its exact triangular theorem is restricted to equal factor orders; at \(a=2\) it gives only the square specialization \(\gamma_2(K_n\mathbin{\Box}K_n)=n\). Targeted searches for rectangular rook/Hamming 2-domination and minimizer counts found no statement implying the two-parameter formula or its classification. The 2020/2023 Carballosa--Wisby work concerns total 2-domination, which is strictly a different requirement because selected vertices must also have two selected neighbors. The 2009 Burchett--Lane--Lachniet predecessor is described by both its abstract and the recent paper as square-rook work; its full text was not available in the inspected open sources, so unadvertised overlap remains a residual risk rather than being declared impossible.

## Value
PASS. The result closes the first nontrivial unbalanced case left outside the recent exact triangular Young-domination theorem. It is a natural complete two-parameter classification, not an arbitrary finite slice: the aspect ratio creates a genuine threshold at \(n=2m\), the extremal configurations change type across that threshold, and the theorem gives exact enumeration of all minimum configurations. These facts are directly reusable as a base case for higher ordinary \(k\)-domination on Hamming rectangles and as a sharp comparison point against the substantially more complicated total 2-domination parameter.

Self-review: passed. Independent audit: not yet performed.
