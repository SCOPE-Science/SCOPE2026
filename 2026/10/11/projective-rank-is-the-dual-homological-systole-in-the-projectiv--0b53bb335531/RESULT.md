# Projective rank is the dual homological systole in the projective plane
## Finding
Let \(G\) be a finite connected graph cellularly embedded in \(\mathbb{RP}^2\). Boyle and Spyropoulos define its projective rank by
\[
\alpha(G)=\min\{|A|:A\subseteq E(G),\;G-A\text{ is local}\}.
\]
Let \(G^\ast\) be the cellular dual. Define \(\operatorname{ew}_1(G^\ast)\) to be the minimum number of edges in a mod-two cycle of \(G^\ast\) representing the nonzero class of \(H_1(\mathbb{RP}^2;\mathbb F_2)\). Then
\[
\alpha(G)=\operatorname{ew}_1(G^\ast).
\]
There is also a signed-graph interpretation. Choose a cellular cocycle \(u\in Z^1(\mathbb{RP}^2;\mathbb F_2)\) representing the nonzero cohomology class and sign each edge \(e\) of \(G\) by \((-1)^{u(e)}\). The switching class is independent of the chosen cocycle representative, and its frustration index equals \(\alpha(G)\).

If \(\widetilde{G^\ast}\) is the lift of the dual graph to the double cover \(S^2\to\mathbb{RP}^2\), with deck involution \(\tau\), then
\[
\alpha(G)=\min_{\tilde v\in V(\widetilde{G^\ast})}d_{\widetilde{G^\ast}}(\tilde v,\tau\tilde v).
\]
Thus the projective rank of a cellular embedding is computable as a shortest-path quantity in its lifted dual.

For a connected reduced alternating link diagram in \(\mathbb{RP}^3\) whose checkerboard graphs \(G_+,G_-\) form a cellular dual pair, Boyle and Spyropoulos prove
\[
\operatorname{br}J_L^\pm=c(L)-\alpha(G_\pm).
\]
Since \(G_- = G_+^\ast\), the preceding identity gives the dual-systolic form
\[
\operatorname{br}J_L^+=c(L)-\operatorname{ew}_1(G_-),\qquad
\operatorname{br}J_L^-=c(L)-\operatorname{ew}_1(G_+).
\]

## Assumptions and scope
The graph statement requires a finite connected cellular embedding in the projective plane. Loops and parallel edges are allowed. The dual-cycle length is counted with unit edge weights and mod-two coefficients. The link consequence is asserted only when the checkerboard graphs form a cellular dual pair; no claim is made for a noncellular embedding without first choosing a cellulation that preserves the relevant edge set.

The signed graph is the switching class obtained from the restriction to \(G\) of the unique nonzero class in \(H^1(\mathbb{RP}^2;\mathbb F_2)\). Changing the cellular cocycle by a coboundary switches signs at vertices, so its frustration index is well defined.

## Proof
Fix a cellular cocycle \(u\) representing the nonzero element of \(H^1(\mathbb{RP}^2;\mathbb F_2)\). For an edge set \(A\subseteq E(G)\), the subgraph \(G-A\) is local exactly when the restriction of this ambient cohomology class to \(G-A\) vanishes. Equivalently, there is a vertex function \(f:V(G)\to\mathbb F_2\) such that
\[
u(e)=\delta f(e)\qquad\text{for every }e\notin A.
\]
Therefore the support of the cocycle \(u+\delta f\) is contained in \(A\). Conversely, if \(B=\operatorname{supp}(u+\delta f)\), then \(u\) restricts to the coboundary \(\delta f\) on \(G-B\), so \(G-B\) is local. Hence
\[
\alpha(G)=\min_{f:V(G)\to\mathbb F_2}|\operatorname{supp}(u+\delta f)|.
\]
The right side is exactly the frustration index of the signing \((-1)^{u(e)}\): switching at the vertices where \(f=1\) replaces \(u\) by \(u+\delta f\), and the number of negative edges after switching is its support size.

