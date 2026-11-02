# Maximal dissociation sets of edge subdivisions and cardinality gaps in subdivided bicliques

## Finding

Let \(S(G)\) be the graph obtained by replacing each edge of a finite simple graph \(G\) by a two-edge path, with a different new vertex for each edge. A dissociation set is a vertex set inducing maximum degree at most one; a maximal dissociation set is inclusion-maximal. Write \(\mathcal D_{S(G)}(z)\) for the cardinality enumerator of maximal dissociation sets. The following gives an explicit finite combinatorial formula for every finite simple base graph and, in particular, a closed form for the complete bipartite family.

For \(A\subseteq V(G)\), put \(C=V(G)\setminus A\) and \(B_A=\{a\in A:N_G(a)\cap C\ne\varnothing\}\). Define \(\mathcal F_A\) to be the set of maps \(f:B_A\longrightarrow C\) such that \(f(a)\in N_G(a)\cap C\) for every \(a\in B_A\) and every \(c\in C\) with \(d_{G[C]}(c)\le 1\) belongs to \(\operatorname{im}(f)\). Empty maps are permitted where appropriate. Then

\[
\boxed{\mathcal D_{S(G)}(z)=\sum_{A\subseteq V(G)}|\mathcal F_A|\,z^{|A|+|E(G[C])|+|B_A|}.}
\]

For \(a,b\ge1\) define \(\mathfrak F(p,t;s)\), for nonnegative integers \(p,t,s\), by
\[
\mathfrak F(p,t;s)=\begin{cases}
1,&t=0,\\
t^p,&t\ge1\text{ and }s\ge2,\\
t!\,\left\{\begin{smallmatrix}p\\t\end{smallmatrix}\right\},&t\ge1\text{ and }s\le1.
\end{cases}
\]
The braces are Stirling numbers of the second kind, with the conventional empty-function values. The full cardinality enumerator of \(S(K_{a,b})\) is
\[
\boxed{\begin{aligned}
\mathcal D_{S(K_{a,b})}(z)=\sum_{s=0}^{a}\sum_{t=0}^{b}&\binom as\binom bt
\mathfrak F(a-s,t;s)\mathfrak F(b-t,s;t)\\[-2pt]
&\cdot z^{a+b-s-t+st+(a-s)\mathbf1_{\{t>0\}}+(b-t)\mathbf1_{\{s>0\}}}.
\end{aligned}}
\]

The natural two-by-\(b\) specialization has the particularly short formula, valid for every integer \(b\ge2\):
\[
\boxed{\mathcal D_{S(K_{2,b})}(z)=(b^2-b+1)z^{b+2}+bz^{b+3}+(3^b-2b-2)z^{2b}+(2b+2)z^{2b+1}.}
\]
When exponents coincide, their coefficients are added. For every \(b\ge5\), the **exact support** is \(\{b+2,b+3,2b,2b+1\}\), so exactly \(b-4\) consecutive cardinalities, from \(b+4\) through \(2b-1\), are absent. The total number of maximal dissociation sets is \(3^b+b^2+1\). Since \(S(K_{2,b})\) is a connected bipartite, \(2\)-degenerate graph comprising \(b\) internally disjoint length-four paths with common endpoints, this gives unbounded gaps in a natural sparse graph family.

## Assumptions and scope

All graphs are finite, simple, and undirected. Isolated vertices are allowed in the arbitrary-graph correspondence. Original vertices and newly subdividing vertices are distinguished, with the new vertex associated to an original edge \(uv\) denoted \(w_{uv}\). A dissociation set need not dominate under the standard graph-domination definition: its maximality means that adding any excluded vertex violates the induced maximum-degree-one condition. Counting is over labeled vertex subsets, not isomorphism types. No assertion is made about arbitrary repeated subdivisions or about spanning subgraphs other than the one-fold edge subdivision.

## Proof

**Step 1: structural bijection.** Fix a maximal dissociation set \(D\) of \(S(G)\), put \(A=D\cap V(G)\), and let \(C=V(G)\setminus A\). An edge-node \(w_{uv}\) with \(u,v\in A\) cannot be selected: the induced degree of this selected node would be two. Every edge-node \(w_{uv}\) with \(u,v\in C\) must be selected: it has no selected neighbor, so adding it would preserve the dissociation condition. For each \(a\in A\), at most one incident edge-node is selected, because the selected original vertex otherwise has induced degree at least two. If \(a\) has a neighbor in \(C\), then at least one corresponding crossing edge-node must be selected, since otherwise adding any such crossing node would preserve the dissociation condition. Hence exactly one is selected and determines \(f(a)\in N_G(a)\cap C\); this applies precisely to \(a\in B_A\). No edge-node incident with an original selected vertex outside this designated set can occur.

The chosen edge-nodes are therefore exactly all \(w_{uv}\) for \(uv\in E(G[C])\), together with one \(w_{a,f(a)}\) for each \(a\in B_A\). In this partial configuration, adding an excluded original vertex \(c\in C\) is impossible exactly if either \(c\) already sees at least two selected edge-nodes from \(E(G[C])\), or some selected crossing edge-node \(w_{a,c}\) already has one selected endpoint \(a\), and would acquire a second selected neighbor. These alternatives are respectively \(d_{G[C]}(c)\ge2\) and \(c\in\operatorname{im}(f)\). Thus maximality forces the image condition defining \(\mathcal F_A\).

