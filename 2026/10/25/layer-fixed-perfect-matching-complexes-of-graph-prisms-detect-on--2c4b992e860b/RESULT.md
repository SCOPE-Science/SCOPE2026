# Layer-fixed perfect-matching complexes of graph prisms detect one-factors

## Finding

For every finite simple graph \(H\) on \(n\ge1\) vertices, let \(P=H\square K_2\), and let \(s\) exchange the two layers of \(P\). Write \(\operatorname{PMC}(P)\) for the simplicial complex whose facets are the edge-sets of perfect matchings of \(P\). Let \(W(H)\) be the **fully whiskered graph**, obtained from \(H\) by adjoining one new pendant vertex to each original vertex, and let \(\mathcal M(W(H))\) be its ordinary matching complex. There is a canonical PL homeomorphism

\[
 |\operatorname{PMC}(P)|^s\ \cong_{\mathrm{PL}}\ |\mathcal M(W(H))|.
\]

Here the left-hand side denotes fixed **points of the geometric realization**, rather than the smaller simplicial complex consisting only of individually fixed edges. Denote by \(p(H)\) the number of perfect matchings (one-factors) of \(H\). Then

\[
 |\operatorname{PMC}(P)|^s\simeq
 \begin{cases}
 \mathrm{point},&p(H)=0,\\
 \displaystyle\bigvee^{p(H)}S^{r-1},&n=2r\ \text{and}\ p(H)>0.
 \end{cases}
\]

The homotopy equivalences are integral. When \(r=1\), the wedge of zero-spheres means precisely a discrete space of \(p(H)+1\) points. The layer-exchange involution has reduced Lefschetz trace

\[
 \sum_{j\ge0}(-1)^j\operatorname{tr}\bigl(s_*\mid\widetilde H_j(\operatorname{PMC}(P);\mathbb Q)\bigr)
 =\begin{cases}
 0,&p(H)=0,\\
 (-1)^{r-1}p(H),&n=2r\ \text{and}\ p(H)>0.
 \end{cases}
\]

In particular, for the circular ladder \(C_n\square K_2\) with \(n\ge3\), the fixed locus is contractible for odd \(n\) and has homotopy type \(S^{n/2-1}\vee S^{n/2-1}\) for even \(n\), since an even cycle has exactly two one-factors.

## Assumptions and scope

Graphs are finite, simple, undirected, and not necessarily connected. There is at least one vertex in \(H\); isolated vertices are allowed. The Cartesian prism \(H\square K_2\) has vertices \((v,\epsilon)\), for \(v\in V(H)\) and \(\epsilon\in\{0,1\}\). Its edges are **rungs** \(\{(v,0),(v,1)\}\) and **horizontal edges** \(\{(u,\epsilon),(v,\epsilon)\}\) with \(\{u,v\}\in E(H)\). All rungs together form a perfect matching, so \(\operatorname{PMC}(P)\) is always nonempty and is defined without any further hypothesis. Perfect matching complexes here include all subsets of facets, whereas ordinary matching complexes include every edge matching, with or without extension to a one-factor.

The involution \(s(v,\epsilon)=(v,1-\epsilon)\) acts simplicially by permuting the prism's edges. The fixed-point notation refers to the resulting continuous involution of the geometric realization.

## Proof

**1. Exact fixed-face model.** The edge-orbits of \(s\) consist of fixed rungs \(\rho_v\), indexed by \(v\in V(H)\), and two-element horizontal orbits \(\eta_{uv}=\{h_{uv,0},h_{uv,1}\}\), indexed by \(\{u,v\}\in E(H)\). A simplex fixed setwise by \(s\) is a union of complete edge-orbits. Choose a set \(T\subseteq E(H)\) of horizontal orbits and a set \(R\subseteq V(H)\) of rung orbits. Their union is an edge-matching precisely if \(T\) is a matching of \(H\) and \(R\cap V(T)=\varnothing\): two horizontal orbits with a common base endpoint collide in both layers, and a rung collides with a horizontal pair precisely at its base endpoint. Under these conditions, all remaining uncovered prism vertices are covered by adding the rungs at \(V(H)\setminus(V(T)\cup R)\). Consequently **every** such union of orbits is extendable to a perfect matching of the prism. Conversely no other invariant simplex is possible.

