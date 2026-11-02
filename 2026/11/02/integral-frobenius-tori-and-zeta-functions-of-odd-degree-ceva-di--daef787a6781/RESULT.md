# Integral Frobenius tori and zeta functions of odd-degree Ceva divisors

## Finding
For every odd integer \(n\ge5\) and every finite field \(k=\mathbb F_q\) of characteristic \(p>n\), set
\[
D_n:\quad (X^n-Y^n)(Y^n-Z^n)(Z^n-X^n)=0\subset\mathbb P^2_k.
\]
For either distinguished residue class \(q\equiv 1\pmod n\) or \(q\equiv-1\pmod n\), the entire connected generalized Jacobian, its finite group of rational points, and the curve zeta function admit the following explicit classification. Put
\[
u_n=n^2+\frac{3(n-1)(n-2)}2,
\qquad g_n=\frac{(3n-1)(3n-2)}2.
\]
The connected Picard scheme has dimension \(g_n\), split unipotent part \(\mathbb G_a^{u_n}\), and torus quotient of dimension \(2n^2-2\). In the two cases its group-scheme structure is
\[
\operatorname{Pic}^0(D_n/k)\cong
\begin{cases}
\mathbb G_a^{u_n}\times\mathbb G_m^{2n^2-2},&q\equiv1\pmod n,\\
\mathbb G_a^{u_n}\times\left(\operatorname{Res}_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m\right)^{n^2-1},&q\equiv-1\pmod n.
\end{cases}
\]
In particular, with \(C_r\) denoting a cyclic group of order \(r\), these are actual finite abelian group isomorphisms:
\[
\operatorname{Pic}^0(D_n)(\mathbb F_q)\cong
\begin{cases}
(\mathbb F_q,+)^{u_n}\times C_{q-1}^{2n^2-2},&q\equiv1\pmod n,\\
(\mathbb F_q,+)^{u_n}\times C_{q^2-1}^{n^2-1},&q\equiv-1\pmod n.
\end{cases}
\]
The corresponding complete curve zeta functions are
\[
Z(D_n/\mathbb F_q,T)=
\begin{cases}
\displaystyle\frac{(1-T)^{2n^2-3}}{(1-qT)^{3n}},&q\equiv1\pmod n,\\[6pt]
\displaystyle\frac{(1-T^2)^{n^2-1}}{(1-T)(1-qT)^3(1-q^2T^2)^{3(n-1)/2}},&q\equiv-1\pmod n.
\end{cases}
\]
Thus the nonsplit rational-point count is the surprising constant-in-degree formula
\[
\#D_n(\mathbb F_q)=3q+1\qquad(q\equiv-1\pmod n),
\]
whereas the split count is \(3nq+3-2n^2\). The nonsplit count over \(\mathbb F_{q^m}\) is \(3q^m+1\) for odd \(m\), and \(3nq^m+3-2n^2\) for even \(m\).

## Assumptions and scope
The integer \(n\) is odd and at least five; \(q\) is any prime power with characteristic \(p>n\). Only the congruence classes \(q\equiv\pm1\pmod n\) are asserted, not the remaining classes in \((\mathbb Z/n\mathbb Z)^\times\). The scheme \(D_n\) is reduced and projective, with the indicated equation, and \(\operatorname{Pic}^0\) denotes the identity component of the Picard scheme. All statements concern the original singular curve, not its normalization or a compactified Jacobian. The characteristic restriction ensures that local truncated logarithms identify the relevant principal-unit groups with additive vector groups.

