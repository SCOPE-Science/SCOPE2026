# A subgroup fixed-space transition for generalized Mycielskian independence complexes

## Finding
Let \(n\ge3\), \(\ell\ge1\), and let \(X_{n,\ell}=\operatorname{Ind}(\mu_\ell(K_n))\), with the generalized-Mycielskian indexing convention below. Every subgroup \(\Gamma\le S_n\) acts on \(X_{n,\ell}\) by permuting the complete-graph labels at every level. The *geometric* fixed-point spaces admit the following complete classification for two natural orbit structures:

1. If \(\Gamma\) acts transitively on all \(n\) labels, there is a canonical piecewise-linear homeomorphism
   \[
   |X_{n,\ell}|^{\Gamma}\cong_{\mathrm{PL}}|\operatorname{Ind}(P_{\ell+1})|.
   \]
   Consequently,
   \[
   |X_{n,\ell}|^{\Gamma}\simeq
   \begin{cases}
   S^{q-1},&\ell=3q-1,\ q\ge1,\\
   \{\mathrm{pt}\},&\ell=3q,\ q\ge1,\\
   S^q,&\ell=3q+1,\ q\ge0.
   \end{cases}
   \]
2. If \(\Gamma\) fixes exactly one label and is transitive on the other \(n-1\) labels, then \(|X_{n,\ell}|^{\Gamma}\) is contractible for every \(\ell\ge1\).

In particular, for the standard point stabilizer \(S_{n-1}<S_n\), the fixed-space inclusion \(|X_{n,\ell}|^{S_n}\hookrightarrow|X_{n,\ell}|^{S_{n-1}}\) is an inclusion from the above periodic sphere-or-point space into a contractible space. When the source is a sphere, all of its reduced homology classes die under this subgroup-relaxation inclusion.

## Assumptions and scope
The graph \(\mu_\ell(K_n)\) has vertices \((j,a)\), for \(0\le j\le\ell\) and \(a\in\{1,\ldots,n\}\), together with an apex \(w\). Its edges are: \((j,a)(j+1,b)\) for \(0\le j<\ell\) and \(a\ne b\); all pairs of distinct labels within the top level \(j=\ell\); and \(w(0,a)\) for every \(a\). There are no other edges. This is the level-zero-to-top convention of the 2026 source; relabeling the levels gives its published definition. The independence complex \(\operatorname{Ind}(G)\) consists of all vertex sets spanning no graph edge. An action on its realization is the affine action induced by permuting vertices. The theorem concerns actual geometric fixed points, not the invariant subspace of homology and not a homotopy-fixed-point construction.

A point-stabilizer-type group in the second clause may be any subgroup with the specified two label orbits, not necessarily the entire \(S_{n-1}\). The requirement \(n\ge3\) guarantees that the nontrivial label orbit has at least two elements. All (co)homology statements in the finding are integral unless coefficients are expressly indicated.

## Proof
**1. Fixed-point orbit triangulation.** Let a finite group \(\Gamma\) permute vertices of any finite simplicial complex \(K\). Every geometric point has unique nonnegative barycentric coordinates with total sum one. Being fixed by \(\Gamma\) is equivalent to having equal coordinates along each vertex orbit. Thus its support is a union of orbits that is a face of \(K\). The complex whose vertices are individually admissible vertex orbits and whose faces are collections of orbits whose unions are faces has a canonical PL homeomorphism onto \(|K|^\Gamma\): assign coordinate \(c_O/|O|\) at every vertex in orbit \(O\), and invert by summing coordinates over each orbit. When \(K=\operatorname{Ind}(G)\), an orbit is admissible precisely if it contains no internal graph edge, and two admissible orbits conflict precisely if some graph edge joins them. Since independence complexes are flag, the orbit complex is the independence complex of this conflict graph.

**2. Transitive subgroup.** The label orbit in each level \(0,\ldots,\ell-1\) is an independent vertex set, while the label orbit in the top level is a clique of size \(n\ge3\) and hence inadmissible. The apex forms its own orbit. Distinct admissible level orbits conflict exactly when their indices are consecutive, because between consecutive levels there are edges joining distinct labels, and levels farther apart have no edges. The apex orbit conflicts only with the level-zero orbit. Therefore the conflict graph is precisely the path with vertex order \(w,0,1,\ldots,\ell-1\), hence is \(P_{\ell+1}\). The orbit triangulation gives the asserted PL homeomorphism, for every transitive subgroup with this orbit partition.

**3. The point-stabilizer orbit graph.** Let \(a\) be the sole fixed label, and let \(B\) denote the orbit of the other \(n-1\ge2\) labels. At each lower level \(0\le j<\ell\) there are admissible orbits \(A_j=\{(j,a)\}\) and \(B_j=\{(j,b):b\in B\}\); at the top level only \(A_\ell=\{(\ell,a)\}\) is admissible, because the top-level orbit \(B_\ell\) contains a graph edge. Include the apex orbit \(W\). Directly applying the graph edge definition shows that the orbit-conflict graph \(Q_\ell\) has precisely the following edges:
\[
WA_0,\quad WB_0,\quad B_jA_{j+1}\ (0\le j<\ell),\quad
A_jB_{j+1},\ B_jB_{j+1}\ (0\le j<\ell-1).
\]
There are no edges among any two of the \(A_j\). The extra edges \(B_jB_{j+1}\) exist because \(|B|\ge2\), so one can choose distinct labels on consecutive levels. By Step 1, \(|X_{n,\ell}|^\Gamma\cong_{\mathrm{PL}}|\operatorname{Ind}(Q_\ell)|\).

