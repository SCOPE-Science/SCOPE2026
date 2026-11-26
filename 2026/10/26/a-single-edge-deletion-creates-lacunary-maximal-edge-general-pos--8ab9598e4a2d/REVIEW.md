# Independent mathematical audit

## correctness

PASS

The only endpoint pair at distance three is the missing edge's endpoint pair: same-side vertices share a neighbor in the nonempty residual opposite part, and all other opposite-side pairs are adjacent. Thus only triples consisting of two opposite spokes and their connecting middle edge can violate the condition. Fixing i included left and j included right spokes prohibits precisely their ij connecting middle edges and leaves all other middle choices free, yielding the binomial all-set enumerator. A maximal set must include every permitted middle edge. With both spoke sets nonempty, each missing spoke completes a forbidden triple using an included opposite spoke and a permitted middle edge, so it is blocked. With one side empty, all spokes of the other side must be chosen, which then blocks every spoke on the empty side; two empty sides are not maximal. The two one-sided cardinalities are st+t and st+s; mixed sizes equal st+1−(i−1)(j−1), ranging from the attained minimum s+t to the attained maximum st+1. These conclusions also hold for s=1 or t=1; at s=t=1 the graph is a three-edge path and the maximal polynomial is 3z². At s=t=m≥3 the mixed maximum is m²+1 and the only larger size is m²+m, omitting exactly the stated intervening m−2 integers. All counts distinguish actual labeled subsets.

## originality

PASS

The earlier inspected sources cover the scalar maximum for certain graph classes and the undeleted diameter-two case, not the complete two polynomials or the unbounded gap. There is a distinct exact catalog overlap on p,q≥3, including the central gap statement, in a record dated 2026-11-22, later than the frozen 2026-10-26 record; it is not ignored, but does not establish antecedent coverage. The pass concerns the complete enumerators and the facet-size effect at the frozen record, not the edge-general-position definition, the scalar maximum by itself, or the thin-class extension by itself.

## value

PASS

Deletion of one edge is the natural smallest perturbation of a diameter-two biclique. Before deletion its edge-general-position complex is a simplex; afterward the full size and facet polynomials describe which choices remain and how many. In particular a single deletion creates arbitrarily long gaps in sizes of inclusion-maximal sets, a structural effect invisible to the scalar maximum and not inferred from a small finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
