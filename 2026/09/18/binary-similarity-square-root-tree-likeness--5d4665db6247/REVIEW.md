# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The exact reduction to correlation clustering was checked in both directions. For any compatible rooted weighted tree, leaf edges can be lengthened so every leaf has depth at least \(b\) without affecting off-diagonal Gromov products or increasing diagonal error against a reflexive \(\{0,b\}\)-valued target. Clipping the tree similarity at \(b\) then decreases pointwise error. For each \(0<t<b\), the threshold relation \(\{\langle x,y\rangle_r\ge t\}\) is a measurable equivalence relation with finitely many nonsingleton classes, because equality of the initial root path through depth \(t\) is transitive and the tree has finitely many internal vertices. Layer cake therefore gives the lower bound \(\operatorname{Tree}(s)\ge b\operatorname{Clust}(A)\). Conversely, any finite-core clustering is represented by a one-level compatible tree with cluster nodes at depth \(b\), singleton leaves at depth \(b\), and arbitrarily short positive leaf edges beneath nonsingleton cluster nodes, giving the reverse inequality in the infimum.

For binary \(s=bA\), the hyperbolicity defect is exactly \(b\) on ordered bad triangles and zero elsewhere, so \(\operatorname{Hyp}(s)=b\beta(A)\).

The Poisson-pivot disagreement estimate was checked case by case. A false positive requires a common positive pivot and contributes at most \(\lambda\beta\). An assigned false negative has an earliest separating pivot; the two orientations contribute at most \(2\lambda\beta\). For an unassigned positive pair, with neighborhood mass \(q(x)\), Poisson thinning gives an upper bound \(\mathbb E[q(X)e^{-\lambda q(X)}]\le1/(e\lambda)\). Hence some finite-core clustering has disagreement at most \(3\lambda\beta+1/(e\lambda)\). Optimizing at \(\lambda=(3e\beta)^{-1/2}\) gives \(2\sqrt{3/e}\sqrt\beta\), and the \(\beta=0\) case follows by letting \(\lambda\to\infty\).

The finite-graph translation was checked with ordered-pair and ordered-triple normalizations. Cluster-edit distance \(k\) gives disagreement \(2k/n^2\), while each unordered induced \(P_3\) gives exactly two ordered bad triples, so \(\beta=2p_3/n^3\). Rearrangement yields \(p_3\ge(e/6)k^2/n\). For the disjoint union of \(m\) copies of \(K_{q,q}\), direct optimization of each cluster's two-side occupancies gives \(k=mq(q-1)\) and direct counting gives \(p_3=mq^2(q-1)\), verifying the claimed quadratic-order sharpness example.

## Originality

Yim's complete arXiv v2 was inspected at the framework definitions, the multilevel pivot construction, Lemma 4.1, Proposition 4.2, the general cube-root theorem, Proposition 5.1, and the discussion of the exponent gap. The paper proves the general \(1/3\)-exponent upper bound, supplies a binary family attaining the square-root lower scale, and asks whether a square-root upper bound holds in the full framework. It does not state the binary-subclass square-root theorem or the exact identity between binary tree-likeness and a finite-core correlation-clustering optimum. Its Proposition 4.2 contains the three disagreement estimates used here at each threshold; the new step is to identify that a genuinely binary target has only one nontrivial threshold, so no discretization or common-refinement loss is necessary.

Chatterjee--Sloman was checked for the earlier qualitative average-hyperbolicity-to-tree-approximation result. Ailon--Charikar--Newman and later correlation-clustering literature establish pivot algorithms and treat bad triangles as standard obstructions; those ingredients are not claimed as new.

Searches covered "average hyperbolicity" with binary/two-valued similarity, tree-likeness, correlation clustering, bad triangles, cluster editing, cluster graphs, induced \(P_3\) density/removal, square-root estimates, and the exact finite-graph inequality. No prior source was found stating \(\operatorname{Tree}(s)=b\operatorname{Clust}(A)\) in this framework, the resulting universal binary square-root bound, or \(p_3(G)\ge(e/6)k(G)^2/n\). Searches of the current SCOPE archive by the same objects and synonymous claim families found no overlap, and recent repository additions did not indicate a collision.

No inaccessible source was identified whose title or accessible metadata specifically signals the same theorem. The correlation-clustering and cluster-editing literatures are large, and the motivating preprint was submitted only days ago, so differently phrased or not-yet-indexed prior coverage remains a residual originality risk.

## Value

The result closes the exponent gap highlighted by Yim on the natural one-threshold subclass and explains exactly why the general multilevel obstruction disappears there. The identity with correlation clustering is structural rather than merely numerical: it identifies binary tree fitting with an established partitioning objective on arbitrary probability spaces. The graph corollary turns the same mechanism into a dimensionally natural quadratic induced-\(P_3\) removal inequality in terms of cluster-edit distance. Yim's binary extremizers certify that the square-root exponent, and hence the quadratic removal order, cannot be improved in general.

## Limitations

Only reflexive two-valued similarities are covered. The argument does not solve the square-root problem for general similarities with many threshold levels. The constant \(2\sqrt{3/e}\) is not proved optimal; the known binary lower family only forces it to be at least \(1\). Likewise, \(e/6\) is not claimed to be the best finite-graph constant. Residual originality uncertainty remains because both the recent tree-likeness work and the broader correlation-clustering literature may contain unindexed or differently formulated related results.
