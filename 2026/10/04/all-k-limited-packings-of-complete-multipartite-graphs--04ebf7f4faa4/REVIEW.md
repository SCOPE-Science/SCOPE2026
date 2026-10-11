# Independent mathematical audit

## correctness

PASS

For a vertex in part \(i\), the closed-neighborhood intersection has size \(1+b-b_i\) if selected and \(b-b_i\) otherwise. If \(b\le k\) feasibility is automatic. If \(b>k\), every part must contain a selected vertex and the selected-vertex inequality is exactly \(b_i\ge b-k+1\); it is also sufficient. For a fixed size \(s>k\), feasibility is equivalent to \(s-k+1\le\min_i n_i\), \(r(s-k+1)\le s\), and \(s\le N\), which yields the maximum formula. Fresh literal replay checked 42,640 cases through order seven.

## originality

PASS

Best-of-knowledge originality passes. Gallant et al. give the exact complete-bipartite value \(L_k(K_{m,n})\) as Lemma 1.3 and general bounds, but their complete six-page paper does not contain the arbitrary complete-multipartite all-set criterion or enumerator. Later sources emphasize bounds and algorithms rather than this symbolic family classification.

## value

PASS

This is a natural complete classification of a standard packing notion on a canonical graph class, refining the known bipartite maximum value to every feasible set and every cardinality. The coefficient formula and sharp maximum are directly useful consequences of one structural quota rule, so the result has independent reference value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
