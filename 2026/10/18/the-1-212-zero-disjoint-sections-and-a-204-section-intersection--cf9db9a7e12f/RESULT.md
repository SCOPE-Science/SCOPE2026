# The 1,212 zero-disjoint sections and a 204-section intersection spectrum on an elliptic K3

## Finding

Consider the complex elliptic K3 surface \(S=F^{(4)}_{E_2,E_5}\), with zero section \(O\), formed by the Kumar--Kuwata fourth base change from the elliptic curves
\[
E_z:\quad \eta^2=\xi\bigl(\xi+(z^2+1)^2\bigr)\bigl(\xi+(z^2-1)^2\bigr).
\]
The same surface occurs as the \(v=5\) elliptic-K3 member of Burek's rank-twelve elliptic Calabi--Yau construction. **Exactly \(1212\) nonzero geometric sections are disjoint from \(O\).** Their canonical-height distribution is
\[
\begin{array}{c|ccc}
\langle P,P\rangle&8/3&10/3&4\\ \hline
\#\{P:P\cdot O=0\}&204&576&432.
\end{array}
\]
For the \(204\) shortest sections, define a symmetric, zero-diagonal, integer-weighted adjacency matrix \(A\) by \(A_{PQ}=P\cdot Q\) for distinct sections. The unordered pair counts according to intersection number \(0,1,2,4\) are respectively \(5868,8868,5868,102\). The last \(102\) are precisely the opposite pairs \(\{P,-P\}\). Every weighted row sum is \(206\), and the complete integral spectrum is
\[
\operatorname{Spec}(A)=\{206^{(1)},2^{(189)},(-32)^{(2)},(-38)^{(4)},(-46)^{(8)}\}.
\]
In particular the weighted intersection graph is connected. Superscripts here denote eigenvalue multiplicities.

## Assumptions and scope

All geometry is over \(\mathbf C\). The chosen surface is the minimal elliptic K3 model of the curve over \(\mathbf C(t)\)
\[
y^2=x^3-27A(2)A(5)t^4x+2916\bigl(B(2)^4t^{10}+B(5)^4t^2\bigr)+54C(2)C(5)t^6,
\]
where
\[
A(z)=z^8+14z^4+1,\quad B(z)=z(z^4-1),\quad C(z)=z^{12}-33z^8-33z^4+1.
\]
It has two split type-IV fibres at \(t=0,\infty\) and sixteen irreducible type-I\(_1\) fibres, as verified in Burek, Appendix A.3. 'Disjoint' means zero intersection number of two effective sections on this minimal smooth surface, including any intersection above reducible fibres. The geometric group is \(S(\mathbf C(t))\); the statement counts **all** such sections, not only sections over the smaller coefficient field and not merely the twelve explicit sections in Burek.

The elliptic curves \(E_2\) and \(E_5\) are not isogenous over \(\overline{\mathbf Q}\): both have rational nonintegral \(j\)-invariant (so neither has complex multiplication), while their good Frobenius traces at \(23\) are \(0\) and \(8\), respectively. Geometrically isogenous non-CM elliptic curves over \(\mathbf Q\) would have traces differing by at most a quadratic character at good primes; these traces cannot be related. Kumar--Kuwata, Theorem 5.1, consequently supplies a **complete integral basis**, and their Theorem 2.5 gives torsion-freeness.

## Proof

