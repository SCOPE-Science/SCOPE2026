# Nijenhuis operators on a canonical two-dimensional anti-flexible algebra

## Finding

Let \(K\) be a field and let \(A_K\) have basis \(\{e_1,e_2\}\) with
\[
e_1\cdot e_1=e_1,\qquad e_1\cdot e_2=0,\qquad e_2\cdot e_1=e_1,\qquad e_2\cdot e_2=e_2.
\]
This is obtained from Dassoundo's Example 1.3 by taking the standard symmetric bilinear form, \(c=e_1\), and \(c_1=e_2\).

For \(x=x_1e_1+x_2e_2\) and \(y=y_1e_1+y_2e_2\),
\[
x\cdot y=(x_1+x_2)y_1e_1+x_2y_2e_2.
\]
The associator is
\[
(x,y,z)=-x_1y_2z_1e_1,
\]
so it is symmetric in the outer variables: \(A_K\) is anti-flexible and nonassociative.

For
\[
N=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
the complete Nijenhuis condition is
\[
\boxed{b=0,\qquad c(a-d)=0.}
\]
Hence
\[
\boxed{\operatorname{Nij}(A_K)=\mathcal D\cup\mathcal J,}
\]
where
\[
\mathcal D=\left\{\begin{pmatrix}a&0\\0&d\end{pmatrix}:a,d\in K\right\},
\qquad
\mathcal J=\left\{\begin{pmatrix}a&0\\c&a\end{pmatrix}:a,c\in K\right\}.
\]
The two affine planes meet in the scalar line \(\{aI:a\in K\}\).

Moreover,
\[
\boxed{\operatorname{Aut}(A_K)=\{I\}.}
\]

Over every finite field \(\mathbf F_q\),
\[
\boxed{|\operatorname{Nij}(A_{\mathbf F_q})|=2q^2-q}
\]
and the rank profile in ranks \(0,1,2\) is
\[
\boxed{\left(1,\ 3(q-1),\ 2(q-1)^2\right).}
\]
All automorphism-conjugacy classes are therefore singleton.

The weight-zero Rota--Baxter operators are exactly
\[
\boxed{\operatorname{RB}_0(A_K)=\{cE_{21}:c\in K\}.}
\]
Thus the Rota--Baxter locus has \(q\) points over \(\mathbf F_q\), compared with \(2q^2-q\) Nijenhuis operators.

Over every extension field,
\[
|\operatorname{Nij}(A_{\mathbf F_q})(\mathbf F_{q^m})|=2q^{2m}-q^m,
\]
so
\[
\boxed{Z(T)=\frac{1-qT}{(1-q^2T)^2}.}
\]

## Assumptions and scope

The primary source first appeared on 24 July 2022 and lists \(17A30\) first among its Mathematics Subject Classification codes. Example 1.3 gives the anti-flexible family, and Definition 4.1 gives the Nijenhuis identity.

The theorem concerns the normalized two-dimensional specialization above and is valid over every field.

It does not classify every member of the full Example 1.3 family.

## Proof

The Nijenhuis torsion is
\[
T_N(x,y)=N(x)\cdot N(y)-N\!\left(N(x)\cdot y+x\cdot N(y)-N(x\cdot y)\right).
\]
On the four ordered basis pairs,
\[
T_N(e_1,e_1)=bc\,e_1+c(d-a)e_2,
\]
\[
T_N(e_1,e_2)=-bc\,e_2,\qquad T_N(e_2,e_1)=-bc\,e_2,
\]
and
\[
T_N(e_2,e_2)=b^2e_1.
\]
Since \(K\) is a field, \(b^2=0\) gives \(b=0\), leaving exactly \(c(d-a)=0\).

For automorphisms, \(e_2\) is the unique left identity. Hence every automorphism fixes \(e_2\). If \(g(e_1)=pe_1+qe_2\), preservation of \(e_1\cdot e_2=0\) gives \(q=0\), and preservation of \(e_1\cdot e_1=e_1\) gives \(p^2=p\). Invertibility gives \(p=1\), so \(g=I\).

For finite fields, each plane has \(q^2\) points and their intersection has \(q\), giving \(2q^2-q\). The diagonal plane contributes \((q-1)^2\) invertible maps and the lower-Jordan plane contributes \(q(q-1)\); their invertible intersection has \(q-1\). Hence the rank-two count is \(2(q-1)^2\), and the remaining nonzero maps number \(3(q-1)\).

For the weight-zero Rota--Baxter identity
\[
R(x)\cdot R(y)=R\!\left(R(x)\cdot y+x\cdot R(y)\right),
\]
basis substitution gives \(a=b=d=0\) with \(c\) arbitrary, proving the stated line.

## Verification

The bundled checker `artifacts/verify.py` independently verifies the anti-flexible identity and reconstructs the Nijenhuis torsion.

It exhaustively tests all \(2\times2\) matrices over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]
The Nijenhuis totals are
\[
6,\quad15,\quad45,\quad91,
\]
with rank profiles
\[
(1,3,2),\quad(1,6,8),\quad(1,12,32),\quad(1,18,72).
\]
It also verifies that the automorphism group is trivial and that the weight-zero Rota--Baxter solution counts are \(2,3,5,7\).

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence; the arbitrary-field theorem is proved above.

## Relationship to prior work

Dassoundo's Example 1.3 supplies the anti-flexible family and Definition 4.1 supplies the Nijenhuis equation. The inspected Nijenhuis section develops general deformation and pre-anti-flexible constructions but contains no worked classification on Example 1.3.

Proposition 4.9 identifies square-zero Nijenhuis operators with weight-zero Rota--Baxter operators. On this algebra that accounts for only the line \(\{cE_{21}\}\), not the complete two-plane Nijenhuis locus.

Earlier center-symmetric literature develops structural and bialgebra theory rather than this operator classification. Targeted searches under the anti-flexible and center-symmetric names, the exact product, the two-plane equations, and the finite-field count \(2q^2-q\) did not locate a covering result.

## Limitations

The theorem treats one canonical two-dimensional specialization of a broader source family.

It does not classify the whole parameter family.

The automorphism group is trivial, so the conjugacy statement gives no further orbit compression.

Failed searches do not prove absolute historical novelty.

## References

1. M. L. Dassoundo, “On Rota-Baxter and Nijenhuis anti-flexible algebras,” arXiv:2207.11834v1, first public 24 July 2022, DOI `10.48550/arXiv.2207.11834`.
2. M. N. Hounkonnou and M. L. Dassoundo, “Center-symmetric algebras and bialgebras: relevant properties and consequences,” arXiv:1507.07718.
