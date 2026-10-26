# A cube-deletion transition for minimum-independent-domination reconfiguration of shallow spiders

## Finding

**Theorem.** Let \(s\ge3\) and \(t\ge0\) be integers. Form a tree \(T_{s,t}\) from a vertex \(c\) by attaching \(s\) pairwise vertex-disjoint two-edge arms \(c-a_i-b_i\), indexed by \(1\le i\le s\), and \(t\) one-edge arms \(c-d_j\), indexed by \(1\le j\le t\). Let \(\mathcal I(T)\) denote the graph whose vertices are *minimum independent dominating sets* of \(T\) and whose edges represent a single token slide along an edge of \(T\), preserving a minimum independent dominating set. Define \(Q_s\) to be the graph on \(\{0,1\}^s\) with edges between binary vectors of Hamming distance one. Then

\[
\mathcal I(T_{s,t})\cong
\begin{cases}
Q_s-\{\mathbf 0\},&t=0,\\
Q_s\text{ with one pendant vertex adjacent to }\mathbf0,&t=1,\\
K_1,&t\ge2.
\end{cases}
\]

In all cases \(i(T_{s,t})=s\) if \(t=0\), and \(i(T_{s,t})=s+1\) if \(t\ge1\). The numbers of minimum independent dominating sets in the three regimes are respectively \(2^s-1\), \(2^s+1\), and \(1\); their reconfiguration edge counts are respectively \(s2^{s-1}-s\), \(s2^{s-1}+1\), and \(0\).

In particular, the once-subdivided star \(T_{s,0}\), an instance of the spider family identified in Problem 5(b) by Brewster--Mynhardt--Teshima [1], has an explicitly identified reconfiguration graph. The graphs in the first two regimes are connected and Hamiltonian traceable but not Hamiltonian. Their diameters are respectively \(s\) and \(s+1\); the first is not median, whereas the second is median. This exhibits a change of reconfiguration geometry caused by adding one or two short arms.

## Assumptions and scope

All graphs are finite, simple and undirected. An independent dominating set \(S\subseteq V(T)\) is independent and satisfies \(N_T[S]=V(T)\); \(i(T)\) denotes the minimum cardinality of such sets. An edge of \(\mathcal I(T)\) joins distinct minimum independent dominating sets \(S,S'\) if \(S'=(S\setminus\{u\})\cup\{v\}\) for some \(uv\in E(T)\), with \(u\in S\) and \(v\notin S\). The primary theorem covers every integer \(s\ge3\), \(t\ge0\), with no assumptions on order or labels beyond the displayed construction. \(\mathbf0\) denotes the zero vector in \(Q_s\), and coordinate \(1\) records choosing \(a_i\) rather than \(b_i\). A graph is *median* when every triple of vertices has a unique vertex lying on shortest paths between each pair.

## Proof

**1. Exhaustive classification of independent dominating sets.** Each leaf \(b_i\) has unique neighbor \(a_i\). Hence every independent dominating set contains at least one member of \(\{a_i,b_i\}\), and independence forces exactly one. If \(c\in S\), independence excludes every \(a_i\) and \(d_j\); each \(b_i\) is consequently forced. Thus the only center-containing independent dominating set is
\[
C=\{c,b_1,\ldots,b_s\},\qquad |C|=s+1.
\]
This set dominates every vertex. If \(c\notin S\), each pendant leaf \(d_j\) must belong to \(S\), and one member of each \(\{a_i,b_i\}\) must belong to \(S\). Such a set has size \(s+t\) and can be written uniquely as
\[
S_X=\{a_i:i\in X\}\cup\{b_i:i\notin X\}\cup\{d_1,\ldots,d_t\},\quad X\subseteq[s].
\]
It is independent. All vertices except the center are dominated; the center is dominated exactly when \(t\ge1\) or \(X\ne\varnothing\). There are no additional independent dominating sets, since the case split is exhaustive.

**2. Minimum-set classification.** If \(t=0\), every admissible \(S_X\) has size \(s\), strictly smaller than \(C\); admissibility requires \(X\ne\varnothing\). Therefore \(i(T_{s,0})=s\), with precisely \(2^s-1\) minimum sets. If \(t=1\), all \(S_X\), including \(S_\varnothing\), and \(C\) have size \(s+1\), yielding \(2^s+1\) minima. If \(t\ge2\), \(|S_X|=s+t>s+1=|C|\), so \(C\) is the unique minimum set.

**3. Every reconfiguration edge.** Between two distinct minima \(S_X,S_Y\) not containing \(c\), all short leaves are fixed. Exchanging exactly one member of a long-arm pair along its edge \(a_ib_i\) is the only possible one-token slide, so \(S_X\sim S_Y\) exactly when \(|X\mathbin\triangle Y|=1\). For \(t=0\), the forbidden subset \(\varnothing\) deletes the zero vertex of the cube and precisely its \(s\) incident edges. For \(t=1\), all cube vertices survive. The only possible slide between a center-containing and a center-excluding minimum set exchanges \(c\) with its unique short leaf \(d_1\), leaving every \(b_i\) fixed. Hence \(C\) is attached solely to \(S_\varnothing\), and this edge exists. For \(t\ge2\), the reconfiguration graph has only the vertex \(C\). This proves each graph isomorphism. Since \(Q_s\) has \(s2^{s-1}\) edges, the displayed size and edge-count formulas follow.

