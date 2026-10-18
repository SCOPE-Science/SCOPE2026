# All perfect edge dominating sets of nontrivial connected chain graphs

## Finding

**Theorem (complete classification and size enumerator).** Let \(G\) be a finite connected chain graph, with its two nonempty bipartition sides decomposed into the canonical open-neighborhood twin classes \(A_1,\ldots,A_p\) and \(B_1,\ldots,B_p\), where the edges between classes satisfy \(A_iB_j\subseteq E(G)\) precisely for \(j\le i\). All class sizes \(\alpha_i=|A_i|\) and \(\beta_i=|B_i|\) are positive. Put
\[
a=\sum_{i=1}^{p}\alpha_i,\qquad b=\sum_{i=1}^{p}\beta_i,\qquad m=\sum_{i=1}^{p}\alpha_i\sum_{j=1}^{i}\beta_j=|E(G)|.
\]
A **perfect edge dominating set** (PED-set) is \(F\subseteq E(G)\) for which every \(e\in E(G)\setminus F\) shares an endpoint with **exactly one** edge of \(F\). The selected edges have no such uniqueness restriction.

For \(p\ge2\), the **only** PED-sets are: the full edge set \(E(G)\); the complete stars of all \(\alpha_p\) vertices in \(A_p\); the complete stars of all \(\beta_1\) vertices in \(B_1\); and, only when \(p=2\) and \(\alpha_2=\beta_1=1\), the one-edge set joining the unique vertices in \(A_2\) and \(B_1\). Every listed set is distinct. Thus the full edge-cardinality polynomial is
\[
P_G(z):=\sum_{F\text{ a PED-set}}z^{|F|}
=z^m+\alpha_p z^b+\beta_1 z^a+
\mathbf{1}_{\{p=2,\ \alpha_2=\beta_1=1\}}z.
\]
In particular the number of PED-sets is \(1+\alpha_p+\beta_1+\mathbf{1}_{\{p=2,\alpha_2=\beta_1=1\}}\). The exceptional one-edge set is also the unique efficient edge dominating set (dominating induced matching); otherwise, no efficient edge dominating set exists when \(p\ge2\).

For \(p=1\), \(G\) is the complete bipartite graph \(K_{a,b}\). Here overlapping star/full-edge descriptions must be deduplicated. Precisely,
\[
P_{K_{a,b}}(z)=
\begin{cases}
z^{ab}+a z^b+b z^a,& a,b\ge2,\\
z^b+bz,&a=1<b,\\
z^a+az,&b=1<a,\\
z,&a=b=1.
\end{cases}
\]
These formulae describe every coefficient, including when several displayed monomials have the same degree.

**Extremal consequences.** For \(p\ge2\) the minimum PED-set size is one exactly in the exceptional case; otherwise it is \(\min\{a,b\}\). Outside the exceptional case, there are \(\beta_1\) minimum sets when \(a<b\), \(\alpha_p\) when \(b<a\), and \(\alpha_p+\beta_1\) when \(a=b\). For \(p=1\), the preceding polynomial immediately gives the minimum size and count, including singleton-side degeneracies.

## Assumptions and scope

All graphs are finite, simple, undirected, and connected, with at least one edge. A connected chain graph is a bipartite graph in which the neighborhoods on either side are linearly nested (equivalently, it has no induced pair of disjoint edges). We use the canonical nonempty twin-class representation above; the class condition ensures that \(A_p\) is complete to the entire \(B\)-side and \(B_1\) is complete to the entire \(A\)-side. The parameter \(p\ge1\) is unrestricted and may grow with graph order. Ordinary PED domination is not the same as perfect **vertex** domination, and it does not require the chosen edges to form a matching.

## Proof

**Step 1: an exact edge/vertex reduction.** Given a PED-set \(F\), write \(d_F(v)\) for the number of its selected edges incident to \(v\), and put \(W=\{v:d_F(v)=0\}\). For any edge \(uv\notin F\), exactly one selected edge shares its endpoints precisely when
\[
d_F(u)+d_F(v)=1.
\]
It follows that \(W\) is independent, since any edge with both endpoints in \(W\) would violate this identity. Also any edge with both endpoints outside \(W\) must belong to \(F\), since otherwise its two endpoints would contribute at least two distinct selected edges. Thus the selected edges are **exactly** the edges induced by \(V(G)\setminus W\). If \(W=\varnothing\), no edge can be missing, so \(F=E(G)\). Conversely \(E(G)\) always works because the outside-edge condition is vacuous.

**Step 2: white vertices on one side only.** Suppose \(W\ne\varnothing\) is contained in \(A=A_1\cup\cdots\cup A_p\). Every vertex of \(B\) is nonwhite. The universal vertex class \(B_1\) sees some vertex of \(W\), so the identity from Step 1 implies that \(d_F(y)=1\) for each \(y\in B_1\). But every nonwhite \(A\)-vertex is adjacent to \(y\) and its edge to \(y\) lies in \(F\). Hence **exactly one** vertex \(x\) of \(A\) is nonwhite. Every vertex of \(B\) is nonwhite and must have a selected incident edge; its only possible selected neighbor is \(x\). Hence \(x\) sees all of \(B\), i.e. \(x\in A_p\). The whole set \(F\) is the star at \(x\). Conversely, this full star is PED: every unselected edge has precisely one endpoint in its star's neighbor set and meets precisely the edge from that neighbor to \(x\). Symmetrically, if \(W\subseteq B\), the set \(F\) is the full star of a vertex \(y\in B_1\), and all such stars work.

