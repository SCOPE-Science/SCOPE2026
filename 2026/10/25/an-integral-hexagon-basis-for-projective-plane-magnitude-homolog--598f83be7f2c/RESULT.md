# An integral hexagon basis for projective-plane magnitude homology

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge2\), and let \(G_\Pi\) be its point–line incidence graph with the shortest-path metric. For ordered distinct points \(P,Q\), let \(L=PQ\). For each point \(R\notin L\), put \(a=PR\), \(b=RQ\), and define the length-four magnitude three-chain
\[
 z_{P,Q;R}=(P,a,b,Q)-(P,a,P,Q)-(P,L,b,Q).
\]
Then the homology classes \(\{[z_{P,Q;R}]:R\notin L\}\) are an **integral basis** of the endpoint-localized group \(\operatorname{MH}^{P,Q}_{3,4}(G_\Pi;\mathbb Z)\). The same assertion holds, by point–line duality, for each ordered pair of distinct lines, indexed by a third line not passing through their intersection.

Write \(\mathcal T_\Pi\) for the set of ordered noncollinear triples of points together with ordered nonconcurrent triples of lines. Every incidence-graph automorphism permutes the displayed homology classes without signs. Thus, naturally for the entire incidence-graph automorphism group \(\Gamma\),
\[
 \bigoplus_{\substack{P\ne Q\\P,Q\text{ of the same type}}}
 \operatorname{MH}^{P,Q}_{3,4}(G_\Pi;\mathbb Z)
 \ \cong_{\mathbb Z[\Gamma]}\ \mathbb Z[\mathcal T_\Pi].
\]
The number of generators is \(2(q^2+q+1)(q^2+q)q^2\). In particular, the basis proves the absence of integral torsion in these endpoint summands, including for non-Desarguesian planes.

For the Fano plane \(\operatorname{PG}(2,2)\), whose incidence graph is the Heawood graph \(H\), the equal-endpoint summands also vanish integrally, and mixed-type endpoint chains of length four do not occur. Consequently the entire group is the **integral regular representation** of the full automorphism group:
\[
 \boxed{\operatorname{MH}_{3,4}(H;\mathbb Z)\cong_{\mathbb Z[\operatorname{Aut}(H)]}\mathbb Z[\operatorname{Aut}(H)]},
 \qquad |\operatorname{Aut}(H)|=336.
\]
In particular, for every subgroup \(K\le\operatorname{Aut}(H)\), the invariant rational homology dimension is \(336/|K|\).

## Assumptions and scope
A projective plane of order \(q\) has \(q^2+q+1\) points and equally many lines; distinct points determine one line and distinct lines meet at one point. The graph vertices are points and lines, with an edge exactly when incident. Magnitude chains \(\operatorname{MC}_{k,\ell}\) are free abelian on tuples of \(k+1\) vertices having distinct consecutive entries and total successive graph distance \(\ell\). The differential is the signed deletion of each internal vertex precisely when distance is additive; endpoints are never deleted. Fixing both endpoints produces a direct-summand chain complex. Parentheses in the displayed cycle represent these *ordered magnitude chains*, not unoriented simplices. Automorphisms act by applying the same graph automorphism to every position; they do not reorder tuple positions.

## Proof
**1. Integral cycles.** Each term in \(z_{P,Q;R}\) has length four. Since \(R\notin L\), the three lines \(a,L,b\) are distinct. Directly from the magnitude boundary rule,
\[
\begin{aligned}
 \partial(P,a,b,Q)&=-(P,b,Q)+(P,a,Q),\\
 \partial(P,a,P,Q)&=(P,a,Q),\\
 \partial(P,L,b,Q)&=-(P,b,Q).
\end{aligned}
\]
Thus \(\partial z_{P,Q;R}=0\) with integral coefficients.

