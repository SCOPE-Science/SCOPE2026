# Review of Perfect Roman domination of crown graphs

## Correctness
PASS. A deleted matched pair labeled \(2,2\) gives a valid weight-\(4\) perfect Roman function because every other vertex is adjacent to exactly one of those two vertices. Weight at most \(3\) allows at most one value-\(2\) vertex; if that vertex lies in one bipartition class, all other vertices of the same class must be positive. At optimum weight \(4\), a one-defender solution is impossible: for \(n\ge4\) it is already too heavy, and for \(n=3\) it leaves the matched opposite vertex undefended. Thus two value-\(2\) vertices are required. They must lie in opposite classes, and their indices must match, because otherwise one zero vertex is precisely the nonneighbor of the opposite value-\(2\) vertex. Exhaustive checks for \(3\le n\le7\) reproduce the value and all minima.

## Originality
PASS. The closest primary source is the 2018 regular-graph paper. Its packing construction yields the same weight-\(4\) candidate when specialized to a deleted matched pair, but its theorem is an upper bound for general regular graphs and does not prove optimality or classify crown minima. Targeted full-text searches found no crown or bipartite occurrence in that paper, and targeted searches of the 2019 algorithmic paper found no crown, deleted-matching, or complete-bipartite-minus-matching formula. Database and web searches under “crown graph,” \(K_{n,n}-M\), and regular-bipartite aliases located no equivalent theorem.

## Value
PASS. Crown graphs are a standard dense regular bipartite family in which every vertex has a unique nonneighbor on the opposite side. The theorem shows that this deleted perfect matching is not merely a convenient construction: it exactly parameterizes every optimum perfect Roman defense. This gives a natural exact family inside the regular-graph setting of the foundational bounds paper and adds a complete optimizer count, rather than only another upper bound.

Same-model review: passed. Independent audit: not yet performed.
