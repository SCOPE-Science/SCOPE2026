# Complete nonidentity dihedral fixed-point types of wheel matching complexes

## Finding
For every integer \(n\geq5\), let \(W_n=C_n*K_1\) be the wheel with rim vertices \(0,\ldots,n-1\), one central vertex, spokes \(S_i=\{*,i\}\), and rim edges \(R_i=\{i,i+1\}\) (indices modulo \(n\)). Let \(X_n=\mathcal M(W_n)\) be the **ordinary matching complex**, with simplices the pairwise vertex-disjoint subsets of edges, and let the dihedral group act by permuting rim vertices. The following are **actual geometric fixed-point spaces**, not fixed-point sets of homology representations.

Write \(r_a(i)=i+a\) and \(s_a(i)=a-i\), with the center fixed. For any nonidentity rotation \(r_a\), set \(g=\gcd(n,a)\). There are natural piecewise-linear homeomorphisms
\[
|X_n|^{\langle r_a\rangle}\cong_{\mathrm{PL}}
\begin{cases}
\varnothing,&g=1,\\
|\operatorname{Ind}(K_2)|,&g=2,\\
|\operatorname{Ind}(C_g)|,&g\geq3.
\end{cases}
\]
For a reflection \(s_a\), if \(n=2m+1\) is odd, then
\[
|X_n|^{\langle s_a\rangle}\cong_{\mathrm{PL}} |\operatorname{Ind}(P_m\sqcup K_1)|,
\]
which is contractible. If \(n=2m\) is even, then
\[
|X_n|^{\langle s_a\rangle}\cong_{\mathrm{PL}}
\begin{cases}
|\operatorname{Ind}(K_2\sqcup P_{m-2})|,&a\text{ even (axis through opposite rim vertices)},\\
|\operatorname{Ind}(P_{m+1})|,&a\text{ odd (axis through opposite rim edges)}.
\end{cases}
\]
Both even-rim reflection spaces are homotopy equivalent to \(|\operatorname{Ind}(P_{m+1})|\). Here \(P_t\) is the graph on \(t\) consecutive vertices and \(K_1\) is an isolated vertex. The small graph \(C_2\) is avoided in favor of \(K_2\).

In particular, nonempty rotation fixed loci are integral wedges of spheres with the following full homotopy types: if \(g=3k\) they are \(S^{k-1}\vee S^{k-1}\); if \(g=3k+1\) (with \(g\geq4\)) they are \(S^{k-1}\); if \(g=3k+2\) (with \(g\geq5\)) they are \(S^k\); and \(g=2\) gives \(S^0\). For even \(n=2m\), let \(t=m+1\); reflection fixed loci are contractible for \(t\equiv1\pmod3\), are \(S^{t/3-1}\) for \(t\equiv0\pmod3\), and are \(S^{(t-2)/3}\) for \(t\equiv2\pmod3\). There are no unstated genericity assumptions.

## Assumptions and scope
The integer \(n\) is the number of **rim vertices** and not the total number of vertices (which is \(n+1\)). All graphs are finite simple graphs; joins and disjoint unions of graphs are distinct operations. The action is the standard rim-dihedral action on the ordinary matching complex. All nonidentity elements of this dihedral group are classified; the identity is intentionally excluded because its fixed space is the already-studied full matching complex. The complexes are finite, and the formulas are for integral homotopy types rather than merely field-dependent homology.

For a graph \(H\), \(\operatorname{Ind}(H)\) denotes its abstract simplicial complex of independent vertex sets. A graph with an isolated vertex has contractible independence complex. When writing \(\operatorname{Ind}(P_0)\) in an inductive recurrence, use the standard augmented convention containing only the empty face.

## Proof
**1. Geometric orbit-simplex lemma.** Let a finite group act by permuting the vertices of a finite abstract simplicial complex \(K\). Retain only group orbits \(O\) of vertices for which \(O\) itself is a simplex, and make a simplex out of a family of retained orbits precisely when their union is a simplex of \(K\). The resulting orbit complex is piecewise-linearly homeomorphic to \(|K|^G\): on each invariant original simplex, an invariant barycentric-coordinate assignment is constant on each vertex orbit and is uniquely a convex combination of the normalized orbit barycenters. These affine simplices glue compatibly on common faces. This is a statement about points in the geometric realization, not merely invariant vertices.

Apply the lemma to the set of wheel edges, whose compatibility condition is that no two selected edges share an endpoint. The orbit complex is \(\operatorname{Ind}(H)\), where \(H\) is the *conflict graph*: its vertices are edge orbits containing pairwise disjoint wheel edges; two such orbits are adjacent when their unions contain incident wheel edges.

**2. Nonidentity rotations.** A rotation \(r_a\) partitions the spokes into orbits of cardinality \(n/g>1\), where \(g=\gcd(n,a)\), so no spoke orbit is admissible (all spokes meet the center). Rim edges \(R_i\) form orbits indexed by their residues modulo \(g\). If \(g=1\), the sole orbit contains adjacent rim edges and is inadmissible. If \(g\geq2\), each orbit has edges whose indices differ by multiples of \(g\), so its distinct edges never share endpoints. Two orbits conflict precisely when their index classes differ by \(1\) or \(-1\) modulo \(g\). Therefore the conflict graph is \(K_2\) for \(g=2\), and \(C_g\) for \(g\geq3\).