Cellular Poincare duality sends a cellular cocycle on \(G\) to the dual one-cycle consisting of precisely the dual edges crossing its support. Coboundary changes do not change the homology class, so the cocycles \(u+\delta f\) are in weight-preserving bijection with dual one-cycles representing the nonzero class of \(H_1(\mathbb{RP}^2;\mathbb F_2)\). Taking minimum support gives
\[
\alpha(G)=\operatorname{ew}_1(G^\ast).
\]
A minimum mod-two dual cycle may be taken to be a shortest homologically nontrivial circuit: if a minimum cycle decomposed into circuits, at least one circuit would carry the nonzero projective-plane class and would use no more edges.

Finally, a homologically nontrivial closed walk in \(G^\ast\) lifts to a path in \(\widetilde{G^\ast}\) from a vertex \(\tilde v\) to its deck mate \(\tau\tilde v\). Conversely, any such lifted path projects to a homologically nontrivial closed walk, which contains a nontrivial circuit no longer than the walk. Minimizing proves the double-cover distance formula. Substitution into the Boyle--Spyropoulos breadth theorem gives the two link formulas.

## Verification
The proof was replayed at the level of cellular cochains and dual chains. The two nontrivial equivalences were checked separately: deleting an edge set kills the ambient projective cohomology class exactly when a vertex switching makes every surviving edge positive, and cellular Poincare duality preserves edge support while exchanging the nonzero degree-one cohomology class with the nonzero degree-one homology class. No finite experiment is used as an infinite proof.

Boundary cases were checked symbolically. A single projective loop has projective rank one and dual systole one. If the relevant ambient cohomology class is already trivial on an embedding, the graph is local and both the signed-graph obstruction and the projective-rank problem degenerate; this case is excluded by cellularity of a nontrivial projective-plane cellulation and is not needed for the link application.

## Relationship to prior work
Boyle and Spyropoulos introduced \(\alpha(G)\) as an edge-deletion invariant and proved that, for connected reduced alternating links in \(\mathbb{RP}^3\), it measures the deficit between crossing number and the breadth of each Jones-polynomial piece. Their paper also develops the Poincare-dual checkerboard graphs, but does not identify projective rank with a frustration index, representativity/dual systole, or a shortest path in the spherical double cover.

The frustration index itself is classical in signed graph theory: it is the minimum number of edge deletions, or equivalently the minimum number of negative edges after switching, needed to make a signed graph balanced. Coding-theoretic treatments identify switching classes with cosets of the cut-space code. The new point here is the exact identification of the newly introduced projective rank with that classical optimization parameter for the ambient projective cohomology signing, followed by the cellular-dual and double-cover formulas.

Literature searches for the phrases “projective rank” together with dual edge-width, frustration index, representativity, and shortest noncontractible dual cycle did not locate this identification. General literature on projective-plane representativity and signed-graph frustration is compatible with the proof but does not, in the material inspected, state the Boyle--Spyropoulos invariant or the displayed Jones-breadth reformulation.

## Limitations
The dual-systole and double-cover formulas are stated only for cellular embeddings. The result does not prove either conjectural non-alternating inequality proposed by Boyle and Spyropoulos, nor does it imply that the full Jones polynomial determines the dual systoles outside their alternating setting. The originality comparison has a residual folklore risk because cocycle switching and surface duality are standard separately; no exact prior statement connecting them to the 2026 projective-rank invariant was located.

## References
1. K. Boyle and D. Spyropoulos, “Myopic Tutte polynomials and Khovanov homology in \(\mathbb{RP}^3\),” arXiv:2609.40122v1, submitted 30 September 2026. In particular, Definition 1.6, Theorem 1.4, Lemma 5.1, and the surrounding discussion of checkerboard duality.
2. P. Sole and T. Zaslavsky, “A Coding Approach to Signed Graphs,” SIAM Journal on Discrete Mathematics, DOI 10.1137/S0895480189174374. The cocycle-code/switching-class viewpoint supplies classical context for the frustration interpretation.
3. S. P. Randby, “Minimal embeddings in the projective plane,” Journal of Graph Theory 25 (1997), 153–163. This is background on representativity and noncontractible curves in projective-plane embeddings.
