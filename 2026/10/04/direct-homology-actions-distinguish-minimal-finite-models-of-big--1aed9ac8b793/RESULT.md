# Direct homology actions distinguish minimal finite models of \(\bigvee^3 S^1\)
## Finding
Barmak and Minian's minimal-graph theorem implies that \(\bigvee_{i=1}^3 S^1\) has exactly three six-point minimal finite models up to homeomorphism. They are the height-two posets whose Hasse graphs are \(K_{2,4}\), its opposite \(K_{4,2}\), and \(K_{3,3}\setminus e\), where one edge is removed from the complete bipartite graph.

For these three models, the set of endomorphisms of integral first homology realized by direct continuous self-maps is not determined by weak homotopy type. For \(K_{2,4}\) and \(K_{4,2}\), there are exactly \(1782\) continuous self-maps and exactly \(421\) distinct induced endomorphisms of \(H_1\cong\mathbb Z^3\). Their ranks are distributed as
\[
1,\ 84,\ 288,\ 48
\]
for ranks \(0,1,2,3\), respectively. Exactly \(48\) self-maps induce homology automorphisms, and these are exactly the \(48\) homeomorphisms.

For \(K_{3,3}\setminus e\), there are exactly \(646\) continuous self-maps and exactly \(113\) distinct induced endomorphisms of \(H_1\cong\mathbb Z^3\), with rank profile
\[
1,\ 60,\ 48,\ 4.
\]
Exactly \(4\) self-maps induce homology automorphisms, and these are exactly the \(4\) homeomorphisms.

Thus even among minimum-cardinality finite models of the same graph homotopy type, direct \(H_1\)-action expressivity can differ: the two opposite complete-bipartite models realize \(421\) homology endomorphisms, while the third minimal model realizes only \(113\).

## Assumptions and scope
A finite \(T_0\)-space is identified with its specialization poset. Continuity is therefore order preservation. All spaces in the claim are height two, so their order complexes are one-dimensional and coincide with the underlying undirected Hasse graphs.

The comparison concerns direct continuous self-maps of the stated six-point spaces. It does not claim that the full self-map monoid of the ordinary bouquet \(\bigvee^3 S^1\), or self-maps of larger finite models and subdivisions, is similarly restricted.

The first-homology action is computed over \(\mathbb Z\). The cardinality of the realized action set and the rank profile are basis-independent, although the certificate uses an explicit spanning-tree cycle basis.

