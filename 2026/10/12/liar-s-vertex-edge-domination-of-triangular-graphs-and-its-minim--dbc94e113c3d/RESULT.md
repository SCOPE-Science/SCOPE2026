# Liar's vertex-edge domination of triangular graphs and its minimum-set census

## Finding

Let \(T_n=L(K_n)=J(n,2)\) be the triangular graph, whose vertices are the two-element subsets of \([n]\). For every integer \(n\ge3\), its liar's vertex-edge domination number is
\[
\boxed{\gamma_{\mathrm{lve}}(T_n)=\left\lceil\frac{3n}{4}\right\rceil.}
\]
More precisely, a vertex set \(S\subseteq V(T_n)\) is liar's vertex-edge dominating if and only if the simple graph \(H=([n],S)\) has at least three distinct edges incident with every three-element subset of \([n]\).

For \(n\ge8\), write \(n=4k+r\), where \(k=\lfloor n/4\rfloor\) and \(0\le r\le3\). A minimum liar's vertex-edge dominating set corresponds **exactly** to one of the following types of graph \(H\):

1. A forest having precisely \(k\) connected components, each a tree of order at least \(4\). Its component orders sum to \(n\), hence every order is at most \(7\).
2. Only when \(r=3\): the disjoint union of one triangle and \(k\) trees of order \(4\).

Conversely every graph in these two types supplies a minimum liar's vertex-edge dominating set. Thus if \(M_n\) counts all minimum sets and \(n\ge8\), then
\[
\boxed{M_n=n![z^n]\frac{1}{k!}\left(\sum_{s=4}^{7}\frac{s^{s-2}z^s}{s!}\right)^k+\mathbf{1}_{\{r=3\}}\frac{n!\,16^k}{3!(4!)^k k!}.}
\]
In particular, for every multiple \(n=4k\ge8\), all minimum configurations are partitions into four-vertex trees and
\[
\boxed{M_{4k}=\frac{(4k)!\,16^k}{(4!)^k k!}.}
\]
The one small exceptional extremal census explicitly established here is \(M_4=20\): every three-element vertex subset of \(T_4\) is minimum.

## Assumptions and scope

All graphs are finite, simple, and undirected. The line graph \(T_n\) has one vertex for every edge of \(K_n\); two vertices are adjacent if their corresponding edges share an endpoint. For an edge \(e=uv\) of any graph \(G\), put \(N_G[e]=N_G[u]\cup N_G[v]\), where vertex neighborhoods are closed. A liar's vertex-edge dominating set \(S\) satisfies both: \(|S\cap N_G[e]|\ge2\) for each edge \(e\), and \(|S\cap(N_G[e]\cup N_G[f])|\ge3\) for each pair of distinct edges \(e,f\).

For \(A\subseteq[n]\), an edge of \(H\) is *incident with* \(A\) when at least one endpoint belongs to \(A\). Tree orders in the census refer to their numbers of original \([n]\)-vertices. The scalar formula holds for every integer \(n\ge3\); the minimum-set classification and the counting formula hold for every \(n\ge8\). No assertion of the displayed census formula is made for \(3\le n\le7\), except the explicitly handled \(n=4\).

## Proof

**Equivalence of the two domination conditions to triple incidence.** Fix distinct \(a,b,c\in[n]\). The three vertices \(ab,ac,bc\) of \(T_n\) induce a triangle, and each of its three edges has exactly the same closed edge neighborhood: the set \(Q_{abc}\) of all pairs of \([n]\) meeting \(\{a,b,c\}\). Applying the distinct-edge union condition to two edges of this triangle gives \(|S\cap Q_{abc}|\ge3\). Conversely, every edge of \(T_n\) is determined by two intersecting pairs, whose union is some triple \(\{a,b,c\}\), and its closed edge neighborhood is exactly \(Q_{abc}\). If every triple meets at least three selected pairs, every edge's neighborhood contains at least three selected vertices, which implies both defining liar's conditions. This proves the equivalence for all \(n\ge3\).

**Lower bound.** Let \(H=([n],S)\) obey the triple condition and put \(m=|E(H)|\). For \(n=3\), the unique triple forces \(m\ge3\). Henceforth suppose \(n\ge4\). Three isolated vertices violate the condition. If exactly two vertices are isolated, using them with any third vertex shows that every other vertex has degree at least \(3\). Consequently \(2m\ge3(n-2)\), which implies \(m\ge\lceil3n/4\rceil\) for every such feasible graph. If exactly one vertex is isolated, there can be at most one vertex of degree \(1\), because the isolated vertex and any two leaves would be incident with at most two edges. Thus \(2m\ge2n-3\), implying \(m\ge n-1\). If \(H\) has no isolated vertex but has a two-vertex component, then the two vertices of that component and any other vertex give at least three incident edges only if the third vertex has degree at least \(2\). Hence \(2m\ge2(n-2)+2\), giving \(m\ge n-1\).

In the remaining case all components have order at least \(3\). A three-vertex component must be a triangle: otherwise its three vertices meet at most two graph edges. Every component of order \(c\ge4\) has at least \(c-1\ge3c/4\) edges, and every triangle has exactly \(3\ge3c/4\) edges. Summing over components gives \(m\ge3n/4\). Combining the cases proves \(m\ge\lceil3n/4\rceil\). For the two-isolate case, the stated comparison follows directly for \(n\ge4\): \(3(n-2)/2\ge3n/4\) whenever \(n\ge4\).

