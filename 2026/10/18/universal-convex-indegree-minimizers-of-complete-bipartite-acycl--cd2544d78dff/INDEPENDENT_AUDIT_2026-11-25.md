# Independent mathematical audit

## correctness

PASS

The orientation fixes the relative order of every opposite-part pair, so changes between topological orders can only permute labels within same-letter runs. An AB/BA swap after prefix counts (i,j) has cost difference Δφ(i)−Δφ(j), retaining all other indegrees. A prefix with A-surplus ≥2 has a future B; at the last A before the first such B the pre-pair surplus is ≥1 and the swap improves. A prefix with B-surplus ≥2 while an A remains similarly has a strictly improving BA swap at the first subsequent A. Consequently every even prefix of length ≤2m must have zero surplus in an optimum: a negative even surplus there cannot occur after all m A's, and positive even surplus is excluded globally. Thus each pair is balanced and all excess B's trail. Each tile starting at (j,j) contributes {j,j+1}; the tail contributes t copies of m, giving the stated value and multiset. Each improving exchange is an integer balancing transfer, terminates by strict decrease of sum of squares, and certifies majorization, so convex costs with flat increments may have extra ties but cannot undercut the tiled words. The multiplicity per word divides m!(m+t)! by its run factorials: a tile change creates one length-2 run and no length-3 run can arise except from the tail; the final run factors are t! and (t+1)!, with 0!=1. The weighted change count at a fixed final tile is (1+1/2)^(m−1), proving the formula including m=1 and t=0. The independent Boolean-row enumeration used nesting (equivalent to no directed 4-cycle, hence no cycle because a longer shortest cycle would have a chord). It checked all 13 packaged sizes, 104334 assignments and 13638 acyclic orientations: every indegree vector dominates the target for every hinge, and equality for all hinges selects exactly the labelled tile-generated masks. The computed counts at (2,3) and (3,3) were 27 and 162.

## originality

PASS

Credit West's exhaustive alternating-block representation and the earlier total orientation counts. The distinct supported claim is the simultaneous strict-convex minimizer class, least-majorized multiset, and exact filtered count over all bicliques. The strongest checked general optimization statements do not establish a least-majorized acyclic orientation in general; the matching biclique statements encode or enumerate the whole orientation class, not this optimizer subset.

## value

PASS

This resolves a natural unbounded graph family for a general acyclic convex optimization problem where the optimizer can otherwise depend on the cost. It gives the common optimizer set, a certificate by balancing transfers, and the exact number of distinct optimal orientations rather than orders or all orientations. The simultaneous hinge/majorization bound is a usable strengthening of one-off quadratic optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