## Proof
Barmak and Minian prove that a minimal finite model of \(\bigvee_{i=1}^n S^1\) has height two, minimum possible cardinality \(i+j\) with \((i-1)(j-1)\ge n\), and exactly \(\#X+n-1\) Hasse edges. For \(n=3\), the minimum cardinality is \(6\) and the number of Hasse edges is \(8\).

Write \(p\) for the number of minimal points and \(q\) for the number of maximal points. Since \(p+q=6\) and the Hasse graph has \(8\) edges, one must have \(pq\ge 8\). Hence, up to exchanging the two levels, only \((p,q)=(2,4)\) and \((3,3)\) occur. In the first case all \(8\) possible edges are present, giving \(K_{2,4}\); exchanging the levels gives its opposite. In the balanced case, exactly one of the \(9\) possible edges is absent, and all one-edge deletions of \(K_{3,3}\) are isomorphic. This recovers the three models listed in the primary source.

For either model, orient every Hasse edge from the lower level to the upper level. Because the order complex is a connected graph with \(6\) vertices and \(8\) edges,
\[
H_1\cong \mathbb Z^{8-6+1}=\mathbb Z^3.
\]
Choose a spanning tree. The three non-tree edges determine a fundamental-cycle basis. Each basis cycle has coefficient \(1\) on its own non-tree edge and coefficient \(0\) on the other two, so the coordinates of any cycle are read directly from its three non-tree-edge coefficients.

There are only \(6^6=46656\) set maps on each six-point underlying set. A map is continuous exactly when every strict relation \(u<v\) satisfies either \(f(u)=f(v)\) or \(f(u)<f(v)\). For every continuous map, the induced simplicial chain map sends an oriented edge \([u,v]\) to zero when its endpoints are identified and otherwise to \([f(u),f(v)]\). Applying this chain map to the three fundamental cycles gives an exact integral \(3\times3\) matrix.

The embedded verifier exhausts all \(46656\) set maps for each model, checks order preservation, reconstructs every image cycle from the fundamental-cycle basis, and then deduplicates the resulting matrices. It obtains:

\[
\begin{array}{c|c|c|c|c}
\text{model} & \text{continuous maps} & \text{distinct }H_1\text{ actions} & \text{distinct ranks }0,1,2,3 & \text{homeomorphisms}\\
\hline
K_{2,4} & 1782 & 421 & (1,84,288,48) & 48\\
K_{4,2} & 1782 & 421 & (1,84,288,48) & 48\\
K_{3,3}\setminus e & 646 & 113 & (1,60,48,4) & 4
\end{array}
\]

For each continuous self-map the verifier also computes the determinant of the induced integral matrix. In the complete-bipartite models exactly \(48\) maps have determinant \(\pm1\), and in \(K_{3,3}\setminus e\) exactly \(4\) do. A separate order-isomorphism test finds exactly the same maps. Therefore a self-map induces an automorphism of \(H_1\) if and only if it is a homeomorphism in all three minimal models.

The opposite model has the same counts because reversing both domain and codomain orders preserves the set of monotone self-functions, while the order complex is unchanged as an abstract graph. The explicit second enumeration in the verifier independently confirms the equality of all stated counts.

## Verification
The package contains `verify.py`, a dependency-free exact verifier. It constructs the three height-two posets, builds a spanning-tree basis of graph cycles, checks the boundary of each basis cycle, enumerates all set maps, filters the monotone maps, computes the induced chain map exactly, reconstructs every image cycle from its basis coordinates, and checks determinant and order-isomorphism conditions.

Running `python3 verify.py` produces `VERIFY_OK` and the exact totals recorded in `verification_output.txt`.

## Relationship to prior work
Barmak and Minian's 2006 preprint `arXiv:math/0611156` is the primary source for the minimal finite graph-model theorem and explicitly states that \(\bigvee^3 S^1\) has three six-point, eight-edge minimal finite models. Their result determines the models but does not state the self-map counts or the induced-homology action counts proved here.

Bradley's 2013 preprint `arXiv:1312.1191` studies homology under monotone maps of finite \(T_0\)-spaces, including a general surjectivity result for surjective monotone maps. That result supplies useful context for map-induced homology but does not determine the complete self-map action semigroups of these three minimal models.

Targeted searches for the exact model aliases, exact counts, self-map monoids, and induced \(H_1\) actions did not locate a published statement implying the \(421\)-versus-\(113\) distinction. A 2026 paper on Whitehead phenomena for minimal finite models concerns weak equivalences between other minimal models and does not supply these direct self-map action censuses.

## Limitations
The numerical classification is a finite exhaustive theorem for these three six-point models, not a closed formula for all minimal finite models of bouquets. The result compares only integral first-homology actions; two distinct self-maps can induce the same homology endomorphism, and no claim is made that the induced-homology action determines the full homotopy class of a finite-space self-map.

The literature search was targeted rather than logically exhaustive over every historical or unindexed source. The strongest identified primary source fixes the three minimal models but does not contain the action census; residual bibliographic risk therefore remains.

## References
1. Jonathan Ariel Barmak and Elias Gabriel Minian, *Minimal Finite Models*, arXiv:math/0611156, first posted 2006-11-06; Journal of Homotopy and Related Structures 2 (2007), 127-140.
2. Patrick Erik Bradley, *Homology under monotone maps between finite topological spaces*, arXiv:1312.1191, first posted 2013-12-04.
3. M. C. McCord, *Singular homology groups and homotopy groups of finite topological spaces*, Duke Mathematical Journal 33 (1966), 465-474.
