# Congruence lattices of marked graph-incidence temporal Heyting algebras

## Finding
For every finite simple graph \(G=(V,E)\), choose a set of marked points \(L\) in its vertex–edge incidence poset. Form the temporal transit whose relation consists of all strict incidence comparisons and the reflexive pairs at the marked points, and let \(A(G,L)\) be its finite temporal Heyting upset algebra. Write \(E_0\) for edges whose incidence-poset points are *not* marked and \(E_1=E\setminus E_0\) for the others. Contract the connected components of \((V,E_0)\), delete the edges in \(E_0\), and retain each edge in \(E_1\) individually, including any resulting loops or parallel edges; call the resulting multigraph \(Q\).

Let \(I(Q)\) be the incidence poset with one minimal point for each vertex of \(Q\) and one maximal point for each edge of \(Q\), placed above its endpoint vertices. Then there is a finite-lattice isomorphism
\[
\operatorname{Con}(A(G,L))\cong\operatorname{Down}(I(Q)).
\]
Consequently, with loops and parallel edges counted individually,
\[
|\operatorname{Con}(A(G,L))|=
\sum_{W\subseteq V(Q)}2^{|E(Q[W])|},
\]
where \(E(Q[W])\) contains exactly the edge tokens with both endpoints in \(W\). The full congruence lattice is independent of whether the original *vertex* points, as opposed to the edge points, carry reflexive loops.

## Assumptions and scope
A finite simple graph may have isolated vertices; it has no graph-theoretic loops or multiple edges. Its incidence poset \(P_G=V\sqcup E\) has strict comparisons \(v<e\) precisely when the vertex \(v\) is an endpoint of the edge \(e\). Any \(L\subseteq P_G\) is permitted. Put
\[
R=\{(p,q):p<q\}\cup\{(p,p):p\in L\},\qquad R^{\circ}=R^{-1}.
\]
Its reflexivisation is the incidence order, making \((P_G,R^{\circ},R,\leq)\) a finite temporal transit. Equip \(P_G\) with the discrete finite Esakia topology. The algebra \(A(G,L)\) consists of all upsets \(X\subseteq P_G\), with set intersection, union, bottom \(\varnothing\), top \(P_G\), and operations
\[
X\to Y=P_G\setminus\downarrow(X\setminus Y),\qquad
\Box X=\{p:R[p]\subseteq X\},\qquad
\blacklozenge X=R[X].
\]
These operations satisfy the temporal Heyting axioms by the standard finite temporal Esakia duality. The theorem concerns the *entire* congruence lattice of these finite expansions; it does not assert a corresponding formula for arbitrary posets or arbitrary temporal Heyting algebras.

For the quotient multigraph \(Q\), every original edge in \(E_1\) remains a distinct edge token, even if both endpoints contract to the same component, and even if several edge tokens acquire the same endpoints. Its incidence poset is still well-defined, treating a loop-edge point as lying strictly above its one endpoint component.

## Proof
Alvarez's congruence/archival-upset correspondence identifies the congruence poset of a temporal Heyting algebra order-dually with the closed archival upsets of its temporal Esakia dual. Because the present space is finite and discrete, all subsets are closed. The archival condition for an upset \(S\subseteq P_G\) is
\[
x\notin S,\ z\in S,\ xRz
\quad\Longrightarrow\quad
\exists y\in S\;[x\leq y\ \land\ yRz].
\]
We characterize precisely the upsets satisfying this condition.

First consider an original edge-point \(e\in E_0\), so \(eRe\) is false. For either endpoint \(v<e\), upsetness says \(v\in S\Rightarrow e\in S\). Conversely, suppose \(e\in S\) and \(v\notin S\). Archivalness would require a point \(y\in S\) with \(v\leq y\) and \(yRe\). In a height-two incidence poset the only such possibilities are \(v\) and \(e\): the former is outside \(S\), and the latter is not related to itself by \(R\). Thus no witness exists. Therefore
\[
e\in S\quad\Longleftrightarrow\quad\text{both endpoints of }e\text{ belong to }S\qquad(e\in E_0).
\]
In particular, the endpoints of each edge in \(E_0\) have the same membership status. Hence the chosen vertex set \(S\cap V\) is a union of entire connected components of \((V,E_0)\). Conversely, any such choice uniquely determines the membership of all points in \(E_0\) by the displayed equivalence.

For any edge-point \(e\in E_1\), the loop \(eRe\) holds. Upsetness forces \(e\in S\) if either endpoint lies in \(S\), while \(e\) may independently lie in \(S\) when both endpoints lie outside. In the latter case every archival obligation with \(z=e\) has the witness \(y=e\). There are no other nontrivial obligations: a vertex-point has no proper predecessor and an implication with \(x=z\) cannot have \(x\notin S\ni z\). Thus marking a vertex-point with a reflexive loop never changes this characterization.

