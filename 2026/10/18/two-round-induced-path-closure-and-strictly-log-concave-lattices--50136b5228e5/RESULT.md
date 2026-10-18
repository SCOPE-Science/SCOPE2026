# Two-round induced-path closure and strictly log-concave lattices of triangular graphs

## Finding

For every integer \(n\ge4\), take the triangular graph \(T_n=L(K_n)\) on the \(\binom n2\) edges of a complete graph. Starting with any edge set \(S\subseteq E(K_n)\), close under the Horn rules that insert the middle vertex of every induced three-vertex path in \(T_n\) whose endpoints have already been chosen. Then the following hold.

1. A parallel application of all rules, denoted \(\Phi_n\), reaches the closure in at most **two strict rounds**: \(c_n(S)=\Phi_n^2(S)\). Two rounds are necessary precisely when \(S\) has two disjoint edges and its support graph has two degree-one vertices with the same unique neighbor. This bound is sharp for every \(n\ge5\); for \(n=4\), one round always suffices.
2. The closed sets are exactly the empty set, every nonempty edge-star (any nonempty subset of the edges sharing a vertex), every three-edge triangle, and the complete edge sets \(E(K_U)\) for \(U\subseteq[n]\) with \(|U|\ge4\). Their inclusion lattice \(\mathcal L_n\) is graded of rank \(n\), with rank polynomial
\[
R_n(t)=1+\binom n2 t+3\binom n3t^2+\sum_{r=3}^{n}(n-r+1)\binom nr t^r.
\]
All rank coefficients are strictly log-concave for \(n\ge4\), and
\[
|\mathcal L_n|=(n+2)2^{n-1}-n(n+1),\qquad
\mu_{\mathcal L_n}(\varnothing,E(K_n))=(-1)^n.
\]
3. For \(n\ge5\), \(\operatorname{Aut}(\mathcal L_n)\cong\mathfrak S_n\). At \(n=4\), \(\operatorname{Aut}(\mathcal L_4)\cong \mathfrak S_2\wr\mathfrak S_3\) has order \(48\), strictly larger than the natural vertex-relabeling group of order \(24\).

## Assumptions and scope

The complete graph is finite, simple, and undirected, with vertex set \([n]\) and \(n\ge4\). Every vertex of the triangular graph represents an unordered two-element subset of \([n]\). Distinct such vertices are adjacent exactly when the represented edges intersect. If \(S\) is a set of these edges, let \(U(S)\) denote their endpoints. The operator \(\Phi_n(S)\) simultaneously adds every crossed edge between two disjoint selected edges, retaining all edges already present; the closure \(c_n(S)\) is its least fixed point. A *round* is one simultaneous application of \(\Phi_n\), not an arbitrary sequential Horn rule firing. The round count is the least \(r\ge0\) with \(\Phi_n^r(S)=c_n(S)\), even when the closure is initially fixed. A *cherry* means two distinct vertices of degree one with a common neighbor in the graph \(([n],S)\).

## Proof

**The induced-path rule.** The two outer vertices of an induced three-vertex path in \(T_n\) are nonadjacent and hence correspond to disjoint complete-graph edges \(ab\) and \(cd\). The middle vertex corresponds to an edge sharing an endpoint with both, namely one of \(ac,ad,bc,bd\). Thus the stated crossed-edge completion is precisely the induced-path closure rule.

**Closure and two-round bound.** If \(S\) contains no disjoint pair, no rule can fire, and \(S\) is closed. Otherwise fix disjoint \(ab,cd\in S\) and put \(Q=\{a,b,c,d\}\). The first round contains all six edges of \(K_Q\). Every \(x\in U(S)\setminus Q\) is incident in \(S\) to some \(xy\). The edge \(xy\) is disjoint from at least one of \(ab,cd\), so the first round adds two edges from \(x\) to two distinct vertices of \(Q\). In the second round, any two active vertices are adjacent: two outside vertices have respective pairs of distinct neighbors in the four-vertex complete core, from which two distinct core neighbors can be chosen; an outside vertex can similarly be connected to any core vertex using one of its two core neighbors and a second core edge; core vertices are already mutually adjacent. No rule can introduce a vertex outside \(U(S)\), so \(\Phi_n^2(S)=E(K_{U(S)})\).

