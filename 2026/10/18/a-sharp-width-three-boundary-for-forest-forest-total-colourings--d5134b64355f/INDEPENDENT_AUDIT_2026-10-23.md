# Independent mathematical audit

## correctness

PASS

For 1<=a<=b and a<=3, N=a+b+1 and M=ab+a+b. Each vertex color class has s_c<N since the tripartite graph contains a triangle; the edge forest of color c avoids s_c vertices and has at most N-s_c-1 edges. Thus M<=k(N-1)-N; algebra gives k>=3 at a=1, >=4 at a=2, and >=4 for a=3,b<=5 or >=5 for b>=6. The explicit hub-color/part-color and AB-star coloring uses a+2 colors where needed. For the finite exceptional K_{1,3,5}, the RESULT.md vertex and 23 edge assignments avoid endpoint colors, give acyclic edge classes with edge counts 7,6,7,3 on the allowed 8,7,8,4 vertices and acyclic vertex-induced graphs; I checked all 23 edges, four forests, and capacity saturation independently. Deleting B columns preserves valid colorings for b=3,4. At (3,5), total forest capacity is exactly M=23, so every optimal coloring saturates each color capacity and gives a spanning tree. This establishes the entire a<=3 infinite family; finite checks only corroborate witness details.

## originality

PASS

Borowiecki–Kemnitz–Marangio–Mihók (2011) explicitly define forest–forest generalized total colorings and prove the complete-graph value in Theorem 8, not a tripartite width-3 family. Cara–Dorfling arxiv:2608.19294 treats planar graph families; K_{1,3,5} contains K_{3,3}. A fractional total-coloring result on complete graphs uses another invariant. No located primary formula dominates the a=1,2,3 all-b classification or the saturation statement; residual coverage risk remains for unindexed tripartite total-coloring articles.

## value

PASS

This gives a complete exact phase diagram in an unbounded natural tripartite family, determines a genuinely exceptional nonplanar K_{1,3,5} four-color witness instead of five generic star colors, and proves structural spanning-tree rigidity of every optimum at the sharp endpoint. These are nonroutine extremal facts, not arbitrary numerical slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
