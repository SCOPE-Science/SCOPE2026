# Five rational nodes on two conjugate twisted cubics: the characteristic-two Bring fibre

## Finding

Let \(e_j\) denote the \(j\)-th elementary symmetric polynomial in the five homogeneous coordinates \(X_1,\ldots,X_5\). The characteristic-two fibre \(B\) of the integral complete intersection
\[
\mathcal B=V(e_1,e_2,e_3)\subset\mathbb P^4_{\mathbb Z_{(2)}}
\]
is a reduced, connected, geometrically reducible stable curve. Over \(\mathbb F_4\), it is the union of two smooth twisted cubics exchanged by arithmetic Frobenius. They intersect transversely in precisely five ordinary nodes, all rational over \(\mathbb F_2\), namely the five coordinate permutations of \([0:1:1:1:1]\). Each component has normalization \(\mathbb P^1\); the arithmetic genus is \(4\). For every integer \(n\ge1\), with \(q=2^n\),
\[
\#B(\mathbb F_q)=\begin{cases}5,&n\text{ odd},\\2q-3,&n\text{ even},\end{cases}
\qquad
Z(B/\mathbb F_2,T)=\frac{(1+T)^4}{(1-T)(1-4T^2)}.
\]

## Assumptions and scope

The defining equations are elementary symmetric equations, rather than a literal coefficientwise reduction of the classical power-sum equations. In characteristic zero, the two sets of equations are equivalent by Newton's identities. In characteristic two they are not: the raw power-sum equation \(\sum X_i^2=0\) is the square of \(\sum X_i=0\). The theorem concerns the displayed flat elementary-symmetric integral model and its ordinary reduced special fibre. No assertion is made about a model cut out by naively reducing all three power sums.

All geometry is over \(\mathbb F_2\) or its algebraic closure as explicitly indicated. The zeta function is the Hasse–Weil zeta function of the *singular* proper curve \(B\), not that of the disjoint normalization.

## Proof

**(1) Two explicit components.** Let \(\omega\) satisfy \(\omega^2+\omega+1=0\) in \(\mathbb F_4\). Define the cubic morphism
\[
\nu_\omega:\mathbb P^1_{\mathbb F_4}\longrightarrow\mathbb P^4_{\mathbb F_4},\quad
[s:t]\longmapsto[s^3:(s+t)^3:(s+\omega t)^3:(s+\omega^2t)^3:t^3].
\]
An exact coefficient expansion shows that the five displayed cubic forms have elementary symmetric polynomials \(e_1=e_2=e_3=0\). In fact, forming the monic polynomial with these five forms as roots yields
\[
\prod_{u\in\mathbb F_4}(Z+(s+ut)^3)(Z+t^3)
=Z^5+(s^{12}+s^9t^3+s^6t^6+s^3t^9+t^{12})Z
 +(s^{12}t^3+s^9t^6+s^6t^9+s^3t^{12}).
\]
The five cubic forms span the full four-dimensional space \(H^0(\mathbb P^1,\mathcal O(3))\): the coefficient vectors of the four \((s+ut)^3\) are indexed by distinct \(u\in\mathbb F_4\), with Vandermonde matrix on powers \(0,1,2,3\), and \(t^3\) is in their span. Consequently \(\nu_\omega\) is a closed immersion with image a smooth, nondegenerate twisted cubic \(T\) of degree three in the hyperplane \(e_1=0\). Its Galois conjugate \(T^\sigma\) is obtained by interchanging the third and fourth displayed coordinates. Both lie on \(B_{\mathbb F_4}\). They are different: at \([s:t]=[1:0]\), their tangent directions are respectively
\[
(0,1,\omega,\omega^2,0),\qquad(0,1,\omega^2,\omega,0),
\]
which give different tangent lines.

**(2) Exhaustion of the complete intersection.** On the hyperplane \(H=V(e_1)\cong\mathbb P^3\), the quadratic form \(e_2\) is nonsingular in characteristic two. Indeed, on the four-dimensional linear space \(\sum X_i=0\), the polar form of \(e_2\) is \(\sum_i v_iw_i\). Its radical is zero: the orthogonal complement in five dimensions is spanned by the all-ones vector, which does not belong to \(H\) in characteristic two. Hence \(Q=V(e_1,e_2)\) is a smooth quadric surface. The cubic \(e_3\) does not vanish identically on \(Q\), as witnessed by \([1:\omega:\omega^2:0:0]\), where \(e_1=e_2=0\) but \(e_3=1\). Thus \(B=Q\cap V(e_3)\) is a pure one-dimensional Cohen–Macaulay complete intersection of degree \(6\). It contains the two distinct integral curves \(T\) and \(T^\sigma\), each of degree \(3\). There is no residual component or multiplicity, and Cohen–Macaulay purity excludes embedded components. Thus \(B_{\overline{\mathbb F}_2}=T\cup T^\sigma\) scheme-theoretically, reduced.

