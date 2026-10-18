# Acyclic and maximal-forest polynomials of crown graphs

## Finding

Let \(H_n=K_{n,n}-M_n\) be the crown graph, for an integer \(n\ge3\). Its bipartition is \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with \(a_i b_j\) an edge exactly when \(i\ne j\). Define the bivariate induced-forest polynomial
\[
F_n(u,v)=\sum_{\substack{I,J\subseteq[n]\\H_n[A_I\cup B_J]\text{ is a forest}}}u^{|I|}v^{|J|},
\]
and define the bivariate facet polynomial \(M_n(u,v)\) by restricting the sum to inclusion-maximal induced forests. Here \(A_I=\{a_i:i\in I\}\) and \(B_J=\{b_j:j\in J\}\).

**Theorem.** For every \(n\ge3\),
\[
\begin{aligned}
F_n(u,v)={}&(1+nu)(1+v)^n+(1+nv)(1+u)^n\\
&-(1+nu)(1+nv)
+\binom n2(2n-3)u^2v^2\\
&+\binom n2(n-2)(u^2v^3+u^3v^2).
\end{aligned}
\]
The maximal-forest polynomial is
\[
M_n(u,v)=\begin{cases}
3(u^2v^3+u^3v^2),&n=3,\\
n(uv^n+u^nv)+\binom n2(n-2)(u^2v^3+u^3v^2),&n\ge4.
\end{cases}
\]
For \(n\ge4\), the maximal forests are **exactly** the following two families, without overlap:

1. One vertex on one side and all \(n\) vertices on the other side; there are \(2n\) such sets, of cardinality \(n+1\).
2. Two vertices on one side and three on the other, with the two selected indices of the smaller side included among the three selected indices of the larger side; there are \(n(n-1)(n-2)\) such sets, of cardinality \(5\).

For \(n=3\), only the second family is maximal, comprising six sets of cardinality five. The induced-forest complex of \(H_n\) is pure (equivalently, \(H_n\) is well-\(f\)-covered) if and only if \(n=3\) or \(n=4\). When \(n\ge6\), none of the \(n-5\) cardinalities \(6,7,\ldots,n\) occurs among its inclusion-maximal induced forests. These gaps have unbounded length.

By complementing the facets, the minimal feedback-vertex-set polynomial is \(6z\) for \(n=3\) and
\[
2nz^{n-1}+n(n-1)(n-2)z^{2n-5}\quad(n\ge4).
\]
In particular the minimum feedback vertex set has size \(n-1\) for \(n\ge4\), and inclusion-minimal feedback vertex sets attain exactly the two sizes \(n-1\) and \(2n-5\), with these sizes coinciding for \(n=4\).

## Assumptions and scope

All graphs are finite, simple, and undirected. An induced forest is a vertex set \(S\) for which the entire induced subgraph \(H_n[S]\) has no cycle. Inclusion-maximal means that no additional vertex may be inserted while keeping the induced graph acyclic; it does **not** mean having largest possible cardinality. An inclusion-minimal feedback vertex set is the complement of an inclusion-maximal induced forest. The domain \(n\ge3\) is essential: the graph \(H_2\) consists of two disjoint edges, so the stated maximality classification is inapplicable. All binomial coefficients use the ordinary integer convention.

## Proof

**1. Classify the acyclic selections.** Let \(I,J\subseteq[n]\), and put \(a=|I|\), \(b=|J|\), \(t=|I\cap J|\). Exactly \(t\) of the \(ab\) cross-pairs are deleted matching edges. Thus \(H_n[A_I\cup B_J]\) has \(a+b\) vertices and \(ab-t\) edges. If \(\min(a,b)\le1\), it is a star plus isolated vertices, hence a forest.

Suppose \(a,b\ge2\). A forest on \(a+b\) vertices has at most \(a+b-1\) edges, so
\[
(a-1)(b-1)\le t\le\min(a,b).
\]
The sizes cannot both be at least three, since \((a-1)(b-1)>\min(a,b)\) when \(a,b\ge3\). If one size is two, the other is at most three. Therefore the only possible configurations with both sides nontrivial are \((a,b)=(2,2)\) with \(t\ge1\), or \((a,b)=(2,3),(3,2)\) with \(t=2\). These are sufficient as well: a \((2,2,t\ge1)\) selection induces at most three edges on four vertices and cannot contain a cycle; a \((2,3,t=2)\) selection induces exactly a five-vertex path, and the transposed configuration does likewise. This proves a necessary-and-sufficient classification, including the boundary values.

**2. Count all forests.** Selections with \(a\le1\) contribute \((1+nu)(1+v)^n\); selections with \(b\le1\) contribute \((1+nv)(1+u)^n\). Their intersection, counted twice, contributes \((1+nu)(1+nv)\). For \(a=b=2\), choose \(I\) in \(\binom n2\) ways and choose \(J\) intersecting \(I\) in at least one point in \(\binom n2-\binom{n-2}2=2n-3\) ways. For \((a,b)=(2,3)\), choose \(I\) in \(\binom n2\) ways and \(J\supset I\) in \(n-2\) ways; transpose for \((3,2)\). These cases are disjoint and exhaust the classification in Step 1, proving \(F_n(u,v)\).