Conversely, start from any \(A\) and \(f\in\mathcal F_A\), and choose exactly the original vertices \(A\), the edge-nodes of \(G[C]\), and the crossing edge-nodes prescribed by \(f\). Each chosen original vertex has at most one chosen incident edge-node, and each chosen edge-node has at most one chosen original endpoint, so this is a dissociation set. Every excluded edge-node either has two selected original endpoints (an edge inside \(A\)), or has a selected original endpoint already incident with one chosen crossing edge-node, so it cannot be added. Every excluded original vertex is obstructed by one of the two conditions in the previous paragraph. The set is maximal. The representation is unique and its cardinality is \(|A|+|E(G[C])|+|B_A|\). Summing proves the arbitrary-graph formula.

**Step 2: exact complete-bipartite enumeration.** In \(G=K_{a,b}\), let \(s\) and \(t\) be the respective numbers of omitted original vertices on the \(a\)-shore and the \(b\)-shore. The omitted-induced subgraph is \(K_{s,t}\), so contributes \(st\) selected edge-nodes. Each of the \(a-s\) selected first-shore vertices must choose one of the \(t\) omitted second-shore vertices if \(t>0\); analogously each of the \(b-t\) selected second-shore vertices must choose one of the \(s\) omitted first-shore vertices if \(s>0\). The omitted vertices on the \(b\)-shore have omitted-induced degree \(s\). Their image condition is automatic for \(s\ge2\) and otherwise requires the first-shore map to be surjective. This gives \(\mathfrak F(a-s,t;s)\). Symmetrically the other shore gives \(\mathfrak F(b-t,s;t)\). The two choices are independent, giving the stated double sum and exponent. It also correctly handles \(s=0\) or \(t=0\): no map is needed into an empty target, while any nonempty target with induced degree zero must be hit.

**Step 3: two-by-\(b\) simplification.** Set \(a=2\), with \(b\ge2\), and split the sum by \(s\in\{0,1,2\}\). For \(s=0\) only \(t=0,1,2\) contribute; these give \((1+b(b-1))z^{b+2}+bz^{b+3}\). For \(s=1\), exactly \(t=0,1\) contribute; these give \((2+2b)z^{2b+1}\). For \(s=2\), the \(t=0\) contribution is \(2^b-2\), the \(t=1\) contribution is \(b(2^{b-1}-2)\), and the sum over \(2\le t\le b\) is \(\sum_{t=2}^{b}\binom bt2^{b-t}=3^b-2^b-b2^{b-1}\). Their total is \(3^b-2b-2\), all at degree \(2b\). Adding gives the formula. When \(b\ge5\), its four displayed exponents are strictly increasing and all four coefficients positive. The interval of missing sizes has length \(2b-1-(b+4)+1=b-4\). Evaluating at \(z=1\) gives \(3^b+b^2+1\). The structural properties of \(S(K_{2,b})\) follow directly from its paths and the fact that every subgraph has a vertex of degree at most two.

## Verification

The standalone standard-library program `verify.py` constructs one-fold edge subdivisions, enumerates vertex subsets, tests induced maximum degree at most one, and tests maximality by attempting to add every omitted vertex. It then independently compares the subsets with the structural map characterization and compares exact cardinality coefficient dictionaries with the formulas. The successful execution produced:

`VERIFY_OK general_graphs 157 bicliques 12 cliques 3 tested_subsets 2225046 arithmetic_bicliques 49`

The direct graph checks comprise all simple base graphs on one through four vertices, selected seeded random base graphs on five and six vertices, twelve complete-bipartite instances, and three complete graphs. Separate arithmetic checks compare the double sum and the four-term specialization for forty-nine additional parameters. These are finite corroborations, not proofs of the all-order statements; the proof above supplies those.

## Relationship to prior work

Tu, Li, and Du (arXiv:2103.01402v1, first publicly available March 2, 2021) establish general and triangle-free sharp bounds on the *total number* of maximal and maximum dissociation sets. Their bounds do not determine the labeled cardinality distribution for one-fold subdivisions, nor do they imply the four-term formula and its gaps. Orlovich, Dolgui, Finke, Gordon, and Werner (2011) investigate computational complexity of maximum and minimum-maximal dissociation-set problems, including restricted graph classes; the publicly accessible abstract and article sections do not supply the present family-specific enumerator. Its full text was not available for complete comparison. Duginov and collaborators (2022) study structural and computational properties of minimum maximal dissociation sets; the available abstract concerns hardness and algorithms, not cardinality coefficients for subdivided bicliques. Their full article was not inspected and is an explicit remaining comparison risk. The complement of a dissociation set is a 3-path vertex cover, so this theorem also describes an equivalent minimal-cover enumeration, rather than a separate claim.

## Limitations

The theorem addresses one-fold edge subdivisions and inclusion-maximal (not maximum-cardinality) dissociation sets. The two-by-\(b\) support statement with four distinct degrees requires \(b\ge5\); the polynomial itself holds for all \(b\ge2\). The finite tests do not certify the infinite claim. Related literature outside the indexed and inspected sources may contain equivalent formulations; publication priority is not independently established.

## References

1. J. Tu, Y. Li, and J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402v1 (March 2, 2021), https://arxiv.org/abs/2103.01402.
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366, https://doi.org/10.1016/j.dam.2011.04.023.
3. J. Tu, L. Zhang, J. Du, and R. Lang, *Polynomial time recognition of vertices contained in all (or no) maximum dissociation sets of a tree*, AIMS Mathematics 7 (2022), 569–578, https://doi.org/10.3934/math.2022036.
4. O. I. Duginov, B. M. Kuskova, D. S. Malyshev, and N. A. Shur, *Structural and algorithmic properties of maximal dissociating sets in graphs*, Trudy Instituta Matematiki i Mekhaniki 28 (2022), 114–142, https://doi.org/10.21538/0134-4889-2022-28-2-114-142.
