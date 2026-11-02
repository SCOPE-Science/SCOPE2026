# Independent mathematical audit

## correctness

PASS

A newly formed 132 pattern during an adjacent swap must use the swapped pair, yielding necessary/sufficient local criterion: ascent x<y may swap when no earlier z<x; descent x>y may swap when no later y<z<x. Repeatedly swapping leftmost ascent reaches the reverse permutation and proves connectivity. To move n left past each b<n legally, every pair a<b<n must reverse orientation twice, giving 2*binom(n-1,2)+(n-1)=(n-1)^2; a constructed ascent-sort-to-reverse followed by legal suffix sorting achieves exactly this. Catalan maximum decomposition yields E(z)=z(C(z)-1)/(1-2zC(z)), whose n coefficient is binom(2n-2,n-2). Independently constructed all 132 avoiders and full swap graph for 2<=n<=8, checked exact vertices, edges, connectivity and BFS distance, without extrapolating finite tests to all n.

## originality

PASS

Catalan vertex count and reduced 132-avoiding sorting networks are known, but the latter enumerate monotone inversion-increasing paths to the reverse permutation. The exact nonmonotone geodesic from identity to the right rotation, requiring wholesale reversal of n-1 other entries, does not follow from the inspected tableaux/sorting-network theorems. Aisbett uses a different non-adjacent block relocation relation.

## value

PASS

The exact ratio n-1 between intrinsic and ambient geodesic distances is unbounded in an induced Catalan permutohedron subgraph. It is a concrete structural obstruction to assuming pattern-avoiding induced paths preserve the ambient metric and comes with the natural full vertex/edge count; it is neither an arbitrary small-case statistic nor an unsupported diameter assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