For two distinct vertices \(u,v\in U(S)\), if their edge is absent after round one, then \(uv\notin S\), and every edge of \(S\) incident with \(u\) must intersect every edge of \(S\) incident with \(v\), for otherwise these two edges would force \(uv\). Since \(uv\) itself is absent, this requires both vertices to have exactly one neighbor and these neighbors to coincide. Conversely, a cherry pair cannot be joined in the first round, because its only incident original edges intersect at their common neighbor. Therefore precisely the stated cherries cause a second strict round. If there is a matching of size two, such a cherry needs at least five vertices, giving the \(n=4\) threshold. For \(n\ge5\), \(S=\{12,13,45\}\) exhibits two rounds.

**Closed forms and rank.** A family of pairwise intersecting two-subsets of \([n]\) is a star or consists of the three edges of a triangle: start with intersecting \(ab,ac\); an edge missing \(a\) must be \(bc\), after which all further edges belong to this triangle. Hence exactly the displayed closed-set types arise. Assign rank \(k\) to each star consisting of \(k\) edges, rank three to each full triangle, rank \(|U|\) to a clique \(E(K_U)\) with \(|U|\ge4\), and rank zero to the empty set. These ranks are strictly increasing on proper inclusion, aside from cases ruled out by the distinct closed-set types. Every nonempty star grows by one edge from another star; a triangle covers its two-edge stars; a clique on \(h\ge4\) vertices contains maximal proper stars with \(h-1\) edges and maximal proper subcliques (triangles when \(h=4\)) with rank \(h-1\). Indeed, every proper closed subset of a clique lies in one of these, by the classification. Thus every cover increases rank exactly one and the inclusion lattice is graded of rank \(n\).

There are \(\binom n2\) one-edge stars, and for \(2\le r\le n-1\) there are \(n\binom{n-1}{r}=(r+1)\binom n{r+1}\) stars consisting of \(r\) edges. The rank-two coefficient is \(n\binom{n-1}2=3\binom n3\). At rank three add \(\binom n3\) triangles to the stars, obtaining \((n-2)\binom n3\). For \(4\le r\le n-1\), add \(\binom nr\) cliques of rank \(r\) to the stars, obtaining \((n-r+1)\binom nr\); the full clique contributes the rank-\(n\) coefficient one. This proves the displayed rank polynomial. At \(t=1\), summing the stars and cliques gives \((n+2)2^{n-1}-n(n+1)\).

Put \(a_r=[t^r]R_n(t)\). The strict log-concavity tests at the first three interior ranks yield
\[
\frac{a_1^2}{a_0a_2}=\frac{n(n-1)}{2(n-2)}>1,\quad
\frac{a_2^2}{a_1a_3}=3>1,\quad
\frac{a_3^2}{a_2a_4}=\frac{4(n-2)^2}{3(n-3)^2}>1.
\]
At each remaining interior rank \(r\ge4\), the coefficient formula \(a_r=(n-r+1)\binom nr\) is the product of a positive strictly log-concave binomial sequence and a positive log-concave linear sequence, and is therefore strictly log-concave.

**Möbius invariant.** The lattice is atomic, with atoms the individual edges of \(K_n\). By the atomic crosscut identity, its bottom-to-top Möbius number is the alternating sum \(\sum_{S:c_n(S)=E(K_n)}(-1)^{|S|}\). Such a set \(S\) has full vertex support and contains a disjoint pair. By inclusion-exclusion over isolated vertices, the alternating sum over *all* edge sets with full support equals \((-1)^{n-1}(n-1)\): in the inclusion-exclusion expansion, only surviving vertex sets of size zero or one contribute. Exactly \(n\) full-support edge sets have no disjoint pair, namely the complete stars; their signs are each \((-1)^{n-1}\). Removing them gives \((-1)^{n-1}(n-1)-n(-1)^{n-1}=(-1)^n\).

