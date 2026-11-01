# Parity-switched geometric fixed spaces of hexagonal-chain independence complexes

## Finding

For every integer \(n\geq1\), let \(G_n\) be the graph with vertices \((r,i)\), where \(r\in\{0,1\}\) and \(1\leq i\leq2n+1\), horizontal edges \((r,i)(r,i+1)\) for \(i<2n+1\), and rungs \((0,i)(1,i)\) exactly when \(i\) is odd. This is the linear chain of \(n\) hexagons. Write \(X_n=\operatorname{Ind}(G_n)\). Let \(h(r,i)=(1-r,i)\) exchange the rows, and \(v(r,i)=(r,2n+2-i)\) reverse the columns. The two involutions commute; write \(w=hv\) and \(V_4=\langle h,v\rangle\).

The **actual geometric fixed-point spaces**, not the fixed subspaces of homology, satisfy the following complete classification:

\[
\begin{array}{c|cc}
 &n=2m\ (m\geq1)&n=2m+1\ (m\geq0)\\\hline
|X_n|^{\langle v\rangle}& S^m\vee S^m&\mathrm{contractible}\\
|X_n|^{\langle w\rangle}&\mathrm{contractible}&S^m\vee S^m.
\end{array}
\]

The symbols in the table specify homotopy types. The other fixed spaces admit the stronger canonical piecewise-linear identifications
\[
|X_n|^{\langle h\rangle}\cong_{\mathrm{PL}}\Delta^{n-1},\qquad
|X_n|^{V_4}\cong_{\mathrm{PL}}\Delta^{\lceil n/2\rceil-1}.
\]
Thus precisely one of the two non-row-exchange involutions has a wedge of two fixed-point spheres, with dimension growing with the chain length, while the other has a collapsible fixed-point complex. For \(n=1\), the expression \(S^0\vee S^0\) means three discrete points.

## Assumptions and scope

All complexes are finite abstract simplicial complexes, and \(|X|^H\) denotes the pointwise \(H\)-fixed subset of their geometric realization. The action on \(X_n\) is induced by the displayed graph automorphisms. The empty face is included in the combinatorial independence complex; its geometric realization contributes no extra point. All stated dimensions, subgroup types and parity cases hold for **every** integer \(n\geq1\), including the smallest cases. The symbol \(\cong_{\mathrm{PL}}\) denotes a piecewise-linear homeomorphism with the indicated natural orbit-barycenter triangulation, not a claim that the original simplicial complex contains a pointwise-fixed simplicial subcomplex with the same vertices.

For a positive integer \(s\), define \(L_s\) as the two-row graph on \((r,i)\) with \(1\leq i\leq s\), consecutive horizontal edges, and rungs at odd columns. Thus \(G_n=L_{2n+1}\). If \(s=2m+1\), the graph \(L_s\) is precisely \(G_m\) (when \(m\geq1\)).

## Proof

**1. Geometric orbit lemma.** For any finite graph \(G\) and finite group \(H\) acting by graph automorphisms, form a graph \(Q_H(G)\). Its vertices are those \(H\)-orbits \(O\subseteq V(G)\) that are independent in \(G\); two distinct such orbits are adjacent if at least one graph edge joins a vertex of one orbit to a vertex of the other. Then
\[
|\operatorname{Ind}(G)|^H\cong_{\mathrm{PL}}|\operatorname{Ind}(Q_H(G))|.
\]
Indeed, a geometric point has barycentric vertex weights constant on each \(H\)-orbit precisely when it is \(H\)-fixed. Orbits of positive weight must be internally independent and pairwise nonadjacent. The orbit barycenters therefore span exactly the claimed independence simplices. This piecewise-affine map is bijective, and its inverse rescales barycentric coefficients within each orbit. Finiteness makes it a PL homeomorphism.

**2. Half-chain descriptions for end reversal and the half-turn.** Under \(v\), every noncentral orbit is the reflected pair within a single row and has a unique representative at a column \(i\leq n\); the central vertices lie at column \(n+1\). These orbits are always internally independent. The only conflicting pairs arise from horizontal neighbors or the rungs at odd columns. Therefore
\[
|X_n|^{\langle v\rangle}\cong_{\mathrm{PL}}|\operatorname{Ind}(L_{n+1})|.
\]

Under \(w\), the noncentral orbits are cross-row pairs, indexed by the two rows and columns \(1\leq i\leq n\). The same horizontal and odd-rung conflicts yield \(L_n\). The central cross-row pair at column \(n+1\) is internally incompatible if \(n\) is even (the central column has a rung), and is a new admissible orbit if \(n\) is odd. In the latter case it conflicts with **both endpoints of the terminal rung**, and with no other orbit. Let \(T_m\) denote \(G_m=L_{2m+1}\) with a single extra vertex adjacent to both vertices of its final rung, so the final rung and the extra vertex form a triangle. Then
\[
|X_n|^{\langle w\rangle}\cong_{\mathrm{PL}}
\begin{cases}
|\operatorname{Ind}(L_n)|,&n\ \text{even},\\
|\operatorname{Ind}(T_m)|,&n=2m+1.
\end{cases}
\]
Here \(T_0\) is the three-vertex complete graph.

