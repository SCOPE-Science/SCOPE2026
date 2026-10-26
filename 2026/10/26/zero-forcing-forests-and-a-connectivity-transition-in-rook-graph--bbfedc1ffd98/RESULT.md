# Zero-forcing forests and a connectivity transition in rook graphs

## Finding

For integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\). Its cells \((i,j)\) are adjacent when they share a row or a column. Given an initial blue set \(B\), define its *white bipartite graph* \(H_B\) on the \(m\) row-vertices and \(n\) column-vertices by putting an edge \(ij\) exactly when cell \((i,j)\) is white. A leaf has degree one; an isolated vertex has degree zero.

**All-set theorem.** The set \(B\) is an ordinary zero-forcing set if and only if \(H_B\) is empty, or it is a forest satisfying at least one of the following: (a) an isolated row-vertex and a leaf column-vertex exist; (b) an isolated column-vertex and a leaf row-vertex exist. Both conditions may hold.

**Minimum-set count.** The minimum cardinality is the previously known value
\[
Z(R_{m,n})=mn-m-n+2.
\]
Every minimum set is the complement of a bipartite tree spanning all row and column vertices except a unique isolated vertex, with a leaf in the opposite bipartition side. The number of these minimum sets is
\[
\begin{aligned}
N_{m,n}={}&m(m-1)^{n-1}\big[n^{m-2}-n!\,S(m-2,n)\big]\\
&+n(n-1)^{m-1}\big[m^{n-2}-m!\,S(n-2,m)\big],
\end{aligned}
\]
where \(S(a,b)\) denotes a Stirling number of the second kind, defined to be zero when \(a<b\). The subtraction is necessary: for instance \(N_{5,2}=42\), rather than the unrestricted spanning-tree contribution.

**Exchange connectivity transition.** Form \(\mathcal E_{m,n}\) on these minimum sets, joining two when they differ by replacing exactly one selected blue cell (equivalently, their white graphs exchange one edge). If \(m,n\ge3\) then \(\mathcal E_{m,n}\) is connected. It is also connected for \((m,n)=(2,2),(2,3),(3,2)\). For \(\{m,n\}=\{2,t\}\) with \(t\ge4\), it has precisely two components, each isomorphic to
\[
K_1\vee L(K_{t,t}-M_t),
\]
where \(M_t\) is a fixed perfect matching. Each component has \(1+t(t-1)\) vertices and \(t(t-1)^2\) edges. Thus \(\mathcal E_{2,t}\) has \(2[1+t(t-1)]\) vertices and \(2t(t-1)^2\) edges.

## Assumptions and scope

All graphs are finite and simple. A blue vertex can force its unique white neighbor, and newly forced vertices remain blue. A zero-forcing set admits a sequence coloring every vertex blue. The exchange graph considers only *minimum-cardinality* initial blue sets, not arbitrary zero-forcing supersets. Distinct row and column labels are retained; counts are labeled, not counted up to automorphism. Exponents with zero exponent use \(u^0=1\) for positive integers \(u\). The classification holds for every integer \(m,n\ge2\), including the thin boundaries.

## Proof