**1. Integral Mordell--Weil coordinates.** In Burek's ordered independent system \((P_1,\ldots,P_6,P'_1,\ldots,P'_6)\), the height Gram matrix is \(G/3\), with
\[
G=\begin{pmatrix}M&N\\N^{\!T}&M\end{pmatrix},\qquad
M=\begin{pmatrix}
8&-4&2&2&2&2\\-4&8&2&2&2&2\\2&2&8&2&2&2\\2&2&2&8&2&2\\2&2&2&2&8&2\\2&2&2&2&2&8
\end{pmatrix},
\]
\[
N=\begin{pmatrix}
3&-3&-3&0&0&0\\-3&3&3&0&0&0\\3&-3&3&0&0&0\\0&0&0&3&3&0\\0&0&0&-3&3&0\\0&0&0&0&0&0
\end{pmatrix}.
\]
This is precisely the previously published Burek matrix (A.10)--(A.11), **not a new height-matrix computation**. By Kumar--Kuwata Theorem 5.1, replace each sixth generator by
\[
Q_1=-\tfrac12(P_1-P_3+P_4-P_5+P_6),\qquad
Q'_1=-\tfrac12(P'_1-P'_3+P'_4-P'_5+P'_6).
\]
Together with the first five generators of each block these form an integral basis of the full geometric Mordell--Weil group. Let \(T\) be this explicit rational basis-change matrix, and put \(Q=T^{\!T}GT\). This \(12\)-by-\(12\) matrix has integral entries and is positive definite; its determinant is \(256\cdot3^{10}\). Every geometric section corresponds uniquely to \(z\in\mathbf Z^{12}\), with height \(z^{\!T}Qz/3\). The original twelve sections form an index-four sublattice; using only those would miss sections.

**2. The geometric cutoff is exact.** Write \(c_0(P),c_\infty(P)\in\mathbf Z/3\mathbf Z\) for the components of the two type-IV fibres, with \(0\) the identity component. The unprimed six basis generators have component labels \((1,1)\), the primed six have \((1,-1)\). The half-sum relations above show that the replacement generators have the same labels. Thus, in integral basis coordinates,
\[
c_0(z)=\sum_{i=1}^{12}z_i\pmod3,\qquad
c_\infty(z)=\sum_{i=1}^{6}z_i-\sum_{i=7}^{12}z_i\pmod3.
\]
For a section \(P\ne O\), Shioda's self-height formula on the elliptic K3 is
\[
\langle P,P\rangle=4+2(P\cdot O)-\kappa(c_0(P))-\kappa(c_\infty(P)),
\quad \kappa(0)=0,\quad\kappa(\pm1)=2/3.
\]
Since \(P\cdot O\) is a nonnegative integer and the total correction lies in \([0,4/3]\), disjointness implies height in \(\{8/3,10/3,4\}\). Conversely, if the height is at most \(4\), then \(2(P\cdot O)\le4/3\), so \(P\cdot O=0\). Thus **the desired census is exactly the complete integer lattice-ball enumeration \(0<z^{\!T}Qz\le12\)**, not a heuristic numerical height cutoff.

**3. Exhaustive finite enumeration.** An exact rational \(LDL^{\!T}\) decomposition of \(Q\), with diagonal
\[
(8,6,6,6,6,3/2,5,24/5,3,3,3,3/2),
\]
allows recursive completion of squares, visiting every lattice point in \(z^{\!T}Qz\le12\) and no point outside. The self-contained `verify_k3_sections.py` gives and proves its finite search bounds; it certifies the full norm histogram
\[
\#\{z:z^{\!T}Qz=0,8,10,12\}=(1,204,576,432),
\]
with all other norms at most \(12\) absent. The nonzero vectors give \(1212\) disjoint sections. The \(204\) minimal vectors divide into the four nonidentity-component signatures \((1,1),(1,-1),(-1,1),(-1,-1)\), exactly \(51\) in each.

**4. Incidence and spectrum.** For distinct sections, the bilinear Shioda formula is
\[
P\cdot R=2-\langle P,R\rangle
-\operatorname{contr}(c_0(P),c_0(R))
-\operatorname{contr}(c_\infty(P),c_\infty(R)),
\]
where the local contribution is \(0\) when either section meets the identity component, \(2/3\) when both meet the same nonidentity component, and \(1/3\) when they meet different nonidentity components. Exact pair enumeration yields intersection multiplicities \(0,1,2,4\) in the stated counts, and verifies that multiplicity \(4\) occurs exactly for opposites. The weighted degree of each vertex is \(206\).

