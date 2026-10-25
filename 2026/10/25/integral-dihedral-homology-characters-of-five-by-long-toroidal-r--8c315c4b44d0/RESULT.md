# Integral dihedral homology characters of five-by-long toroidal Rips complexes

## Finding
For every integer \(n\ge7\), equip the vertex set of \(C_5\square C_n\) with the shortest-path metric and take the **inclusive** scale-two Vietoris–Rips complex \(X_n=\operatorname{VR}_{\le2}(C_5\square C_n)\). The natural action of \(D_5\times D_n\) has integral homology representations
\[
\widetilde H_1(X_n;\mathbb Z)\cong\mathbf1_{D_5}\boxtimes\varepsilon_n,
\qquad
\widetilde H_2(X_n;\mathbb Z)\cong\varepsilon_5\boxtimes\bigl(\varepsilon_n\otimes\mathbb Z[\mathcal E_n]\bigr),
\]
with all other reduced integral homology zero. Here \(\varepsilon_j\) is the degree-one character that is \(+1\) on rotations and \(-1\) on reflections of \(D_j\), and \(\mathcal E_n\) is the set of **unoriented edges**, not vertices, of the column cycle \(C_n\). The dihedral group \(D_n\) acts on \(\mathbb Z[\mathcal E_n]\) by edge permutation; \(D_5\) acts trivially on that lattice. In particular, these are integral, not merely rational, module identities.

Equivalently, write an arbitrary product symmetry as \(g(a,b)=(ua+c,vb+d)\), where \(u,v\in\{+1,-1\}\), \(c\in\mathbb Z/5\), and \(d\in\mathbb Z/n\). Then
\[
\operatorname{tr}(g\mid\widetilde H_1(X_n;\mathbb Q))=v,
\qquad
\operatorname{tr}(g\mid\widetilde H_2(X_n;\mathbb Q))=uvF_n(v,d),
\]
where
\[
F_n(+1,d)=\begin{cases}n,&d\equiv0\pmod n,\\0,&\text{otherwise},\end{cases}
\quad
F_n(-1,d)=\#\{j\in\mathbb Z/n:2j\equiv d-1\pmod n\}.
\]
Thus the second value is \(1\) for odd \(n\), or for even \(n\) is \(2\) when \(d\) is odd and \(0\) when \(d\) is even. Neither positive-degree rational homology group has invariants under the complete \(D_5\times D_n\)-action. The underlying homotopy type is the **previously known** \(S^1\vee\bigvee^nS^2\); it is included only as a premise, not claimed as a new classification.

## Assumptions and scope
The cycle \(C_j\) has vertices \(\mathbb Z/j\) and edges joining consecutive residues. Distances are the sum of two circular distances. \(\operatorname{VR}_{\le2}\) contains a finite set of vertices precisely when every pair has distance at most two. We require \(n\ge7\); the action is by the displayed affine dihedral maps. All homology is unreduced in degree zero and reduced in positive degrees; coefficients are integral unless explicitly stated. The claimed representation is under this natural product subgroup, with no assertion that it equals every automorphism for exceptional parameters.

## Proof
**A natural sphere-block decomposition.** Let \(U_n\) be the union, for \(j\in\mathbb Z/n\), of the induced two-column complexes \(B_j=X_n[\{(a,j),(a,j+1):a\in\mathbb Z/5\}]\). A clique of \(X_n\) can meet at most three consecutive columns. Any clique using outer columns \(j-1\) and \(j+1\) contains a distance-two edge \(e_{a,j}=\{(a,j-1),(a,j+1)\}\) for a unique row \(a\). Its link is the full simplex on \(\{(a-1,j),(a,j),(a+1,j)\}\). For each such edge, collapsing the pairs obtained by adding the middle vertex \((a,j)\), in decreasing cardinality of the chosen subset of the other two middle-column neighbors, yields four valid elementary free-face pairs. No simplex contains two distinct spanning edges when \(n\ge7\). This gives exactly \(20n\) elementary collapses \(X_n\searrow U_n\). The inclusion \(U_n\hookrightarrow X_n\) is invariant under the entire action, even though the sequential order of collapses need not be equivariant, so it induces an **equivariant** isomorphism of integral homology modules.

