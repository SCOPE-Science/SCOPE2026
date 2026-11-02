# Involution-clique geometry distinguishes degree-equivalent \(\mathrm{SL}_2\) groups

## Finding

Let \(q=2^f\) with \(f\ge1\) and \(k=\mathbb F_q\). Write \(R_{\mathrm{sp}}=k[\varepsilon]/(\varepsilon^2)\) and \(R_{\mathrm W}=W_2(k)\), the length-two Witt ring; put \(G_{\mathrm{sp}}=\mathrm{SL}_2(R_{\mathrm{sp}})\) and \(G_{\mathrm W}=\mathrm{SL}_2(R_{\mathrm W})\). For a group \(G\), set \(I(G)=\{g\in G:g^2=1\}\), including the identity, and let \(\mathcal C_I(G)\) be its simple commuting graph: distinct vertices are adjacent exactly when they commute. An inclusion-maximal elementary abelian subgroup means a subgroup of exponent at most two maximal by inclusion.

**Theorem (complete involution-clique geometry).** Both groups have order \(q^4(q^2-1)\) and the same multiset of complex irreducible character degrees (the latter by Stasinski's theorem). Nevertheless:

1. Every element of \(I(G_{\mathrm W})\) belongs to the congruence kernel \(K_{\mathrm W}=\ker(G_{\mathrm W}\to\mathrm{SL}_2(k))\), which is elementary abelian of order \(q^3\). Hence \(\mathcal C_I(G_{\mathrm W})\) is the complete graph on \(q^3\) vertices, and \(K_{\mathrm W}\) is its **unique** inclusion-maximal elementary abelian subgroup.
2. In \(G_{\mathrm{sp}}\) let \(K=\ker(G_{\mathrm{sp}}\to\mathrm{SL}_2(k))\cong(\mathfrak{sl}_2(k),+)\). For every line \(L\in\mathbb P^1(k)\), let \(U_L\le\mathrm{SL}_2(k)\) be the unipotent root subgroup fixing \(L\), and let \(K_L=C_K(U_L)\), an elementary abelian group of order \(q^2\). The group \(E_L=K_L\times U_L\), embedded by constant matrices and the congruence kernel, is elementary abelian of order \(q^3\). The complete list of inclusion-maximal elementary abelian subgroups is **exactly** \(K\) and \(E_L\) for the \(q+1\) lines \(L\), so there are \(q+2\) in all. In the induced involution graph these are precisely its maximal cliques, each of size \(q^3\). For distinct lines \(L,M\), the intersections have sizes \(|K\cap E_L|=q^2\) and \(|E_L\cap E_M|=q\), with common intersection the scalar congruence subgroup \(Z=\{1+\varepsilon aI_2:a\in k\}\) of order \(q\). Every edge of \(\mathcal C_I(G_{\mathrm{sp}})\) lies in one of these \(q+2\) cliques.
3. In the split group the exact involution-centralizer spectrum, where \(c_I(g)=|\{h\in I(G_{\mathrm{sp}}):hg=gh\}|\), is
\[
\begin{array}{c|c}
 c_I(g)&\#\{g\in I(G_{\mathrm{sp}}):c_I(g)\text{ has this value}\}\\ \hline
 q^4+q^3-q^2&q\\
 2q^3-q^2&q^3-q\\
 q^3&q^4-q^2
\end{array}
\]
The three values are distinct for every \(q\ge2\). Thus
\[
 |I(G_{\mathrm{sp}})|=q^4+q^3-q^2,\qquad
 \#\{(g,h)\in I(G_{\mathrm{sp}})^2:gh=hg\}=q^7+2q^6-q^5-q^4.
\]
For the Witt group, both corresponding counts are \(q^3\) and \(q^6\), and its spectrum consists of \(q^3\) occurrences of \(c_I=q^3\).

For \(q=2\), the two order-\(48\) groups have respectively \(20\) and \(8\) solutions to \(g^2=1\). Their involution graphs have respectively \(4\) and \(1\) maximal cliques, although each maximal clique has \(8\) vertices.

## Assumptions and scope

The field has **even characteristic**, \(q\) is any positive power of \(2\), the ring length is exactly two, and the matrix size is exactly two. All groups are finite. The Witt ring has characteristic four, its ideal \(2R_{\mathrm W}\) is square-zero, and multiplication by two identifies its residue vector space with \(k\). The split ring has characteristic two. The subgroup \(E_L\) uses the canonical constant-matrix section of the split ring only; no such section is assumed for the Witt group.

The commuting graph here includes the identity as a vertex, unlike the convention in some conjugacy-class involution-graph literature. All occurrences of \(g^2=1\) include the identity, and all ordered-pair counts include diagonal pairs.

## Proof

**Step 1: the congruence kernels and equal group orders.** Reduction from either ring to \(k\) maps \(\mathrm{SL}_2\) surjectively onto \(H=\mathrm{SL}_2(k)\). The kernel is \(\{1+\pi X:X\in\mathfrak{sl}_2(k)\}\), where \(\pi=\varepsilon\) or \(2\), respectively. The determinant identity \(\det(1+\pi X)=1+\pi\operatorname{tr}X\) follows from \(\pi^2=0\), so there are exactly \(q^3\) kernel elements. Their product is addition of \(X\), and since the residue characteristic is two, both kernels are elementary abelian \(2\)-groups. Because \(|\mathrm{SL}_2(k)|=q(q^2-1)\), both full groups have order \(q^4(q^2-1)\).

**Step 2: all Witt involutions lie in the kernel.** Let \(A\in\mathrm{SL}_2(W_2(k))\) and suppose \(A^2=I_2\). Cayley--Hamilton over the commutative ring gives \(A^2-(\operatorname{tr}A)A+I_2=0\), hence \((\operatorname{tr}A)A=2I_2\). On reduction, \(\bar A^2=I_2\) in characteristic two, so \(\operatorname{tr}\bar A=0\); write \(\operatorname{tr}A=2u\). Because the annihilator of \(2\) is precisely \(2W_2(k)\), the identity \(2(uA-I_2)=0\) implies \(\bar u\bar A=I_2\). Thus \(\bar A\) is scalar; as \(\bar A^2=I_2\) over \(k\) it must be \(I_2\). Therefore \(A=I_2+2X\) with \(\operatorname{tr}\bar X=0\). Every such matrix has determinant one and squares to the identity, giving exactly \(q^3\) involutive elements. The kernel is elementary abelian and exhausts the involution set, proving statement 1.

**Step 3: split involutions and the projective-line pencil.** The constant-coefficient section identifies \(G_{\mathrm{sp}}=K\rtimes H\). Represent a group element by \((X,h)\) with \(X\in\mathfrak{sl}_2(k)\) and \(h\in H\); then
\[
 (X,h)^2=(X+hXh^{-1},h^2).
\]
In characteristic two, a nonidentity \(h\in H\) with \(h^2=1\) is a transvection \(h=I_2+N\), where \(N\) has rank one and \(N^2=0\). Its kernel/image is a unique line \(L\). All such transvections fixing that line form \(U_L=\{I_2+tN_L:t\in k\}\), of order \(q\), for any chosen nonzero rank-one nilpotent \(N_L\) with kernel \(L\). There are \(q+1\) lines. A direct centralizer computation (put \(N_L=E_{12}\)) gives
\[
 \{X\in\mathfrak{sl}_2(k):[X,N_L]=0\}=kI_2\oplus kN_L,
\]
which has cardinality \(q^2\). Consequently, the square-one lifts over \(U_L\) are exactly \(E_L=K_L\times U_L\): all coordinates lie in the fixed subspace, so these elements commute and square to one. The only remaining involutions are the elements of \(K\).

For any traceless \(2\)-by-\(2\) matrix \(X\) over \(k\), Cayley--Hamilton gives \(X^2=(\det X)I_2\). The square map on \(k\) is bijective, so \(X=aI_2+N\) for a unique \(a\in k\) and a square-zero matrix \(N\). If \(X\) is nonscalar, then \(N\) is nonzero rank one and determines a unique line \(L\); hence \(X\) belongs to exactly one of the planes \(kI_2\oplus kN_L\). These planes pairwise meet in \(kI_2\). It follows that \(|K\cap E_L|=q^2\), \(|E_L\cap E_M|=q\) for \(L\ne M\), and their common intersection is \(Z\).

**Step 4: every commuting pair and every maximal clique.** All elements of \(K\) commute. If \((X,1)\in K\) and \((Y,h)\in E_L\setminus K\), their commutation is equivalent to \(hXh^{-1}=X\), or \(X\in K_L\). If two involutions outside \(K\) commute, their reductions are commuting nonidentity transvections in \(H\). The centralizer in \(\mathrm{SL}_2(k)\) of a nonidentity transvection is precisely its root group \(U_L\) (directly from the centralizer of \(E_{12}\), since a scalar \(a\) must satisfy \(a^2=1\), and thus \(a=1\)). Therefore the reductions fix the same line, and both original involutions lie in \(E_L\), which is abelian. Conversely, all pairs inside \(K\) or any \(E_L\) commute. So the entire commuting graph has exactly the asserted clique-union description.

Every clique is a set of commuting elements whose squares are one, so it generates an elementary abelian subgroup. Conversely, every elementary abelian subgroup is a clique. Any clique containing an element of \(E_L\setminus K\) is contained in \(E_L\) because its entire involution centralizer is \(E_L\). A clique inside \(K\) is contained in \(K\). None of \(K,E_L\) lies in another; therefore these are all and exactly the maximal cliques and inclusion-maximal elementary abelian subgroups.

**Step 5: the spectrum and ordered-pair total.** The scalar group \(Z\subseteq K\) has \(q\) elements, each commuting with every involution, so its centralizer size inside the involutions is \(|I|\). The remaining \(q^3-q\) elements of \(K\) each lie in exactly one \(K_L\), so commute with all \(q^3\) elements of \(K\) and precisely the \(q^3-q^2\) elements of \(E_L\setminus K\), giving \(2q^3-q^2\). Every one of the \((q+1)(q^3-q^2)=q^4-q^2\) involutions outside \(K\) commutes with exactly the \(q^3\) involutions in its unique \(E_L\). Their total number is
\[
 q^3+(q+1)(q^3-q^2)=q^4+q^3-q^2.
\]
Summing the three centralizer strata counts the ordered commuting pairs:
\[
 q(q^4+q^3-q^2)+(q^3-q)(2q^3-q^2)+(q^4-q^2)q^3
 =q^7+2q^6-q^5-q^4.
\]
This proves the theorem in full.

**Representation-theoretic consequence.** The Frobenius--Schur involution-count identity says \(\sum_{\chi\in\mathrm{Irr}(G)}\nu_2(\chi)\chi(1)=|I(G)|\). Despite equality of the entire irreducible-degree multiplicity distribution, these indicator-weighted sums differ between the two groups by exactly \(q^2(q^2-1)\). No classification of individual indicators is asserted.

## Verification

Run `python verify.py` with Python 3 and optional `networkx`. The program builds the rings independently using \(\mathbb F_2[\varepsilon]/\varepsilon^2\), \(\mathbb Z/4\mathbb Z\), \(\mathbb F_4[\varepsilon]/\varepsilon^2\), and the Galois ring \((\mathbb Z/4\mathbb Z)[z]/(z^2+z+1)\). For each ring it enumerates all four-entry matrices, checks determinant one, squares each matrix, enumerates all ordered commuting pairs within the square-one set, and (when `networkx` is installed) lists all maximal cliques of that induced graph. The code uses elementary ring arithmetic rather than the formulas proved above.

The exhaustive outputs are: at \(q=2\), group order \(48\); split/Witt involution counts \(20/8\), ordered commuting pairs \(208/64\), and maximal clique counts \(4/1\). At \(q=4\), group order \(3840\); corresponding counts \(304/64\), \(23296/4096\), and \(6/1\). Full split centralizer distributions are \(\{8:12,12:6,20:2\}\) and \(\{64:240,112:60,304:4\}\) for \(q=2,4\) respectively. Every test passed. Finite checks are corroboration, not a proof of arbitrary \(f\).

## Relationship to prior work

Stasinski [1], Theorem 5.3, proves that the two groups have the same numbers of complex irreducible representations in every dimension. Its Remark 6.3 already proves that in characteristic two a specific nontrivial unipotent element of \(\mathrm{SL}_2(k)\) has no order-two lift to the Witt group; the no-lift observation is explicitly **not** claimed here as new. Indeed, the argument in Step 2 gives a short complete lift obstruction, and that consequence alone would not establish originality. The assessed additional claim is the classification of **all** inclusion-maximal elementary abelian subgroups and their pairwise intersection geometry for the split group, together with the full involution centralizer spectrum and exact graph comparison.

Singla [2] studies degree-preserving character correspondences for classical groups over length-two local rings, but the cited article's initial scope assumes odd residue characteristic; Stasinski supplies the even-characteristic result used here. The commuting-involution-graph studies of Everett--Rowley [3] and Aubad--Rowley [4] concern projective symplectic and exceptional simple groups, respectively, and their selected-conjugacy-class graphs do not include these length-two special-linear group extensions. More general Sylow-subgroup or local-ring group results could implicitly subsume some of the clique geometry; the literature comparison does not certify global priority.

## Limitations

The theorem is restricted to \(q=2^f\), matrix size two, and length-two rings. It does not classify all Sylow two-subgroups, all ordinary group conjugacy classes, character values, or individual Frobenius--Schur indicators. For the graph, vertices are **all** square-one elements, including the identity, not just elements of exact order two or a single conjugacy class. The finite verifier covers \(q=2\) and \(q=4\) only; the algebraic proof covers every \(f\ge1\). Publication priority is provisional pending broader independent literature review.

## References

[1] A. Stasinski, *Representations of \(\mathrm{SL}_n\) over finite local rings of length two*, arXiv:1907.09878, first publicly posted 2019-07-23; Journal of Algebra 566 (2021), 119–135, doi:10.1016/j.jalgebra.2020.08.036. In particular Theorem 5.3 and Remark 6.3.

[2] P. Singla, *On representations of classical groups over principal ideal local rings of length two*, arXiv:1101.3696 (2011); Communications in Algebra 40 (2012), 4060–4067.

[3] A. Everett and P. Rowley, *Commuting Involution Graphs for 4-Dimensional Projective Symplectic Groups*, Graphs and Combinatorics 36 (2020), 959–1000, doi:10.1007/s00373-020-02156-x.

[4] A. Aubad and P. Rowley, *Commuting Involution Graphs for Certain Exceptional Groups of Lie Type*, Graphs and Combinatorics 37 (2021), 1345–1355, doi:10.1007/s00373-021-02321-w.
