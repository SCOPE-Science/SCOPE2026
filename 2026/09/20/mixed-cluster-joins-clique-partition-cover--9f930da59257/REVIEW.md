# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The covering number follows from a representative-induced $K_{h,\ell}$ lower bound and the obvious $h\ell$ cluster-pair cover. For the partition number, the Erdős--Faudree--Ordman cut inequality gives the lower bound $s-2a-b$ because the load condition implies $a\le b$. The constructive upper bound is edge-disjoint by cluster-pair design: every first-side internal edge is paired with a distinct second-side internal edge in a $K_4$; the remaining second-side internal edges use distinct still-unused cluster pairs in triangles; all other crossing edges are single-edge cliques. The three finite hypotheses are exactly what is needed for these assignments. The asymptotic parameter choice satisfies them with slack except for the defining second-side size capacity, which is enforced exactly by the choice of $q$.

The proof was stress-tested against small and moderate admissible parameters by direct construction. The public verifier checks 898 parameter tuples and confirms exact edge coverage, edge-disjointness, clique validity, and the stated partition cardinality. Finite verification is supportive rather than a replacement for the symbolic proof.

## Originality

**PASS, to the best of our knowledge.** Ning's 2026 preprint proves the order $d_n=\Theta(n^{4/3})$ and gives an exact formula for the balanced uniform family $(hK_k)\vee(hK_k)$ for even $k$, followed by isolated-vertex padding for arbitrary $n$. The Erdős--Faudree--Ordman cut inequality is prior work and is not claimed as new. Searches using clique partition/covering, joins of cluster graphs, unequal clique clusters, cographs, and equivalent construction language did not locate the heterogeneous formula here or the explicit all-order limsup coefficient $3/2^{5/3}$. The checked primary statements in Ning's current preprint do not contain either result.

Residual risk remains from older clique-decomposition and design literature that may use different terminology, and from very recent unindexed work. No specific inaccessible source was found whose stated results strongly suggest coverage of the mixed-cluster theorem.

## Value

**PASS.** The result strengthens the currently used extremal construction in two ways that matter quantitatively: it permits unequal cluster scales and absorbs the exact vertex-count remainder inside cluster sizes rather than isolated vertices. Optimizing the two cluster scales then gives an explicit coefficient $3/2^{5/3}\approx0.9449407874$ in the known $n^{4/3}$ deficit order. The theorem also provides a reusable finite criterion for exact attainment of the cut lower bound on a natural cograph family.

## Limitations

The stated capacity conditions are sufficient, not asserted necessary. The numerical coefficient is an explicit construction bound, not proved optimal. The result does not improve the known $\Theta(n^{4/3})$ order itself. Independent audit has not been performed.