**3. Odd-rim reflections.** All reflections are conjugate when \(n=2m+1\). Take \(s_0(i)=-i\). It fixes the spoke \(S_0\) and the opposite rim edge \(R_m\). Every other spoke orbit has two edges meeting the center and is inadmissible. The rim-edge orbit incident to vertex \(0\) is likewise inadmissible because its two edges meet at \(0\). The remaining admissible rim-edge orbits are \(\{R_i,R_{2m-i}\}\) for \(1\leq i\leq m-1\), together with \(\{R_m\}\), forming a conflict path on \(m\) vertices. The fixed spoke \(S_0\) conflicts with none of them, so the conflict graph is \(P_m\sqcup K_1\), and the fixed-point complex is a cone.

**4. Even-rim reflections.** Put \(n=2m\), where \(m\geq3\). For \(s_0(i)=-i\), the two fixed spokes \(S_0,S_m\) meet at the center and therefore form a \(K_2\) conflict component. Rim orbits touching \(0\) or \(m\) are inadmissible; the remaining \(m-2\) rim-edge orbits form a disjoint conflict path \(P_{m-2}\), giving \(K_2\sqcup P_{m-2}\). For \(s_1(i)=1-i\), no spoke is fixed and all spoke orbits are inadmissible. The two opposite fixed rim edges and the \(m-1\) admissible paired rim-edge orbits, ordered along a semicircle, form precisely one conflict path \(P_{m+1}\). Every even-axis reflection is conjugate to \(s_0\) or \(s_1\), as appropriate.

**5. Homotopy types.** The independence complex of a graph disjoint union is the join of the two independence complexes. Since \(\operatorname{Ind}(K_2)=S^0\), the even vertex-axis fixed space is \(S^0*\operatorname{Ind}(P_{m-2})\), the suspension of the latter. The standard path fold gives \(\operatorname{Ind}(P_t)\simeq\Sigma\operatorname{Ind}(P_{t-3})\) for \(t\geq3\): on the path \(1,\ldots,t\), the open-neighborhood inclusion \(N(1)\subseteq N(3)\) allows deletion of vertex \(3\) from the independence complex, leaving the disjoint union \(K_2\sqcup P_{t-3}\). Equivalently, the deletion is effected by toggling vertex \(1\) on faces containing vertex \(3\), ordered from largest faces down. Initial cases are \(\operatorname{Ind}(P_1)\simeq\mathrm{pt}\), \(\operatorname{Ind}(P_2)=S^0\), and \(\operatorname{Ind}(P_3)\simeq S^0\). Thus both even reflection cases have the stated path-periodic types. The known integral cycle-independence homotopy formula, recalled as Proposition 5.1 in Vega's work cited below, yields the stated rotation periodicity. This proves every case.

## Verification
The complete accompanying standard-library Python checker `VERIFIER.py` enumerates all admissible edge orbits and their actual conflict relations. It checks graph-isomorphism templates by connected-component sizes, edge counts and maximum degrees for **all 4,080 nonidentity dihedral actions with \(5\leq n\leq64\)**. A separate check directly enumerates all matching faces of each wheel with \(5\leq n\leq11\), retains the invariant matchings, and compares them with the faces assembled from orbit vertices, for **105 actions**. Independently constructed mod-two boundary ranks test path and cycle homology templates in **28 cases** (path sizes \(1\)–\(15\), cycle sizes \(3\)–\(15\)). All checks passed. Run `python3 VERIFIER.py` with no third-party packages. These finite checks test the construction but are not a substitute for the parameter-uniform proof above.

## Relationship to prior work
Vega, *2-Matching Complexes*, Section 5, Theorem 5.2, gives the nonequivariant homotopy type of ordinary wheel matching complexes; its Proposition 5.1 recalls the cycle-independence formula. Neither determines geometric fixed-point spaces under a specified symmetry. Bayer, Jelić Milutinović and Vega's *Matching Complexes of Outerplanar Graphs* proves a nonequivariant wedge-of-spheres theorem for outerplanar graphs and explicitly cites wheels as a separate planar example; it does not cover their fixed-point spaces. The current result identifies the exact fixed-locus orbit complexes for **every nonidentity wheel dihedral symmetry**, including the empty primitive-rotation locus, the different even reflection triangulations, and the integral sphere and two-sphere-wedge cases. Results about the **discrete-Morse matching complex** of a wheel concern matchings in a Hasse diagram and are not results about the ordinary edge-matching complex here.

## Limitations
No claim is made for the identity's fixed space, larger wheel automorphism actions outside the standard rim dihedral group, or the homotopy types of quotient spaces. The formula gives ordinary (nonequivariant) homotopy types of geometric fixed-point spaces, not an integral module decomposition of their residual normalizer actions. Finite verification only reaches the stated ranges; validity for all integers follows from the structural proof. Prior indexed searches cannot exclude all unindexed or unpublished equivalent formulations, and no independent external mathematical audit has been performed.

## References
1. J. Vega, *2-Matching Complexes*, arXiv:1909.10406 (first posted September 23, 2019), especially Section 5 and Theorem 5.2; accessible full text: https://arxiv.org/html/1909.10406v2 .
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first posted November 7, 2024), especially Introduction, Theorem 2 and Conclusion; accessible full text: https://arxiv.org/pdf/2411.04601 .
3. D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory A 88 (1999), 112–122 (cycle-independence result as cited in Vega's Proposition 5.1).