**3. Identify inclusion-maximal forests.** If \(\min(a,b)=0\), a forest can be extended by adding a vertex from the missing side (also if the occupied side is full); if \(\min(a,b)=1\), it can be extended on the larger selected side unless that side is already full. The only possible maximal sets in this range therefore have profile \((1,n)\) or \((n,1)\). Each is maximal if \(n\ge4\), since adding another vertex would produce profile \((2,n)\), prohibited by Step 1. For \(n=3\), each extends to a \((2,3)\) or \((3,2)\) forest and is not maximal.

Every feasible \((2,2)\) forest extends to a feasible \((2,3)\) or \((3,2)\) forest: if \(t=1\), add the matching partner of the selected index missing from the opposite side; if \(t=2\), add any third vertex on either side (possible since \(n\ge3\)). Every feasible \((2,3,t=2)\) forest is maximal, because any further insertion makes one side have size at least four or makes both sides have size at least three, both forbidden by Step 1. The same holds for its transpose.

Consequently the two displayed types exhaust the facets. Their counts are \(n\) per orientation for the \((1,n)\) type and \(\binom n2(n-2)\) per orientation for the \((2,3)\) type. At \(n=3\), only the latter survive. This proves the stated formula for \(M_n(u,v)\).

**4. Purity, gaps, and feedback vertex sets.** At \(n=3\) all facets have cardinality five; at \(n=4\), the two types both have cardinality five. For \(n\ge5\), their cardinalities \(5\) and \(n+1\) differ, so the induced-forest complex is not pure. For \(n\ge6\), exactly the interior integers \(6,\ldots,n\) are absent, and their count is \(n-5\). Since complements biject inclusion-maximal induced forests with inclusion-minimal feedback vertex sets and send size \(k\) to \(2n-k\), the last polynomial and size assertions follow.

## Verification

The included standard-library program `verify_crown_forests.py` constructs the graph from the adjacency rule, checks acyclicity using disjoint-set union on selected edges, and checks inclusion-maximality by attempting every one-vertex insertion. It compares every bivariate coefficient of \(F_n\) and \(M_n\) for all \(3\le n\le9\), examining exactly \(349{,}504\) vertex subsets in total. The reproduced output is in `verification_output.txt`. This finite check corroborates the proof; no infinite claim rests solely on computation.

## Relationship to prior work

Barton, Brown, and Pike (2020, arXiv:2011.01735) introduced the vertex-induced acyclic polynomial and studied its general properties, including disjoint unions and graph joins. Their Theorem 1.3 applies to actual graph joins; the matching-deleted crown graph is not a graph join of its independent bipartition classes, so their join formula does not imply the result here. Jafarpour-Golzari (2021, arXiv:2105.14339, Theorem 6.15 and Corollary 6.16) characterized the well-\(f\)-covered property of complete bipartite graphs, including \(K_{n,n}\); the perfect-matching-deleted family is not covered by that statement. Gunderson, Meagher, Morris, and Pantangi (2023, arXiv:2301.05207, Theorem 3.9) study \(K_n\times K_n\), whose vertex set has cardinality \(n^2\); this differs from \(K_2\times K_n\), which has \(2n\) vertices. Coincidence of an expression for some maximum induced-forest sizes does not establish the present crown-graph face or facet enumeration.

The facet-size gap resembles phenomena for different hereditary vertex-set properties but is not a corollary of their enumerators; for example, a dissociation set must induce maximum degree at most one, whereas an induced forest may include arbitrarily long paths or stars. A search of directly relevant published mathematical records under crown, bipartite-double-cover, minimal-feedback-vertex-set, and induced-forest terminology identified no statement implying the complete bivariate formulas. Absence of a matching indexed statement is not a guarantee of historical priority.

## Limitations

The theorem concerns the specific perfect-matching deletion \(K_{n,n}-M_n\) with \(n\ge3\); it makes no claim for arbitrary deleted matchings, arbitrary bipartite graphs, or generalized graph products. Acyclic means vertex-induced acyclicity, not an arbitrary chosen spanning forest or an edge-acyclic subgraph. The exhaustive checks establish finite consistency only. An equivalently formulated enumeration in currently unindexed literature may exist; comprehensive bibliographic priority and independent scientific assessment remain outstanding.

## References

1. C. Barton, J. I. Brown, and D. A. Pike, *Acyclic polynomials of graphs*, arXiv:2011.01735, first posted 2020-11-03. https://arxiv.org/abs/2011.01735
2. R. Jafarpour-Golzari, *Graphs whose all maximal induced forests are of the same order*, arXiv:2105.14339, first posted 2021-05-29. https://arxiv.org/abs/2105.14339
3. K. Gunderson, K. Meagher, J. Morris, and V. R. T. Pantangi, *Induced forests in some distance-regular graphs*, arXiv:2301.05207, first posted 2023-01-12. https://arxiv.org/abs/2301.05207
