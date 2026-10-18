# Sharp simple-connectivity threshold for strong Morse matching complexes of cycles

## Finding
Let \(C_n\) be the one-dimensional simplicial cycle with vertices \(v_0,\ldots,v_{n-1}\), indexed cyclically, for each integer \(n\ge3\). Let \(X_n=\mathcal{SM}(C_n)\) be the **full strong discrete Morse matching complex** of Knudson and Owens–White: its simplices are the nonempty subsets of vertex–edge pairs occurring in at least one strong gradient arising from an injective ordering of the cycle's vertices.

**Theorem (sharp simple-connectivity threshold).** For every integer \(n\ge6\), the geometric realization \(|X_n|\) is path connected and simply connected:
\[
\pi_1(|\mathcal{SM}(C_n)|)=1.
\]
The bound is sharp: \(\mathcal{SM}(C_5)\simeq S^1\), whereas \(\mathcal{SM}(C_4)\simeq\bigvee^5S^1\) and \(\mathcal{SM}(C_3)\simeq\bigvee^5S^0\), by the earlier classification in [1, Proposition 8.5].

More precisely, for every \(n\ge7\), the entire two-skeleton of \(X_n\) is the two-skeleton of the independence complex of an explicit bipartite graph \(H_n\) on \(2n\) vertices. At \(n=6\), the two-skeleton differs only by four explicitly listed monochromatic triangles, none of which affects the fundamental group. This two-skeleton model, not any conjectured complete homotopy classification, proves the theorem.

## Assumptions and scope
The cycle \(C_n\) is a one-dimensional simplicial complex, not a filled polygon. Its edges are \(e_i=\{v_i,v_{i+1}\}\), with indices in \(\mathbb Z/n\mathbb Z\). The matching vertices are \(R_i=(v_{i+1},e_i)\) and \(L_i=(v_i,e_i)\); these are **incidences**, not vertices of the original cycle. A strong gradient uses a vertex order and pairs a newly inserted vertex with its one earlier incident neighbor precisely when it has exactly one earlier neighbor. The full strong matching complex is the downward simplicial closure of such gradients, and should not be confused with either the pure strong complex or the ordinary (Forman) discrete-Morse complex.

The theorem only concerns ordinary (nonequivariant) \(\pi_1\). It does not assert a sphere-wedge homotopy type, higher connectivity, vanishing of higher homology, or torsion-freeness in all dimensions.

## Proof
**Step 1. An exact constraint description for faces with at most three incidences.** Fix any injective vertex order, written as heights \(h_i\). The incidence \(R_i\) is selected by its strong gradient precisely if
\[
h_i<h_{i+1}<h_{i+2},
\]
whereas \(L_i\) is selected precisely if
\[
h_{i+1}<h_i<h_{i-1}.
\]
In the first case the two directed cycle edges \(e_i,e_{i+1}\) must point clockwise in the order; in the second case \(e_{i-1},e_i\) must point counterclockwise.

A set of prescribed incidences therefore gives consistent local inequalities exactly when it contains no \(R_i,L_j\) with
\[
j-i\pmod n\in\{0,1,2\}.
\]
Any such consistent partial orientation of the cycle can be extended to a strict vertex order unless it already forces **every** edge of the cycle to point in the same direction. This is because the only directed cycles in an oriented simple cycle traverse all its edges coherently. If the forced partial orientation is not a directed cycle, orient each remaining edge so that no directed cycle is created, then take a topological ordering. The resulting strong gradient contains every prescribed incidence. This proves an exact criterion for membership of a face, not merely a necessary test.

Define \(H_n\) as the bipartite graph with vertex classes \(\{R_i\}\) and \(\{L_j\}\) and edges \(R_iL_j\) precisely when \(j-i\pmod n\in\{0,1,2\}\). Each incidence forces the directions of only two cycle edges. Thus, if \(n\ge7\), no collection of at most three mutually compatible incidences can force a coherent orientation of all \(n\) edges. We obtain the exact equality
\[
X_n^{(2)}=\operatorname{Ind}(H_n)^{(2)}\qquad(n\ge7).
\]
When \(n=6\), the only compatible triples that force a directed cycle are the two alternating all-clockwise triples and the two alternating all-counterclockwise triples:
\[
\{R_0,R_2,R_4\},\ \{R_1,R_3,R_5\},\
\{L_0,L_2,L_4\},\ \{L_1,L_3,L_5\}.
\]
All compatible mixed triples are still present. Every same-color pair is present, for all \(n\ge6\).

**Step 2. Each of the two monochromatic subcomplexes is simply connected.** Let \(A_n\subseteq X_n\) be the induced subcomplex on all \(R_i\), and let \(B_n\subseteq X_n\) be its counterpart on all \(L_i\). For \(n\ge7\), each contains the full two-skeleton of the \((n-1)\)-simplex. In particular, its one-skeleton is complete, and every three-edge loop bounds a two-simplex; therefore \(\pi_1(A_n)=\pi_1(B_n)=1\).

For \(n=6\), the monochromatic one-skeleta remain complete; only two triangles are missing from each color's complete two-skeleton. The missing triangles are disjoint. For each missing triangle \(\{a,b,c\}\), choose any vertex \(z\) in the other missing triangle of **the same color**. All three triangles \(\{z,a,b\}\), \(\{z,b,c\}\), and \(\{z,c,a\}\) are present, and their union fills the three-edge boundary \(a-b-c-a\). Hence every triangular loop is null-homotopic. A loop in a complete graph is generated by triangular loops, proving \(\pi_1(A_6)=\pi_1(B_6)=1\). Both monochromatic subcomplexes are path connected for all \(n\ge6\).

