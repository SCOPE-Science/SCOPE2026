# Four automorphism classes of product structures in Hou–Ma–Chen Example 4.17

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2.
\]
Let \(T_K\) have basis
\[
\{e_1,e_2,e_3\},
\]
twist
\[
\alpha=\operatorname{diag}(1,-1,-1),
\]
and sole independent nonzero bracket
\[
\{e_1,e_2,e_1\}=e_3.
\]
Equivalently,
\[
\{x,y,z\}=(x_1y_2-x_2y_1)z_1e_3.
\]

A product structure is an endomorphism \(E\) satisfying
\[
E^2=I,\qquad E\ne\pm I,\qquad E\alpha=\alpha E,
\]
together with the integrability identity of Hou–Ma–Chen. The complete product-structure locus is
\[
\boxed{
\{\alpha,-\alpha\}
\ \sqcup\
\{E_+(r):r\in K\}
\ \sqcup\
\{E_-(r):r\in K\},
}
\]
where
\[
E_+(r)=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&r&-1
\end{pmatrix},
\qquad
E_-(r)=
\begin{pmatrix}
-1&0&0\\
0&-1&0\\
0&r&1
\end{pmatrix}.
\]

The perfect product structures are exactly
\[
\boxed{\alpha\quad\text{and}\quad-\alpha.}
\]

The full Hom-Lie-triple automorphism group is
\[
\boxed{
\operatorname{Aut}(T_K,\alpha)=
\left\{
\begin{pmatrix}
x&0&0\\
0&y&0\\
0&w&x^2y
\end{pmatrix}
:
x,y\in K^\times,\ w\in K
\right\}.
}
\]

Conjugation acts transitively on each affine family:
\[
gE_+(r)g^{-1}=E_+\!\left(rx^2+\frac{2w}{y}\right),
\]
\[
gE_-(r)g^{-1}=E_-\!\left(rx^2-\frac{2w}{y}\right).
\]
Hence there are exactly four automorphism-conjugacy classes, represented by
\[
\boxed{
\alpha,\qquad
-\alpha,\qquad
E_+(0),\qquad
E_-(0).
}
\]

Over every odd finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{Prod}(T_{\mathbf F_q})|=2q+2
}
\]
and there are exactly
\[
\boxed{4}
\]
automorphism-conjugacy classes.

Over every extension field \(\mathbf F_{q^m}\),
\[
|\operatorname{Prod}(T_{\mathbf F_q})(\mathbf F_{q^m})|
=
2q^m+2.
\]
Thus the reduced product-structure variety has Hasse–Weil zeta function
\[
\boxed{
Z(T)=\frac{1}{(1-qT)^2(1-T)^2}.
}
\]

## Assumptions and scope

Hou, Ma, and Chen study product and complex structures on Hom-Lie triple systems. Their author-posted manuscript was publicly uploaded on 14 May 2020 and lists \(17B56\) first among its Mathematics Subject Classification codes.

Example 4.17 is exactly the three-dimensional involutive Hom-Lie triple system above. The source exhibits
\[
E=\operatorname{diag}(1,-1,-1)=\alpha
\]
as a perfect product structure.

The theorem here classifies every product structure on that example over fields of characteristic different from \(2\). It does not classify product structures on arbitrary Hom-Lie triple systems.

## Proof

Because \(E\) commutes with
\[
\alpha=\operatorname{diag}(1,-1,-1),
\]
it has block form
\[
E=
\begin{pmatrix}
a&0&0\\
0&p&q\\
0&r&s
\end{pmatrix}.
\]
The involution equation \(E^2=I\) gives
\[
a^2=1,
\]
\[
p^2+qr=1,
\qquad
q(p+s)=0,
\qquad
r(p+s)=0,
\qquad
rq+s^2=1.
\]

Put
\[
F=E\alpha.
\]
The source's product-structure integrability equation is exactly the Hom-Nijenhuis condition for \(F\). Direct evaluation on the basis reduces the nonzero conditions to
\[
(a+s)(ap-as+ps-2qr-s^2)=0,
\]
\[
q(a^2+2as+qr+s^2)=0,
\]
\[
q^2(2a+p+s)=0.
\]

Suppose first that \(q\ne0\). The involution equations give
\[
p+s=0.
\]
The last integrability equation then gives
\[
2a=0,
\]
contradicting \(a^2=1\) because the characteristic is not \(2\). Hence
\[
q=0.
\]

Now \(p^2=s^2=1\) and
\[
r(p+s)=0.
\]
Thus \(p,s\in\{\pm1\}\), and the remaining integrability equation determines the allowed sign patterns.