Map each archival upset \(S\) to the subset of \(I(Q)\) consisting of (i) the quotient vertices whose whole \(E_0\)-component lies in \(S\) and (ii) the retained \(E_1\)-edge points lying in \(S\). The preceding conditions say exactly that this image is an upset of \(I(Q)\). Conversely, every upset of \(I(Q)\) uniquely specifies the chosen original vertices, all forced \(E_0\)-edge points, and the retained \(E_1\)-edge points. The correspondence and its inverse preserve inclusion. Hence the archival-upset poset is isomorphic to \(\operatorname{Up}(I(Q))\). Combining this with Alvarez's order-dual congruence correspondence and then taking complements gives
\[
\operatorname{Con}(A(G,L))\cong
\operatorname{Up}(I(Q))^{\mathrm{op}}\cong
\operatorname{Down}(I(Q)).
\]
These are lattice isomorphisms because they are order isomorphisms between finite lattices.

To count the upsets of \(I(Q)\), choose the set \(W\) of quotient vertices **not** in an upset. Every edge-point with an endpoint outside \(W\) is forced into that upset; exactly the edge-points with both endpoints in \(W\) can be selected independently. There are \(2^{|E(Q[W])|}\) possibilities. Sum over all \(W\subseteq V(Q)\) to obtain the formula.

For example, if \((V,E_0)\) is connected, there is one quotient vertex; writing \(b=|E_1|\), the number of congruences is \(1+2^b\). If \(E_0=\varnothing\), then \(Q=G\) and the count becomes \(\sum_{W\subseteq V}2^{|E(G[W])|}\). For an all-marked complete graph on \(n\) vertices it is \(\sum_{j=0}^n\binom nj2^{\binom j2}\). These are consequences, not separate novelty claims.

## Verification
Two standalone Python programs accompany this result. Running `python verify_archival.py` exhaustively checks the archival quantifiers directly against the contraction formula for **every** labeled graph on at most four vertices and every marking of its edge points: \(1+1+3+27+729=761\) cases. Running `python verify_algebra.py` evaluates \(\blacklozenge\)-compatible elements directly in finite upset algebras for all edge-loop assignments of the two-edge path, triangle, three-edge path, and four-cycle, and also for all vertex-loop assignments on the three-vertex cases. All tests passed.

The second route uses the independently stated finite compatible-element criterion \(a\wedge\blacklozenge b\leq\blacklozenge(a\wedge b)\) for all \(b\) instead of enumerating archival upsets. These computations test finite instances only; the unrestricted finite-graph theorem follows from the proof above, not from enumeration.

## Relationship to prior work
David Quinn Alvarez's *A dual characterisation of simple and subdirectly-irreducible temporal Heyting algebras* (arXiv:2505.08014, initially public 12 May 2025; later Algebra Universalis 87, 36 (2026)) supplies the temporal-transit duality and the general order-dual congruence/archival-upset theorem. Those general statements are essential premises here. They do not provide the contracted marked-graph incidence-poset normal form or the resulting complete congruence lattice and induced-edge enumeration. The graph generating function in the displayed count is not claimed to be a newly invented graph polynomial; the contribution is its precise realization as a full temporal-Heyting congruence lattice in a natural graph-indexed family.

## Limitations
The claim requires finite incidence posets of *simple graphs* before contraction, with a transit obtained solely by choosing which diagonal loops to retain. It does not classify other finite temporal transits. The quotient is permitted to be a multigraph with loops and is not to be silently simplified. The literature comparison cannot exclude undiscovered equivalent representations, and no independent external mathematical audit has been performed.

## References
1. D. Q. Alvarez, *A dual characterisation of simple and subdirectly-irreducible temporal Heyting algebras*, arXiv:2505.08014 (first posted 2025-05-12), especially finite-transit definitions and the congruence/archival-upset correspondence, https://arxiv.org/abs/2505.08014 and https://arxiv.org/html/2505.08014v2.
2. D. Q. Alvarez, *A dual characterisation of simple and subdirectly-irreducible temporal Heyting algebras*, Algebra Universalis 87, article 36 (2026), https://doi.org/10.1007/s00012-026-00939-6.
3. Y. Tadesse, *Using Edge-Induced and Vertex-Induced Subhypergraph Polynomials*, Mathematica Scandinavica 117 (2015), 161–169, https://doi.org/10.7146/math.scand.a-22864 (background on already-studied graph-induction enumerators; no temporal-Heyting congruence assertion is attributed to it).