## Proof
**(1) Geometry and singularities.** In an algebraic closure fix a primitive \(n\)-th root \(\zeta\). The components are \(A_i:X=\zeta^iY\), \(B_j:Y=\zeta^jZ\), and \(C_k:Z=\zeta^kX\), for indices modulo \(n\). Lines within the same family meet at the corresponding coordinate point, giving three ordinary \(n\)-fold points. A cross-family intersection of \(A_i\) and \(B_j\) is also on \(C_{-i-j}\); the \(n^2\) points \(M_{ij}\) so obtained are distinct ordinary triple points, and there are no others. Every line contains its family coordinate point and precisely \(n\) mixed triple points. All tangent directions are distinct because \(p\nmid n\). Thus there are \(3n\) rational geometric line components, three \(n\)-fold points and \(n^2\) triple points over the algebraic closure. The arithmetic genus equals \((3n-1)(3n-2)/2\), and the normalization is a disjoint union of \(3n\) projective lines.

**(2) Local identity-component structure.** At an ordinary \(r\)-fold plane point, \(\delta=\binom r2\) and there are \(r\) branches. The quotient of normalization units by local units has torus part \(\mathbb G_m^{r-1}\) and smooth unipotent dimension \(\delta-r+1=\binom{r-1}{2}\). For completeness, the conductor in each normalized branch begins at order \(r-1\). If \(p>r\), truncated logarithm and exponential identify the principal-unit quotient with a vector group: the denominators needed have orders below \(p\). These descriptions commute with descent from a perfect finite field. Consequently the direct local unipotent contribution is \(n^2\) from the triple points and \(3\binom{n-1}{2}\) from the coordinate points. The normalization has trivial connected Picard scheme. Dividing the multiplicative branch-gluing groups by the scalar trivializations of the connected collection of components yields a torus whose character lattice is the integral cycle lattice of the branch-incidence graph. The resulting commutative affine group is the direct product of its torus and vector-unipotent subgroup over the perfect field \(k\).

**(3) The integral torus lattice.** Construct the bipartite graph \(\Gamma_n\) with vertices for the \(3n\) components, the three coordinate points and the \(n^2\) points \(M_{ij}\). Its edges are the branches of \(D_n\) at these points, namely \(3n(n+1)\) edges. The graph is connected. Its first integral homology is free of rank
\[
b_1(\Gamma_n)=3n(n+1)-(3n+n^2+3)+1=2n^2-2.
\]
Its oriented branch edges run from component vertices to singular-support vertices. For \(q\equiv1\pmod n\), all vertices and edges are Frobenius-fixed, so this lattice is a trivial Frobenius lattice of the stated rank.

For \(q\equiv-1\pmod n\), Frobenius sends each index to its negative. Since \(n\) is odd, its fixed graph has exactly seven vertices: the three components of index zero, three coordinate singularities, and \(M_{00}\); it has exactly six edges, forming a tree with \(M_{00}\) as central vertex. Every remaining vertex and every remaining edge is in a two-element Frobenius orbit. Starting from the fixed tree, add a pair of conjugate edges whenever their terminal two-vertex orbit has not yet been reached. Connectedness guarantees such an edge until every orbit is reached. Every step adds two new vertices and two edges, so this constructs a Frobenius-invariant spanning tree. All its non-tree edges are paired by Frobenius. Their fundamental cycles are an integral basis of \(H_1(\Gamma_n,\mathbb Z)\), also paired by Frobenius, because the spanning tree and the edge orientation are invariant. Therefore, as an *integral* module rather than only after tensoring with \(\mathbb Q\),
\[
H_1(\Gamma_n,\mathbb Z)\cong
\mathbb Z[\operatorname{Gal}(\mathbb F_{q^2}/\mathbb F_q)]^{\,n^2-1}.
\]
A regular rank-two character module gives an induced multiplicative torus \(\operatorname{Res}_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m\). The quotient torus and the point-group conclusions follow. The direct-product and logarithm arguments in (2) justify the claimed unipotent factors as group schemes and on rational points.

