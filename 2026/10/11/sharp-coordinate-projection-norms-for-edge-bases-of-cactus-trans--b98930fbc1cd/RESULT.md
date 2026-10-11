# Sharp coordinate-projection norms for edge bases of cactus transportation spaces

## Finding
Let \(G=(V,E)\) be a finite connected simple cactus graph with at least two vertices and strictly positive edge lengths \(w_e\). Give the vertex set the shortest-path metric. For an arbitrary spanning tree \(T\) let \(b_e=\delta_{e^+}-\delta_{e^-}\), \(e\in T\), be the oriented edge-molecule basis of the real Lipschitz-free space \(\mathcal F(V)\). For \(S\subseteq T\), let \(P_S\) retain the coordinates of this basis indexed by \(S\) and delete all others.

Every simple cycle \(C\) contains exactly one edge \(r_C\notin T\). Define \(L_C=\sum_{e\in C}w_e\) and \(W_C(S)=\sum_{e\in C\cap S}w_e\). Then, exactly,
\[
\boxed{\|P_S\|=\max\left\{\mathbf1_{S\ne\varnothing},\ \max_{C\in\mathcal C(G)}\frac{\min\{W_C(S),L_C-W_C(S)\}}{w_{r_C}}\right\}.}
\]
Here \(\mathcal C(G)\) is the family of simple cycles, and a maximum over an empty family is zero. In particular, \(P_\varnothing=0\).

For unit edge lengths, put \(\kappa(G)=\max\{1,\max_{C\in\mathcal C(G)}\lfloor |E(C)|/2\rfloor\}\). For every spanning tree and **every ordering of its edges**, both the maximum norm of all coordinate-suppression projections and the maximum norm of all nonzero partial-sum projections equal \(\kappa(G)\). Consequently these tree-edge Schauder bases are monotone if and only if all cycles are triangles or there are no cycles. The result is independent of the choice of base vertex and all edge orientations.

## Assumptions and scope
A cactus is a finite connected simple graph in which any two distinct simple cycles have no common edge (equivalently, every edge lies on at most one simple cycle). Cycles may meet at articulation vertices. Bridges, branching, and arbitrarily many cycles are permitted. Edge lengths are positive and need not equal their own endpoint shortest-path distance: an overlong edge remains part of the weighted graph presentation. The norm is over the real scalars. The coordinate projections refer to the tree edge molecules, not to orthogonal or metric projections, not to projections onto the cycle space, and not to arbitrary Schauder bases.

To define \(P_S\), first observe that these \(|V|-1\) molecules form a basis of the zero-total-mass measures on \(V\) because the oriented incidence matrix restricted to \(T\) is a linear isomorphism onto that space. The assertion covers every \(S\subseteq T\), including the empty set and the full tree.

## Proof
**1. Graph-flow quotient.** Equip the edge-flow space \(\mathbb R^E\) with \(\|z\|_{1,w}=\sum_{e\in E}w_e|z_e|\). Let \(\partial:\mathbb R^E\to\mathbb R^V_0\) be the oriented incidence operator. The induced quotient norm on \(\mathbb R^E/\ker\partial\) equals the Lipschitz-free norm for the shortest-path metric: the dual of the quotient is exactly the vertex potentials whose edge differences satisfy \(|f(e^+)-f(e^-)|\le w_e\) for every edge, which are exactly the \(1\)-Lipschitz potentials for the shortest-path metric. Thus
\[\mathcal F(V)\ \cong\ \ell_1(E,w)/\ker\partial\]
**isometrically**. Write \(q\) for this quotient map, so \(q(\mathbf e_e)=b_e\) for every oriented edge; orientations may be chosen consistently around each simple cycle.

**2. Cactus decomposition.** Every cycle is edge-disjoint from all the others. Orient the edges of each cycle coherently and orient bridges arbitrarily. The flow kernel is spanned by the vectors \(\mathbf1_C=\sum_{e\in C}\mathbf e_e\), one for each cycle. Indeed these vectors are independent because their edge supports are disjoint, and their number equals \(|E|-|V|+1=\dim\ker\partial\); the dimension follows from connectedness. Hence the quotient norm splits as a weighted \(\ell_1\)-sum of the individual cycle quotients and the one-dimensional bridge spaces. Every spanning tree contains each bridge and all but one edge of each cycle. Call the omitted edge of cycle \(C\) by \(r_C\). Inside the quotient,
\[q(\mathbf e_{r_C})=-\sum_{e\in C\setminus\{r_C\}}q(\mathbf e_e).\]
The edge orientations can be reversed at will without affecting any resulting operator norm.

**3. Exact coordinate-projection norm.** The quotient map \(q:\ell_1(E,w)\to\mathcal F(V)\) is a metric quotient. For any bounded operator \(P\) on the quotient,
\[\|P\|=\max_{e\in E}\frac{\|Pq(\mathbf e_e)\|}{w_e}.\]
The upper bound follows by applying \(Pq\) to arbitrary edge flows and minimizing over representatives; the lower bound follows by testing each \(q(\mathbf e_e)\), whose norm is at most \(w_e\). Apply this equality to \(P_S\). For a tree edge not in \(S\), the image vanishes. For a tree edge in \(S\), its image has quotient norm at most its edge weight, so its ratio is at most one. For every omitted edge \(r_C\), the image is the negative of the sum of the selected tree edges of \(C\). By the single cycle relation, its quotient norm is exactly
\[
\inf_{t\in\mathbb R}\bigg(\sum_{e\in C\cap S}w_e|1-t|+\sum_{e\in C\setminus S}w_e|t|\bigg)
=\min\{W_C(S),L_C-W_C(S)\}.
\]
The last equality is the weighted-median minimization for two values \(0\) and \(1\), and it holds even when an edge is not shortest between its endpoints. Division by \(w_{r_C}\) gives the cycle terms. If \(S\ne\varnothing\), the nonzero idempotent \(P_S\) has norm at least one (take a nonzero vector in its range). Combining this with the edge tests proves the displayed identity for all subsets, including \(S=\varnothing\).