**Step 3. The mixed-edge incidence graph is connected.** Define a bipartite graph \(D_n\) on the same two classes by taking the allowed cross edges of \(X_n\):
\[
R_iL_j\in E(D_n)\iff j-i\pmod n\notin\{0,1,2\}.
\]
Every \(L_j\) has \(n-3>0\) neighbors. Consecutive \(R_i,R_{i+1}\) have a common \(L\)-neighbor because their forbidden \(L\)-indices together occupy only four of the \(n\ge6\) positions. Thus all \(R\)-vertices, and consequently all \(L\)-vertices, lie in one component of \(D_n\).

Whenever two edges of \(D_n\) share one endpoint, their other endpoints lie in a common monochromatic simplex edge. Their three vertices span a **mixed two-simplex** of \(X_n\), by Step 1. This remains true in the exceptional case \(n=6\), whose four deleted triangles are monochromatic.

**Step 4. A van Kampen reduction.** Fundamental groups depend only on the two-skeleton. Collapse each of the two path-connected, simply connected monochromatic subcomplexes to a point at the level of \(\pi_1\), using van Kampen. The remaining one-skeleton has two vertices joined by one edge for every edge of \(D_n\). Every mixed triangle from Step 3 identifies two of these parallel edges up to homotopy relative to their endpoints. Since the edge-adjacency graph of a connected graph is connected, all cross edges are identified to a single relative homotopy class. The resulting fundamental group is that of a single interval, hence trivial. This gives \(\pi_1(X_n)=1\) for all \(n\ge6\), as claimed.

**Step 5. Sharpness.** The earlier explicitly computed homotopy equivalence \(\mathcal{SM}(C_5)\simeq S^1\) in [1, Proposition 8.5] shows that the threshold cannot be reduced to five. Its computations for four and three edges similarly show the smaller-cycle behavior stated in the theorem.

## Verification
The standalone Python program `check_cycle.py` independently reconstructs all strong gradients from all vertex permutations for \(4\le n\le8\), constructs the corresponding one-, two-, and three-vertex faces, and compares these **exact** enumerations with the forced-orientation criterion. It checks the connectedness and exact edge counts of \(D_n\), and independently computes mod-two first homology ranks from the triangle-to-edge boundary matrix. The recorded output (`check_cycle.stdout`) reports exact agreement for all five sizes; the first mod-two Betti numbers for \(n=4,5,6,7,8\) are respectively \(5,1,0,0,0\). These finite checks are cross-checks only: the uniform simple-connectivity theorem is proved by Steps 1–4, not inferred from tests.

Reproduce by running `python3 check_cycle.py` in the directory containing the embedded files. Python 3 standard library suffices.

## Relationship to prior work
Knudson and Owens–White [1] introduce the full strong-Morse matching complexes and determine the homotopy type of their **pure** cycle subcomplexes. They tabulate homology of the full complexes through \(n=21\), and in Proposition 8.5 establish the small cases used for sharpness. Integral homology calculations, whether in finite tables or closed all-length formulas, do not imply this fundamental-group theorem: even vanishing first integral homology only makes the fundamental group perfect, not necessarily trivial. The pure complexes need not share the full complex's homotopy type.

The previously published face-enumeration result [2] gives an exact three-symbol criterion, face polynomials and periodic Euler characteristics for the full cycle complexes; its stated scope explicitly does not determine connectivity or individual homology. Its local compatibility criterion is mathematically consistent with Step 1 above, but Euler characteristics cannot certify simple connectivity. The dihedral alternating-character result [3] computes virtual homology and quotient Euler characteristics, not the fundamental groups of the full complexes. The pure-complex representation result [4] concerns a distinct subcomplex. Fernández [5] provides the strong-Morse framework, not this cycle-family connectivity classification.

The new information is the **uniform, sharp fundamental-group threshold** and the constructive two-skeleton/van-Kampen explanation that applies regardless of the unknown higher-dimensional homotopy type. No uniqueness of this argument across all unindexed literature is asserted.

## Limitations
No calculation of \(\pi_j\) for \(j\ge2\) is made. In particular, the theorem does not prove that the full strong complex is a sphere wedge for arbitrary cycle length, nor determine integral homology in any degree not separately established in other work. The all-length proof relies on the exact descending-link definition of a strong gradient for a one-dimensional cycle; it is not a theorem about general graphs. The literature check includes the directly relevant manuscripts and indexed sources but cannot exclude unpublished equivalent work.

## References
[1] Kevin P. Knudson and Abigail Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first public September 6, 2026, particularly §§3–4, §8, Proposition 8.5 and Table 1. https://arxiv.org/html/2609.06844

[2] *Face enumeration and Euler periodicity of strong Morse cycle complexes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-face-enumeration-and-euler-periodicity-of-strong-morse-cycle-com--7ecee706974b

[3] *Dihedral Euler characters of full strong Morse complexes of cycles*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-euler-characters-of-full-strong-morse-complexes-of-cycl--4819a9d67705

[4] *The threefold rotation character of pure strong Morse matching complexes of cycles*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-threefold-rotation-character-of-pure-strong-morse-matching-c--0dacd6b82f58

[5] Ximena L. Fernández, *Strong discrete Morse theory*, arXiv:2504.15729v1, April 22, 2025. https://arxiv.org/abs/2504.15729
