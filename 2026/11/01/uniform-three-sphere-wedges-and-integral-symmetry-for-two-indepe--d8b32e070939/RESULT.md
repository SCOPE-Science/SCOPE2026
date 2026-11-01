# Uniform three-sphere wedges and integral symmetry for two-independence Kneser complexes

## Finding
For every integer \(n\ge4\), put \(G_n=\operatorname{KG}(n,2)\), the graph with vertices the two-element subsets of \([n]=\{1,\ldots,n\}\), where two vertices are adjacent if the underlying sets are disjoint. Let \(X_n=\operatorname{Ind}_2(G_n)\), whose faces are vertex sets inducing graph components of at most two vertices. There is a nonequivariant integral homotopy equivalence
\[
X_n\simeq \bigvee^{\binom{n-1}{4}}S^3.
\]
The wedge with zero summands is a point. Furthermore, for the natural \(\mathfrak S_n\)-action induced by permuting the underlying ground set, there is a natural integral module isomorphism
\[
\widetilde H_3(X_n;\mathbb Z)\cong \bigwedge^4 V_n,\qquad V_n=\ker\left(\mathbb Z^{[n]}\xrightarrow{\sum}\mathbb Z\right).
\]
All other reduced integral homology groups vanish. The homology module statement is equivariant; an equivariant homotopy splitting is not asserted. In particular, for the graph on fifteen vertices \(\operatorname{KG}(6,2)\), the complex is a wedge of five three-spheres, with its integral \(\mathfrak S_6\)-module given by the fourth exterior power of the rank-five augmentation lattice.

## Assumptions and scope
All simplicial complexes are finite and abstract. The usual \(1\)-independence complex \(Y_n=\operatorname{Ind}_1(G_n)\) is the complex of families of pairwise-intersecting two-element subsets of \([n]\). For a four-element ground subset \(T\), write \(D_T\) for the full simplex on its six two-element subsets, and \(B_T=D_T\cap Y_n\). The action of \(\mathfrak S_n\) on these objects is by relabeling the ground elements. All statements hold for every integer \(n\ge4\), without an asymptotic or computational cutoff.

## Proof
**1. Cover by four-ground-set simplices.** The graph induced by the six two-element subsets of a four-set \(T\) in \(G_n\) consists of three independent graph edges: its disjoint pairs are the three pairs of complementary two-subsets. Thus every subset of those six vertices has induced maximum graph degree at most one and \(D_T\subset X_n\). If a face \(F\) of \(X_n\) is not in \(Y_n\), it contains two disjoint two-subsets \(e,f\). Their two vertices are already adjacent in the induced graph; since all induced degrees are at most one, every other member of \(F\) intersects both \(e\) and \(f\). Such a two-subset is contained in \(e\cup f\), a four-set. Hence
\[
X_n=Y_n\cup\bigcup_{|T|=4}D_T.
\]
Moreover, for distinct four-sets \(T,U\), their intersection has at most three ground elements, and all two-subsets of a three-set pairwise intersect. Consequently \(D_T\cap D_U\subset Y_n\). Finally \(B_T\) chooses at most one vertex from each of three complementary pairs. It is the boundary of a three-dimensional cross-polytope, \(B_T\cong S^0*S^0*S^0\cong S^2\).

**2. A contractible core.** Fix the ground element \(1\) and write \(v_i=\{1,i\}\) for \(i=2,\ldots,n\). These vertices form a simplex of the flag complex \(Y_n\). Define
\[
A=\bigcup_{i=2}^{n}\operatorname{st}_{Y_n}(v_i),
\]
using the closed simplicial stars. Every nonempty intersection of these stars is the closed star of the corresponding common simplex: the flag property makes pairwise compatibility sufficient. Every such intersection is a cone, and all intersections occur. The finite nerve of this cover is a simplex, so \(A\) is contractible.

Every pairwise-intersecting family of two-subsets is either contained in a star of ground edges incident to one point or is the three-edge set \(\tau_{abc}=\{\{a,b\},\{a,c\},\{b,c\}\}\) of a triangle on three ground points. This follows directly: if a family has no common ground point, three of its members must be the edges of one triangle, and no further different two-subset meets all three. Thus the only simplices of \(Y_n\) missing from \(A\) are the triangles \(\tau_{abc}\) with \(1\notin\{a,b,c\}\). Their proper faces lie in \(A\).

Let \(X_0=A\cup\bigcup_{T\ni1,\,|T|=4}D_T\). For each \(T=\{1,a,b,c\}\), the intersection \(D_T\cap A\) is precisely the octahedral sphere \(B_T\) with the open triangular facet \(\tau_{abc}\) removed; hence it is a closed two-disk. Intersections of distinct such \(D_T\)'s are already in \(A\). Adjoining each contractible simplex along a nonempty contractible subcomplex preserves contractibility (the CW gluing lemma); therefore \(X_0\) is contractible. Furthermore, every triangle omitted from \(A\) occurs in \(D_{\{1,a,b,c\}}\). Thus \(Y_n\subseteq X_0\).

For every four-set \(T\) avoiding \(1\), the intersection \(D_T\cap X_0\) is exactly \(B_T\cong S^2\): all intersections with other four-set simplices are in \(Y_n\), and \(Y_n\subset X_0\). The intersections of distinct remaining \(D_T\) likewise lie in \(Y_n\). As \(X_0\) is contractible and is a subcomplex, collapsing it is a homotopy equivalence. The quotient is a wedge of \(D_T/B_T\), each a copy of \(\Sigma S^2\simeq S^3\). The number of four-sets avoiding \(1\) is \(\binom{n-1}{4}\). This proves the homotopy formula integrally and for all \(n\).