**(4) Normalization and zeta functions.** For a projective reduced curve whose normalization components and branches are finite Frobenius sets, let \(c_d\), \(s_d\), \(b_d\) denote the numbers of Frobenius orbits of length \(d\) on components, singular supports and branches. Comparing the normalization with the singular curve gives
\[
Z(D_n,T)=\prod_{d\ge1}
\frac{(1-T^d)^{b_d-c_d-s_d}}{(1-q^dT^d)^{c_d}}.
\]
For the split case \((c_1,s_1,b_1)=(3n,n^2+3,3n(n+1))\), with all other orbit counts zero, giving the first formula. In the nonsplit case the only nonzero orbit counts are
\[
\begin{array}{c|cc}
 & d=1 & d=2\\\hline
c_d &3&3(n-1)/2\\
s_d &4&(n^2-1)/2\\
b_d &6&3(n^2+n-2)/2.
\end{array}
\]
Substituting gives the second displayed zeta function. The point formulas follow by logarithmic differentiation, or directly: for odd extension degree the only rational components are the three index-zero lines, concurrent at \(M_{00}\), yielding \(3(q^m+1)-2\); even extensions split all geometric lines.

## Verification
The standalone standard-library script `verifier.py` constructs the exact branch-incidence graphs for odd \(n\in\{3,5,7,9,11,13,15\}\), verifies all degrees and the seven-vertex fixed tree, explicitly constructs Frobenius-invariant spanning trees and confirms that every fundamental-cycle chord is paired. It also exhaustively enumerates projective rational points over ten prime fields for odd \(n\in\{5,7,9,11,13\}\), checks both congruence cases, and independently differentiates both zeta-function expressions through extension degree eight. Executing `python3 verifier.py` produces the supplied `verifier_output.txt` ending in `VERIFY_OK`. This finite check supplements, but does not replace, the uniform argument in the proof. The package contains no claim of an independent external audit.

## Relationship to prior work
The Fermat/Ceva incidence family and its \(n^2+3\) special point configuration are classical. Harbourne–Seceleanu (2013) and Nagel–Seceleanu (2015) study the ideals and symbolic/ordinary powers of those points. Artebani–Dolgachev (2006) explain the Hesse configuration, including the degree-three member and its classical nine-line dual. The result here is not the incidence configuration, a statement about symbolic-power containment, or a general normalization theorem; it evaluates the **integral** arithmetic torus, the high-multiplicity unipotent Picard contribution, the rational-point groups, and both zeta functions uniformly for every odd \(n\ge5\) in two Frobenius regimes. The uniform pure-induced torus decomposition and \(3q+1\) nonsplit count are the distinguished structural conclusions.

## Limitations
The cases \(q\not\equiv\pm1\pmod n\), even \(n\), and characteristic \(p\le n\) are not covered. An extension-field count is not an arithmetic classification of the entire ambient plane complement. The infinite proof relies on standard normalization and Picard-group structure, with a new explicit computation of its Frobenius lattice for this family. Earlier general structure theorems supply crucial tools, so claims of historical priority should remain provisional pending specialist review. No external or independent validation is asserted.

## References
1. Michela Artebani and Igor Dolgachev, *The Hesse pencil of plane cubic curves*, first arXiv version 2006-11-19, arXiv:math/0611590; Enseign. Math. 55 (2009), 235–273. https://arxiv.org/abs/math/0611590
2. Brian Harbourne and Alexandra Seceleanu, *Containment Counterexamples for Ideals of Various Configurations of Points in Projective Space*, first arXiv version 2013-06-16, arXiv:1306.3668. https://arxiv.org/abs/1306.3668
3. Uwe Nagel and Alexandra Seceleanu, *Ordinary and symbolic Rees algebras for ideals of Fermat point configurations*, first arXiv version 2015-09-16, arXiv:1509.04977. https://arxiv.org/abs/1509.04977
4. Ferruccio Orecchia, *Points in Generic Position and Conductors of Curves with Ordinary Singularities*, J. London Math. Soc. 24 (1981), 85–96, DOI:10.1112/jlms/s2-24.1.85 (background on local conductor structure).