**Step 3: white vertices on both sides.** Now suppose \(W\cap A\ne\varnothing\) and \(W\cap B\ne\varnothing\). The universal classes \(A_p\) and \(B_1\) lie outside \(W\), as each is adjacent to some white vertex on the opposite side. For every \(x\in A_p\), \(d_F(x)=1\) because it sees a white \(B\)-vertex; analogously every \(y\in B_1\) has \(d_F(y)=1\). Each edge between nonwhite vertices belongs to \(F\). Since every vertex of \(A\setminus W\) is adjacent to each vertex of \(B_1\), the condition \(d_F(y)=1\) forces \(A\setminus W=\{x\}\), with \(x\in A_p\); likewise \(B\setminus W=\{y\}\), with \(y\in B_1\). The induced selected edge set is therefore \(F=\{xy\}\). The remaining vertices are all white, and their set \(V(G)\setminus\{x,y\}\) must be independent. If \(p\ge3\), an edge between \(A_2\) and \(B_2\) remains, contradiction. If \(p=2\), an extra vertex of \(A_2\) would still be adjacent to a vertex of \(B_2\), and an extra vertex of \(B_1\) would still be adjacent to a vertex of \(A_1\); therefore \(\alpha_2=\beta_1=1\). These conditions suffice: with \(A_2=\{x\}\) and \(B_1=\{y\}\), all other vertices are independent and every other edge meets exactly one endpoint of \(xy\), so the singleton is a PED-set and a dominating induced matching. If \(p=1\), the graph is complete bipartite and \(W\) cannot contain both sides, so there is no mixed-side case.

**Step 4: uniqueness and enumeration.** For \(p\ge2\), both bipartition sides have at least two vertices, so stars at different centers are distinct, stars from opposite sides differ, and none equals the full edge set. The extra singleton, when present, is distinct because all these stars have at least two edges. A star from \(A_p\) has \(b\) edges; a star from \(B_1\) has \(a\); the full set has \(m\); the singleton has one. These observations give the polynomial and count. For \(p=1\), every solution remains the full edge set or a star (Steps 1–3), but a star may equal the full set when its center lies on a singleton side; when both sides are singletons every description denotes the same edge. Deduplicating yields the displayed four-case formula. The minimum-cardinality and efficient-domination claims now follow by direct inspection; in the \(p\ge2\) nonexceptional case no selected set can be an induced matching because every available star has at least two edges sharing its center, and the full edge set contains adjacent edges.

## Verification

The standalone C++17 program `verify_ped_chain.cpp` uses independent edge-subset enumeration: it builds a chain graph from each profile, checks each potential \(F\) by counting selected incident edges at endpoints of every **unselected** edge, and compares the complete set of accepted edge masks to the explicit predicted families, deduplicated by edge masks. It exhaustively processed **1,049 profiles** with total order at most \(12\) and at most \(19\) edges; these require **137,303,442** edge-subset tests, finding **4,524** PED-sets. Every predicted set and every actual set matched. Reproduce with `g++ -std=c++17 -O2 verify_ped_chain.cpp -o verify_ped_chain && ./verify_ped_chain`. The finite checks are confirmation only; Steps 1–4 establish the unrestricted theorem.

## Relationship to prior work

Grippo, Lin, Moyano and Vera (2026) motivate PED-set enumeration and give extremal counts and algorithms for trees, forests, chordal graphs and generalized series-parallel graphs, but their accessible abstract does not describe an all-chain-graph closed form. Grippo, Lin and Vera (2025/2026), **fully inspected** in its publicly available HTML presentation (definitions, structural coloring, and Section 6), already give a cubic-time **algorithm to count all PED-sets in \(P_6\)-free graphs**, a class that includes every chain graph. Thus polynomial-time *countability* in the present class **is not new**. The distinct result here is the complete explicit classification of **which edges can occur in every PED-set**, a degree-sparse cardinality polynomial, and an exact singleton exception for efficient domination; these are not stated in that paper. Earlier work on dominating induced matchings concerns the more restrictive condition that selected edges are pairwise nonincident. The structural reduction in Proof Step 1 is a specialization of the established general PED 3-color characterization; the chain-specific case distinction and all-optimizer enumerator are the additional conclusions.

## Limitations

The theorem covers connected chain graphs only. It is not a general algorithmic improvement for arbitrary \(P_6\)-free graphs, and it does not claim that counting on chain graphs was previously intractable. The complete 2026 source text could not be inspected; its accessible abstract alone cannot exclude an equivalent chain-specific lemma in an appendix. Unindexed prior work using Ferrers-graph or difference-graph terminology could also overlap. The exhaustive computational check stops at the stated order/edge thresholds and cannot certify an infinite statement independently.

## References

1. L. N. Grippo, M. C. Lin, V. Moyano, C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1 (first publicly posted 2026-07-04), https://arxiv.org/abs/2607.03894 .
2. L. N. Grippo, M. C. Lin, C. Vera, *Perfect Edge Domination in \(P_6\)-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598v2 (initially posted 2025-09-04; v2 2026-03-05), https://arxiv.org/html/2509.04598v2 .
3. M. C. Lin, V. Lozin, V. Moyano, J. L. Szwarcfiter, *Perfect Edge Domination: Hard and Solvable Cases*, Annals of Operations Research (2018), DOI: 10.1007/s10479-017-2664-3 .
4. D. M. Cardoso, N. Korpelainen, V. V. Lozin, *On the complexity of the dominating induced matching problem in hereditary classes of graphs*, Discrete Applied Mathematics (2011), https://doi.org/10.1016/j.dam.2010.03.011 .