**Sharp construction.** For \(n\ge4\), let \(k=\lfloor n/4\rfloor\). Partition \([n]\) into \(k\) disjoint groups of size at least \(4\), taking \(k-1\) groups of size \(4\) and one group of size \(4+r\), where \(r=n-4k\). Put a spanning tree on each group. For every nonempty vertex set \(A\) of size at most three in a tree component, the edges incident to \(A\) number at least \(|A|\): the induced forest on \(A\) has, say, \(h\) edges and \(|A|-h\) components, each with at least one edge to the nonempty complement because the original tree is connected. Splitting a triple across components and adding these inequalities shows that every triple of \([n]\) meets at least \(3\) chosen edges. The constructed forest therefore satisfies the liar's condition and has \(n-k=\lceil3n/4\rceil\) edges. For \(n=3\) the triangle has exactly three edges and is feasible.

**All minimum configurations for \(n\ge8\).** At the optimum \(m=\lceil3n/4\rceil\), one has \(m<n-1\) for \(n\ge8\). Therefore the earlier lower-bound cases rule out isolated vertices and two-vertex components. Each component is either a triangle or has order at least four. Define the nonnegative **defect** of a component with \(c\) vertices and \(e\) edges by \(4e-3c\). Each triangle has defect \(3\); each tree on \(c\ge4\) vertices has defect \(c-4\); any component on \(c\ge4\) vertices with a cycle has defect at least \(c\ge4\). But the sum of all component defects is
\[
4m-3n=4\left\lceil\frac{3n}{4}\right\rceil-3n=r\in\{0,1,2,3\}.
\]
Thus cyclic components of order at least four are impossible; at most one triangle occurs, and a triangle forces \(r=3\) and all other components to be four-vertex trees. Without a triangle, write \(q\) for the number of tree components. Since each tree contributes \(c-1\) edges, \(m=n-q\); hence \(q=n-m=k\). Their sizes sum to \(n=4k+r\), so every size lies between \(4\) and \(7\). With a triangle, the remaining graph has \(n-3=4k\) vertices split into four-vertex trees, hence exactly \(k\) such trees. Conversely, in every configuration just listed, any triple has at least three incident edges: the tree-component argument applies to the trees, and a triangle contributes \(2\) incident edges for one chosen vertex and \(3\) for two or three; these bounds add across components. Every listed graph also has exactly \(\lceil3n/4\rceil\) edges. The characterization is exact.

**Enumeration.** On any specified \(s\)-element label set, there are \(s^{s-2}\) trees by Cayley's formula. The labeled-component exponential formula therefore counts the first class by
\[
n![z^n]\frac{1}{k!}\left(\sum_{s=4}^{7}\frac{s^{s-2}z^s}{s!}\right)^k.
\]
For \(r=3\), independently choose the three triangle labels, partition the other \(4k\) labels into unordered four-blocks and choose one of the \(4^{4-2}=16\) labeled trees on each block. This gives the second displayed term, and the classes are disjoint. If \(n=4k\), all groups have size four. At \(n=4\), any three of the six vertices of \(T_4\) are feasible because no original pair is disjoint from a three-element subset of \([4]\), giving \(\binom63=20\).

## Verification

The included standard-library script `verify.py` constructs every edge and its closed edge neighborhood in \(T_n\) independently of the incidence reduction. It checks the original two liar's conditions against the triple reduction for each candidate of sizes one below the claimed optimum and at the optimum for \(3\le n\le6\). It separately checks the incidence criterion for every candidate at those two sizes through \(n=8\), including exact agreement with the displayed count at \(n=8\), and checks algebraic count identities through \(n=24\). Run `python3 verify.py`; expected output is embedded in `verification_output.txt`. The unbounded case is proved by the component argument, not by the finite checks.

## Relationship to prior work

Bhattacharya and Paul introduce liar's vertex-edge domination and develop hardness, approximation, and tree algorithms [1]; their paper does not give these exact triangular-graph results. Their parallel treatment of general \(k\)-vertex-edge domination [2] supplies a broader definition: on \(T_n\), liar's vertex-edge domination coincides with \(3\)-vertex-edge domination because every edge neighborhood occurs identically for three distinct edges. That equivalence does not itself provide the optimum, component classification, or enumeration. Later chordal-subclass algorithms [3] are also not statements about this nonchordal triangular-graph family for \(n\ge5\).

## Limitations

The all-minimum-set component classification and counting formula require \(n\ge8\). The theorem gives neither a formula for the full liar's vertex-edge domination polynomial nor a claim about arbitrary line graphs or arbitrary \(3\)-vertex-edge domination instances. A finite verifier cannot prove the infinite assertions. Equivalence to older incidence-covering formulations is a possible remaining literature-overlap risk.

## References

1. Debojyoti Bhattacharya and Subhabrata Paul, *Algorithmic study on liar's vertex-edge domination problem*, arXiv:2310.07465v1 (first public 2023-10-11), https://arxiv.org/abs/2310.07465.
2. Debojyoti Bhattacharya and Subhabrata Paul, *On \(k\)-vertex-edge domination of graph*, arXiv:2310.07452v1 (first public 2023-10-11), https://arxiv.org/abs/2310.07452.
3. Debojyoti Bhattacharya and Subhabrata Paul, *Liar's vertex-edge domination in subclasses of chordal graphs*, arXiv:2507.04721v1 (2025), https://arxiv.org/abs/2507.04721.