For \(a=1\), the allowed cases are
\[
(p,s,r)=(-1,-1,0)
\]
and
\[
(p,s,r)=(1,-1,r)
\quad\text{with arbitrary }r.
\]
The first gives \(\alpha\), while the second gives \(E_+(r)\). The pattern \(p=s=1\) gives \(E=I\), which is excluded by definition, and the remaining mixed sign pattern fails integrability.

For \(a=-1\), the allowed cases are
\[
(p,s,r)=(1,1,0)
\]
and
\[
(p,s,r)=(-1,1,r)
\quad\text{with arbitrary }r.
\]
These give \(-\alpha\) and \(E_-(r)\), respectively. The case \(E=-I\) is excluded, and the other mixed sign pattern fails integrability.

This proves the complete product-structure list.

For perfection, the source requires
\[
(E\alpha)\{x,y,z\}
=
\{(E\alpha)x,(E\alpha)y,(E\alpha)z\}.
\]
For \(E=\pm\alpha\), one has \(E\alpha=\pm I\), and the identity holds by trilinearity.

For \(E_+(r)\),
\[
(E_+(r)\alpha)e_1=e_1,\qquad
(E_+(r)\alpha)e_2=-e_2-re_3,\qquad
(E_+(r)\alpha)e_3=e_3.
\]
Applying the perfect identity to \((e_1,e_2,e_1)\) compares \(e_3\) with \(-e_3\), so perfection fails.

For \(E_-(r)\), the same basis triple compares \(-e_3\) with \(e_3\), so perfection again fails. Thus only \(\pm\alpha\) are perfect.

To compute automorphisms, let \(g\) commute with \(\alpha\). Then
\[
g=
\begin{pmatrix}
x&0&0\\
0&y&z\\
0&w&t
\end{pmatrix}.
\]
Preservation of
\[
\{e_1,e_2,e_1\}=e_3
\]
forces
\[
z=0,\qquad t=x^2y.
\]
Invertibility is therefore equivalent to
\[
x\ne0,\qquad y\ne0.
\]
This yields the displayed automorphism group.

A direct matrix multiplication gives the two conjugation formulas. Since \(2\ne0\) and \(w\) is arbitrary, every \(E_+(r)\) is conjugate to \(E_+(0)\), and every \(E_-(r)\) is conjugate to \(E_-(0)\). The two isolated maps \(\pm\alpha\) commute with every automorphism. The four representatives have distinct eigenvalue/sign data and are not mutually conjugate.

The finite-field count and zeta function now follow from the disjoint decomposition into two affine lines and two rational points.

## Verification

The included `artifacts/verify.py` reconstructs the ternary product, the twist, the product-structure integrability identity, the perfect identity, and the automorphism condition.

It symbolically checks the complete families and derives the conjugation formulas.

It then exhaustively enumerates every endomorphism commuting with \(\alpha\) over
\[
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]
For each field it filters involutions, excludes \(\pm I\), tests the product identity on all basis triples, and confirms that the survivors are exactly the two affine families plus \(\pm\alpha\).

The counts are
\[
8,\quad12,\quad16,
\]
which equal \(2q+2\).

It separately checks the perfect identity and finds exactly two perfect product structures in every tested field.

Finally, it constructs the full automorphism group and verifies that the product structures form exactly four conjugacy orbits.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. Completeness over arbitrary characteristic not \(2\) follows from the symbolic case analysis above.

## Relationship to prior work

The primary paper defines product structures, proves their relation with Hom-Nijenhuis operators, characterizes them through eigenspace decompositions, and introduces perfect product structures. Example 4.17 exhibits the specific map
\[
E=\alpha=\operatorname{diag}(1,-1,-1)
\]
as a perfect product structure on the present three-dimensional example.

The inspected paper does not classify all product structures on Example 4.17, does not compute its automorphism quotient, and does not give finite-field counts.

Targeted searches for the exact multiplication, Example 4.17, all product structures, Hom-Nijenhuis involutions, the formula \(2q+2\), and automorphism conjugacy found no covering classification.

The closest operator-normal-form result found in semantic search concerns averaging operators on a nilpotent two-dimensional pre-Lie algebra, which uses a different algebra and operator identity.

## Limitations

Characteristic \(2\) is excluded because the proof uses the separation of the \(\pm1\) eigenspaces and the nonvanishing of \(2\).

The result concerns one three-dimensional involutive Hom-Lie triple system.

The author-posted 2020 manuscript was the earliest verified public source; the later journal publication supplies the same general framework.

Failed searches do not prove absolute historical novelty.

## References

1. Y. Hou, Y. Ma, and L. Chen, “Product and complex structures on Hom-Lie triple systems,” author-posted manuscript, first public upload 14 May 2020, ResearchGate record `341360022`; later published in *Journal of Shandong University (Natural Science)* 56 (2021), 48–60, DOI `10.6040/j.issn.1671-9352.9.2021.008`.