Each \(B_j\) is isomorphic to a universal ten-vertex block \(B\) with face vector \((10,35,50,25,2)\) (numbers of simplices by dimensions zero to four). A completely specified finite free-face algorithm in the accompanying `verify_rips_c5_cylinder.py` performs exactly 48 valid elementary collapses on \(B\), leaving the boundary of an octahedron with face vector \((6,12,8)\). Hence \(H_2(B;\mathbb Z)\cong\mathbb Z\) and higher reduced homology vanishes. The intersection of neighboring blocks is the full four-simplex on their common column; all other intersections are empty. The resulting graph-of-spaces decomposition over the cycle gives natural inclusions
\[
\bigoplus_{j\in\mathbb Z/n}H_2(B_j;\mathbb Z)\xrightarrow{\ \cong\ }H_2(U_n;\mathbb Z),
\]
and \(H_1(U_n;\mathbb Z)\cong H_1(C_n;\mathbb Z)\cong\mathbb Z\). The latter has ordinary column-reflection orientation sign and trivial row action.

**The two orientation signs.** On the ten-vertex block \(B\), row rotation by one position has degree \(+1\) on its rank-one integral second homology, since the rotation has odd order five. Every row reflection is conjugate to \(a\mapsto-a\); every block-flipping column involution is conjugate to \((a,b)\mapsto(a,1-b)\) on \(B\). Their integral degrees are both \(-1\). To verify these finite degrees, use the signed simplicial Lefschetz formula
\[
L(h;B)=\sum_{\varnothing\ne\sigma\in B,\ h\sigma=\sigma}(-1)^{\dim\sigma}\operatorname{sgn}(h|_\sigma)
=1+\operatorname{tr}(h|H_2(B;\mathbb Z)).
\]
The finite enumeration in `verify_rips_c5_symmetry.py` checks all 20 combinations of the ten row-dihedral symmetries and two column symmetries and obtains the degrees \((-1)^{\delta_{\text{row reflection}}+\delta_{\text{column swap}}}\). Because \(B\) contains only 122 nonempty faces, this is a direct, exhaustive arithmetic check, not an extrapolation from finite \(n\). Row and column translations carry \(B_j\) to the corresponding translated block without changing a coherently transported generator. Column reflections send block \(j\) to block \(d-j-1\), with the verified local degree \(-1\). Row reflections contribute the other \(-1\). Combining these facts gives precisely the integral signed edge-permutation module in the finding.

For the character formula, a block is fixed by \(b\mapsto b+d\) exactly when \(d\equiv0\pmod n\), whereas a block \(\{j,j+1\}\) is fixed by \(b\mapsto d-b\) exactly when \(2j\equiv d-1\pmod n\). Each fixed block contributes the product of the two orientation signs, proving the trace formula. Row reflection acts by \(-1\) on every second-homology generator, and column reflection acts by \(-1\) on \(H_1\), establishing the invariant-subspace claim.

## Verification
The complete, dependency-free executable scripts `verify_rips_c5_cylinder.py` and `verify_rips_c5_symmetry.py` are included. Run `python3 verify_rips_c5_symmetry.py` in their directory. The cylinder checker independently constructs the **entire** flag complex from graph distances for \(n=7,8,9,10\), checks the exact \(20n\) global free-face moves, and verifies the 48-move local octahedron collapse. The symmetry checker independently enumerates all signed fixed-face contributions for 20 local actions and all 140, 160 and 180 product-dihedral actions at \(n=7,8,9\), verifying the stated homology traces. These finite examples check the implementation; the infinite assertion comes from the uniform three-column link and natural block decomposition proved above. Full complexes have face vector \((5n,30n,55n,35n,6n)\).

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling (first posted 2025-02-10) determine several homotopy types of square torus-grid Vietoris–Rips complexes, but not the present **integral dihedral action** on rectangular five-by-long grids. A prior rectangular-grid result already establishes the exact nonequivariant homotopy type \(S^1\vee\bigvee^n S^2\), and therefore the present theorem deliberately makes **no novelty claim** about its Betti numbers or homotopy type. The new information is the signed integral module, the distinction between the edge- and vertex-permutation actions for even \(n\), the character for every reflection type and the consequent full-group invariant vanishing. The closest other grid result concerns the width-four case and is not an implication of this width-five character.

## Limitations
The result covers graph-distance inclusive scale two and \(n\ge7\). It does not classify other scales, widths or the small cyclic cases. The local orientation computation is certified by an exact finite enumerator, not by a hand-drawn octahedral embedding. The findings have been reviewed using the stated explicit finite calculations and the uniform mathematical argument but have not undergone an independent audit. An equivalent group-representation calculation in literature not accessible to the searches remains a possibility.

## References
Adams, H., Adetowubo, A. Y., Barriga-Acosta, H., Feng, Z., and Sterling, J., *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134 (initial public version February 10, 2025), https://arxiv.org/abs/2502.07134. Relevant material inspected: introduction and Section 5.2, including the small-scale torus theorem and special square-grid regimes. General graph-of-spaces homotopy and elementary simplicial collapse are standard tools; the complete local certificates are supplied here.