**4. Contractibility.** Let \(u=A_{\ell-1}\) and \(v=A_\ell\). These vertices are nonadjacent. If \(\ell=1\), their respective open neighborhoods are \(N(u)=\{W\}\) and \(N(v)=\{B_0\}\), with the two neighbor vertices adjacent. If \(\ell\ge2\), they are \(N(u)=\{B_{\ell-2}\}\) and \(N(v)=\{B_{\ell-1}\}\), again with the two neighbor vertices adjacent. Hence no independent set of \(Q_\ell\) can meet both \(N(u)\) and \(N(v)\). Every face can therefore be extended by at least one of \(u\) and \(v\), so
\[
\operatorname{Ind}(Q_\ell)=\operatorname{st}(u)\cup\operatorname{st}(v).
\]
Both closed stars are cones. Because \(u,v\) are nonadjacent, their intersection is precisely \(\operatorname{st}(\{u,v\})\), another cone. A finite simplicial complex that is a union of two contractible subcomplexes with nonempty contractible intersection is contractible, by the homotopy-pushout or nerve lemma. This proves the second classification for every \(\ell\ge1\).

**5. The path periodicity.** For \(m\ge4\), the first vertex of \(P_m\) has open neighborhood contained in that of the third vertex. The ordinary independence-complex fold deleting the third vertex gives
\[
\operatorname{Ind}(P_m)\simeq\operatorname{Ind}(K_2\sqcup P_{m-3})\cong
\operatorname{Ind}(K_2)*\operatorname{Ind}(P_{m-3})\simeq\Sigma\operatorname{Ind}(P_{m-3}).
\]
The fold is proved directly by pairing faces containing the third vertex with faces to which the first vertex can be added. The bases are \(\operatorname{Ind}(P_1)\simeq\{\mathrm{pt}\}\), \(\operatorname{Ind}(P_2)\cong S^0\), and \(\operatorname{Ind}(P_3)\simeq S^0\). The suspension recurrence yields precisely the three cases in the finding after substituting \(m=\ell+1\). This proves all homotopy assertions.

## Verification
The standalone Python 3 program `verify.py` constructs the graph from the stated edge definition and computes permutation orbits using a cyclic transitive group and a cyclic subgroup fixing one label. For each \(3\le n\le7\) and \(1\le\ell\le9\), it independently reconstructs the admissible orbit-conflict graph from all original edges, compares every vertex and conflict edge with Steps 2 and 3, enumerates all quotient faces, checks mod-two reduced homology in both cases, and confirms face-by-face that the two stars in Step 4 cover the stabilizer case. The 90 orbit-graph comparisons enumerate 99,590 quotient faces in total. Running `python3 verify.py` prints `VERIFY_OK orbit_graphs=90 quotient_faces=99590 homology_and_star_cover=passed`.

These finite checks are not the proof for unbounded \(n,\ell\). The unrestricted statements follow from the orbit argument, exact graph description, star cover, and path fold.

## Relationship to prior work
Carnero Bravo's 2026 generalized-Mycielskian paper, especially its definition and Theorem 5, determines the *nonequivariant* independence-complex homotopy type. Goyal–Shukla–Singh (2019), Section 4 and Theorem 4.12, likewise studies the nonequivariant complete-graph cases using another level convention. The published result *The symmetric-group homology modules of generalized Mycielskians of complete graphs* determines the rational \(S_n\)-representation on the ambient homology, using equivariant folds for component subcomplexes, but does not identify the geometric fixed loci or show contractibility for stabilizer orbit type. Invariant homology of a space is not generally homology of its fixed-point space, and the earlier component folds alone do not identify the full geometric fixed-space attaching map.

The present theorem determines both geometric fixed-space homotopy types and their subgroup-relaxation inclusion for all the stated parameters and group orbit types, not merely homological characters. No novelty is asserted for the ordinary path-independence recurrence or the general orbit-barycenter construction. Searches and inspections do not rule out an equivalent unindexed prior observation.

## Limitations
Only the two specified label-orbit structures are classified; general subgroups with three or more orbits are not addressed. The theorem assumes \(n\ge3\) and \(\ell\ge1\) and concerns the label-permutation action, not every graph automorphism. It makes no assertion of an equivariant ambient homotopy splitting, nor of a collapse of the contractible stabilizer fixed complex. The result has not undergone independent mathematical validation, and equivalent unindexed literature remains a possibility.

## References
1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432v1 (first public 2026-01-19), especially the definition and Theorem 5; inspected revised full text https://arxiv.org/html/2601.13432v2.
2. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019), Section 4 and Theorem 4.12, https://arxiv.org/abs/1905.06926.
3. *The symmetric-group homology modules of generalized Mycielskians of complete graphs*, published mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-symmetric-group-homology-modules-of-generalized-mycielskians--a69c919d2b95, especially its Finding, Assumptions and Proof §§1–4.