**Automorphisms.** A lattice automorphism permutes its atoms. The join of two distinct atoms has exactly two atoms below it if and only if the two represented complete-graph edges meet; disjoint edge atoms have the six atoms of their four-vertex clique below their join. Hence every lattice automorphism acts as a graph automorphism of \(T_n\). Conversely every automorphism of \(T_n\) preserves induced paths and therefore the closure lattice, so the two automorphism groups coincide. When \(n\ge5\), maximal cliques of cardinality at least four in \(T_n\) are exactly the stars of size \(n-1\), recovering the original \(n\) vertices and giving \(\mathfrak S_n\). When \(n=4\), the triangular graph is the complete tripartite graph with three parts of size two, whose automorphism group is \(\mathfrak S_2\wr\mathfrak S_3\) of order \(2^3\cdot3!=48\).

## Verification

A self-contained exhaustive checker (`verify.py`) enumerates all initial edge subsets for \(n=4,5,6\), computes simultaneous-rule closure directly, and checks the two-round/cherry criterion and all closed sets against the formula. It independently computes lattice ranks from the inclusion order, compares rank distributions, verifies Möbius values from their defining recurrence for \(n=4,5\), checks strict log-concavity for all \(4\le n\le100\), and enumerates the \(48\) automorphisms of \(T_4\). The exact recorded terminal summary is:

```
EXHAUSTIVE 4 subsets 64 closed 28 ranks [1, 6, 12, 8, 1] time_counts {0: 28, 1: 36} PASS
EXHAUSTIVE 5 subsets 1024 closed 82 ranks [1, 10, 30, 30, 10, 1] time_counts {0: 82, 1: 822, 2: 120} PASS
EXHAUSTIVE 6 subsets 32768 closed 214 ranks [1, 15, 60, 80, 45, 12, 1] time_counts {0: 214, 1: 29854, 2: 2700} PASS
AUTOMORPHISM_T4 48 PASS
VERIFY_OK exact_closure=PASS two_round_cherry=PASS graded_rank=PASS mobius=PASS strict_logconcavity=PASS exceptional_symmetry=PASS
```

Run `python3 verify.py` in an environment with Python 3 standard library. Exhaustive finite computations corroborate but are not substitutes for the all-parameter proof.

## Relationship to prior work

The induced-path convexity of order three, called \(P_3^*\)-convexity or \(l^2\)-convexity, predates this theorem. Araújo, Sampaio and Szwarcfiter (2013) introduce and investigate the associated closure notion, and Gutierrez, Protti and Tondato (2022) study which graphs make this convexity a convex geometry. Those general formulations supply the underlying closure operator, not the derived two-round behavior, the full graded lattice and its exact rank/Möbius/symmetry invariants for triangular graphs. Dourado, Penso and Rautenbach study hull-number problems for this convexity. The present statements concern a different, highly structured graph family and different exact invariants.

## Limitations

The domain is restricted to triangular graphs \(L(K_n)\) with \(n\ge4\) and the *simultaneous induced-three-vertex-path closure*. A sequential rule-firing time is not claimed to obey the same round bound. Neither the formulas nor the automorphism classification are asserted for arbitrary line graphs. The novelty assessment is based on inspected accessible literature and searches, not an exhaustive proof of publication priority; an equivalent treatment under induced-path convexity or graph-bootstrap terminology remains a residual possibility. Independent external mathematical audit has not been performed.

## References

1. M. C. Araújo, R. M. Sampaio and J. L. Szwarcfiter, *The convexity of induced paths of order three*, Electronic Notes in Discrete Mathematics (2013). DOI: 10.1016/j.endm.2013.10.017.
2. M. Gutierrez, F. Protti and J. Tondato, *Convex geometries over induced paths with bounded length*, arXiv:2203.05588 (first posted 2022-03-10).
3. M. C. Dourado, L. D. Penso and D. Rautenbach, *The hull number in the convexity of induced paths of order 3*, Theoretical Computer Science (2022). DOI: 10.1016/j.tcs.2022.01.004.