**3. Integral symmetric-group module.** Put \(M=\mathbb Z^{[n]}\), with basis \(e_1,\ldots,e_n\) permuted by \(\mathfrak S_n\), and \(\varepsilon:M\to\mathbb Z\) sending every basis vector to one. Set \(V=\ker\varepsilon\). The relative pairs \((D_T,B_T)\) give an equivariant decomposition
\[
H_3(X_n,Y_n;\mathbb Z)\cong\bigoplus_{|T|=4}\mathbb Z\,[T]\cong\bigwedge^4M,
\]
where the orientation of the octahedral fundamental class for \(T=\{a<b<c<d\}\) is the join of the three zero-sphere differences \(([ab]-[cd])*([ac]-[bd])*([ad]-[bc])\). Under ground-label permutations this class transforms by the sign of the induced permutation of the ordered four-set. This can be checked directly from the eight oriented facets (and is independently checked for all 24 permutations of four labels by the attached verifier).

Since \(Y_n/A\) has one two-cell for each \(\tau_{abc}\) avoiding \(1\) and no nontrivial relative differential, \(H_2(Y_n;\mathbb Z)\cong H_2(Y_n,A;\mathbb Z)\cong\bigwedge^3W\), where \(W\) is spanned by \(e_2,\ldots,e_n\). In particular \(H_3(Y_n;\mathbb Z)=0\). On the above oriented octahedral cycle, the coefficients of the four triangle facets \(\tau_{bcd},\tau_{acd},\tau_{abd},\tau_{abc}\) are \(+1,-1,+1,-1\), respectively. Therefore the connecting map in the pair sequence, followed by the natural relative projection, is
\[
\delta:\bigwedge^4M\longrightarrow\bigwedge^3W,
\qquad\delta=\pi\circ\iota_{\varepsilon},
\]
where the Koszul contraction is \(\iota_\varepsilon(e_a\wedge e_b\wedge e_c\wedge e_d)=e_b\wedge e_c\wedge e_d-e_a\wedge e_c\wedge e_d+e_a\wedge e_b\wedge e_d-e_a\wedge e_b\wedge e_c\), and \(\pi\) removes all terms containing \(e_1\).

The map \(\iota_\varepsilon\) has image \(\bigwedge^3V\) and kernel \(\bigwedge^4V\) integrally: split \(M=\mathbb Ze_1\oplus V\), noting \(\varepsilon(e_1)=1\), and take exterior powers. The projection \(\pi:\bigwedge^3V\to\bigwedge^3W\) is an integral isomorphism, since the basis \(e_i-e_1\) of \(V\), for \(i>1\), maps to the basis \(e_i\) of \(W\). Therefore \(\ker\delta=\bigwedge^4V\). The long exact homology sequence and \(H_3(Y_n)=0\) give the required equivariant isomorphism \(H_3(X_n)\cong\ker\delta\); everything in the contraction description is natural under \(\mathfrak S_n\). The homotopy statement already proves the vanishing of other reduced integral homology.

For a permutation with cycle lengths \(\ell_1,\ldots,\ell_r\), the rational character is consequently the coefficient of \(t^4\) in \(\prod_{j=1}^r(1-(-t)^{\ell_j})/(1+t)\). This formula is a consequence of the integral module theorem, not an additional assumption.

## Verification
The accompanying Python 3 standard-library script `verify_kneser2.py` independently constructs all faces for ground-set sizes \(4\le n\le8\); for \(n=6\) it additionally checks all \(2^{15}\) vertex subsets by a separate direct membership test. It constructs and verifies full acyclic discrete-Morse matchings on the complete directed face-incidence graphs. The critical cells are exactly one vertex and \(\binom{n-1}{4}\) three-cells. It also checks the octahedral cycle's integer boundary, its 24 orientation transformations, and every symmetry Lefschetz trace for \(\mathfrak S_5\) and \(\mathfrak S_6\), agreeing with the character of \(\bigwedge^4V\). The actual standard output is embedded as `verification_output.txt`. These finite checks are supplementary; the proof above establishes the result for every \(n\ge4\).

## Relationship to prior work
Deshpande and Singh introduced and studied higher-independence complexes and calculated several graph families, but not this two-subset Kneser family at cutoff two. Barmak established the ordinary independence-complex homotopy type \(\operatorname{Ind}_1(\operatorname{KG}(n,2))\simeq\bigvee^{\binom{n-1}{3}}S^2\) using star clusters. Its three-dimensional suspension count and natural integral fourth-exterior-power module do not follow simply from that ordinary-cutoff result. Feng and Wang studied ordinary independence complexes of Kneser graphs using homological methods, not the two-independence complex treated here. Existing neighborhood- and Čech-complex results for small Kneser graphs concern different simplicial complexes. The known Petersen five-ground-point instance is a special boundary case, not claimed as independently novel. The contribution here is the uniform all-size theorem and the integral symmetry module.

## Limitations
The classification requires two-element Kneser vertices and induced component cutoff exactly two; it does not cover larger subset sizes, larger cutoffs or Schrijver restrictions. The wedge equivalence is nonequivariant, while the homology isomorphism is integral and equivariant. The finite checker only tests \(n\le8\); it is not an exhaustive proof for arbitrary \(n\). Novelty comparisons are based on inspected literature and indexed research, and an unindexed equivalent formulation remains a residual bibliographic risk. No independent audit or external certification is claimed.

## References
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, first available 2020-01-15, arXiv:2001.05448, https://arxiv.org/abs/2001.05448 .
- J. A. Barmak, *Star clusters in independence complexes of graphs*, first available 2010-07-02, arXiv:1007.0418, https://arxiv.org/abs/1007.0418 .
- Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, https://arxiv.org/abs/2404.10566 .
- F. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, https://arxiv.org/abs/2106.10863 .
