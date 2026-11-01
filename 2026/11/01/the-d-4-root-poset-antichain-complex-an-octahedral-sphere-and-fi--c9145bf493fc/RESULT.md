# The \(D_4\) root-poset antichain complex: an octahedral sphere and five circles

## Finding
Let \(\Delta(D_4)\) be the simplicial complex of antichains in the positive-root poset of type \(D_4\). Its geometric realization has exactly three connected components and the integral homotopy type
\[
|\Delta(D_4)|\simeq
\left(S^2\vee\bigvee^5 S^1\right)\sqcup\{\mathrm{pt}\}\sqcup\{\mathrm{pt}\}.
\]
In fact, five elementary simplicial collapses expose a literal octahedral two-sphere with eight additional graph edges attached using three additional vertices, as well as two isolated vertices. In particular, the nontrivial component has fundamental group the free group \(F_5\), and its integral homology is free; the two other components are points.

## Assumptions and scope
Use \(\Phi^+(D_4)=\{e_i-e_j,e_i+e_j:1\le i<j\le4\}\) and the simple roots
\[
\alpha_1=e_1-e_2,\quad\alpha_2=e_2-e_3,\quad
\alpha_3=e_3-e_4,\quad\alpha_4=e_3+e_4.
\]
For positive roots \(\rho,\sigma\), set \(\rho\le\sigma\) precisely when \(\sigma-\rho\) is a nonnegative integral linear combination of the four simple roots. A face of \(\Delta(D_4)\) is a set of mutually incomparable positive roots. All homotopy claims use ordinary geometric realizations and all homology claims use integral coefficients. There is no assertion for \(D_n\) at other ranks.

For readable facet notation, name the twelve positive roots as follows:
\[
\begin{aligned}
p&=e_1-e_2,&q&=e_1-e_3,&r&=e_1-e_4,&s&=e_1+e_4,\\
t&=e_2-e_3,&u&=e_2+e_3,&a&=e_2-e_4,&b&=e_2+e_4,\\
c&=e_3-e_4,&d&=e_3+e_4,&x&=e_1+e_2,&y&=e_1+e_3.
\end{aligned}
\]

## Proof
**Exact facet enumeration.** Writing each root in simple-root coordinates and comparing the resulting four-component nonnegative integer vectors gives exactly the following maximal faces:

* Two vertices: \(\{x\},\{y\}\).
* Six edges: \(\{p,u\},\{q,u\},\{r,b\},\{r,d\},\{s,a\},\{s,c\}\).
* Eight triangles: \(\{p,a,b\},\{p,a,d\},\{p,b,c\},\{q,a,b\},\{q,a,d\},\{q,b,c\},\{q,c,d\},\{r,s,u\}\).
* One tetrahedron: \(\{p,t,c,d\}\).

The entire complex comprises these faces and their subsets, with face numbers \((f_0,f_1,f_2,f_3)=(12,24,12,1)\). The standalone verifier independently reconstructs simple-root coordinates by exact rational linear algebra and confirms the maximal-face list.

**Five elementary collapses.** In the indicated order, remove each free face on the left together with its unique containing coface on the right:
\[
\begin{array}{rcl}
\{p,t,c\}&\subset&\{p,t,c,d\},\\
\{p,t\}&\subset&\{p,t,d\},\\
\{r,s\}&\subset&\{r,s,u\},\\
\{t,c\}&\subset&\{t,c,d\},\\
\{t\}&\subset&\{t,d\}.
\end{array}
\]
The facet list shows, at each step, that the left face occurs in precisely one remaining maximal coface (of dimension one larger); hence these are elementary simplicial collapses and preserve simple-homotopy type.

**Octahedral core and graph.** After the collapses, the eight remaining triangles are
\[
\{z,v,w\}\qquad
(z\in\{p,q\},\;\{v,w\}\in
\{\{a,b\},\{b,c\},\{c,d\},\{d,a\}\}).
\]
They form the simplicial suspension of the square \(a-b-c-d-a\), namely the boundary of an octahedron, a two-sphere \(S\). There are exactly eight edges not belonging to \(S\):
\[
\{p,u\},\{q,u\},\{r,u\},\{r,b\},\{r,d\},
\{s,u\},\{s,a\},\{s,c\}.
\]
They introduce only the three new vertices \(r,s,u\). The isolated vertices are \(x,y\).

**Homotopy splitting.** Inside \(S\), choose the five-edge spanning tree
\(\{a,b\},\{b,c\},\{c,d\},\{p,a\},\{q,a\}\). Extend it by \(\{p,u\},\{u,r\},\{u,s\}\); this is a tree on all nine vertices of the nontrivial component. Collapsing this contractible CW subcomplex to a point is a homotopy equivalence. The quotient of \(S\) by its five-edge subtree is still homotopy equivalent to \(S^2\). Precisely five of the eight extra edges are not in the tree; all become loops at the collapsed point and occur in no two-cell boundary. Thus the quotient is \(S^2\vee\bigvee^5 S^1\). Restoring the two isolated vertices proves the result.

## Verification
Run `python verify_d4.py` using Python 3 and only its standard library. It independently solves for all twelve root coefficient vectors, constructs all antichains, checks the full seventeen-facet list, validates every unique free coface in the five collapse pairs, and checks the exact octahedral-triangle and eight-edge residue. It verifies the spanning tree and five leftover loops. Independent mod-two boundary calculations return ranks \((9,10,1)\) for \((\partial_1,\partial_2,\partial_3)\), giving reduced Betti numbers \((2,5,1)\) in degrees \((0,1,2)\), consistent with the geometric proof. The mod-two calculation is a check, **not** a substitute for the integral homotopy argument.

## Relationship to prior work
Mu and Welker (2026, arXiv:2609.14054v1, Section 5, Figure 6) introduced this antichain-complex viewpoint, proved that \(\Delta(D_n)\) is nonshellable for every \(n\ge4\), and tabulated the integral homology groups of \(\Delta(D_4)\) as \(\widetilde H_0\cong\mathbb Z^2\), \(\widetilde H_1\cong\mathbb Z^5\), and \(\widetilde H_2\cong\mathbb Z\). Those numerical groups agree with the present result but do not by themselves determine the fundamental group or homotopy type. The additional statement here is the explicit five-collapse octahedral-core model and resulting complete homotopy classification at the first nonshellable type-\(D\) rank. Shellability-to-wedge theorems do not apply because nonshellability was proved for this complex.

## Limitations
The theorem concerns the canonical rank-four root poset only. It does not assert an analogous splitting for higher-rank \(D_n\), or any equivariant action or canonical generator basis. This analysis is a direct finite combinatorial proof; independent mathematical review has not been performed. As always, an undiscovered equivalent classification under another name remains an originality risk.

## References
1. L. Mu and V. Welker, *Simplicial Complexes of Antichains in Root Posets and Related Combinatorics of Dyck Paths*, arXiv:2609.14054v1 (first posted 12 September 2026), especially Section 5 and Figures 5–6. https://arxiv.org/abs/2609.14054
2. M. L. Wachs, *Poset Topology: Tools and Applications*, survey notes, especially Theorem 3.1.3 on the homotopy consequence of shellability (background, not used to infer this nonshellable case). https://users.math.msu.edu/users/magyarp/math880/Wachs-Poset-Topology.pdf