**3. Even half-chains collapse.** For every \(m\geq1\), \(\operatorname{Ind}(L_{2m})\) is simplicially collapsible. Let \(a,b\) be the two vertices at column \(2m-1\), and let \(x,y\) be those at column \(2m\), with \(a-x\), \(b-y\) and \(a-b\) edges. The open neighborhood of \(x\) is \(\{a\}\), contained in the open neighborhood of \(b\). The standard independence-complex fold pairs every independent face containing \(b\) but not \(x\) with its union with \(x\), ordered from larger to smaller faces. This collapses \(\operatorname{Ind}(L_{2m})\) onto \(\operatorname{Ind}(L_{2m}\setminus\{b\})\). The remaining vertex \(y\) is isolated, so the remaining independence complex is a cone and itself collapsible.

**4. Triangle-terminated half-chains.** If \(m\geq1\), let \(z\) be the extra vertex of \(T_m\) attached to the final rung \(\{a,b\}\). Its link in \(\operatorname{Ind}(T_m)\) is
\[
\operatorname{link}(z)=\operatorname{Ind}(G_m\setminus\{a,b\})
=\operatorname{Ind}(L_{2m}).
\]
The last complex is collapsible by Step 3. Consequently the cone \(z*\operatorname{link}(z)\), attached along its collapsible base, collapses relatively onto the base, yielding a simplicial collapse
\[
\operatorname{Ind}(T_m)\searrow\operatorname{Ind}(G_m).
\]
For \(m=0\), \(T_0=K_3\), whose independence complex is three isolated vertices, homotopy equivalent to \(S^0\vee S^0\).

**5. The known ordinary hex-chain homotopy theorem.** Chandrakar and Singh, *Independence Complexes of Hexagonal Grid Graphs* (arXiv:2512.21318v1, Theorem 3.1), proved
\[
\operatorname{Ind}(G_m)\simeq S^m\vee S^m\qquad(m\geq1).
\]
If \(n=2m\), Step 2 gives \(v\)-fixed type \(\operatorname{Ind}(G_m)\), while the \(w\)-fixed type is \(\operatorname{Ind}(L_{2m})\), collapsible by Step 3. If \(n=2m+1\), the \(v\)-fixed type is \(\operatorname{Ind}(L_{2m+2})\), collapsible by Step 3, while Step 4 identifies the \(w\)-fixed type with \(\operatorname{Ind}(G_m)\) for \(m\geq1\), or with three points for \(m=0\). This proves the two-parity classification.

**6. Row exchange and the whole group.** For \(h\), the two vertices in an odd column form an inadmissible orbit (they are joined by a rung), whereas the two vertices in an even column form an independent orbit. Orbits from different even columns are mutually nonadjacent. There are exactly \(n\) of them, so their fixed-point complex is the full simplex \(\Delta^{n-1}\). The remaining reflection \(v\) permutes these \(n\) orbit barycenters by reversing their column order. Requiring invariance under both involutions leaves the simplex on the \(\lceil n/2\rceil\) resulting vertex-orbits. The orbit-barycenter construction proves the two claimed PL identifications.

## Verification

The accompanying standalone Python program `verify_hex_fixed.py` reconstructs the original graphs and each subgroup action without using the displayed quotient formulas as input. For every \(1\leq n\leq12\), it checks that the graph involutions preserve the edge set and that all four independently enumerated orbit-compatibility graphs agree with the proposed models (48 group-and-size cases). For every \(1\leq n\leq7\), it computes their full reduced-independent face lists and mod-two simplicial boundary ranks, independently confirming the prescribed Betti numbers in all four cases. Run with `python3 verify_hex_fixed.py` (Python standard library only).

These finite computations are consistency checks. The all-parameter proof uses the exact orbit enumeration, graph fold and relative cone collapse, together with the cited published ordinary homotopy theorem; it does **not** extrapolate an infinite conclusion from enumerated finite cases.

## Relationship to prior work

The 2025 paper by Chandrakar and Singh gives the ordinary homotopy type \(\operatorname{Ind}(G_m)\simeq S^m\vee S^m\) but does not formulate the geometric fixed-point spaces of the two reflection axes or their product. A subsequent published calculation of the integral reflection characters of hexagonal-chain top homology determines traces of the commuting symmetries, and already notes the row-swap fixed simplex. Such character information determines equivariant Euler characteristics but **not** the full geometric fixed-space homotopy types. The new contribution here is the simultaneous orbit-graph identification and parity-switched homotopy classification for both remaining nonidentity involutions, including collapsible/spherical distinctions and the whole-subgroup fixed diagram. The previously established ordinary wedge and the already-known row-swap simplex are used openly as inputs, not claimed as independently new.

## Limitations

The result concerns the ordinary independence complexes of linear single-width hexagon chains and the displayed Klein-four automorphism subgroup; it does not classify arbitrary planar hexagonal regions, higher-independence parameters, or equivariant stable homotopy. The fixed sphere identifications are homotopy equivalences, not assertions of PL sphere-wedge models. No independent mathematical audit has been performed. A mathematically equivalent, unindexed treatment of this subgroup fixed-space diagram cannot be categorically excluded.

## References

1. H. Chandrakar and A. Singh, *Independence Complexes of Hexagonal Grid Graphs*, arXiv:2512.21318v1 (first public preprint 2025-12-24), especially Section 2.2, Lemma 2.3 and Theorem 3.1.
2. *Reflection characters of linear hexagonal-chain independence complexes* (published 2026 research result): comparison source for the previously calculated integral top-homology action, not for the geometric fixed-point theorem proved here.