**4. Further geometry.** Any shortest coordinate-flip path between two nonzero vectors may be chosen never to visit \(\mathbf0\): first flip coordinates needed to turn zeros into ones, then flip coordinates needed to turn ones into zeros. The order preserves a nonzero vector throughout, and its length is their Hamming distance. Thus \(Q_s-\{\mathbf0\}\) is isometric in \(Q_s\); its diameter is \(s\) (for example, \(\mathbf e_1\) and its bitwise complement attain this distance for \(s\ge2\)). Attaching one pendant vertex at \(\mathbf0\) changes the diameter to \(s+1\).

The standard binary reflected Gray cycle gives a Hamilton cycle of \(Q_s\) for \(s\ge2\). Removing \(\mathbf0\) from that cycle gives a Hamilton path in \(Q_s-\{\mathbf0\}\). Starting at the new pendant vertex, traversing its incident edge, then following a Hamilton path of the cube from \(\mathbf0\) gives a Hamilton path in the second regime. The first graph has odd order \(2^s-1\) and is bipartite, so has no spanning cycle; the second graph has a degree-one vertex, so has no spanning cycle.

To see the first graph is not median, take three different coordinate unit vectors \(\mathbf e_1,\mathbf e_2,\mathbf e_3\). The interval of shortest paths between \(\mathbf e_i\) and \(\mathbf e_j\) is precisely \(\{\mathbf e_i,\mathbf e_i+\mathbf e_j,\mathbf e_j\}\). The three pairwise intervals have empty common intersection. The cube itself is median (coordinatewise majority gives the unique median). Adjoining a leaf at one existing vertex preserves this property: for triples not involving the leaf the median is unchanged, and for triples involving the leaf the required intersection equals the unique cube median of the attachment vertex and the other two vertices. Therefore the second reconfiguration graph is median.

## Verification

The standalone script `verify.py` enumerates every vertex subset of independently constructed \(T_{s,t}\) trees for \(2\le s\le6\) and \(0\le t\le3\), retaining independent dominating sets, extracting all minimum sets, and computing actual token-slide adjacencies directly from the tree edges. For the stated range \(s\ge3\), all tested results agree with the theorem; the additional \(s=2\) checks test a natural boundary. The execution examines \(163680\) candidate subsets across \(20\) instances, \(258\) minimum sets and \(625\) reconfiguration edges. Its recorded output is in `verification_output.txt`.

These finite checks do not establish the unrestricted theorem. All universal quantifiers are established by the case analysis and graph-isomorphism proof above.

## Relationship to prior work

Brewster, Mynhardt and Teshima [1, §8, Problem 5(b)] explicitly ask for the structure of reconfiguration graphs of spiders obtained by subdividing star edges. The case \(t=0\) describes the once-subdivided star for every number of arms, and \(t=1,2\) exhibit a sharp two-short-arm perturbation. That paper studies realizability of theta graphs rather than giving the seed-specific spider classification. The same authors' earlier paper [2] develops general realizability constructions for numerous target graph families including hypercubes; abstract realizability does not imply this characterization for the particular spider seeds. Their paper [3] determines reconfiguration graphs for paths and cycles, not the branching spider family \(s\ge3\).

The explicit distinction between a punctured cube, a cube with a leaf, and a singleton is not a mere restatement of cube realizability: it specifies all minimum feasible solutions and all token-slide adjacencies for the given trees, and distinguishes median and Hamiltonian properties of the resulting graphs.

## Limitations

The theorem covers exactly the prescribed shallow spiders with arms of length one or two. It does not classify spiders with arms of length three or greater, nor arbitrary trees. The first regime represents one exact slice of the published spider question, not a purported resolution for every convention of spider subdivision. The asserted originality is relative to inspected primary literature and available research records; an unindexed equivalent or an unexpected reduction from another family remains a possible priority risk.

## References

[1] R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *The Realizability of Theta Graphs as Reconfiguration Graphs of Minimum Independent Dominating Sets*, arXiv:2305.17814v1, first posted 2023-05-28, §8 Problem 5(b). https://arxiv.org/html/2305.17814v1

[2] R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *Reconfiguration of Minimum Independent Dominating Sets in Graphs*, arXiv:2303.06299v1, 2023-03-11. https://arxiv.org/html/2303.06299v1

[3] R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *The i-Graphs of Paths and Cycles*, arXiv:2303.08190v1, 2023-03-14. https://arxiv.org/html/2303.08190v1