**2. Integral elimination in the endpoint complex.** Fix distinct points \(P,Q\), and let \(L=PQ\). The length-four two-chain group has a basis consisting of \(r_S=(P,S,Q)\) for the \(q^2+q-1\) points \(S\notin\{P,Q\}\), of \(p_a=(P,a,Q)\) for the \(q\) lines \(a\ni P\), \(a\ne L\), and of \(q_b=(P,b,Q)\) for the \(q\) lines \(b\ni Q\), \(b\ne L\). In particular its rank is \(q^2+3q-1\).

Every length-four three-chain is of exactly one of the forms
\[
 A_{a,S}=(P,a,S,Q),\qquad B_{a,b}=(P,a,b,Q),\qquad C_{S,b}=(P,S,b,Q),
\]
with the incidence and distinctness conditions forced by length four. Here \(a\) ranges over lines through \(P\) and \(b\) over lines through \(Q\). For \(a\ne b\), the unique length-four four-chain \((P,a,a\cap b,b,Q)\) has a boundary containing \(B_{a,b}\) with coefficient \(+1\), and no other four-chain boundary contains that same \(B_{a,b}\). These are independent integral unit pivots. The remaining four-chains are \((P,L,S,L,Q)\) for \(S\in L\); their boundaries are \(-A_{L,P}\) at \(S=P\), \(-C_{Q,L}\) at \(S=Q\), and \(-A_{L,S}-C_{S,L}\) otherwise. They provide another \(q+1\) disjoint unit pivots. No other four-chains occur, so all relations in \(\operatorname{MC}_{3,4}/\operatorname{im}\partial_4\) have been exhausted over \(\mathbb Z\).

After these unit eliminations a free basis of the quotient is
\[
 u_a=A_{a,P}\ (a\ni P,a\ne L),\quad
 v_b=C_{Q,b}\ (b\ni Q,b\ne L),\quad
 w_S=A_{L,S}\ (S\in L\setminus\{P,Q\}),
\]
plus \(A_R=A_{PR,R}\) and \(C_R=C_{R,RQ}\) for each of the \(q^2\) points \(R\notin L\). Their induced differential to the two-chain group is
\[
 \partial u_a=p_a,\quad\partial v_b=-q_b,\quad\partial w_S=-r_S,
 \quad\partial A_R=-r_R+p_{PR},\quad\partial C_R=r_R-q_{RQ}.
\]
The columns indexed by the \(u\)'s, \(v\)'s, \(w\)'s and one \(A_R\) for every off-line \(R\) provide integral unit pivots for **every** basis element of the two-chain group; hence this differential is split surjective. Its kernel is a free lattice with basis
\[
 A_R+C_R-u_{PR}-v_{RQ}\qquad (R\notin L).
\]
The four-chain relation at \((P,PR,R,RQ,Q)\) identifies \(B_{PR,RQ}\) with \(A_R+C_R\) in the quotient, and that at \((P,L,Q,RQ,Q)\) identifies \(B_{L,RQ}\) with \(v_{RQ}\). Therefore the final basis element is exactly the image of \(z_{P,Q;R}\). This proves a complete \(\mathbb Z\)-basis, not merely ranks over fields. Duality supplies the same result for line-line endpoints.

**3. Natural symmetry.** All constructions of \(L,a,b\) use unique joins and intersections, and their ordered chain coefficients are fixed \(+1,-1,-1\). Every incidence automorphism, even one interchanging points and lines, therefore sends \(z_{P,Q;R}\) to \(z_{gP,gQ;gR}\), with the dual convention in the latter case. This proves the integral permutation-module isomorphism.

**4. Exhausting Fano endpoints.** For the Fano incidence graph, a tuple of even total length always starts and ends in the same bipartite class, so there are no mixed endpoints in length four. For a fixed equal endpoint, the ranks of \(\operatorname{MC}_{2,4}\), \(\operatorname{MC}_{3,4}\), and \(\operatorname{MC}_{4,4}\) are respectively \(6,18,15\). The fully specified finite integer matrices in the accompanying checker have \(\operatorname{rank}\partial_3=6\) with six unit Smith factors and \(\operatorname{rank}\partial_4=12\) with twelve unit Smith factors; their composition is zero. Hence the image of \(\partial_4\) is a primitive rank-twelve sublattice of the rank-twelve kernel of \(\partial_3\), so the equal-endpoint \(\operatorname{MH}_{3,4}\) vanishes over \(\mathbb Z\). The checker also independently verifies the primitive four-cycle basis for one distinct-endpoint pair. Vertex transitivity of the Fano incidence graph transfers the equal-endpoint calculation to all vertices.

