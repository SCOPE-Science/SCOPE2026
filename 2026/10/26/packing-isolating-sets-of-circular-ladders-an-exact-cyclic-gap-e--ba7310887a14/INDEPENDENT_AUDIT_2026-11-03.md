# Independent mathematical audit

## correctness

PASS

For the simple labeled prism C_n square K_2, n>=3, disjoint closed neighborhoods prohibit two selected vertices in one or neighboring columns. For consecutive selected columns any clockwise gap >=4 leaves both vertices of an interior rung at distance >=2 from every selection and hence an uncovered edge; gap 2 cannot have equal selected rows because the two selections would have a common neighbor; gap 3 with equal rows leaves an edge joining the two undominated vertices in the opposite row. Thus all gaps are 2 or 3 with row alternation, which forces even k; a single selected vertex fails also on the n=3 triangular prism. Conversely, alternating rows across 2/3 gaps make selected vertices at least graph distance 3, dominate the selected columns and all vertices of 2-gaps, and leave only isolated opposite-row vertices across a 3-gap, with selected columns separating gaps. A cyclic k-gap word has n possible marked column starts, 2 row starts, and k counts of each unmarked placement, hence i_{n,k}=2n/k*binom(k,n-2k) for even k>=2 and 2k<=n<=3k. Differentiation of -log(1-u^2(t^2+t^3)^2) yields the claimed rational series and recurrence. Integer interval overlap gives exact existence n>=4 except 7 and minimum/maximum even cardinalities. Independent direct vertex-set enumeration with graph adjacency, closed-neighborhood intersections, and residual-edge test matched every k count for n=3..12; independent arithmetic matched recurrence through n=120.

## originality

PASS

Qualified best-of-knowledge originality. The defining mixed 2-packing plus vertex-edge isolation condition is in the 2026 Boyer–Goddard–Henning primary paper, but its tree existence and NP-hardness theorems do not give cyclic-prism counts. The 2023 Brešar–Klavžar–Rall bipartite-prism theorem concerns an open-packing maximum without edge isolation, and the 2025 Bujtás et al cycle gap theorem concerns vertex distance-domination in the base cycle. Actual full primary material and three published Resultary searches found no implication producing alternating rows plus 2/3 gaps and a full bivariate enumerator. Prior knowledge of cyclic gap encoding is acknowledged; a semantic nonmatch is not a mathematical novelty guarantee.

## value

PASS

The circular ladder C_n square K2 is a canonical connected cubic family with nontrivial cyclic obstruction beyond tree existence. Packing-isolating sets were explicitly studied for existence in trees and general graphs in 2026, making this exact infinite-family classification a motivated structural problem. The 2/3 cyclic-gap and forced alternate-row bijection simultaneously resolves existence, the exceptional n=7, every feasible even size and exact labeled multiplicities, together with an explicit rational bivariate generating function. This exact natural counting law is not a routine restatement of the prism open-packing maximum, and may serve for graph isolation/packing enumeration in other product families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
