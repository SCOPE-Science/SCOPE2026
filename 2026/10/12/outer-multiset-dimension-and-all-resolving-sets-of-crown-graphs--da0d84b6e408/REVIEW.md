# Independent mathematical audit

## correctness

PASS

For n>=3, the crown graph has distance 1 between nonpaired opposite-shore vertices, 2 within a shore, and 3 across the missing matched edge. For each omitted a_i, the selected-vertex distance multiset has n-x copies of 2 and, depending on i in Y, either n-y copies of 1 or n-y-1 copies of 1 plus one 3; the symmetric expression holds for b_j. Each shore therefore admits at most two omissions, and two require exactly one mate omitted across the shore. When x=y=1 the two omitted vertices have identical multisets; when x=y=2, the required intersection=1 also produces a cross-shore collision. Different x,y give different 2-counts, leaving precisely (0,0),(1,0),(0,1),(2,1),(1,2), with the latter requiring intersection=1. Counting omitted indexed pairs gives odim(Cr_n)=2n-3, 2n(n-1) bases and the exact three-term set enumerator. Independently implemented exhaustive graph-distance/subset checks n=3,4,5,6 confirmed all cases, including the absent size 2n-2;  finite checks do not prove the infinite theorem.

## originality

PASS

The equal-distance-multiset classification is not implied by the existing multipartite invariant because Cr_n has missing cross edges, diameter 3, and contains a non-multipartite adjacency pattern; fixed complete-bipartite baselines and edge-metric or odd-coloring results are different invariants. The primary outer-multiset literature states diameter-two extremals and multipartite families, not this all-set classification. Best-of-knowledge originality survives with indexing/alias risk.

## value

PASS

Crown graphs are a standard symmetric one-factor-deletion model. An exact full resolving-set classification, base count, and forbidden size 2n-2 answer a natural identification invariant under the smallest structured change to a biclique; the sharp dimension drop 2 from K_{n,n} gives a perturbation boundary beyond a bare small-number computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