**4. Unit-weight consequence.** If every \(w_e=1\), the cycle term becomes \(\min\{|S\cap C|,|E(C)|-|S\cap C|\}\) because the omitted edge has weight one. Its maximum as \(S\) varies is \(\lfloor |E(C)|/2\rfloor\); this value is attained by choosing any \(\lfloor |E(C)|/2\rfloor\) tree edges of that cycle. For any ordering of the tree edges, as the partial-sum prefix increases, the count of included edges of each fixed cycle runs through every integer from \(0\) to \(|E(C)|-1\). Hence the same maximum is attained by some prefix, irrespective of the ordering and of the other cycles. A tree (no cycles) has the weighted \(\ell_1\) unit-vector basis, so its nonzero partial sums and suppressions have norm one. Finally, since every simple cycle has at least three edges, \(\lfloor |E(C)|/2\rfloor\le1\) holds precisely when every cycle has three edges. This proves the monotonicity characterization.

## Verification
The included file `verify_cactus.py` requires only the Python standard library and can be run as `python verify_cactus.py`. It computes the transportation norms using a separate formulation as minima of exact rational edge costs across all spanning trees of each test graph and compares the resulting operator norms on all graph-edge generators with the claimed expression. The successful run printed `EXACT_CACTUS_CHECK_OK 8 128`: eight test graphs and 128 coordinate-subset checks. Test graphs include unweighted cycles, several unequal-weight cycles including an overlong edge, two cycles meeting at one vertex, cycles with bridges, and a tree. The exact mathematical proof above is valid in every finite dimension; this finite verifier is supplementary and is not an exhaustive proof for arbitrary cactus graphs.

## Relationship to prior work
Lancien and Pernecká (2012, arXiv:1207.1583) proved approximation properties and monotone finite-dimensional decompositions for other Lipschitz-free metric spaces. Hájek and Pernecká (2013 preprint; 2014 journal) constructed Schauder bases over \(\ell_1\)-type ambient sets. Neither result computes coordinate-suppression constants for a spanning-tree molecular basis over graph cacti.

The edge-flow quotient representation and cycle-space machinery are established background, notably in Ostrovska and Ostrovskii (arXiv:1910.03625). The cycle-transportation norm was studied much earlier by Cabrelli and Molter (1995), and the weighted cycle formula was revisited by Skandalis and Valette (arXiv:2601.16859). Those formulae describe norms of transportation demands, not the complete family of **operator norms of coordinate projections** or the ordering-independent cactus-basis constant. Novotný (arXiv:1905.13188) obtained lower bounds for **retractional** bases on a circle with an additional center vertex; a retractional basis is not a spanning-tree edge-molecule basis. Dilworth, Kutzarova, and Ostrovskii (arXiv:2305.12582) study minimal projections **onto graph cycle subspaces** in edge \(\ell_1\), a different operator and target from suppression projections on the transportation quotient.

## Limitations
The result concerns finite real weighted cactus graphs and one explicitly specified family of bases. For general graphs with cycles sharing edges, the quotient kernel does not split into disjoint one-cycle blocks, so the formula need not hold. The constant computed is the **suppression** unconditional constant \(\max_S\|P_S\|\), not the norm of arbitrary coefficient sign changes. The theorem does not optimize over all choices of bases. Prior literature contains the quotient representation and weighted-cycle transportation norm; the new calculation concerns their induced operator norms and sharp graph classification. Unindexed historical discussion of these same projections remains a bibliographic risk.

## References
1. G. Lancien and E. Pernecká, *Approximation Properties and Schauder Decompositions in Lipschitz-Free Spaces*, arXiv:1207.1583 (first posted 2012-07-06), https://arxiv.org/abs/1207.1583.
2. P. Hájek and E. Pernecká, *On Schauder Bases in Lipschitz-Free Spaces*, J. Math. Anal. Appl. **416** (2014), 629–646, https://doi.org/10.1016/j.jmaa.2014.02.060. Preprint available at https://msekce.karlin.mff.cuni.cz/ms-preprints/kma-preprints/2013-pap/2013-446.pdf.
3. S. Ostrovska and M. I. Ostrovskii, *On Relations Between Transportation Cost Spaces and \(\ell_1\)*, arXiv:1910.03625, https://arxiv.org/abs/1910.03625.
4. M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188, https://arxiv.org/abs/1905.13188.
5. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582, https://arxiv.org/abs/2305.12582.
6. G. Skandalis and A. Valette, *On the Transportation Cost Norm on Finite Metric Graphs*, arXiv:2601.16859, https://arxiv.org/abs/2601.16859.
7. C. A. Cabrelli and U. M. Molter, *The Kantorovich Metric for Probability Measures on the Circle*, J. Comput. Appl. Math. **57** (1995), 345–361, https://doi.org/10.1016/0377-0427(93)E0213-6.