**(3) Exactly five transverse nodes.** For each of the five points \([s:t]\in\mathbb P^1(\mathbb F_4)\), the five coordinate forms in \(\nu_\omega([s:t])\) are, up to common scalar, four ones and a single zero: the four values \(s+ut\) together with \(t\) comprise all the projective linear forms whose vanishing labels the five parameters. Consequently the images are the five distinct \(\mathbb F_2\)-points obtained by permuting \([0:1:1:1:1]\). Each lies on both Galois-conjugate components. Since a smooth cubic rational curve on \(Q_{\overline{\mathbb F}_2}\simeq\mathbb P^1\times\mathbb P^1\) must have bidegree \((1,2)\) or \((2,1)\), two components of the same bidegree have intersection number \(4\), whereas those of opposite bidegree have intersection number \(5\). Five distinct points force opposite bidegrees and total intersection multiplicity exactly five. Each intersection is consequently transverse, and they are the entire intersection. Therefore the singularities are precisely five ordinary double points with distinct branches, and the normalization is the disjoint union of two copies of \(\mathbb P^1_{\mathbb F_4}\).

**(4) Genus, stability and flatness.** The dual graph consists of two genus-zero vertices joined by five edges. Its first Betti number is \(4\), giving arithmetic genus \(4\); equivalently the genus-one correction \(\sum\delta-(2-1)\) equals \(5-1=4\). Each rational component meets the remainder in five geometric nodes, so the curve is stable. The equations \((e_1,e_2,e_3)\) form a regular sequence modulo two, hence define a flat projective complete-intersection model over \(\mathbb Z_{(2)}\). Its generic fibre is the classical smooth Bring complete intersection, of genus four. Thus this model is already stable at the prime two.

**(5) All finite-extension counts.** Frobenius interchanges the two irreducible components. When \(n\) is odd, a point rational over \(\mathbb F_{2^n}\) must belong to their intersection, giving exactly the five rational nodes. When \(n\) is even, both components are individually defined over \(\mathbb F_{2^n}\), each contributing \(2^n+1\) points, with the five nodes counted twice, giving \(2(2^n+1)-5=2^{n+1}-3\). The displayed zeta function follows by taking the exponential generating series \(\exp(\sum_{n\ge1}\#B(\mathbb F_{2^n})T^n/n)\): equivalently its logarithmic coefficients are \(1+4(-1)^{n+1}+2^{n+1}\mathbf 1_{2\mid n}\), which reproduce the two point-count cases.

## Verification

The standalone file `bring_char2_verify.py` uses only Python's standard library and performs arithmetic over \(\mathbb F_4\) to confirm \(e_1=e_2=e_3=0\) coefficient by coefficient; it confirms the explicit degree-twelve and degree-fifteen coefficients in the displayed quintic identity, checks point counts by independent projective enumeration for extension degrees one through four, identifies the five candidate intersection points, and checks two distinct tangent directions. Run `python3 bring_char2_verify.py`, which prints `CHECK_OK`. The proof above, not the finite-field experiments, establishes statements for all extensions.

## Relationship to prior work

The classical Bring curve, its symmetric canonical equations, and its complex-analytic period geometry are discussed by Braden–Northover (2012) and Braden–Disney-Hogg (2023). Braden–Disney-Hogg explicitly state that extensions to positive characteristic are outside their focus. These general foundational results do not supply the displayed characteristic-two component structure, node configuration, or zeta function. The present assertion is specifically about the elementary-symmetric model at the bad prime; results on characteristic-five fibres, or on the raw power-sum reduction, do not imply it.

## Limitations

The conclusion does not identify an arbitrary integral model with the displayed one, nor assert a universal description of bad reduction for all constructions of Bring's curve. Literature concerning modular interpretations or alternative stable models might contain related special-fibre calculations; exhaustive historical novelty cannot be certified here. No independent audit of the proof has been undertaken.

## References

- H. W. Braden and T. P. Northover, *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, arXiv:1206.6004 (first posted 26 June 2012), https://arxiv.org/abs/1206.6004.
- H. W. Braden and L. Disney-Hogg, *Bring's curve: old and new*, https://doi.org/10.1007/s40879-023-00706-0 (published 2023).