**1. The local rule and the forest criterion.** At a blue cell \((r,c)\), the number of white neighbors is exactly \(d_H(r)+d_H(c)\), since a white cell lies in the same row or the same column, with no duplication. Consequently a blue cell can force an edge of \(H\) if and only if that edge has a degree-one endpoint on one side and there exists an isolated vertex on the *opposite* side: for a leaf row \(r\), use the blue cell \((r,c')\) with isolated column \(c'\); for a leaf column \(c\), use \((r',c)\) with isolated row \(r'\). Each force deletes exactly one edge of \(H\).

If \(H\ne\varnothing\), a first force must therefore exhibit one of the two leaf/isolate pairs in the assertion. Furthermore, a cycle in \(H\) can never lose its first edge: at that moment both endpoints of every cycle edge still have white degree at least two. Thus zero forcing requires acyclicity. Conversely, a forest with the stated initial pair admits its first force. After this force, both bipartition sides contain isolated vertices (the pre-existing isolate and the new isolate at the deleted leaf). As long as a forest has edges it has a leaf; a blue cell at that leaf and an isolate on the opposite side permits deletion. Iteration empties the forest. This proves necessity and sufficiency. Empty \(H\) means every cell is already blue.

**2. Cardinality and every extremizer.** A nonempty admissible forest on \(m+n\) vertices contains an isolated vertex, hence has at most \(m+n-2\) edges. This bound is attained: isolate any one row, take a spanning tree of the remaining \(K_{m-1,n}\) with a column leaf (a spanning star-and-attachments construction works even if \(m=2\)); or interchange the sides. Equality forces exactly two forest components, one of them a singleton isolate and the other a tree spanning all other vertices, with the specified opposite-side leaf. Since the initially blue cells are the complement of the forest edges, the minimum is \(mn-(m+n-2)\). There are no other equality types.

**3. Enumeration.** For labeled spanning trees of \(K_{a,b}\), the bipartite Prüfer coding gives one word of length \(b-1\) on the \(a\) left labels and one word of length \(a-1\) on the \(b\) right labels. A right vertex is a leaf precisely when it is absent from the second word. The number of trees with at least one right leaf is therefore
\[
a^{b-1}\big[b^{a-1}-b!S(a-1,b)\big].\]
This also follows from the weighted bipartite spanning-tree generating identity \(a^{b-1}(\sum_j y_j)^{a-1}\), with the exponent of \(y_j\) equal to right degree minus one. For a fixed isolated row use \(a=m-1,b=n\), then multiply by \(m\); for a fixed isolated column interchange the parts and multiply by \(n\). The two classes are disjoint because a maximum-edge admissible forest has exactly one isolated vertex. This gives the stated formula.

**4. Connectedness when both dimensions exceed two.** Fix an isolated row \(a\). For any chosen column \(c\) constrained to remain a leaf, all spanning trees of \(K_{m-1,n}\) with this leaf are connected by single-edge exchanges: remove \(c\) and its incident edge, vary the resulting spanning tree of \(K_{m-1,n-1}\) using the usual graphic-matroid basis exchanges, and freely vary the attachment of \(c\). For any two columns \(c,d\), a spanning tree with both as leaves exists when \(m,n\ge3\): connect all nonisolated rows to a third column, and attach all other columns as leaves. Hence all feasible trees with a *fixed* isolated row are connected. Any two choices of isolated row are joined: within the first fiber choose a tree in which the second row is a leaf and some column leaf attaches elsewhere; exchange that second row's incident edge for the corresponding edge at the first isolated row, leaving the second row isolated. Thus all row-isolate configurations are in one component. The dual argument connects all column-isolate configurations. Finally, from any row-isolate tree with column leaf \(c\), delete the leaf edge and add an edge incident with the formerly isolated row and with a different column. The new white graph is a tree with isolated column \(c\) and a leaf row, so this one exchange joins the two types. Therefore \(\mathcal E_{m,n}\) is connected.

**5. Thin-case isomorphism and sharp transition.** By symmetry set \(m=t,n=2\). When \(t\ge4\), every minimum white forest has a unique *dominant column* \(c\) containing at least \(t-1\) white edges. For each fixed \(c\) its possibilities are exactly an *apex* \(A_c\) consisting of every edge in column \(c\), and the states \(T_{a,b,c}\) indexed by ordered pairs of distinct rows \(a\ne b\): omit \((a,c)\) from column \(c\) and add \((b,1-c)\). The apex is adjacent to all \(t(t-1)\) states. Two distinct states \(T_{a,b,c}\) and \(T_{a',b',c}\) are adjacent if and only if \(a=a'\) or \(b=b'\). The latter graph is the line graph of the crown graph \(K_{t,t}-M_t\), with an edge indexed by \((a,b)\) for \(a\ne b\). A single exchange cannot change the dominant column for \(t\ge4\), because it can decrease the dominant-column count by at most one, leaving at least \(t-2\ge2\) edges, whereas the other type permits at most one. This proves the two components, their isomorphism, and their edge counts: \(t(t-1)\) apex edges plus \(t(t-1)(t-2)\) line-graph edges per component.

For \(t=3\) the two dominant types communicate: for any isolated row \(a\) and remaining rows \(b,d\), the white tree \(\{(b,0),(d,0),(b,1)\}\) exchanges \((d,0)\) for \((d,1)\), reversing the dominant column. The connectivity argument within each dominant type as above then yields a single component. At \(t=2\), direct classification gives four minimum sets whose exchange graph is a four-cycle. Both boundary cases are also verified by exhaustive enumeration.

## Verification

Run \(\texttt{python3 verify_rook.py}\) with Python 3 standard library. The program generates every white-edge subset, tests ordinary forcing independently by two procedures, tests the forest/isolate/leaf criterion via a disjoint-set forest check, and computes optimum-set exchange edges and components for \((m,n)=(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(4,4)\). It also checks the counting formula and explicit thin-component bijections and every adjacency at \(4\le t\le12\). All checks return \(\texttt{VERIFY_OK}\). These finite computations corroborate the all-parameter proof; they are not substituted for it.

## Relationship to prior work

The zero-forcing process and minimum-number setting follow the foundational research of Barioli, Barrett, Fallat, Hogben and collaborators. Montazeri and Soltankhah already determine the scalar zero-forcing number for Cartesian products of complete graphs (the case \(k=1\)); the same scalar is not claimed as original here. Geneson, Haas and Hogben establish the general notion and properties of zero-forcing reconfiguration graphs, without the present rook-graph classification in the material inspected. The complete bipartite spanning-tree count and Prüfer encoding are classical. The claimed additional information is the *all-set* leaf/isolate criterion, exact labeled enumeration including the missing-leaf correction, and the connected-versus-two-components transition with explicit crown line-graph geometry.

## Limitations

The result concerns ordinary zero forcing only, not skew or positive-semidefinite variants. Counts retain labels. No diameter formula is claimed for the connected thick exchange graphs. A covering earlier result may exist under the equivalent name \(L(K_{m,n})\), or in unpublished/unindexed enumeration. The 2008 foundational article was available in abstract form but not as complete text; the 2010 foundational preprint and the specifically relevant 2020 and 2021 primary articles were inspected at substantive full-text level. No independent audit has been performed.

## References

1. F. Barioli et al., *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028, first public preprint March 10, 2010, https://arxiv.org/abs/1003.2028.
2. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648, DOI:10.1016/j.laa.2007.10.009 (abstract and bibliographic information inspected; complete text inaccessible).
3. Z. Montazeri and N. Soltankhah, *k-Forcing Number for the Cartesian Product of Some Graphs*, Contributions to Discrete Mathematics 16 (2021), DOI:10.55016/ojs/cdm.v16i1.68557 (full article inspected; Theorem 2.1).
4. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020), https://arxiv.org/abs/2009.00220 (full preprint inspected).
