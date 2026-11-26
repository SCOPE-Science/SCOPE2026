# Independent mathematical audit

## correctness

PASS

At each Fisher triangle, either three external edges are matched or one is matched and the other sockets are paired. When two matchings differ at a triangle the two changed sockets are linked by either one internal edge or a two-edge path; hence alternating-cycle components correspond bijectively to the cycle components in the difference of even base subgraphs. In the given binary coordinates, a difference with b=1 selects one horizontal edge per sector, with rungs exactly at switches, making one connected cycle. With b=0 a single proper run gives a cycle, separate runs give separate cycles, and all ones gives two rim cycles, not one. An independent planar-dual argument confirms this: the dual is the suspension of C_n by two nonadjacent poles, and simple primal cycles correspond to bonds. Opposite pole colors make both sides of the cut connected regardless of the equatorial colors. Equal pole colors give a bond iff the other color occupies one nonempty proper interval; the whole equator in the other color would disconnect the poles. This yields the join for every n≥3, including the triangular prism. There are cross-part two-step paths and a nonedge inside each part (complementing all coordinates), so the diameter is exactly two. Counting the interval generators gives the stated degree, edge count and distance distribution.

## originality

PASS

The Fisher bijection and state count are prior. The exact generator count, hence regular degree once one identifies flips with base cycles, is also prior in a different formulation: OEIS A077265 counts prism cycles (equivalently dipyramid bonds) by exactly 2^n+n(n−1). The distinct contribution supported here is the classification of all adjacency by the interval-Cayley join and the resulting uniform sharp two-flip distance, not the raw counts or general connectivity.

## value

PASS

The join determines every legal move in an exponentially large matching space and gives an explicit at-most-two-move routing rule independent of n. That structural information is useful and distinct from the old counts; the uniform sharp metric conclusion does not depend on estimates for the length of each move.

The dated certificate retains the supplied scientific assessment, sources and limitations.