The Fano plane is \(\operatorname{PG}(2,2)\), so an ordered noncollinear point triple is exactly an ordered vector-space basis of \(\mathbb F_2^3\): there are \(168\) such triples, and \(\operatorname{GL}_3(\mathbb F_2)\) acts simply transitively on them. The same holds for ordered nonconcurrent line triples. Point–line polarity exchanges these two \(168\)-element sets. Every graph automorphism either preserves or exchanges the bipartition, and a color-preserving automorphism is uniquely determined by the images of an ordered noncollinear triple, so there are at most \(2\cdot168=336\) automorphisms. The invertible linear maps and polarity attain this bound. Thus the automorphism group of order \(336\) acts freely and transitively on all \(336\) basis labels, giving the regular integral module as asserted. In a regular permutation lattice, each subgroup \(K\) has \(336/|K|\) orbits, establishing the invariant-dimension consequence.

## Verification
Run `python3 verify_hexagon_magnitude.py` with Python 3 and SymPy. The checker constructs the fourteen-vertex Fano incidence graph from orthogonality in \(\mathbb F_2^3\), enumerates all localized length-four tuples and every signed boundary coefficient, verifies that the two consecutive boundaries compose to zero, and computes exact Smith forms. It independently confirms the primitive four-generator distinct-endpoint basis and integral vanishing at equal endpoints. Finally it enumerates all \(168\) invertible ternary-bit matrices, tests their incidence automorphisms, checks naturality of the displayed cycles and the polarity, and verifies the free-transitive action on the \(336\) basis labels. The general projective-plane assertion is proved by the integral elimination above; the finite checker is required only for the Fano equal-endpoint assertion and corroborative consistency tests.

## Relationship to prior work
Asao, Hiraoka and Kanazawa proved a girth-dependent near-diagonal vanishing theorem. Its girth-seven hypothesis for the first off-diagonal does not apply to the incidence graph of a projective plane, which has girth six. Existing exact calculations for these incidence graphs determined the fieldwise dimension \(q^2\) for each ordered distinct same-type pair, and the overall Heawood mod-two dimension \(336\). Those dimensions are explicitly **not** claimed as new. The result here strengthens the endpoint calculation to a canonical integral basis, identifies the natural representation for all incidence symmetries, and gives the *complete* integral Heawood group including all equal-endpoint summands. A search for stronger results under the aliases magnitude-chain hexagon bases, Fano incidence homology, and integral automorphism modules did not identify a covering statement. This does not establish absolute bibliographic uniqueness.

## Limitations
For a general finite plane, this theorem describes the direct sum over distinct same-type endpoints; it does not determine equal-endpoint summands outside the Fano case, nor other bidegrees. It makes no claim about integral representations for larger projective planes on their equal-endpoint summands. The Fano equal-endpoint statement uses a finite exact-computation proof with a fully executable checker, not a uniform closed-form calculation. The irreducible decomposition of the Fano regular representation is not separately tabulated because its integral lattice, not a rational character table, is the asserted structure. Unindexed equivalent presentations remain a residual priority risk.

## References
1. Y. Asao, Y. Hiraoka and S. Kanazawa, “Girth, magnitude homology, and phase transition of diagonality,” arXiv:2101.09044v1 (public January 22, 2021), especially Corollary 1.4 and the definition of magnitude chains.
2. “Endpoint-localized first off-diagonal magnitude homology of finite projective planes,” public mathematical research note (2026): previously known fieldwise local dimension \(q^2\) for each distinct same-type endpoint pair.
3. “The first off-diagonal magnitude homology of the Heawood graph has mod-2 rank 336,” public mathematical research note (2026): previously known finite mod-two total dimension.
