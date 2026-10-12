# Two-dimensional Lie–Yamaguti integrability is automatic

## Finding

Let \(L\) be any two-dimensional Lie–Yamaguti algebra over a field \(K\) with
\[
\operatorname{char}K\ne2.
\]
Every nontrivial involution
\[
E^2=I,\qquad E\ne\pm I
\]
is automatically a product structure, and every endomorphism
\[
J^2=-I
\]
satisfies the Nijenhuis integrability identities defining an algebraic complex structure. Over \(\mathbb R\), this is the usual complex-structure notion of Sheng–Zhao–Zhou.

Consequently every pair satisfying
\[
J^2=-I,\qquad E^2=I,\qquad E\ne\pm I,\qquad JE=-EJ
\]
is a complex product structure.

For every odd prime power \(q\),
\[
\#\operatorname{Prod}(L)=q(q+1),
\]
\[
\#\operatorname{Cpx}(L)=
\begin{cases}
q(q-1),&-1\text{ nonsquare},\\
q(q+1)+2,&-1\text{ square},
\end{cases}
\]
and
\[
\#\operatorname{CpxProd}(L)=q(q^2-1).
\]
Over \(\mathbf F_{q^m}\), the last count is \(q^{3m}-q^m\), hence
\[
Z_{\operatorname{CpxProd}}(T)=\frac{1-qT}{1-q^3T}.
\]

## Assumptions and scope

The primary source, first published 24 July 2020, introduces Nijenhuis, product, complex, and complex-product structures on Lie–Yamaguti algebras and lists primary MSC \(17B56\). Its product theorem identifies product structures with decompositions into two Lie–Yamaguti subalgebras.

The later Hom-Lie–Yamaguti analogue of Dong–Ma gives the polynomial integrability formulas in openly readable full text. With identity twisting, those formulas reduce to the Lie–Yamaguti identities used here.

Over fields other than \(\mathbb R\), “algebraic complex structure” means precisely \(J^2=-I\) plus the same Nijenhuis polynomial identities; no analytic geometry is asserted.

## Proof

Only skew-symmetry in the first two inputs is needed. On a two-dimensional vector space every skew bilinear operation has the form
\[
[x,y]=\omega(x,y)b
\]
for an alternating form \(\omega\) and a fixed vector \(b\). Likewise every trilinear operation skew in its first two inputs has the form
\[
\{x,y,z\}=\omega(x,y)A(z)
\]
for some endomorphism \(A\).

For a nontrivial involution choose an eigenbasis
\[
Ee_1=e_1,\qquad Ee_2=-e_2.
\]
The binary Nijenhuis identity
\[
[Ex,Ey]
=
E\bigl([Ex,y]+[x,Ey]-E[x,y]\bigr)
\]
is skew bilinear, so it suffices to check \((e_1,e_2)\). With \(b=[e_1,e_2]\), both sides are \(-b\).

For the ternary Nijenhuis identity, multilinearity and first-two skew-symmetry reduce the check to
\[
x=e_1,\qquad y=e_2,\qquad z=e_j.
\]
Write
\[
Ee_j=\epsilon_j e_j,\qquad t_j=\{e_1,e_2,e_j\}.
\]
Direct substitution makes both sides equal to
\[
-\epsilon_j t_j.
\]
Thus every nontrivial involution is integrable.

Now let \(J^2=-I\). A scalar \(J\) is Nijenhuis by direct substitution, as is every scalar endomorphism. If \(J\) is not scalar, choose \(e_1\) so that
\[
e_1,\qquad e_2=Je_1
\]
is a basis. Then
\[
Je_1=e_2,\qquad Je_2=-e_1.
\]
The binary Nijenhuis identity at \((e_1,e_2)\) has both sides equal to \([e_1,e_2]\). If
\[
t_1=\{e_1,e_2,e_1\},\qquad
t_2=\{e_1,e_2,e_2\},
\]
the ternary identity at \(z=e_1\) has both sides \(t_2\), while at \(z=e_2\) both sides are \(-t_1\). Hence every \(J\) with \(J^2=-I\) is integrable.

