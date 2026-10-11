# Independent mathematical audit

## correctness

PASS

Let \(X=V(G)\setminus D\), \(q=|X|\), and \(t=q-k\). For a selected vertex in part \(V_i\), the number of outside neighbors is exactly \(q-x_i\); the capacity condition is therefore \(x_i\ge t\), equivalently \(d_i\le n_i-t\). A minimum solution has \(q\ge k\), cannot be a singleton in the range \(k<\Delta(G)\), and when \(t>0\) cannot lie in a single part, giving the stated bounds on \(t\). Summing the part capacities yields \(\sum_i\min(n_i,t)\le k+t\). Conversely, any feasible \(t\) provides at least two positive part capacities whose total is at least \(N-k-t\), so one can choose a dominating set meeting two parts and satisfying every capacity inequality. The balanced specialization reduces exactly to \((r-1)t\le k\).

## originality

PASS

The initiating 2026 paper gives exact values for paths, stars, complete graphs, and complete bipartite graphs, and explicitly lists determination on additional graph families as future work. Its regular-graph connection to \((1,t)\)-domination does not determine arbitrary unbalanced complete multipartite profiles. Fresh Resultary and literature searches found no same-invariant complete-multipartite threshold formula or stronger theorem implying it. The biclique result is strictly a specialization of the audited formula, not the other way around.

## value

PASS

Complete multipartite graphs are a standard structural family containing cliques, stars, bicliques, and Turán graphs. The theorem strictly extends the initiating paper's exact biclique result, gives a sharp one-dimensional criterion for every part profile, and yields a closed balanced formula. This is a motivated complete family classification rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