In \(W(H)\), ordinary matching faces comprise exactly the same pairs \((T,R)\): choose base matching edges \(T\), and independently choose pendant edges \(\{v,v'\}\) for any subset \(R\) of vertices not incident to \(T\). Therefore the invariant face-orbit complex is simplicially **isomorphic** to \(\mathcal M(W(H))\).

Any point fixed by \(s\) in a geometric simplex has equal barycentric weights at the two horizontal edges of each chosen horizontal orbit; fixed rung vertices have arbitrary weights. The intersection of the simplex with the fixed-point locus is consequently the simplex on its fixed rung vertices and the **midpoints** of its horizontal two-orbits. These subdivisions agree on intersections of original simplices. Sending a base-edge vertex of \(\mathcal M(W(H))\) to the midpoint of its horizontal orbit, and each pendant-edge vertex to its rung vertex, gives the asserted PL homeomorphism. In particular, the geometric fixed locus must not be confused with the subcomplex spanned only by fixed rung vertices.

**2. Complete acyclic matching.** Order the vertices of \(H\). Represent every face of \(\mathcal M(W(H))\) by \((T,R)\) as above. Whenever \(V(H)\setminus V(T)\ne\varnothing\), let \(v\) be the least vertex not incident to the base matching \(T\), and pair \((T,R\setminus\{v\})\) with \((T,R\cup\{v\})\). This pairing is well defined regardless of the membership of \(v\), and it pairs **all** faces in each fixed-\(T\) fiber with a free original vertex. The unpaired faces occur exactly when \(V(T)=V(H)\). Such \(T\) is a perfect matching of \(H\), and \(R=\varnothing\). Thus there are precisely \(p(H)\) unpaired faces, each of dimension \(r-1\) when \(n=2r\). There are none when \(H\) has no one-factor.

Acyclicity holds in the augmented Hasse diagram, oriented upwards on matched covers and downwards on all unmatched covers. Along each upward matched arrow, \(T\) is unchanged; along an unmatched downward arrow, \(T\) is unchanged or strictly loses an edge. Therefore \(T\) is nonincreasing along every directed path, and every directed cycle must be contained in a single fixed-\(T\) fiber. In that fiber the chosen pendant edge at \(v\) is only **added** by a matched upward arrow, never deleted by an unmatched downward arrow. Every nonempty directed cycle would require such an addition and its reversal, impossible. Hence the matching is acyclic.

The augmented matching pairs the empty simplex with one pendant-edge vertex. In ordinary (nonaugmented) simplicial Morse theory, retain that pendant-edge vertex as a single critical zero-cell. Together with the \(p(H)\) remaining critical \((r-1)\)-cells, this yields a CW model with exactly one zero-cell and exactly \(p(H)\) additional cells, all of the same dimension. If \(r\ge2\), each attaching map into the zero-skeleton is constant, and the CW complex is \(\bigvee^{p(H)}S^{r-1}\). If \(r=1\), there are \(p(H)+1\) zero-cells. If \(p(H)=0\), the Morse model has only one vertex, so it is contractible. Every assertion is over integral topology, not inferred from numerical field ranks.

**3. Reduced Lefschetz number.** For any finite simplicial automorphism, the Lefschetz fixed-point formula on a barycentrically subdivided equivariant complex identifies its ordinary Lefschetz number with the Euler characteristic of its geometric fixed-point locus. Subtracting the degree-zero contribution of an invariant constant function gives the reduced Lefschetz number equal to the reduced Euler characteristic of that locus. The wedge model therefore yields exactly \(0\) when \(p(H)=0\), and \((-1)^{r-1}p(H)\) otherwise.

## Verification

The standalone `verify.py` enumerates perfect-matchings facets of the prism **independently** of the orbit model, enumerates all invariant simplicial faces, and compares the resulting orbit-faces to every ordinary matching face of the fully whiskered graph. It checks all labeled simple graphs on one through five vertices and four larger representatives (two six-vertex cycle/complete/bipartite cases and one seven-vertex cycle): **1,103 graphs** in total. For all graphs with at most four vertices and the four larger cases, it independently topologically sorts the entire directed matched Hasse graph to certify acyclicity: **79 acyclicity certificates**. All examples also verify the exact reduced Euler characteristic from the one-factor count. Execute with `python3 verify.py` in an ordinary Python 3 environment; no additional packages or input files are needed. Finite verification corroborates but is **not** the proof for all graphs; that proof is the explicit face identification, acyclic matching and fixed-point argument above.

## Relationship to prior work

Agarwal and Basak's 2026 study of Möbius and circular ladder independence and perfect-matching complexes gives their **nonequivariant** homotopy types and motivates an equivariant invariant. Its circular-ladder classification does not determine the geometric fixed-point topology or the layer-swap trace, and it does not concern prisms of arbitrary base graphs. Chandrakar and Singh analyze polygonal line tilings and open ladders, not the present layer involution. Bayer, Jelić Milutinović and Vega prove a sphere-wedge theorem for ordinary matching complexes of outerplanar graphs; that statement supplies neither the one-factor multiplicity nor a fixed-point realization of a prism PMC, and full whiskerings need not be outerplanar. The PL orbit-face identification and the exact all-base-graph one-factor enumeration are distinct from a known Betti-number calculation on intact ladder complexes.

## Limitations

No claim is made about the homotopy type of the **whole** perfect-matching complex \(\operatorname{PMC}(H\square K_2)\), the entire graded representation of the involution, or homotopy type of its orbit quotient. The alternating reduced rational trace is determined, not separate traces in every homological degree. The PL homeomorphism is a statement about fixed geometric points and not the set of simplicial vertices individually fixed. No independent external validation is asserted. The originality comparison is constrained by accessible indexed literature; potentially unindexed equivalent treatments of fully whiskered matching complexes or prism involutions remain a risk.

## References

1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (2026); first public version arXiv:2608.30601v1, 2026-08-31. https://arxiv.org/html/2608.30601v2
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v2 (2025). https://arxiv.org/html/2407.05809v2
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2 (2026). https://arxiv.org/html/2411.04601v2