For finite fields, a nontrivial involution is determined by its ordered \(+1\) and \(-1\) eigenlines. Since \(\mathbf P^1(\mathbf F_q)\) has \(q+1\) points, there are \(q(q+1)\) such operators.

For \(J^2=-I\), if \(-1\) is nonsquare all solutions form the conjugacy class with irreducible characteristic polynomial \(X^2+1\), whose centralizer has order \(q^2-1\). This gives \(q(q-1)\) solutions. If \(-1\) is square, there are two scalar solutions and one non-scalar conjugacy class with centralizer order \((q-1)^2\), giving \(q(q+1)+2\).

Finally, in an eigenbasis of a fixed product structure,
\[
E=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
The anticommutation condition forces
\[
J=\begin{pmatrix}0&b\\c&0\end{pmatrix},
\]
and \(J^2=-I\) becomes \(bc=-1\), with \(q-1\) solutions. Therefore
\[
q(q+1)(q-1)=q(q^2-1)
\]
complex-product pairs occur. Replacing \(q\) by \(q^m\) yields the stated zeta function.

## Verification

The bundled checker represents completely arbitrary two-dimensional skew binary and first-two-skew ternary operations symbolically. It verifies every component of the binary and ternary Nijenhuis defects for
\[
E_0=\operatorname{diag}(1,-1),
\qquad
J_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
and for arbitrary scalar endomorphisms.

It then exhaustively enumerates every \(2\times2\) matrix over
\[
\mathbf F_3,\quad \mathbf F_5,\quad \mathbf F_7,\quad \mathbf F_{11}.
\]
The triples
\[
(\#\operatorname{Prod},\#\operatorname{Cpx},\#\operatorname{CpxProd})
\]
are
\[
(12,6,24),\quad(30,32,120),\quad(56,42,336),\quad(132,110,1320),
\]
exactly matching the formulas. The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence only; the arbitrary-field theorem is proved symbolically.

## Relationship to prior work

Sheng–Zhao–Zhou introduce exactly the relevant structures and prove the general product-decomposition theorem. The accessible abstract and publisher preview do not state the universal two-dimensional theorem or finite-field counts.

Dong–Ma give the full Hom-Lie–Yamaguti analogue and one explicit two-dimensional example with a particular product structure. Their full text does not state that every admissible involution and every \(J\) with \(J^2=-I\) is integrable in dimension two, nor does it give the multiplication-independent finite-field counts.

The later para-Kähler work of Zhao–Feng–Qiao recalls complex-product structures but develops metric constructions rather than a two-dimensional classification.

Searches under automatic-integrability, low-dimensional classification, finite-field, and exact-count formulations found no statement implying the present result.

## Limitations

Characteristic \(2\) is excluded.

The interior of the 2020 primary article beyond the available publisher preview was not openly readable during this verification. Its abstract, preview, bibliographic metadata, indexed formula snippets, and the later full-text analogue were checked. A same-paper two-dimensional corollary hidden in the inaccessible interior remains a residual literature risk.

Failed searches do not prove absolute historical novelty.

## References

1. Y. Sheng, J. Zhao, Y. Zhou, “Nijenhuis operators, product structures and complex structures on Lie–Yamaguti algebras,” *Journal of Algebra and Its Applications* 20 (2021), 2150146, first published 24 July 2020, DOI `10.1142/S0219498821501462`.
2. L. Dong, L. Ma, “Product Structures and Complex Structures of Hom-Lie-Yamaguti Algebras,” *Filomat* 35 (2021), 5115–5130, DOI `10.2298/FIL2115115D`.
3. J. Zhao, Y. Feng, Y. Qiao, “Para-Kähler and pseudo-Kähler structures on Lie-Yamaguti algebras,” arXiv:2302.11145.