The spectrum has an additional exact low-rank proof. Let \(V\) be the \(204\)-by-\(12\) matrix of minimum-vector coordinates, let \(s_0,s_\infty\in\{\pm1\}^{204}\) record their type-IV nonidentity components, put \(R=V^{\!T}V\), and let \(J\) denote the all-ones matrix. Include diagonal self-intersections \(P^2=-2\) in the full intersection matrix \(B\). Then
\[
B=J-\tfrac13VQV^{\!T}-\tfrac16(s_0s_0^{\!T}+s_\infty s_\infty^{\!T}),\qquad A=B+2I.
\]
The exact finite certificate verifies the four orthogonality relations \(\mathbf1^{\!T}V=0\), \(V^{\!T}s_0=V^{\!T}s_\infty=0\), \(s_0^{\!T}s_\infty=0\), and \(\mathbf1^{\!T}s_0=\mathbf1^{\!T}s_\infty=0\). It also verifies
\[
(RQ-120I)(RQ-144I)=0,\qquad\operatorname{tr}(RQ)=1632.
\]
Positivity and the trace give eigenvalues \(120\) with multiplicity \(4\) and \(144\) with multiplicity \(8\). The two sign vectors have eigenvalue \(-34\) for \(B\), while the constant vector has eigenvalue \(204\); all \(189\) orthogonal remaining directions give eigenvalue \(0\) for \(B\). Adding \(2I\) proves the displayed spectrum, and simplicity of the positive regular eigenvalue proves graph connectivity.

## Verification

Run `python verify_k3_sections.py` with Python 3.9 or later; no nonstandard libraries, network access or downloaded inputs are needed. The script constructs Burek's integral block matrix and the full-group basis change, checks exact \(LDL^{\!T}\) reconstruction and determinant, enumerates **every** lattice vector below the geometric bound by rational arithmetic, verifies component signatures, all pairwise section-intersection numbers, every weighted degree and a size-\(12\) exact polynomial certificate for the eigenvalues. It also counts points over \(\mathbf F_{23}\) to check the nonisogeny premise. Success prints `PASS` and the numerical outputs.

## Relationship to prior work

Kumar--Kuwata, Theorem 5.1, determines the full geometric Mordell--Weil basis for nonisogenous pairs and therefore dominates any claim that this work discovers a rank-twelve basis; it also gives the basis replacement used above. Burek, Appendix A.3, provides the precise chosen surface, its reducible-fibre types, height matrix and independent sections, while Theorem 1.1 constructs the larger elliptic Calabi--Yau threefold. Their established data are used as premises and are **not** presented as new. The new result is the complete zero-intersection census and the precise geometric intersection-weighted spectrum of the shortest sections, neither of which appears in the inspected passages. The full lattice data make this finite computation possible but do not by themselves give these numerical classifications without the exhaustive enumeration and local-component comparison.

## Limitations

The statement concerns the explicit \(E_2,E_5\) specialization and its smooth minimal elliptic-K3 surface, not a count of disjoint divisors on the full Calabi--Yau threefold or a classification of all elliptic K3 surfaces. It does not enumerate every pairwise intersection among all \(1212\) sections, nor sections of higher height. The algebraic passage from sections to integral vectors uses the published full-basis theorem and the published specialized height matrix; this work independently verifies the finite arithmetic consequences, not those external theorems. A previously unnoticed lattice-table or equivalent enumeration could cover the exact numbers; the available targeted literature comparisons found no such source. The accompanying checks are not an independent external audit.

## References

1. Dominik Burek, *An elliptic Calabi--Yau threefold of Mordell--Weil rank twelve*, arXiv:2610.01276, version 1 first public 2026-10-01, especially Theorem 1.1 and Appendix A.3, equations (A.8)--(A.11).
2. Abhinav Kumar and Masato Kuwata, *Elliptic K3 surfaces associated with the product of two elliptic curves: Mordell--Weil lattices and their fields of definition*, arXiv:1409.2931, first public 2014; see Theorems 2.5 and 5.1 and Section 5.3.
3. Tetsuji Shioda, *On the Mordell--Weil lattices*, Comment. Math. Univ. St. Pauli 39 (1990), Section 8, for the height/intersection formula and local fibre contributions, as cited in Burek.
