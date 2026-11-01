# Independent mathematical audit

## correctness

PASS

Represent each rook cell as an edge of K_{p,q}. The exact uncovered-cell set after a chosen edge prefix is unused-row×unused-column cells plus chosen incidence edges that remain isolated K2 components. A legal newly chosen edge with both endpoints used must touch an isolated previous component, hence joins different forest components; if an endpoint is unused, it cannot form a cycle. Thus EVERY legal prefix is a forest and length<=p+q−1. If a spanning tree is attained, at first exhaustion of one side, with b opposite unused vertices, c existing edge components, and s isolated edge components, the remaining construction needs b+c−1 moves but at most s<=c can be legal, forcing b=1 and s=c, and hence q=p+1. Explicit diagonal-first and star-then-merging legal sequences attain p+q−2 for all 2<=p<=q and p+q−1 exactly when q=p+1. Known duality with skew zero forcing gives Z_-=pq−p−q+2−1_{q=p+1}. Independent exhaustive direct rook-neighborhood DP reproduced formula on 8 small rectangular boards, not as infinite proof.

## originality

PASS

General Grundy total domination and skew zero-forcing duality are prior. Brešar et al. primary full paper treats Cartesian products of paths and cycles, not the exact complete-factor Kp□Kq rook family. Prior positive-semidefinite forcing result on square rook graphs has a distinct forcing convention and does not imply the claimed skew formula in rectangles. A specialized line-graph theorem or dissertation could contain an equivalent count, so priority remains qualified.

## value

PASS

This exactly classifies Grundy total domination for a canonical two-parameter Cartesian graph family, including a genuine one-column exception. The incidence-forest invariant for every legal sequence explains the global obstruction and yields an independently useful skew-forcing number; this is not a mere renaming of general domination duality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
